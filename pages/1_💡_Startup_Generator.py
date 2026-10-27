import streamlit as st
import time
from datetime import datetime

# Configure page settings
st.set_page_config(
    page_title="NIC Venture Forge | Startup Generator",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Corporate CSS for National Incubation Center (Blue/Slate Theme)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .block-container {
        padding-top: 1.8rem;
        padding-bottom: 5.5rem;
        max-width: 1200px;
    }

    /* Generator Header */
    .generator-header {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 58, 138, 0.8) 100%);
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-radius: 16px;
        padding: 2rem 2.2rem;
        margin-bottom: 1.8rem;
        box-shadow: 0 16px 32px -12px rgba(0, 0, 0, 0.4);
    }

    .gen-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(37, 99, 235, 0.25);
        border: 1px solid rgba(96, 165, 250, 0.4);
        color: #93C5FD;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 0.8rem;
    }

    .generator-header h1 {
        font-size: 2.2rem;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 0.5rem;
        line-height: 1.2;
    }

    .generator-header p {
        font-size: 1rem;
        color: #CBD5E1;
        margin: 0;
        line-height: 1.5;
    }

    /* Form Container Card */
    div[data-testid="stForm"] {
        background: rgba(19, 28, 49, 0.7);
        border: 1px solid rgba(51, 65, 85, 0.85);
        border-radius: 14px;
        padding: 1.8rem;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
    }

    /* Output Memo Container */
    .memo-output-wrapper {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.95) 0%, rgba(19, 28, 49, 0.9) 100%);
        border: 1px solid rgba(59, 130, 246, 0.35);
        border-radius: 16px;
        padding: 2.2rem;
        margin-top: 1.8rem;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.6), 0 0 25px rgba(37, 99, 235, 0.12);
    }

    .memo-top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid rgba(51, 65, 85, 0.8);
        padding-bottom: 1rem;
        margin-bottom: 1.5rem;
    }

    .memo-tag {
        font-size: 0.8rem;
        color: #60A5FA;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    .memo-date {
        font-size: 0.8rem;
        color: #94A3B8;
        font-family: 'JetBrains Mono', monospace;
    }

    /* Fixed Bottom Footer */
    .nic-footer-container {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: #090D1A;
        border-top: 1px solid rgba(51, 65, 85, 0.8);
        padding: 0.8rem 1rem;
        text-align: center;
        z-index: 99999;
        box-shadow: 0 -4px 16px rgba(0, 0, 0, 0.4);
    }

    .nic-footer-text {
        margin: 0;
        font-size: 0.88rem;
        color: #94A3B8;
        font-weight: 500;
        letter-spacing: 0.02em;
    }

    .nic-footer-text span {
        color: #60A5FA;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# SAFE API KEY RETRIEVAL & ERROR HANDLING
# -------------------------------------------------------------
groq_api_key = None

# First, check st.secrets
if "GROQ_API_KEY" in st.secrets:
    secret_val = st.secrets["GROQ_API_KEY"]
    if secret_val and isinstance(secret_val, str) and secret_val.strip() != "your_groq_api_key_here":
        groq_api_key = secret_val.strip()

# Sidebar: Environment & API Key Status
with st.sidebar:
    st.markdown("### 🏢 NIC Venture Studio")
    st.caption("Principal Venture Architect Suite")
    st.divider()

    st.markdown("#### 🔑 Groq API Configuration")
    if not groq_api_key:
        # Fallback input for convenience if user hasn't edited secrets.toml
        manual_key = st.text_input(
            "Enter Groq API Key (Session Override):",
            type="password",
            help="Alternatively, set GROQ_API_KEY inside .streamlit/secrets.toml"
        )
        if manual_key and manual_key.strip():
            groq_api_key = manual_key.strip()

    if groq_api_key:
        st.success("✅ Groq API Key Connected")
    else:
        st.warning("⚠️ API Key Not Configured")

    st.divider()
    st.markdown("#### ⚡ Active Model Engine")
    st.code("llama-3.3-70b-versatile", language="text")
    st.caption("High-context, high-reasoning venture synthesis model via Groq LPUs.")

# Check API key requirement: Show st.error and stop if missing
if not groq_api_key:
    st.error("""
    ❌ **Groq API Key Missing or Not Configured**
    
    To use the **NIC Venture Forge Startup Generator**, please configure your Groq API key:
    1. Open the file [`.streamlit/secrets.toml`](file:///.streamlit/secrets.toml).
    2. Replace `"your_groq_api_key_here"` with your actual Groq API key:
       ```toml
       GROQ_API_KEY = "gsk_your_actual_key_here"
       ```
    3. Or enter your key in the sidebar under **Groq API Configuration**.
    
    *Get your free API key at [console.groq.com/keys](https://console.groq.com/keys).*
    """)
    
    # Display fixed footer even on stopped page
    st.markdown("""
    <div class="nic-footer-container">
        <p class="nic-footer-text">
            Developed for <span>National Incubation Center</span> | Built by <span>Alishba Naeem</span>
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.stop()

# Initialize Groq client
try:
    from groq import Groq
    groq_client = Groq(api_key=groq_api_key)
except Exception as e:
    st.error(f"Failed to initialize Groq client: {str(e)}")
    st.stop()

# -------------------------------------------------------------
# MAIN GENERATOR INTERFACE
# -------------------------------------------------------------
st.markdown("""
<div class="generator-header">
    <div class="gen-badge">
        <span>💡</span> VENTURE ARCHITECTURE STUDIO
    </div>
    <h1>Startup Idea & Investment Memo Generator</h1>
    <p>
        Formulate institutional-grade startup investment & execution memoranda calibrated to the National Incubation Center (NIC) investment standards. Powered by Groq LPU™ ultra-fast inference.
    </p>
</div>
""", unsafe_allow_html=True)

# Preset Templates for Rapid Evaluation
st.markdown("##### ⚡ Quick Load Architectural Presets (Optional)")
preset_cols = st.columns(3)

if "problem_input" not in st.session_state:
    st.session_state.problem_input = (
        "Post-harvest supply chain friction in emerging agricultural markets causes 30-40% "
        "crop spoilage between smallholder farmers and urban wholesale mandi distributors due to "
        "opaque pricing, zero cold-chain tracking, and predatory middleman lending."
    )
if "themes_input" not in st.session_state:
    st.session_state.themes_input = "IoT Sensors, Micro-warehousing, Agritech, Embedded Microfinance, Route Optimization"
if "sector_input" not in st.session_state:
    st.session_state.sector_input = "AgriTech & Rural Logistics"

with preset_cols[0]:
    if st.button("🌾 AgriTech Cold-Chain & Mandi", use_container_width=True):
        st.session_state.problem_input = (
            "Smallholder farmers lose 35% of high-value perishable produce due to the absence of distributed "
            "solar-powered cold storage and exploitative commission agent cartels in regional agricultural markets."
        )
        st.session_state.themes_input = "Distributed Solar Cold Rooms, Mandi Price Discovery, Pay-per-crate, Quality AI Grading"
        st.session_state.sector_input = "AgriTech & Rural Logistics"
        st.rerun()

with preset_cols[1]:
    if st.button("💳 SME Embedded Invoice Factoring", use_container_width=True):
        st.session_state.problem_input = (
            "Over 4 million unbanked and informal retail merchants struggle with 60 to 90-day cash conversion cycles, "
            "unable to secure liquidity from commercial banks due to lack of audited financials and collateral."
        )
        st.session_state.themes_input = "Digital Ledger, Alternative Credit Scoring, Micro-Factoring, WhatsApp Bot API, Daily Deductions"
        st.session_state.sector_input = "FinTech & Embedded Finance"
        st.rerun()

with preset_cols[2]:
    if st.button("🩺 Rural Tele-Diagnostics & AI Triage", use_container_width=True):
        st.session_state.problem_input = (
            "Secondary and tertiary healthcare facilities in peri-urban and rural districts face an acute shortage "
            "of qualified specialist radiologists and pathologists, leading to critical diagnostic delays of 10-14 days."
        )
        st.session_state.themes_input = "Computer Vision Radiology Triage, Edge Computing, Asynchronous Cloud PACS, Community Health Worker UI"
        st.session_state.sector_input = "HealthTech & Telemedicine"
        st.rerun()

st.write("")

# INTERACTIVE FORM
with st.form("startup_generator_form"):
    st.markdown("### 📝 Venture Parameters & Seed Inputs")

    # 1. Market Problem Statement (Full width at the very top)
    problem_statement = st.text_area(
        "Market Problem Statement",
        value=st.session_state.problem_input,
        height=140,
        help="Elaborate on the acute customer friction, inefficiency, or structural bottleneck in the target market."
    )

    # 2. Domain Vertical & Keywords (Two columns right below problem statement)
    st.markdown("##### 💡 Domain Vertical & Strategic Themes")
    sector_col1, sector_col2 = st.columns([1, 1])

    with sector_col1:
        sector = st.selectbox(
            "Industry Sector",
            options=[
                "AgriTech & Rural Logistics",
                "FinTech & Embedded Finance",
                "HealthTech & Telemedicine",
                "ClimateTech & Clean Energy",
                "AI & B2B Enterprise SaaS",
                "Logistics, Fleet & Supply Chain",
                "EdTech & Workforce Reskilling",
                "E-Commerce Enablement & Quick-Commerce",
                "Cybersecurity & Cloud Infrastructure",
                "Smart Mobility & EV Infrastructure"
            ],
            index=[
                "AgriTech & Rural Logistics",
                "FinTech & Embedded Finance",
                "HealthTech & Telemedicine",
                "ClimateTech & Clean Energy",
                "AI & B2B Enterprise SaaS",
                "Logistics, Fleet & Supply Chain",
                "EdTech & Workforce Reskilling",
                "E-Commerce Enablement & Quick-Commerce",
                "Cybersecurity & Cloud Infrastructure",
                "Smart Mobility & EV Infrastructure"
            ].index(st.session_state.sector_input) if st.session_state.sector_input in [
                "AgriTech & Rural Logistics",
                "FinTech & Embedded Finance",
                "HealthTech & Telemedicine",
                "ClimateTech & Clean Energy",
                "AI & B2B Enterprise SaaS",
                "Logistics, Fleet & Supply Chain",
                "EdTech & Workforce Reskilling",
                "E-Commerce Enablement & Quick-Commerce",
                "Cybersecurity & Cloud Infrastructure",
                "Smart Mobility & EV Infrastructure"
            ] else 0,
            help="Primary domain vertical for the venture."
        )

    with sector_col2:
        themes_keywords = st.text_input(
            "Key Themes, Tech Pillars & Keywords",
            value=st.session_state.themes_input,
            help="Comma-separated concepts, technologies, and strategic angles (e.g. AI Agents, Computer Vision, WhatsApp Native, Offline-first)."
        )

    # 3. Architectural & Market Filters (3 columns at the bottom of the form)
    st.markdown("##### 🎯 Architectural & Market Filters")
    col_region, col_monetization, col_capital = st.columns(3)

    with col_region:
        target_region = st.selectbox(
            "Target Market Region",
            options=[
                "Pakistan & South Asia (National Focus)",
                "Middle East & North Africa (MENA / GCC)",
                "Southeast Asia (ASEAN)",
                "North America (US & Canada)",
                "European Union (EU)",
                "Global Emerging Markets"
            ],
            index=0,
            help="Geographic territory where primary customer acquisition and initial pilots will deploy."
        )

    with col_monetization:
        monetization_models = st.multiselect(
            "Preferred Monetization Models",
            options=[
                "B2B SaaS Subscription (Per-seat / Per-org)",
                "Marketplace Take Rate / Commission (5% - 18%)",
                "Usage-based / Metered API Consumption",
                "Transaction Fees & Interchange Revenue",
                "Freemium with Enterprise Custom Contracts",
                "Hardware + Software-as-a-Service (HaaS)",
                "Data Analytics & Anonymized Industry Intelligence"
            ],
            default=[
                "B2B SaaS Subscription (Per-seat / Per-org)",
                "Transaction Fees & Interchange Revenue"
            ],
            help="Select one or more target economic engines for the venture."
        )

    with col_capital:
        capital_intensity = st.selectbox(
            "Risk Appetite / Capital Intensity",
            options=[
                "Bootstrap / Lean Capital ($10,000 - $50,000) — Fast to Break-Even",
                "Angel / Incubator Seed ($100,000 - $350,000) — Product-Market Fit Sprint",
                "Venture Scale Institutional ($500,000 - $2,500,000+) — Hyper-Growth"
            ],
            index=1,
            help="Available runway and risk profile determining MVP scope and technical complexity."
        )

    # 4. Form Submit Button
    submitted = st.form_submit_button(
        "⚡ Synthesize Institutional Investment Memorandum",
        type="primary",
        use_container_width=True
    )

# -------------------------------------------------------------
# MASTER PROMPT DESIGN & GENERATION ENGINE
# -------------------------------------------------------------
SYSTEM_PROMPT = """You are the Principal Venture Architect at the National Incubation Center (NIC).
Your responsibility is to evaluate market friction and architect an exhaustive, institutional-grade startup investment & execution memorandum.

Your output must be authoritative, rigorous, strategic, quantitative, and ready for scrutiny by an Investment Committee, Venture Capital Syndicate, or Incubation Board.

CRITICAL INSTRUCTIONS:
- You must structure the memorandum EXACTLY using the 6 mandatory sections below.
- Do NOT use generic high-level fluff. Use specific terminology, realistic unit economic metrics (CAC, LTV, margins, pricing tiers), concrete tech stack choices, exact 30-60-90 day milestone cadences, and realistic defensibility moats.
- Format strictly in clean GitHub Markdown with headers, bullet points, callout blocks, and structured comparison tables.

MANDATORY MARKDOWN OUTPUT STRUCTURE:
# [Venture Name] — Institutional Investment & Execution Memorandum
*National Incubation Center • Venture Architecture Directorate*

## 1. Executive Blueprint & Value Proposition
- **Venture Name & Tagline:** A memorable, institutional-grade name with a sharp one-line commercial hook.
- **Elevator Pitch:** 2-3 crisp sentences conveying Who, What, How, and the Unique Transformation.
- **Strategic Category:** Category creation or disruptor framing.
- **Unique Value Proposition (UVP):** Quantifiable, unfair advantage delivered to target customers.

## 2. Market Problem & Ideal Customer Profile (ICP)
- **Granular Problem Breakdown:** Root-cause market frictions, inefficiencies, and economic costs.
- **Total Addressable Market (TAM / SAM / SOM):** Realistic top-down and bottom-up sizing with market dynamics.
- **Ideal Customer Profile (ICP):**
  - Demographics / Firmographics (Industry, company size, revenue, geography).
  - Decision-Maker Buyer Persona vs. End-User Persona.
  - Critical Pain Points & Current Workarounds.

## 3. MVP Technical Architecture & Core Feature List
- **Architectural Philosophy:** Monolith vs. Microservices, Serverless, Edge, or Event-driven approach.
- **Modern Recommended Tech Stack:**
  - Frontend: Framework & Mobile Strategy.
  - Backend & APIs: Language, framework, and communication protocols.
  - Database & Caching: Relational, document, vector store, and caching layers.
  - Cloud / AI / Infrastructure: Hosting, models/LPUs, CI/CD, and telemetry.
- **MVP Core Feature Specifications (Sprint 1 Scope):** 4-5 non-negotiable features for day-1 viability.

## 4. Unit Economics & Monetization Strategy
- **Revenue Model & Pricing Matrix:** Detailed tiers, take rates, seat costs, or API metering.
- **Customer Acquisition Cost (CAC) & Lifetime Value (LTV):** Estimated target CAC, estimated blended LTV, and LTV:CAC target ratio.
- **Gross Margins & Contribution Margin Targets:** Target gross margin % and operational break-even horizon.
- **Capital Runway & Use of Funds:** Breakdown tailored to the selected capital intensity.

## 5. 90-Day Go-To-Market (GTM) Roadmap
- **Days 1–30 (Foundation & Alpha Design Partners):** Discovery sprints, 3-5 anchor pilots, foundational MVP build.
- **Days 31–60 (Beta Testing & Closed Cohort Launch):** Private beta rollout, instrumentation of retention loops, feedback iteration.
- **Days 61–90 (Public Launch, Monetization & Cohort Graduation):** Revenue activation, paid marketing testing, incubator demo day readiness.

## 6. Operational Risks & Competitive Moats
- **Risk Matrix & Mitigation Strategies:**
  - Regulatory / Compliance Risks & Mitigation.
  - Execution / Distribution Risks & Mitigation.
  - Technology / Scalability Risks & Mitigation.
- **Defensible Competitive Moats:** Proprietary data flywheels, high switching costs, network effects, or regulatory arbitrage.
"""

if submitted:
    if not problem_statement.strip():
        st.warning("Please provide a Market Problem Statement before generating.")
    else:
        user_prompt = f"""Synthesize an institutional-grade investment & execution memorandum based on these venture parameters:

- **Industry Vertical:** {sector}
- **Market Problem Statement:** {problem_statement.strip()}
- **Strategic Themes & Tech Pillars:** {themes_keywords.strip() if themes_keywords else 'None provided'}
- **Target Market Geography:** {target_region}
- **Selected Monetization Models:** {', '.join(monetization_models) if monetization_models else 'Open / Optimized by Architect'}
- **Capital Intensity & Risk Appetite:** {capital_intensity}

Produce the exhaustive memorandum now adhering strictly to the 6-pillar framework."""

        with st.spinner("Synthesizing Institutional Investment Memorandum via Groq LPU (llama-3.3-70b-versatile)..."):
            start_time = time.time()
            try:
                response = groq_client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.4,
                    max_tokens=6000
                )
                
                generation_duration = round(time.time() - start_time, 2)
                generated_memo = response.choices[0].message.content
                
                # Save to session state
                st.session_state["generated_memo"] = generated_memo
                st.session_state["generation_time"] = generation_duration
                st.session_state["generated_sector"] = sector
                
            except Exception as e:
                st.error(f"Groq API Error: {str(e)}")

# -------------------------------------------------------------
# DISPLAY GENERATED MEMORANDUM & EXPORT OPTIONS
# -------------------------------------------------------------
if "generated_memo" in st.session_state:
    st.write("")
    st.divider()
    
    # Telemetry Bar
    telemetry_col1, telemetry_col2, telemetry_col3 = st.columns([2, 1, 1])
    with telemetry_col1:
        st.success(f"✨ **Memorandum Synthesized Successfully** in **{st.session_state.get('generation_time', 0)}s** using `llama-3.3-70b-versatile`.")
    with telemetry_col2:
        st.caption(f"Sector: **{st.session_state.get('generated_sector', 'Venture')}**")
    with telemetry_col3:
        st.download_button(
            label="📥 Download Plan (.md)",
            data=st.session_state["generated_memo"],
            file_name=f"NIC_Venture_Memorandum_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
            mime="text/markdown",
            type="primary",
            use_container_width=True
        )

    # Render Markdown in container
    st.markdown('<div class="memo-output-wrapper">', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="memo-top-bar">
        <span class="memo-tag">🏛️ National Incubation Center • Official Dossier</span>
        <span class="memo-date">Synthesized: {datetime.now().strftime('%B %d, %Y | %H:%M UTC')}</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(st.session_state["generated_memo"])
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Bottom Download Option for Convenience
    st.write("")
    col_d1, col_d2, col_d3 = st.columns([1, 2, 1])
    with col_d2:
        st.download_button(
            label="📥 Download Full Memorandum as Markdown (.md)",
            data=st.session_state["generated_memo"],
            file_name=f"NIC_Venture_Memorandum_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
            mime="text/markdown",
            use_container_width=True
        )

# FIXED BOTTOM FOOTER
st.markdown("""
<div class="nic-footer-container">
    <p class="nic-footer-text">
        Developed for <span>National Incubation Center</span> | Built by <span>Alishba Naeem</span>
    </p>
</div>
""", unsafe_allow_html=True)
