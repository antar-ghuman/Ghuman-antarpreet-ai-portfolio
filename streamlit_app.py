import streamlit as st
import time
import json
from groq import Groq
import os

# Page configuration
st.set_page_config(
    page_title="Antarpreet Kaur Ghuman - AI/ML Engineer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Advanced CSS with impressive visuals
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    
    /* Advanced gradient background with moving patterns */
    .stApp {
        background: 
            radial-gradient(circle at 20% 50%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 40% 80%, rgba(120, 198, 161, 0.3) 0%, transparent 50%),
            linear-gradient(135deg, #0f0f23 0%, #1a1a2e 25%, #16213e 50%, #1a1a2e 75%, #0f0f23 100%);
        background-size: 200% 200%, 200% 200%, 200% 200%, 400% 400%;
        animation: 
            gradientMove1 8s ease infinite,
            gradientMove2 12s ease infinite reverse,
            gradientMove3 10s ease infinite,
            mainGradient 15s ease infinite;
        color: #ffffff;
        font-family: 'Space Grotesk', sans-serif;
        min-height: 100vh;
    }
    
    @keyframes gradientMove1 {
        0%, 100% { background-position: 0% 50%, 100% 50%, 50% 0%, 0% 50%; }
        50% { background-position: 100% 50%, 0% 50%, 50% 100%, 100% 50%; }
    }
    
    @keyframes gradientMove2 {
        0%, 100% { background-position: 50% 0%, 50% 100%, 0% 50%, 50% 0%; }
        50% { background-position: 50% 100%, 50% 0%, 100% 50%, 50% 100%; }
    }
    
    @keyframes gradientMove3 {
        0%, 100% { background-position: 0% 0%, 100% 100%, 0% 100%, 0% 0%; }
        50% { background-position: 100% 100%, 0% 0%, 100% 0%, 100% 100%; }
    }
    
    @keyframes mainGradient {
        0%, 100% { background-position: 0% 50%, 0% 50%, 0% 50%, 0% 50%; }
        50% { background-position: 100% 50%, 100% 50%, 100% 50%, 100% 50%; }
    }
    
    /* Floating particles system */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
    }
    
    .particle {
        position: absolute;
        background: rgba(120, 119, 198, 0.6);
        border-radius: 50%;
        animation: float 6s infinite ease-in-out;
    }
    
    @keyframes float {
        0%, 100% { 
            transform: translateY(0px) rotate(0deg); 
            opacity: 1; 
        }
        50% { 
            transform: translateY(-20px) rotate(180deg); 
            opacity: 0.5; 
        }
    }
    
    /* Hero section with advanced typography */
    .hero-container {
        position: relative;
        text-align: center;
        padding: 6rem 2rem 4rem;
        z-index: 10;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    
    .hero-bg-effect {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(120, 119, 198, 0.1) 0%, rgba(255, 119, 198, 0.05) 50%, transparent 100%);
        border-radius: 50%;
        animation: pulseGlow 4s ease-in-out infinite;
        z-index: -1;
    }
    
    @keyframes pulseGlow {
        0%, 100% { transform: translate(-50%, -50%) scale(1); opacity: 0.5; }
        50% { transform: translate(-50%, -50%) scale(1.1); opacity: 0.8; }
    }
    
    .name-display {
        font-size: 4.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #7877c6, #ff77c6, #77c6a1, #c677ff);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: rainbowText 3s ease-in-out infinite;
        letter-spacing: -0.02em;
        text-shadow: 0 0 30px rgba(120, 119, 198, 0.5);
    }
    
    @keyframes rainbowText {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .title-role {
        font-size: 1.6rem;
        color: #b8b8ff;
        font-weight: 500;
        margin-bottom: 2rem;
        letter-spacing: 0.1em;
        text-transform: uppercase;
    }
    
    .hero-description {
        font-size: 1.2rem;
        color: #e0e0ff;
        max-width: 700px;
        margin: 0 auto 3rem;
        line-height: 1.8;
        opacity: 0.9;
        text-align: center;
    }
    
    /* Skills showcase with interactive elements */
    .skills-showcase {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 1rem;
        max-width: 800px;
        margin: 2rem auto;
        padding: 0 2rem;
    }
    
    .skill-badge {
        background: rgba(120, 119, 198, 0.2);
        border: 1px solid rgba(120, 119, 198, 0.4);
        border-radius: 25px;
        padding: 0.8rem 1.2rem;
        text-align: center;
        font-weight: 500;
        font-size: 0.9rem;
        color: #d0d0ff;
        transition: all 0.3s ease;
        cursor: pointer;
        backdrop-filter: blur(10px);
    }
    
    .skill-badge:hover {
        background: rgba(120, 119, 198, 0.4);
        border-color: #7877c6;
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 10px 25px rgba(120, 119, 198, 0.3);
        color: #ffffff;
    }
    
    /* Experience cards with glassmorphism */
    .experience-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        gap: 2.5rem;
        max-width: 1400px;
        margin: 4rem auto;
        padding: 0 2rem;
    }
    
    .experience-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2.5rem;
        position: relative;
        transition: all 0.4s ease;
        overflow: hidden;
    }
    
    .experience-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(120, 119, 198, 0.1) 0%, rgba(255, 119, 198, 0.05) 100%);
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    
    .experience-card:hover {
        transform: translateY(-10px) rotateX(5deg);
        border-color: rgba(120, 119, 198, 0.5);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
    }
    
    .experience-card:hover::before {
        opacity: 1;
    }
    
    .card-header {
        position: relative;
        z-index: 2;
        margin-bottom: 1.5rem;
    }
    
    .card-icon {
        font-size: 3.5rem;
        margin-bottom: 1rem;
        display: block;
        background: linear-gradient(135deg, #7877c6, #ff77c6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .card-title {
        font-size: 1.6rem;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    
    .card-company {
        font-size: 1rem;
        color: #b8b8ff;
        font-weight: 500;
        margin-bottom: 1rem;
    }
    
    .card-description {
        color: #e0e0ff;
        line-height: 1.6;
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 2;
    }
    
    .tech-stack {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        position: relative;
        z-index: 2;
    }
    
    .tech-item {
        background: rgba(120, 119, 198, 0.3);
        color: #d0d0ff;
        padding: 0.4rem 0.8rem;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 500;
        border: 1px solid rgba(120, 119, 198, 0.4);
    }
    
    /* Enhanced AI chat section */
    .ai-chat-container {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(25px);
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 3rem;
        margin: 4rem auto;
        max-width: 1000px;
        position: relative;
        overflow: hidden;
    }
    
    .ai-chat-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(120, 119, 198, 0.05), transparent);
        animation: rotate 10s linear infinite;
        z-index: -1;
    }
    
    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .chat-title {
        font-size: 2.5rem;
        font-weight: 600;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #7877c6, #ff77c6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .chat-subtitle {
        text-align: center;
        color: #b8b8ff;
        margin-bottom: 2rem;
        font-size: 1.1rem;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .name-display { font-size: 3rem; }
        .experience-grid { grid-template-columns: 1fr; }
        .skills-showcase { grid-template-columns: repeat(auto-fit, minmax(100px, 1fr)); }
    }
