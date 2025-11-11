import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Quantum Gate Simulator — Home",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Styling (Dark mode friendly)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    * { font-family: 'Poppins', sans-serif; }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .main-header {
        font-size: 3.2rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0.25rem 0 0.5rem 0;
        animation: fadeIn 0.9s ease-in;
    }
    .subtitle {
        text-align: center;
        color: rgba(255,255,255,0.85);
        font-size: 1.1rem;
        margin-bottom: 1.2rem;
        font-weight: 300;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-8px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .gradient-hero {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 22px;
        color: white !important;
        padding: 2.2rem;
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.35);
        text-align: center;
        margin-bottom: 1rem;
    }
    .gradient-hero h1, .gradient-hero p { color: white !important; }

    .section-header {
        font-size: 1.9rem;
        font-weight: 800;
        color: #667eea;
        margin: 1.8rem 0 1rem 0;
        text-align: center;
        position: relative;
    }
    .section-header::after {
        content: '';
        display: block;
        width: 100px;
        height: 4px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin: 0.5rem auto;
        border-radius: 2px;
    }

    .feature-card {
        background: rgba(102, 126, 234, 0.08);
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-radius: 16px;
        padding: 1.2rem;
        height: 100%;
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
        transition: all 0.25s ease;
    }
    .feature-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 14px 32px rgba(102, 126, 234, 0.25);
    }
    .feature-card h3 {
        color: #667eea !important;
        margin-bottom: 0.35rem;
    }
    .feature-card p {
        font-size: 0.98rem;
        opacity: 0.95;
        margin-top: 0.35rem;
    }
    .mini-badge {
        display: inline-block;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
        font-weight: 700;
        font-size: 0.8rem;
        padding: 0.25rem 0.6rem;
        border-radius: 999px;
        margin-bottom: 0.6rem;
    }

    .info-box {
        background: rgba(102, 126, 234, 0.1);
        padding: 1.2rem;
        border-radius: 15px;
        margin: 0.6rem 0;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.08);
        border-left: 5px solid #667eea;
    }
    .info-box h4 {
        color: #667eea !important;
        margin-bottom: 0.4rem;
    }

    .custom-link-button {
        display: inline-block;
        width: 100%;
        padding: 1.1rem 2rem;
        font-size: 1.25rem;
        font-weight: 800;
        color: white !important;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border: none;
        border-radius: 14px;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        box-shadow: 0 10px 26px rgba(245, 87, 108, 0.35);
        transition: all 0.25s ease;
        letter-spacing: 1px;
    }
    .custom-link-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 14px 36px rgba(245, 87, 108, 0.55);
        background: linear-gradient(135deg, #f5576c 0%, #f093fb 100%);
    }

    .footer {
        text-align: center;
        padding: 1.2rem 0 0.4rem 0;
        border-top: 2px solid rgba(102, 126, 234, 0.25);
        margin-top: 2.2rem;
        opacity: 0.9;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">⚛ Quantum Gate Simulator</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">A beautiful, interactive way to learn qubits, gates, rotations, optical physics, and BB84 quantum cryptography.</p>', unsafe_allow_html=True)

# Hero
st.markdown("""
<div class="gradient-hero">
    <h1 style="margin-top: 0;">Welcome to the Quantum Realm</h1>
    <p style="font-size: 1.1rem; opacity: 0.95; max-width: 860px; margin: 0 auto;">
        Explore core quantum concepts with real-time visuals:
        apply standard gates, rotate qubits on the Bloch sphere, simulate the Faraday effect,
        and dive into BB84 quantum key distribution — all in one app.
    </p>
</div>
""", unsafe_allow_html=True)

# CTA Button (centered)
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    # Use st.link_button when available; fallback to styled anchor
    if getattr(st, "link_button", None):
        st.link_button("🚀 Enter the Quantum Realm", "https://qubit-gates-ibhanmukh.streamlit.app/")
    else:
        st.markdown("""
            <a href="https://qubit-gates-ibhanmukh.streamlit.app/" target="_blank" class="custom-link-button">
                🚀 Enter the Quantum Realm
            </a>
        """, unsafe_allow_html=True)

st.markdown('<p style="text-align:center; opacity:0.85; margin-top: 0.35rem;">Opens the full app in a new tab</p>', unsafe_allow_html=True)

# What's inside
st.markdown('<p class="section-header">What You Can Explore</p>', unsafe_allow_html=True)
a, b, c = st.columns(3)
with a:
    st.markdown("""
    <div class="feature-card">
        <span class="mini-badge">🎯 Module</span>
        <h3>Standard Quantum Gates</h3>
        <p>Apply X, Y, Z, H, S, T (and inverses) to |0⟩, |1⟩, |+⟩, |−⟩. 
        See amplitudes, probabilities, and a Bloch-sphere view — plus circuit diagrams.</p>
    </div>
    """, unsafe_allow_html=True)
with b:
    st.markdown("""
    <div class="feature-card">
        <span class="mini-badge">🌀 Module</span>
        <h3>Rotation Gates</h3>
        <p>Rotate around X, Y, or Z by a custom angle (degrees or radians).
        Watch smooth animation of state evolution and track |α|² and |β|².</p>
    </div>
    """, unsafe_allow_html=True)
with c:
    st.markdown("""
    <div class="feature-card">
        <span class="mini-badge">🔮 Module</span>
        <h3>Faraday Rotator</h3>
        <p>Simulate polarization rotation with Verdet constant, magnetic field, and path length.
        Dual-view plots and an optional animation bring the physics to life.</p>
    </div>
    """, unsafe_allow_html=True)

d, e = st.columns(2)
with d:
    st.markdown("""
    <div class="feature-card">
        <span class="mini-badge">🔐 Module</span>
        <h3>BB84 Protocol</h3>
        <p>Understand the steps of quantum key distribution: transmission, basis reconciliation,
        error checking, and privacy amplification — with an external live simulator.</p>
    </div>
    """, unsafe_allow_html=True)
with e:
    st.markdown("""
    <div class="feature-card">
        <span class="mini-badge">🧑‍🔬 Info</span>
        <h3>About & Team</h3>
        <p>Meet the minds behind the project and learn about the motivation, design choices,
        and where to explore next.</p>
    </div>
    """, unsafe_allow_html=True)

# How it feels to use
st.markdown('<p class="section-header">Why You’ll Love This App</p>', unsafe_allow_html=True)
col_l, col_r = st.columns(2)
with col_l:
    st.markdown("""
    <div class="info-box">
        <h4>✨ Intuitive Visuals</h4>
        <p>Bespoke UI, gradients, and clean metrics make quantum states less abstract and more relatable.</p>
    </div>
    <div class="info-box">
        <h4>⚛️ Concept-to-Circuit</h4>
        <p>See the mapping from math to circuits to Bloch-sphere states all in one place.</p>
    </div>
    """, unsafe_allow_html=True)
with col_r:
    st.markdown("""
    <div class="info-box">
        <h4>🧪 Guided Exploration</h4>
        <p>From basic gates to rotations to optical effects — build intuition step by step.</p>
    </div>
    <div class="info-box">
        <h4>🔐 Real-World Relevance</h4>
        <p>Connect core quantum mechanics with modern cryptography via BB84.</p>
    </div>
    """, unsafe_allow_html=True)

# Quick start steps
st.markdown('<p class="section-header">Quick Start</p>', unsafe_allow_html=True)
st.markdown("""
- Pick a module that interests you (e.g., Standard Gates or Rotation Gates).
- Choose an initial state and apply a gate or rotation.
- Read the metrics, study the Bloch sphere, and inspect the circuit diagram.
- Jump to the Faraday Rotator to relate qubit phases to polarization rotation.
- Explore the BB84 section to see how quantum rules enable secure communication.
""")

# Second CTA Button (centered)
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    if getattr(st, "link_button", None):
        st.link_button("🧭 Take me to the App", "https://qubit-gates-ibhanmukh.streamlit.app/")
    else:
        st.markdown("""
            <a href="https://qubit-gates-ibhanmukh.streamlit.app/" target="_blank" class="custom-link-button">
                🧭 Take me to the App
            </a>
        """, unsafe_allow_html=True)

# FAQ
with st.expander("FAQ — What do I need to run this?"):
    st.write("- A modern browser. No installs required for the deployed app.")
    st.write("- For local dev, you'll need Python, Streamlit, Qiskit, NumPy, and Matplotlib.")
with st.expander("FAQ — Is this suitable for teaching?"):
    st.write("Yes! The visuals, animations, and metrics are designed for classrooms, workshops, and self-learning.")
with st.expander("FAQ — Can I contribute or extend it?"):
    st.write("Absolutely. Add new gates, more rotations (e.g., composite sequences), or new optical components.")

# Footer
st.markdown("""
    <div class="footer">
        <p style='font-size: 1.05rem; margin-bottom: 0.4rem;'>Made By Engineers 👷🏻‍♂️ For Curiosity Not Just For Credits 😉</p>
        <p style='font-size: 0.9rem; opacity: 0.85;'>Quantum visuals | Bloch sphere | QKD (BB84) | Built with Streamlit</p>
    </div>
""", unsafe_allow_html=True)
