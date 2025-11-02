# insider-risk-ai
# 🛡️ Insider Login Behavior Risk Analyzer

AI-Ready Identity Threat Detection for SOC Analysts

---

## 📌 Overview

This project detects unusual or risky sign-in behavior that may indicate **account compromise** or **insider threat** activity.
It analyzes login context such as geography, MFA usage, device changes, and user privileges — and flags activity that deviates from normal behavior.

The system generates enriched alerts that **AI assistants** or SOC analysts can use to take action faster.

✅ Built for hands-on cybersecurity learning
✅ Fully deployable tool imitating modern SOC identity analytics
✅ Demonstrates behavioral detection, triage, and alert response

---

## 🚀 Live Demo

Use this web app to test a CSV dataset of sign-in logs:

🔗 [https://insider-risk-ai-gzutvbhohruz3flq8xklpe.streamlit.app/](https://insider-risk-ai-gzutvbhohruz3flq8xklpe.streamlit.app/)

---

## 🧠 AI-Assisted SOC Triage

While initial detection is rule-based, every alert is structured for **AI-driven decision support**, providing:

✔ Professional triage notes
✔ Severity rating
✔ Explanation of risk
✔ Suggested mitigation actions
✔ Optional MITRE ATT&CK mapping

This mirrors how top platforms like Microsoft Entra ID Protection, Sentinel, and Splunk UBA assist SOC teams today.

---

## 🔍 What It Detects

| Threat Indicator       | Description                                       |
| ---------------------- | ------------------------------------------------- |
| 🌍 Impossible Travel   | Sign-ins from distant locations within short time |
| 📱 New Device Seen     | Potential account takeover                        |
| 🌐 New/Unusual IP      | Proxy or malicious login methods                  |
| ❌ MFA Failures         | Credential misuse detected                        |
| 🛑 High-Privilege Risk | Admin logins showing unusual behavior             |
| 🕑 Off-Hour Access     | Behavioral shift analysis                         |

These factors roll into a **risk score** & triage explanation.

---

## 🧩 How It Works (Pipeline)

```
Sign-In Logs
     ↓
Feature Engineering (geo-distance, device changes, MFA results)
     ↓
Risk Rules + Behavior Signals
     ↓
Alert Enrichment (reason + severity)
     ↓
AI-Ready Triage Output (recommended SOC actions)
```

---

## 🛠️ Tech Stack

| Component      | Technology                                         |
| -------------- | -------------------------------------------------- |
| Frontend       | Streamlit Web App                                  |
| Backend        | Python (Pandas, Geopy)                             |
| Deployment     | Streamlit Cloud                                    |
| Data           | Synthetic identity sign-in logs                    |
| Security Focus | Identity Threat Detection + Insider Risk Analytics |

---

## 📂 Repository Structure

```
insider-risk-ai/
│
├── app/                    → Streamlit UI & logic
│     └── streamlit_app.py
├── data/                   → Example synthetic datasets
├── reports/                → Output screenshots, alert samples
├── notebooks/              → Experiments / feature engineering
├── diagram/                → Architecture diagrams
├── README.md               → Documentation (this file)
└── requirements.txt
```

---

## 🧪 The app will:

✔ Enrich events
✔ Score behavior
✔ Generate risk alerts
✔ Suggest SOC actions

---

## 📊 Sample Output

| Timestamp  | User  | Country | Risk Score | Severity | AI Guidance                                         |
| ---------- | ----- | ------- | ---------- | -------- | --------------------------------------------------- |
| 2025-11-01 | admin | Romania | 90         | High     | Verify identity, reset MFA, check privilege changes |

---

## 📖 MITRE ATT&CK Alignment

| Technique                                      | Code   |
| ---------------------------------------------- | ------ |
| Valid Accounts                                 | T1078  |
| Multi-Factor Authentication Request Generation | T1621  |
| Remote Services                                | T1021  |
| Initial Access                                 | TA0001 |
| Credential Access                              | TA0006 |

This shows us **real-world relevance** 🌎

---

## 🔮 Future Enhancements

✅ Isolation Forest ML anomaly scoring
✅ Geo-visual alert map
✅ User risk profiles & dashboards
✅ Integration with a chatbot for SOC automation
✅ Support for multiple organizations

---

## 🎯 Why This Matters

Identity is the **#1 attack vector** today.
Credential theft now causes more breaches than malware.

This project gives analysts a quick way to detect:

✅ Compromised accounts
✅ Insider threats
✅ Privilege abuse efforts

…before damage occurs.

---

## 👩‍💻 Author

**Lahari Kadiri** — Cybersecurity Graduate & Blue Team Practitioner
Passionate about identity security and SOC operations 🚀

📫 LinkedIn: www.linkedin.com/in/kadiri-lahari3
📌 Portfolio Projects Coming Soon

---

## ⭐ If You Like It

Feel free to ⭐ star the repo — feedback and suggestions welcome! 🙌

---


Just say: **Yes — add visuals!** 🙌
