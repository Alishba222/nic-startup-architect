# 🚀 NIC Venture Studio — Multi-Page Generative AI Application

An institutional-grade Venture Architecture & Startup Synthesis engine designed for the **National Incubation Center (NIC)**. Powered by **Groq LPU™** and the **openai/gpt-oss-120b** model.

---

## 🏛️ Project Overview
**NIC Venture Studio** empowers venture builders, incubator directors, and visionary founders to translate raw market problems into exhaustive, institutional-grade startup investment & execution memoranda within sub-second inference speeds.

### Key Capabilities:
- **Landing Page (`Home.py`)**:
  - Executive introduction with National Incubation Center corporate blue/slate branding.
  - Telemetry & metric indicators (Groq LPU Latency, Model Velocity, Architecture Depth, Incubation Readiness).
  - Detailed 6-pillar framework breakdown and step-by-step navigation guide.
- **Startup Generator Studio (`pages/1_💡_Startup_Generator.py`)**:
  - Safe API key retrieval with validation and fallbacks.
  - Interactive input form (Problem Statement, Strategic Themes & Keywords, Industry Sector).
  - Sidebar architectural filters (Target Region, Preferred Monetization Models, Capital Intensity).
  - Pre-loaded rapid evaluation templates (AgriTech, FinTech, HealthTech).
  - Full institutional memorandum output with instant `.md` export.
- **Fixed Corporate Footer**:
  - `"Developed for National Incubation Center | Built by Alishba Naeem"`

---

## 📂 Project Directory Structure

```text
KARACHI AI ASSIGNMENT/
├── .streamlit/
│   ├── config.toml            # Corporate blue/slate theme & server configuration
│   └── secrets.toml           # Groq API Key credential store
├── pages/
│   └── 1_💡_Startup_Generator.py  # Page 2: Venture Architect & Memo Generator
├── Home.py                    # Page 1: Landing Page & Telemetry
├── requirements.txt           # Python dependencies (Streamlit, Groq)
└── README.md                  # Comprehensive documentation
```

---

## ⚡ Quickstart Guide

### 1. Install Dependencies
Make sure you have Python 3.9+ installed. Run:
```bash
pip install -r requirements.txt
```

### 2. Configure Groq API Key
1. Sign up for free at [Groq Console](https://console.groq.com/keys) to get an API key.
2. Open `.streamlit/secrets.toml` and paste your key:
```toml
GROQ_API_KEY = "gsk_your_actual_groq_api_key_here"
```
*(Alternatively, you can provide the key directly in the sidebar during local testing).*

### 3. Launch the Application
Start the Streamlit multi-page web application:
```bash
streamlit run Home.py
```
Open your browser at `http://localhost:8501`.

---

## 🏛️ 6-Pillar Memorandum Framework

Every generated memorandum includes:
1. **Executive Blueprint & Value Proposition**: Venture Name, Tagline, Elevator Pitch, Strategic Category, and UVP.
2. **Market Problem & Ideal Customer Profile (ICP)**: Root causes, TAM/SAM/SOM sizing, buyer vs. end-user personas.
3. **MVP Technical Architecture & Feature List**: Modern stack recommendations (Frontend, Backend, DB, Cloud/AI) and Day-1 core features.
4. **Unit Economics & Monetization Strategy**: Tiered revenue models, CAC, blended LTV, target gross margins, and use of funds.
5. **90-Day Go-To-Market (GTM) Roadmap**: Concrete Day 1-30, 31-60, and 61-90 execution milestones.
6. **Operational Risks & Competitive Moats**: Regulatory, technical, and execution risk matrices paired with defensible flywheels.

---

## 👤 Credits & Attribution
**Client:** National Incubation Center (NIC)  
**Developed by:** Alishba Naeem
