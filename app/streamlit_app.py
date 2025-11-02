import streamlit as st
import pandas as pd
from geopy.distance import geodesic

st.set_page_config(page_title="Insider Risk AI", layout="wide")
st.title("Insider Risk AI — Login Anomaly Detector (Demo)")

st.write("Upload your sign-in CSV (try the one in your repo: `data/synthetic_signins.csv`).")

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    # normalize column names
    df = df.rename(columns={c: c.strip().lower() for c in df.columns})

    # required columns
    required = {"timestamp","user","latitude","longitude","ip","device","country","mfa_result","success","is_admin","city"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"CSV is missing required column(s): {', '.join(sorted(missing))}")

    # robust timestamp parsing
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)
    df = df.dropna(subset=["timestamp"]).copy()

    # ensure numeric types
    for col in ["latitude","longitude","mfa_result","success","is_admin"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["latitude","longitude"]).fillna(0)

    # time features
    df = df.sort_values(["user","timestamp"]).copy()
    df["hour"] = df["timestamp"].dt.hour
    df["is_weekend"] = df["timestamp"].dt.weekday.isin([5,6]).astype(int)

    # previous values per user
    for col in ["latitude","longitude","timestamp","ip","device","country"]:
        df[f"prev_{col}"] = df.groupby("user")[col].shift(1)

    # distance/time deltas
    df["dist_km"] = df.apply(
        lambda r: geodesic((r["prev_latitude"], r["prev_longitude"]),
                           (r["latitude"], r["longitude"])).km
        if pd.notna(r.get("prev_latitude")) else 0, axis=1)
    df["mins_since_last"] = (
        (df["timestamp"] - df["prev_timestamp"]).dt.total_seconds().div(60).fillna(0)
    )

    # novelty flags
    for col in ["ip","device","country"]:
        df[f"new_{col}"] = (df[col] != df[f"prev_{col}"]).astype(int).fillna(0)

    return df.fillna(0)

uploaded = st.file_uploader("Upload CSV", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    feat = add_features(df)

    # simple heuristic score (we can swap to ML later)
    feat["risk_score"] = (
        (feat["dist_km"]>800).astype(int)*40 +
        feat["new_device"]*20 +
        feat["new_ip"]*15 +
        (1-feat["mfa_result"])*25
    )
    threshold = st.slider("Risk threshold", 0, 100, 40, step=5)

    alerts = feat[feat["risk_score"]>=threshold].copy()

    def triage_summary(row):
        tips=[]
        if row["dist_km"]>800: tips.append("impossible travel")
        if row["new_device"]: tips.append("new device")
        if row["new_ip"]: tips.append("new IP")
        if row["mfa_result"]==0: tips.append("MFA not completed")
        reason=", ".join(tips) or "baseline deviation"
        return (f"{row['user']} login from {row['city']}, {row['country']} "
                f"({int(row['dist_km'])} km since last). Indicators: {reason}. "
                "Next: confirm user, review last 3 logins, enforce MFA, check access changes.")

    alerts["triage_note"] = alerts.apply(triage_summary, axis=1)

    st.subheader("High-Risk Logins")
    st.dataframe(
        alerts[["timestamp","user","city","country","device","risk_score","triage_note"]]
        .sort_values("risk_score", ascending=False),
        use_container_width=True
    )

    st.download_button("Download alerts CSV",
                       alerts.to_csv(index=False),
                       file_name="alerts.csv")
else:
    st.info("Upload a CSV to score (use your data/synthetic_signins.csv).")
