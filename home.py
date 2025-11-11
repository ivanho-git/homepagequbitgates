import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Quantum Gate Simulator",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dark Mode Compatible CSS
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Main Header */
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        animation: fadeIn 1s ease-in;
    }
    
    .subtitle {
        text-align: center;
        color: var(--text-color);
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Section headers */
    .section-header {
        font-size: 2rem;
        font-weight: 700;
        color: #667eea;
        margin: 2rem 0 1rem 0;
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
    
    /* Info Boxes - Dark Mode Compatible */
    .info-box {
        background: rgba(102, 126, 234, 0.1);
        padding: 1.8rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #667eea;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .info-box:hover {
        transform: translateX(5px);
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.2);
    }
    
    .info-box h3 {
        font-weight: 700;
        font-size: 1.4rem;
        margin-bottom: 0.8rem;
        color: #667eea !important;
    }
    
    .info-box h4 {
        font-weight: 600;
        font-size: 1.2rem;
        margin-bottom: 0.5rem;
        color: #764ba2 !important;
    }
    
    /* Custom link button */
    .custom-link-button {
        display: inline-block;
        width: 100%;
        padding: 1.2rem 2rem;
        font-size: 1.3rem;
        font-weight: 700;
        color: white;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border: none;
        border-radius: 15px;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        box-shadow: 0 8px 25px rgba(245, 87, 108, 0.4);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .custom-link-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(245, 87, 108, 0.6);
        background: linear-gradient(135deg, #f5576c 0%, #f093fb 100%);
    }
    
    /* Feature boxes */
    .feature-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(245, 87, 108, 0.3);
        text-align: center;
    }
    
    .feature-box h2, .feature-box p {
        color: white !important;
    }
    
    /* Profile Cards */
    .profile-card {
        background: rgba(102, 126, 234, 0.05);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        text-align: center;
        transition: all 0.3s ease;
        border: 1px solid rgba(102, 126, 234, 0.2);
        height: 100%;
    }
    
    .profile-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.25);
    }
    
    .profile-img {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #667eea;
        margin-bottom: 1rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        margin-left: auto;
        margin-right: auto;
    }
    
    .profile-name {
        font-size: 1.3rem;
        font-weight: 700;
        color: #667eea;
        margin-bottom: 0.25rem;
    }
    
    .profile-role {
        font-size: 1rem;
        font-weight: 600;
        color: #764ba2;
        margin-bottom: 0.8rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2.5rem;
        }
        .info-box, .profile-card {
            margin-bottom: 1.5rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# === ANIMATED HEADER ===
st.markdown('<h1 class="main-header">⚛️ Quantum Gate Simulator</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Explore the fascinating world of quantum computing through interactive visualizations</p>', unsafe_allow_html=True)

# === APP OVERVIEW ===
st.markdown('<p class="section-header">What You Can Explore</p>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="info-box">
        <h4>⚡ Standard Gates</h4>
        <p>Experiment with fundamental quantum gates (X, Y, Z, H, S, T) and see how they manipulate qubit states in real-time.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-box">
        <h4>🌀 Rotation Gates</h4>
        <p>Visualize the effect of rotating qubits around X, Y, and Z axes with adjustable angles. Watch the Bloch sphere update dynamically.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-box">
        <h4>🔮 Faraday Rotator</h4>
        <p>Simulate the Faraday effect - observe how magnetic fields rotate the polarization of light and its quantum representation.</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="info-box">
        <h4>🔐 BB84 Protocol</h4>
        <p>Learn quantum key distribution by simulating the BB84 protocol and see how it enables absolutely secure communication.</p>
    </div>
    """, unsafe_allow_html=True)

# === MEET THE TEAM ===
st.markdown('<p class="section-header">Meet The Team</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="profile-card">
        <img src="https://github.com/ivanho-git/qubit-gates/blob/main/abhinav.jpeg?raw=true" class="profile-img">
        <p class="profile-name">ABHINAV SUNEESH</p>
        <p class="profile-role">BB84 in DFS Researcher</p>
        <p>Explores how BB84 operates within a Decoherence-Free Subspace.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="profile-card">
        <img src="https://github.com/ivanho-git/qubit-gates/blob/main/ibhann.jpeg?raw=true" class="profile-img">
        <p class="profile-name">IBHAN MUKHERJEE</p>
        <p class="profile-role">Security Analyst</p>
        <p>Tests quantum protocols for vulnerabilities and demonstrates detection of eavesdropping attempts.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="profile-card">
        <img src="https://github.com/ivanho-git/qubit-gates/blob/main/IMG-20251106-WA0032.jpg?raw=true" class="profile-img">
        <p class="profile-name">HARI ASHWIN</p>
        <p class="profile-role">Quantum Circuit Designer</p>
        <p>Designs and implements quantum circuits for gate and protocol simulations.</p>
    </div>
    """, unsafe_allow_html=True)

# === CALL TO ACTION ===
st.markdown("""
<div class="feature-box" style="margin-top: 3rem;">
    <h2>🚀 Ready to Enter the Quantum Realm?</h2>
    <p style="font-size: 1.2rem; margin-bottom: 2rem; opacity: 0.95;">
        Click below to start your quantum computing journey!
    </p>
    <a href="https://qubit-gates-ibhanmukh.streamlit.app/" target="_blank" style="text-decoration: none;">
        <button class="custom-link-button">ENTER THE QUANTUM REALM</button>
    </a>
</div>
""", unsafe_allow_html=True)

# === FOOTER ===
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; padding: 2rem 0; border-top: 2px solid rgba(102, 126, 234, 0.3); margin-top: 3rem;'>
        <p style='font-size: 1.1rem; margin-bottom: 0.5rem;'>Made By Engineers 👷🏻‍♂️ For Curiosity Not Just For Credits 😉</p>
        <p style='font-size: 0.9rem; opacity: 0.8;'>Visualizing quantum states on the Bloch sphere</p>
    </div>
""", unsafe_allow_html=True)