</style>
""", unsafe_allow_html=True)

# Initialize Groq client
@st.cache_resource
def init_groq_client():
    # You'll need to set your Groq API key
    # Either set it as environment variable or through Streamlit secrets
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        return client
    except:
        st.warning("🔑 Please set your Groq API key in Streamlit secrets to enable AI responses")
        return None

# Antarpreet's resume data for context
RESUME_CONTEXT = """
Antarpreet Kaur Ghuman has an MS in Robotics & AI and 5+ years of tech experience. She is currently an AI/ML Engineer at Sanmina (1 year) and was previously a Software Engineer at Dell Technologies (4 years).

CURRENT ROLE: AI/ML Engineer at Sanmina (Jul 2024 - Present)
- Applied self-supervised learning pipelines for 3D medical image segmentation using MONAI
- Benchmarked Auto3Dseg models (DINTS, SwinUNetR, SegResNet) 
- Engineered face analytics using MTCNN and MediaPipe
- Implemented Distributed Data Parallel (DDP) training, reducing training time by 53.5%
- Applied Stable Diffusion and StyleGAN for medical text-to-image synthesis
- Deployed Kubeflow on Kubernetes for ML pipelines

PREVIOUS ROLES:
- Graduate Research Assistant at UB AI Lab (Oct 2023 - June 2024): Vector Quantized Diffusion model for chest X-ray synthesis
- Software Engineer 2 at Dell Technologies (Jul 2018 - Aug 2022): IoT Core Containerization, achieved 80% startup time reduction

