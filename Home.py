import streamlit as st

# Configure page settings
st.set_page_config(
    page_title="NIC Venture Forge",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Corporate CSS for National Incubation Center (Blue/Slate Theme)
st.markdown("""
<style>
    /* Google Fonts import */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Main Container Padding */
    .block-container {
        padding-top: 1.8rem;
        padding-bottom: 5.5rem;
        max-width: 1200px;
    }

    /* Hero Banner Styling */
    .nic-hero {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 58, 138, 0.85) 50%, rgba(15, 23, 42, 0.95) 100%);
        border: 1px solid rgba(59, 130, 246, 0.3);
        border-radius: 18px;
        padding: 3rem 2.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.5), 0 0 30px rgba(37, 99, 235, 0.15);
        position: relative;
        overflow: hidden;
    }

    .nic-hero::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 350px;
        height: 350px;
        background: radial-gradient(circle, rgba(37, 99, 235, 0.25) 0%, transparent 70%);
        pointer-events: none;
    }

    .nic-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(37, 99, 235, 0.2);
        border: 1px solid rgba(96, 165, 250, 0.4);
        color: #93C5FD;
        padding: 6px 14px;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 1.2rem;
    }

    .nic-hero h1 {
        font-size: 2.85rem;
        font-weight: 800;
        color: #FFFFFF;
        line-height: 1.15;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
    }

    .nic-hero p {
        font-size: 1.15rem;
        color: #CBD5E1;
        line-height: 1.6;
        max-width: 820px;
        margin-bottom: 1.8rem;
    }

    /* Action Banner */
    .nic-cta-box {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(148, 163, 184, 0.2);
        border-radius: 12px;
        padding: 1.2rem 1.6rem;
        backdrop-filter: blur(10px);
    }

    .nic-cta-text {
        color: #E2E8F0;
        font-size: 0.98rem;
        font-weight: 500;
    }

    .nic-cta-highlight {
        color: #60A5FA;
        font-weight: 700;
    }

    /* Feature Cards */
    .feature-card {
        background: linear-gradient(180deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.8) 100%);
        border: 1px solid rgba(51, 65, 85, 0.8);
        border-radius: 14px;
        padding: 1.6rem;
        height: 100%;
        transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
    }

    .feature-card:hover {
        transform: translateY(-4px);
        border-color: rgba(96, 165, 250, 0.6);
        box-shadow: 0 12px 24px -10px rgba(37, 99, 235, 0.25);
    }

    .feature-icon {
        width: 44px;
        height: 44px;
        background: rgba(37, 99, 235, 0.18);
        border: 1px solid rgba(59, 130, 246, 0.35);
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.35rem;
        margin-bottom: 1rem;
    }

    .feature-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 0.5rem;
    }

    .feature-desc {
        font-size: 0.9rem;
        color: #94A3B8;
        line-height: 1.55;
    }

    /* Metric Cards Custom Styling */
    div[data-testid="stMetric"] {
        background: rgba(19, 28, 49, 0.75);
        border: 1px solid rgba(51, 65, 85, 0.7);
        border-radius: 12px;
        padding: 1rem 1.25rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }

    div[data-testid="stMetricLabel"] p {
        color: #94A3B8 !important;
        font-size: 0.82rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 600;
    }

    div[data-testid="stMetricValue"] div {
        color: #60A5FA !important;
        font-weight: 800 !important;
        font-size: 1.85rem !important;
    }

    div[data-testid="stMetricDelta"] {
        font-size: 0.8rem !important;
    }

    /* Guide Box */
    .guide-step {
        display: flex;
        align-items: flex-start;
        gap: 14px;
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(51, 65, 85, 0.6);
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 0.85rem;
    }

    .step-number {
        background: #2563EB;
        color: #FFFFFF;
        width: 32px;
        height: 32px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.95rem;
        flex-shrink: 0;
    }

    .step-content h4 {
        margin: 0 0 4px 0;
        font-size: 1rem;
        color: #F1F5F9;
        font-weight: 600;
    }

    .step-content p {
        margin: 0;
        font-size: 0.88rem;
        color: #94A3B8;
        line-height: 1.45;
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

# Sidebar Navigation & Branding
with st.sidebar:
    st.image(
        "https://images.unsplash.com/photo-1557804506-669a67965ba0?w=600&auto=format&fit=crop&q=80",
        caption="NIC Venture Forge Lab",
        use_container_width=True
    )
    st.markdown("### 🏢 National Incubation Center")
    st.caption("Empowering Visionary Founders Across Emerging Markets")
    
    st.divider()
    
    st.markdown("#### 🧭 Platform Navigation")
    st.info("👈 **Select Mode from Sidebar:**\n\nClick on **`1_💡_Startup_Generator`** above to formulate institutional-grade startup investment & execution memoranda.")
    
    st.divider()
    
    st.markdown("#### ⚡ Hardware Engine Specs")
    st.markdown("""
    - **Hardware:** Groq Tensor Streaming Processor (LPU™)
    - **Model:** `llama-3.3-70b-versatile`
    - **Context Window:** 128,000 tokens
    - **Throughput:** ~750 tokens/sec
    """)

# HERO SECTION
st.markdown("""
<div class="nic-hero">
    <div class="nic-badge">
        <span>⚡</span> NATIONAL INCUBATION CENTER • VENTURE ARCHITECTURE AI
    </div>
    <h1>NIC Venture Forge</h1>
    <p>
        The National Incubation Center's AI-powered Venture Architecture Engine. Built for venture builders, 
        incubators, and founders, NIC Venture Forge transforms raw problems and disruptive ideas into 
        institutional-grade startup investment and execution memoranda in sub-second inference speeds.
    </p>
    <div class="nic-cta-box">
        <div class="nic-cta-text">
            🚀 <strong>Ready to architect your venture?</strong> Switch to the <span class="nic-cta-highlight">💡 Startup Generator</span> in the left sidebar to begin.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# REAL-TIME PLATFORM & LATENCY METRICS
st.markdown("### 📊 Platform Architecture & Performance Telemetry")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Groq LPU Latency",
        value="~280 ms",
        delta="-85% vs Cloud GPUs",
        delta_color="normal",
        help="Ultra-low first-token latency delivered by Groq Language Processing Unit (LPU) architecture."
    )

with col2:
    st.metric(
        label="Generation Velocity",
        value="~750 T/s",
        delta="Real-Time Streaming",
        delta_color="normal",
        help="Throughput velocity of the LLaMA 3.3 70B parameter engine."
    )

with col3:
    st.metric(
        label="Venture Depth",
        value="6 Core Pillars",
        delta="Institutional Standard",
        delta_color="normal",
        help="Comprehensive investment memo covering ICP, Unit Economics, MVP Tech, and Moats."
    )

with col4:
    st.metric(
        label="Incubation Readiness",
        value="100% Cohort Ready",
        delta="NIC Framework Aligned",
        delta_color="normal",
        help="Engine calibrated to National Incubation Center investment committee standards."
    )

st.write("")
st.write("")

# PLATFORM FEATURE BREAKDOWN
st.markdown("### 🏛️ Venture Memorandum Architecture Breakdown")
st.markdown("Every venture synthesized through the platform undergoes rigorous structural formulation across 6 core pillars:")

f_col1, f_col2, f_col3 = st.columns(3)

with f_col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💎</div>
        <div class="feature-title">1. Executive Blueprint & Value Prop</div>
        <div class="feature-desc">
            Venture nomenclature, core identity, high-impact elevator pitch, and unique value proposition (UVP) calibrated for angel syndicates and venture funds.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💰</div>
        <div class="feature-title">4. Unit Economics & Monetization</div>
        <div class="feature-desc">
            Rigorous pricing dynamics, CAC:LTV estimates, gross margin targets, multi-tiered revenue models, and runway requirements based on capital intensity.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f_col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">2. Market Problem & ICP Profiling</div>
        <div class="feature-desc">
            Root-cause breakdown of market frictions, Total Addressable Market (TAM) indicators, and granular Ideal Customer Profiles (B2B buyer persona or consumer segment).
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🗺️</div>
        <div class="feature-title">5. 90-Day GTM Execution Roadmap</div>
        <div class="feature-desc">
            Phased sprint timeline (Days 1-30, 31-60, 61-90) detailing design-partner acquisition, pilot deployments, distribution channels, and cohort graduation metrics.
        </div>
    </div>
    """, unsafe_allow_html=True)

with f_col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">3. MVP Technical Architecture</div>
        <div class="feature-desc">
            Production-grade system topology: Recommended modern tech stack, frontend & backend frameworks, database persistence, and external APIs.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🛡️</div>
        <div class="feature-title">6. Operational Risks & Moats</div>
        <div class="feature-desc">
            Identification of regulatory, technical, and execution risks alongside concrete risk-mitigation vectors and defensible network effects.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# HOW TO USE / WORKFLOW
st.markdown("### 📋 How to Architect Your Startup")

step1, step2, step3 = st.columns(3)

with step1:
    st.markdown("""
    <div class="guide-step">
        <div class="step-number">1</div>
        <div class="step-content">
            <h4>Select Generator in Sidebar</h4>
            <p>Click on <code>1_💡_Startup_Generator</code> in the left sidebar menu to open the active generator studio.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with step2:
    st.markdown("""
    <div class="guide-step">
        <div class="step-number">2</div>
        <div class="step-content">
            <h4>Configure Parameters</h4>
            <p>Define your core problem, domain keywords, industry sector, target geographic region, and monetization preferences.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with step3:
    st.markdown("""
    <div class="guide-step">
        <div class="step-number">3</div>
        <div class="step-content">
            <h4>Synthesize & Export Memo</h4>
            <p>Generate the full investment memorandum in seconds and download it directly as a ready-to-share Markdown document.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Direct launch action button
st.write("")
col_cta1, col_cta2, col_cta3 = st.columns([1, 2, 1])
with col_cta2:
    if st.button("🚀 Proceed to Startup Generator", type="primary", use_container_width=True):
        st.switch_page("pages/1_💡_Startup_Generator.py")

# FIXED BOTTOM FOOTER
st.markdown("""
<div class="nic-footer-container">
    <p class="nic-footer-text">
        Developed for <span>National Incubation Center</span> | Built by <span>Alishba Naeem</span>
    </p>
</div>
""", unsafe_allow_html=True)
