import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Quantum Realm - Welcome",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Stunning CSS with animations
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Animated background */
    .stApp {
        background: linear-gradient(135deg, #0a0a1a 0%, #1a0a2e 50%, #0a0a1a 100%);
        animation: gradientShift 10s ease infinite;
        background-size: 200% 200%;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Hero Section */
    .hero-container {
        text-align: center;
        padding: 3rem 1rem;
        margin-top: 2rem;
    }
    
    .quantum-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 5rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        animation: titleFloat 3s ease-in-out infinite;
        text-shadow: 0 0 40px rgba(102, 126, 234, 0.5);
    }
    
    @keyframes titleFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    .quantum-subtitle {
        font-size: 1.8rem;
        color: #a8a8d8;
        margin-bottom: 2rem;
        font-weight: 300;
        animation: fadeIn 2s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    /* Glowing particle effect */
    .particle {
        position: fixed;
        width: 4px;
        height: 4px;
        background: #667eea;
        border-radius: 50%;
        pointer-events: none;
        animation: float 6s infinite;
        box-shadow: 0 0 20px #667eea;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0) translateX(0); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-100vh) translateX(100px); opacity: 0; }
    }
    
    /* Feature boxes */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
        padding: 0 2rem;
    }
    
    .feature-card {
        background: rgba(102, 126, 234, 0.1);
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 20px;
        padding: 2.5rem;
        text-align: center;
        transition: all 0.4s ease;
        backdrop-filter: blur(10px);
        position: relative;
        overflow: hidden;
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(102, 126, 234, 0.1) 0%, transparent 70%);
        animation: rotate 10s linear infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .feature-card:hover {
        transform: translateY(-10px) scale(1.02);
        border-color: #667eea;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
        background: rgba(102, 126, 234, 0.15);
    }
    
    .feature-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
        filter: drop-shadow(0 0 20px rgba(102, 126, 234, 0.6));
        animation: pulse 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    .feature-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #667eea;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .feature-desc {
        font-size: 1.1rem;
        color: #c8c8e8;
        line-height: 1.6;
        position: relative;
        z-index: 1;
    }
    
    /* Call to action button */
    .cta-container {
        text-align: center;
        margin: 4rem 0;
        padding: 3rem;
    }
    
    .quantum-button {
        display: inline-block;
        padding: 2rem 4rem;
        font-family: 'Orbitron', sans-serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: white;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        border-radius: 50px;
        cursor: pointer;
        text-decoration: none;
        box-shadow: 0 0 40px rgba(102, 126, 234, 0.6), 0 0 80px rgba(118, 75, 162, 0.4);
        transition: all 0.4s ease;
        text-transform: uppercase;
        letter-spacing: 3px;
        position: relative;
        overflow: hidden;
        animation: buttonGlow 2s ease-in-out infinite;
    }
    
    @keyframes buttonGlow {
        0%, 100% { box-shadow: 0 0 40px rgba(102, 126, 234, 0.6), 0 0 80px rgba(118, 75, 162, 0.4); }
        50% { box-shadow: 0 0 60px rgba(102, 126, 234, 0.8), 0 0 120px rgba(118, 75, 162, 0.6); }
    }
    
    .quantum-button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
        transition: left 0.5s;
    }
    
    .quantum-button:hover::before {
        left: 100%;
    }
    
    .quantum-button:hover {
        transform: scale(1.05) translateY(-5px);
        box-shadow: 0 0 60px rgba(102, 126, 234, 0.9), 0 0 120px rgba(118, 75, 162, 0.7);
    }
    
    /* Info section */
    .info-section {
        background: rgba(102, 126, 234, 0.05);
        border-radius: 30px;
        padding: 3rem;
        margin: 3rem 2rem;
        border: 1px solid rgba(102, 126, 234, 0.2);
        backdrop-filter: blur(10px);
    }
    
    .info-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        color: #667eea;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .info-text {
        font-size: 1.2rem;
        color: #d8d8e8;
        line-height: 1.8;
        text-align: center;
        max-width: 900px;
        margin: 0 auto;
    }
    
    /* Tech stack badges */
    .tech-stack {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        flex-wrap: wrap;
        margin: 2rem 0;
    }
    
    .tech-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.8rem 1.5rem;
        border-radius: 25px;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
    }
    
    .tech-badge:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .quantum-title {
            font-size: 3rem;
        }
        .quantum-subtitle {
            font-size: 1.3rem;
        }
        .quantum-button {
            font-size: 1.3rem;
            padding: 1.5rem 3rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero-container">
        <h1 class="quantum-title">⚛️ QUANTUM REALM</h1>
        <p class="quantum-subtitle">Journey into the Fascinating World of Quantum Computing</p>
    </div>
""", unsafe_allow_html=True)

# What is this app section
st.markdown("""
    <div class="info-section">
        <h2 class="info-title">What Awaits You?</h2>
        <p class="info-text">
            Step into an interactive quantum laboratory where complex quantum mechanics concepts come alive. 
            Our Quantum Gate Simulator transforms abstract quantum theory into visual, hands-on experiences. 
            Whether you're a curious beginner or an advanced learner, explore quantum gates, visualize qubit states 
            on the Bloch sphere, and witness the magic of quantum cryptography—all through an intuitive, 
            beautifully designed interface.
        </p>
    </div>
""", unsafe_allow_html=True)

# Feature Grid
st.markdown('<div class="feature-grid">', unsafe_allow_html=True)

features = [
    {
        "icon": "🎯",
        "title": "Standard Quantum Gates",
        "desc": "Experiment with Pauli gates (X, Y, Z), Hadamard, Phase gates, and more. See how each gate transforms qubit states in real-time."
    },
    {
        "icon": "🌀",
        "title": "Rotation Gates",
        "desc": "Control precise rotations around X, Y, and Z axes. Watch animated transitions as qubits evolve through continuous transformations."
    },
    {
        "icon": "🔮",
        "title": "Faraday Rotator",
        "desc": "Simulate polarization rotation using magnetic fields. Explore the quantum-classical connection through optical phenomena."
    },
    {
        "icon": "🔐",
        "title": "BB84 Protocol",
        "desc": "Discover quantum cryptography! Learn how BB84 enables unbreakable quantum key distribution and secure communication."
    },
    {
        "icon": "📊",
        "title": "Bloch Sphere",
        "desc": "Visualize quantum states geometrically on the Bloch sphere. Understand superposition and phase in an intuitive 3D representation."
    },
    {
        "icon": "⚡",
        "title": "Real-Time Simulation",
        "desc": "Experience instant feedback with high-performance quantum state calculations powered by Qiskit's cutting-edge algorithms."
    }
]

cols = st.columns(3)
for idx, feature in enumerate(features):
    with cols[idx % 3]:
        st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{feature['icon']}</div>
                <h3 class="feature-title">{feature['title']}</h3>
                <p class="feature-desc">{feature['desc']}</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Tech Stack
st.markdown("""
    <div class="info-section">
        <h2 class="info-title">Built With Cutting-Edge Technology</h2>
        <div class="tech-stack">
            <span class="tech-badge">🐍 Python</span>
            <span class="tech-badge">⚛️ Qiskit</span>
            <span class="tech-badge">🎨 Streamlit</span>
            <span class="tech-badge">📊 Matplotlib</span>
            <span class="tech-badge">🔢 NumPy</span>
            <span class="tech-badge">🎭 Quantum Mechanics</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Call to Action
st.markdown("""
    <div class="cta-container">
        <a href="https://qubit-gates-ibhanmukh.streamlit.app/" target="_blank" style="text-decoration: none;">
            <button class="quantum-button">
                🚀 ENTER THE QUANTUM REALM
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

# Footer section
st.markdown("""
    <div class="info-section" style="margin-top: 4rem;">
        <h2 class="info-title">Made by Engineers 👷🏻‍♂️</h2>
        <p class="info-text" style="font-size: 1.1rem; margin-bottom: 0.5rem;">
            For Curiosity, Not Just For Credits 😉
        </p>
        <p class="info-text" style="font-size: 0.95rem; opacity: 0.8;">
            A collaborative project by passionate students exploring the quantum frontier
        </p>
    </div>
""", unsafe_allow_html=True)