EDUCATION:
- MS in Robotics & AI, University at Buffalo (2022-2024)
- BE Computer Science, Chandigarh University (2014-2018)

KEY PROJECTS:
- AI-Driven Speech Therapy Simulator (Master's Thesis): BART for sequence-to-sequence modeling
- Computer Vision projects: Face clustering with 91% accuracy, facial analysis systems
- Robotics: RRT pathfinding, PID controllers, stereo odometry
- Cloud/API projects: Tweet translator, real-time log management

TECHNICAL SKILLS:
Languages: Java, Python, HTML/CSS, JavaScript, C++, SQL
AI/ML: OpenCV, TensorFlow, PyTorch, Keras, Scikit-learn, MONAI, ROS
Cloud: Kubernetes, Docker, AWS, GCP, Kubeflow
Frameworks: Spring Boot, REST APIs, Kafka, ElasticSearch

LEADERSHIP:
- Google Women Techmakers Ambassador
- Selected for Dell IT Development Program (27 of 500+ participants)
- Google Cloud Digital Leader Certification
- Gen AI Intensive Course with Kaggle and Google
"""

def get_ai_response(user_question, groq_client):
    if not groq_client:
        return "I need a Groq API key to provide intelligent responses. Please check the setup instructions."
    
    try:
        completion = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": f"""You are Antarpreet's portfolio assistant. Use this resume information to answer questions accurately:

{RESUME_CONTEXT}

Guidelines:
- Only provide information that's in the resume
- Be specific about projects, achievements, and technologies
- If asked about something not in the resume, say you don't have that information
- Keep responses conversational but professional
- Include specific metrics and achievements when relevant"""
                },
                {
                    "role": "user",
                    "content": user_question
                }
            ],
            temperature=0.7,
            max_tokens=500
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hi! I'm Antarpreet's AI assistant. I can answer questions about her experience in AI/ML, robotics, computer vision, and software engineering. What would you like to know?"}
    ]

# Initialize Groq client
groq_client = init_groq_client()

# Add floating particles
st.markdown("""
<div class="particles" id="particles"></div>
<script>
    function createParticles() {
        const container = document.getElementById('particles');
        if (!container) return;
        
        for (let i = 0; i < 20; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.top = Math.random() * 100 + '%';
            particle.style.width = Math.random() * 4 + 2 + 'px';
            particle.style.height = particle.style.width;
            particle.style.animationDelay = Math.random() * 6 + 's';
            particle.style.animationDuration = Math.random() * 3 + 4 + 's';
            container.appendChild(particle);
        }
    }
    
    // Create particles when page loads
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', createParticles);
    } else {
        createParticles();
    }
</script>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-container">
    <div class="hero-bg-effect"></div>
    <h1 class="name-display">Antarpreet Kaur Ghuman</h1>
    <p class="title-role">AI/ML Engineer | WTM Ambassador</p>
    <p class="hero-description">
        MS in Robotics & AI graduate with 5+ years of experience in tech. Currently working as an AI/ML Engineer 
        at Sanmina, having transitioned from 4 years as a Software Engineer at Dell Technologies. 
        Passionate about applying cutting-edge AI research to solve real-world problems in medical imaging, 
        computer vision, and robotics. Always eager to learn new technologies and tackle challenging projects.
    </p>
</div>
""", unsafe_allow_html=True)

# Skills Showcase
st.markdown("""
<div class="skills-showcase">
    <div class="skill-badge">Python</div>
    <div class="skill-badge">PyTorch</div>
    <div class="skill-badge">TensorFlow</div>
    <div class="skill-badge">OpenCV</div>
    <div class="skill-badge">MONAI</div>
    <div class="skill-badge">Kubernetes</div>
    <div class="skill-badge">Docker</div>
    <div class="skill-badge">ROS</div>
    <div class="skill-badge">AWS</div>
    <div class="skill-badge">GCP</div>
