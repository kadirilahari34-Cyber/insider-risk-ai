def add_features(df: pd.DataFrame) -> pd.DataFrame:
    # --- normalize column names just in case ---
    df = df.rename(columns={c: c.strip().lower() for c in df.columns})

    # make sure mandatory columns exist
    required = {"timestamp","user","latitude","longitude","ip","device","country","mfa_result","success","is_admin","city"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"CSV is missing required column(s): {', '.join(sorted(missing))}")

    # --- robust timestamp parsing ---
    # coerce invalid rows to NaT instead of crashing
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", utc=True)

    # drop rows with bad timestamps
    df = df.dropna(subset=["timestamp"]).copy()

    # ensure numeric types (sometimes get read as strings)
    for col in ["latitude","longitude","mfa_result","success","is_admin"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["latitude","longitude"]).fillna(0)

    # basic time features
    df = df.sort_values(["user","timestamp"]).copy()
    df["hour"] = df["timestamp"].dt.hour
    df["is_weekend"] = df["timestamp"].dt.weekday.isin([5,6]).astype(int)

    # previous values per user
    for col in ["latitude","longitude","timestamp","ip","device","country"]:
        df[f"prev_{col}"] = df.groupby("user")[col].shift(1)

    # distance/time deltas
    from geopy.distance import geodesic
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