</div>
""", unsafe_allow_html=True)
# AI Chat Section (moved up)
st.markdown("""
<div class="ai-chat-container">
    <h2 class="chat-title">🤖 AI Portfolio Assistant</h2>
    <p class="chat-subtitle">Powered by Groq AI • Ask anything about Antarpreet's experience</p>
</div>
""", unsafe_allow_html=True)

# Chat messages with enhanced styling
st.markdown("""
<style>
    .chat-messages {
        background: rgba(0, 0, 0, 0.4);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem 0;
        max-height: 500px;
        overflow-y: auto;
        border: 1px solid rgba(120, 119, 198, 0.3);
        backdrop-filter: blur(10px);
    }
    
    .user-message-enhanced {
        background: linear-gradient(135deg, #7877c6, #ff77c6);
        color: white;
        padding: 1.2rem 1.8rem;
        border-radius: 20px 20px 5px 20px;
        margin: 1rem 0 1rem auto;
        max-width: 75%;
        font-size: 1rem;
        line-height: 1.5;
        box-shadow: 0 4px 15px rgba(120, 119, 198, 0.3);
    }
    
    .assistant-message-enhanced {
        background: rgba(120, 119, 198, 0.2);
        color: #ffffff;
        padding: 1.2rem 1.8rem;
        border-radius: 20px 20px 20px 5px;
        margin: 1rem auto 1rem 0;
        max-width: 75%;
        border: 1px solid rgba(120, 119, 198, 0.4);
        font-size: 1rem;
        line-height: 1.6;
        backdrop-filter: blur(15px);
    }
    
    .stTextInput > div > div > input {
        background: rgba(120, 119, 198, 0.15) !important;
        border: 2px solid rgba(120, 119, 198, 0.4) !important;
        border-radius: 25px !important;
        color: #ffffff !important;
        padding: 1rem 1.5rem !important;
        font-size: 1.1rem !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #7877c6 !important;
        box-shadow: 0 0 0 3px rgba(120, 119, 198, 0.3) !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #7877c6, #ff77c6) !important;
        border: none !important;
        border-radius: 25px !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        padding: 1rem 2.5rem !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 10px 25px rgba(120, 119, 198, 0.4) !important;
    }
    
    .quick-actions {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 2rem 0;
    }
    
    .quick-action-btn {
        background: rgba(120, 119, 198, 0.15);
        border: 1px solid rgba(120, 119, 198, 0.4);
        color: #d0d0ff;
        padding: 1rem;
        border-radius: 15px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        font-weight: 500;
    }
    
    .quick-action-btn:hover {
        background: rgba(120, 119, 198, 0.3);
        border-color: #7877c6;
        color: #ffffff;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(120, 119, 198, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Display chat messages
st.markdown('<div class="chat-messages">', unsafe_allow_html=True)

for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="user-message-enhanced">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="assistant-message-enhanced">{message["content"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Chat input section
col_input, col_send = st.columns([4, 1])

with col_input:
    user_input = st.text_input(
        "Ask about projects, skills, achievements...", 
        key="chat_input", 
        label_visibility="collapsed",
        placeholder="e.g., 'What medical AI projects has Antarpreet worked on?'"
    )

with col_send:
    send_clicked = st.button("Send", key="send_message", use_container_width=True)

# Handle new messages with Groq AI
if send_clicked and user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get AI response using Groq
    with st.spinner("🤖 AI is thinking..."):
        ai_response = get_ai_response(user_input, groq_client)
    
    # Add assistant response
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    st.rerun()

# Quick action buttons
st.markdown("""
<div class="quick-actions">
    <div class="quick-action-btn">🧠 Current AI/ML Projects</div>
    <div class="quick-action-btn">🔬 Research Experience</div>
    <div class="quick-action-btn">⚙️ Software Engineering</div>
    <div class="quick-action-btn">🤖 Robotics Projects</div>
    <div class="quick-action-btn">🏥 Medical AI Work</div>
    <div class="quick-action-btn">🎓 Education & Skills</div>
</div>
""", unsafe_allow_html=True)

# Experience Section (moved down)
st.markdown("""
<div style="margin: 4rem 0; text-align: center;">
    <h2 style="font-size: 2.5rem; margin-bottom: 2rem; background: linear-gradient(135deg, #7877c6, #ff77c6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
        Professional Experience
    </h2>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="experience-grid" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 2.5rem; max-width: 1400px; margin: 0 auto; padding: 0 2rem;">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="experience-card" style="height: 420px; display: flex; flex-direction: column; justify-content: flex-start; padding: 2rem;">
        <div class="card-header" style="margin-bottom: 1rem;">
            <div class="card-icon">🧠</div>
            <div class="card-title">AI/ML Engineer</div>
            <div class="card-company">Sanmina • Jul 2024 - Present</div>
        </div>
        <div class="card-description" style="flex-grow: 1; margin-bottom: 1rem;">
            Benchmarked cutting-edge Auto3Dseg models (DINTS, SwinUNetR, SegResNet) for medical imaging. 
            Applied self-supervised learning pipelines for 3D medical image segmentation using MONAI. 
            Implemented Distributed Data Parallel training, achieving 53.5% training time reduction on H200 GPUs.
        </div>
        <div class="tech-stack" style="margin-top: auto;">
            <span class="tech-item">MONAI</span>
            <span class="tech-item">PyTorch</span>
            <span class="tech-item">Kubeflow</span>
            <span class="tech-item">Kubernetes</span>
            <span class="tech-item">NVIDIA GPUs</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🧠 Ask about AI/ML Work", key="ai_work", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Tell me about Antarpreet's current AI/ML work at Sanmina"})

with col2:
    st.markdown("""
    <div class="experience-card" style="height: 420px; display: flex; flex-direction: column; justify-content: flex-start; padding: 2rem;">
        <div class="card-header" style="margin-bottom: 1rem;">
            <div class="card-icon">🔬</div>
            <div class="card-title">Graduate Research Assistant</div>
            <div class="card-company">University at Buffalo • Oct 2023 - June 2024</div>
        </div>
        <div class="card-description" style="flex-grow: 1; margin-bottom: 1rem;">
            Developed Vector Quantized Diffusion model for chest X-ray synthesis. 
            Improved DenseNet-121 classification accuracy from 38.2% to 69.1% using synthetic data augmentation. 
            Created novel loss function with Multi-scale Structural Similarity.
        </div>
        <div class="tech-stack" style="margin-top: auto;">
            <span class="tech-item">Diffusion Models</span>
            <span class="tech-item">Medical Imaging</span>
            <span class="tech-item">Computer Vision</span>
            <span class="tech-item">Research</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔬 Ask about Research", key="research", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "What research has Antarpreet done at University at Buffalo?"})

# Second row
col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="experience-card" style="height: 420px; display: flex; flex-direction: column; justify-content: flex-start; padding: 2rem;">
        <div class="card-header" style="margin-bottom: 1rem;">
            <div class="card-icon">⚙️</div>
            <div class="card-title">Software Engineer 2</div>
            <div class="card-company">Dell Technologies • Jul 2018 - Aug 2022</div>
        </div>
        <div class="card-description" style="flex-grow: 1; margin-bottom: 1rem;">
            Led containerization of IoT Core applications achieving 80% startup time reduction. 
            Eliminated 1000+ critical security vulnerabilities. 
            Built RESTful microservices with 100% CI/CD maturity scores.
        </div>
        <div class="tech-stack" style="margin-top: auto;">
            <span class="tech-item">Kubernetes</span>
            <span class="tech-item">Docker</span>
            <span class="tech-item">Spring Boot</span>
            <span class="tech-item">Microservices</span>
            <span class="tech-item">CI/CD</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("⚙️ Ask about Dell Experience", key="dell", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "What did Antarpreet accomplish at Dell Technologies?"})

with col4:
    st.markdown("""
    <div class="experience-card" style="height: 420px; display: flex; flex-direction: column; justify-content: flex-start; padding: 2rem;">
        <div class="card-header" style="margin-bottom: 1rem;">
            <div class="card-icon">🤖</div>
            <div class="card-title">Master's Thesis Project</div>
            <div class="card-company">AI-Driven Speech Therapy Simulator</div>
        </div>
        <div class="card-description" style="flex-grow: 1; margin-bottom: 1rem;">
            Developed an AI-powered speech therapy simulator using BART for sequence-to-sequence modeling. 
            Integrated Human-in-the-Loop system with expert SLP feedback for personalized healthcare applications.
        </div>
        <div class="tech-stack" style="margin-top: auto;">
            <span class="tech-item">BART</span>
            <span class="tech-item">Hugging Face</span>
            <span class="tech-item">NLP</span>
            <span class="tech-item">Healthcare AI</span>
            <span class="tech-item">HITL</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🤖 Ask about Thesis", key="thesis", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "Tell me about Antarpreet's master's thesis on speech therapy"})

st.markdown('</div>', unsafe_allow_html=True)


# Leadership and achievements section
st.markdown("""
<div style="margin: 4rem 0; padding: 3rem; background: rgba(255, 255, 255, 0.03); border-radius: 25px; border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(20px);">
    <h2 style="font-size: 2.2rem; text-align: center; margin-bottom: 2rem; color: #ffffff;">
        🌟 Leadership & Recognition
    </h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
        <div style="text-align: center; padding: 1.5rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">👩‍💻</div>
            <h3 style="color: #7877c6; margin-bottom: 0.5rem;">Google WTM Ambassador</h3>
            <p style="color: #e0e0ff;">Advancing diversity and inclusivity in tech industry</p>
        </div>
        <div style="text-align: center; padding: 1.5rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🏆</div>
            <h3 style="color: #ff77c6; margin-bottom: 0.5rem;">Dell IT Development Program</h3>
            <p style="color: #e0e0ff;">Selected as 1 of 27 from 500+ global participants</p>
        </div>
        <div style="text-align: center; padding: 1.5rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">⭐</div>
            <h3 style="color: #77c6a1; margin-bottom: 0.5rem;">Dell Rockstar Award</h3>
            <p style="color: #e0e0ff;">Recognition for outstanding performance and impact</p>
        </div>
        <div style="text-align: center; padding: 1.5rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🛡️</div>
            <h3 style="color: #c677ff; margin-bottom: 0.5rem;">Dell Bravo Award</h3>
            <p style="color: #e0e0ff;">Security Champion for enhancing application security</p>
        </div>
        <div style="text-align: center; padding: 1.5rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">☁️</div>
            <h3 style="color: #7877c6; margin-bottom: 0.5rem;">Google Cloud Certified</h3>
            <p style="color: #e0e0ff;">Digital Leader Certification + Gen AI Course</p>
        </div>
        <div style="text-align: center; padding: 1.5rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🎤</div>
            <h3 style="color: #ff77c6; margin-bottom: 0.5rem;">Toastmasters Member</h3>
            <p style="color: #e0e0ff;">Developed public speaking and leadership skills</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer with contact info
st.markdown("""
<div style="text-align: center; margin-top: 4rem; padding: 2rem; border-top: 1px solid rgba(120, 119, 198, 0.3);">
    <p style="color: #b8b8ff; font-size: 1.1rem; margin-bottom: 1rem;">
        🚀 Ready to discuss AI/ML projects and opportunities?
    </p>
    <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
        <a href="mailto:antarpre@buffalo.edu" style="color: #7877c6; text-decoration: none; font-weight: 500;">📧 Email</a>
        <a href="https://linkedin.com/in/antarpreet-kaur-ghuman" style="color: #ff77c6; text-decoration: none; font-weight: 500;">💼 LinkedIn</a>
        <a href="https://github.com/antar-ghuman" style="color: #77c6a1; text-decoration: none; font-weight: 500;">🔗 GitHub</a>
    </div>
    <p style="color: #9090ff; font-size: 0.9rem; margin-top: 1.5rem;">
        💡 This AI assistant uses Groq's Llama 3.3 70B model to answer questions about Antarpreet's experience
    </p>
</div>
""", unsafe_allow_html=True)