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
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    .stToolbar {visibility: hidden;}
    .stDecoration {visibility: hidden;}
    .stAppViewContainer > .main > div:first-child {display: none;}
    
    /* Sophisticated dark background like lofi.cafe */
    .stApp {
        background: 
            radial-gradient(ellipse at top, #1a1625 0%, #0f0f17 50%),
            radial-gradient(ellipse at bottom, #2d1b3d 0%, #1a1625 50%),
            linear-gradient(135deg, #0f0f17 0%, #1a1625 25%, #2d1b3d 50%, #1a1625 75%, #0f0f17 100%);
        background-size: 100% 100%, 100% 100%, 400% 400%;
        animation: ambientGlow 20s ease-in-out infinite;
        color: #e8e6f0;
        font-family: 'Inter', sans-serif;
        min-height: 100vh;
        position: relative;
    }
    
    @keyframes ambientGlow {
        0%, 100% { background-position: 0% 50%, 0% 50%, 0% 50%; }
        50% { background-position: 0% 50%, 0% 50%, 100% 50%; }
    }
    
    /* Subtle ambient particles */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, rgba(138, 43, 226, 0.3), transparent),
            radial-gradient(2px 2px at 40px 70px, rgba(75, 0, 130, 0.2), transparent),
            radial-gradient(1px 1px at 90px 40px, rgba(138, 43, 226, 0.4), transparent),
            radial-gradient(1px 1px at 130px 80px, rgba(75, 0, 130, 0.3), transparent),
            radial-gradient(2px 2px at 160px 30px, rgba(138, 43, 226, 0.2), transparent);
        background-repeat: repeat;
        background-size: 200px 100px;
        animation: drift 60s linear infinite;
        pointer-events: none;
        z-index: 1;
    }
    
    @keyframes drift {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-200px); }
    }
    
    /* Hero section with warm accent glow - RESPONSIVE */
    .hero-container {
        position: relative;
        text-align: center;
        padding: 2rem 1rem 1rem;
        z-index: 10;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    
    .hero-container::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, rgba(255, 140, 105, 0.15) 0%, rgba(255, 107, 107, 0.05) 50%, transparent 100%);
        border-radius: 50%;
        animation: heroGlow 8s ease-in-out infinite;
        z-index: -1;
    }
    
    @keyframes heroGlow {
        0%, 100% { transform: translate(-50%, -50%) scale(1); opacity: 0.6; }
        50% { transform: translate(-50%, -50%) scale(1.1); opacity: 0.8; }
    }
    
    /* Sophisticated name styling - RESPONSIVE */
    .name-display {
        font-size: clamp(2rem, 8vw, 4.5rem);
        font-weight: 700;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #ff8c69 0%, #ff6b6b 25%, #ffa726 50%, #ff8a65 75%, #ff7043 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        background-size: 300% 300%;
        animation: warmShimmer 6s ease-in-out infinite;
        letter-spacing: -0.02em;
        text-shadow: 0 4px 20px rgba(255, 107, 107, 0.3);
        line-height: 1.2;
    }
    
    @keyframes warmShimmer {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    .title-role {
        font-size: clamp(1rem, 4vw, 1.4rem);
        color: #c9b3ff;
        font-weight: 500;
        margin-bottom: 1.5rem;
        background: rgba(25, 23, 40, 0.8);
        padding: 0.6rem 1.5rem;
        border-radius: 50px;
        border: 1px solid rgba(138, 43, 226, 0.3);
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 20px rgba(138, 43, 226, 0.2);
    }
    
    .hero-description {
        font-size: clamp(0.9rem, 3vw, 1.1rem);
        color: #b8b5c8;
        max-width: 650px;
        margin: 0 auto 1rem;
        line-height: 1.7;
        background: rgba(25, 23, 40, 0.6);
        padding: 1rem;
        border-radius: 20px;
        border: 1px solid rgba(138, 43, 226, 0.2);
        backdrop-filter: blur(15px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
    }
    
    /* Glowing skill badges - FULLY RESPONSIVE */
    .skills-showcase {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
        gap: 0.8rem;
        max-width: 800px;
        margin: 1rem auto;
        padding: 0 1rem;
    }
    
    .skill-badge {
        background: linear-gradient(135deg, rgba(25, 23, 40, 0.8), rgba(45, 27, 61, 0.6));
        border: 1px solid rgba(138, 43, 226, 0.4);
        border-radius: 15px;
        padding: 0.6rem 0.8rem;
        text-align: center;
        font-weight: 500;
        font-size: clamp(0.7rem, 2.5vw, 0.9rem);
        color: #e8e6f0;
        transition: all 0.3s ease;
        cursor: pointer;
        backdrop-filter: blur(10px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .skill-badge::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 140, 105, 0.2), transparent);
        transition: left 0.5s ease;
    }
    
    .skill-badge:hover {
        transform: translateY(-3px);
        border-color: #ff8c69;
        box-shadow: 0 8px 25px rgba(255, 140, 105, 0.3);
        color: #ffffff;
    }
    
    .skill-badge:hover::before {
        left: 100%;
    }
    
    /* Sophisticated experience cards - RESPONSIVE */
    .experience-card {
        background: linear-gradient(135deg, rgba(25, 23, 40, 0.9), rgba(45, 27, 61, 0.7));
        border: 1px solid rgba(138, 43, 226, 0.3);
        border-radius: 20px;
        padding: 1.2rem;
        margin: 1rem 0;
        position: relative;
        transition: all 0.4s ease;
        backdrop-filter: blur(20px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
        overflow: hidden;
        min-height: 300px;
    }
    
    .experience-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(255, 140, 105, 0.05), rgba(138, 43, 226, 0.05));
        opacity: 0;
        transition: opacity 0.4s ease;
    }
    
    .experience-card:hover {
        transform: translateY(-8px);
        border-color: rgba(255, 140, 105, 0.6);
        box-shadow: 0 15px 40px rgba(255, 140, 105, 0.2);
    }
    
    .experience-card:hover::before {
        opacity: 1;
    }
    
    .card-icon {
        font-size: clamp(2.5rem, 6vw, 3.5rem);
        margin-bottom: 1rem;
        display: block;
        filter: drop-shadow(0 4px 8px rgba(255, 140, 105, 0.3));
        position: relative;
        z-index: 2;
    }
    
    .card-title {
        font-size: clamp(1.1rem, 4vw, 1.5rem);
        font-weight: 600;
        color: #ff8c69;
        margin-bottom: 0.5rem;
        position: relative;
        z-index: 2;
        line-height: 1.3;
    }
    
    .card-company {
        font-size: clamp(0.8rem, 3vw, 1rem);
        color: #c9b3ff;
        font-weight: 500;
        margin-bottom: 1rem;
        position: relative;
        z-index: 2;
    }
    
    .card-description {
        color: #b8b5c8;
        line-height: 1.6;
        margin-bottom: 1rem;
        position: relative;
        z-index: 2;
        font-weight: 400;
        font-size: clamp(0.8rem, 2.5vw, 0.95rem);
    }
    
    .tech-stack {
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem;
        position: relative;
        z-index: 2;
    }
    
    .tech-item {
        background: linear-gradient(135deg, rgba(138, 43, 226, 0.3), rgba(75, 0, 130, 0.4));
        color: #e8e6f0;
        padding: 0.3rem 0.6rem;
        border-radius: 12px;
        font-size: clamp(0.65rem, 2vw, 0.8rem);
        font-weight: 500;
        border: 1px solid rgba(138, 43, 226, 0.5);
        backdrop-filter: blur(5px);
    }
    
    /* Ambient chat section - RESPONSIVE */
    .ai-chat-container {
        background: linear-gradient(135deg, rgba(25, 23, 40, 0.95), rgba(45, 27, 61, 0.8));
        border: 1px solid rgba(255, 140, 105, 0.3);
        border-radius: 25px;
        padding: 1rem;
        margin: 1rem auto;
        max-width: 550px;
        position: relative;
        backdrop-filter: blur(20px);
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.4);
        overflow: hidden;
    }
    
    .ai-chat-container::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(from 0deg, transparent, rgba(255, 140, 105, 0.1), transparent);
        animation: rotate 30s linear infinite;
        z-index: -1;
    }
    
    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .chat-title {
        font-size: clamp(1.5rem, 5vw, 2.2rem);
        font-weight: 600;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #ff8c69, #c9b3ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        position: relative;
        z-index: 2;
    }
    
    .chat-subtitle {
        text-align: center;
        color: #b8b5c8;
        margin-bottom: 1rem;
        font-size: clamp(0.9rem, 3vw, 1.1rem);
        position: relative;
        z-index: 2;
    }
    
    /* Chat messages container - RESPONSIVE */
    .chat-messages {
        background: rgba(0, 0, 0, 0.4);
        border-radius: 20px;
        padding: 1rem;
        margin: 1rem 0;
        max-height: 350px;
        overflow-y: auto;
        border: 1px solid rgba(120, 119, 198, 0.3);
        backdrop-filter: blur(10px);
    }
    
    .user-message-enhanced {
        background: linear-gradient(135deg, #7877c6, #ff77c6);
        color: white;
        padding: 1rem 1.2rem;
        border-radius: 20px 20px 5px 20px;
        margin: 1rem 0 1rem auto;
        max-width: 85%;
        font-size: clamp(0.85rem, 3vw, 1rem);
        line-height: 1.5;
        box-shadow: 0 4px 15px rgba(120, 119, 198, 0.3);
    }
    
    .assistant-message-enhanced {
        background: rgba(120, 119, 198, 0.2);
        color: #ffffff;
        padding: 1rem 1.2rem;
        border-radius: 20px 20px 20px 5px;
        margin: 1rem auto 1rem 0;
        max-width: 85%;
        border: 1px solid rgba(120, 119, 198, 0.4);
        font-size: clamp(0.85rem, 3vw, 1rem);
        line-height: 1.6;
        backdrop-filter: blur(15px);
    }
    
    /* Sophisticated input styling - RESPONSIVE */
    .stTextInput > div > div > input {
        background: rgba(120, 119, 198, 0.15) !important;
        border: 2px solid rgba(120, 119, 198, 0.4) !important;
        border-radius: 25px !important;
        color: #ffffff !important;
        padding: 0.8rem 1.2rem !important;
        font-size: clamp(0.9rem, 3.5vw, 1.1rem) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #7877c6 !important;
        box-shadow: 0 0 0 3px rgba(120, 119, 198, 0.3) !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #8a87a0 !important;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #7877c6, #ff77c6) !important;
        border: none !important;
        border-radius: 25px !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        padding: 0.8rem 1.5rem !important;
        font-size: clamp(0.9rem, 3.5vw, 1.1rem) !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(10px) !important;
        width: 100% !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px) scale(1.05) !important;
        box-shadow: 0 10px 25px rgba(120, 119, 198, 0.4) !important;
    }
    
    /* Enhanced quick actions - RESPONSIVE */
    .quick-actions {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 0.8rem;
        margin: 1rem 0;
        padding: 0 1rem;
    }
    
    .quick-action-btn {
        background: rgba(120, 119, 198, 0.15);
        border: 1px solid rgba(120, 119, 198, 0.4);
        color: #d0d0ff;
        padding: 0.8rem 0.6rem;
        border-radius: 15px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
        backdrop-filter: blur(10px);
        font-weight: 500;
        font-size: clamp(0.8rem, 2.5vw, 0.95rem);
    }
    
    .quick-action-btn:hover {
        background: rgba(120, 119, 198, 0.3);
        border-color: #7877c6;
        color: #ffffff;
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(120, 119, 198, 0.3);
    }
    
    /* COMPREHENSIVE RESPONSIVE DESIGN */
    
    /* Mobile First - Extra Small devices (phones, 576px and down) */
    @media (max-width: 576px) {
        .hero-container { 
            padding: 1.5rem 0.8rem 1rem; 
        }
        
        .hero-container::before {
            width: 200px;
            height: 200px;
        }
        
        .hero-description {
            padding: 0.8rem;
            margin: 0 0.5rem 1rem;
        }
        
        .skills-showcase {
            grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
            gap: 0.6rem;
            padding: 0 0.8rem;
        }
        
        .experience-card {
            padding: 1rem;
            margin: 0.8rem 0;
            min-height: 280px;
        }
        
        .ai-chat-container {
            margin: 1rem 0.5rem;
            padding: 0.8rem;
        }
        
        .chat-messages {
            max-height: 300px;
            padding: 0.8rem;
        }
        
        .quick-actions {
            grid-template-columns: 1fr;
            gap: 0.6rem;
        }
        
        .user-message-enhanced,
        .assistant-message-enhanced {
            max-width: 95%;
            padding: 0.8rem 1rem;
        }
    }
    
    /* Small devices (landscape phones, 576px and up) */
    @media (min-width: 576px) and (max-width: 768px) {
        .skills-showcase {
            grid-template-columns: repeat(auto-fit, minmax(90px, 1fr));
        }
        
        .quick-actions {
            grid-template-columns: repeat(2, 1fr);
        }
        
        .experience-card {
            min-height: 320px;
        }
    }
    
    /* Medium devices (tablets, 768px and up) */
    @media (min-width: 768px) and (max-width: 992px) {
        .hero-container {
            padding: 2rem 1rem 1.5rem;
        }
        
        .skills-showcase {
            grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
        }
        
        .quick-actions {
            grid-template-columns: repeat(3, 1fr);
        }
        
        .experience-card {
            min-height: 360px;
            padding: 1.3rem;
        }
    }
    
    /* Large devices (desktops, 992px and up) */
    @media (min-width: 992px) {
        .hero-container {
            padding: 2rem 2rem 1rem;
        }
        
        .hero-container::before {
            width: 500px;
            height: 500px;
        }
        
        .skills-showcase {
            grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        }
        
        .quick-actions {
            grid-template-columns: repeat(5, 1fr);
        }
        
        .experience-card {
            min-height: 420px;
            padding: 1.5rem;
        }
        
        .ai-chat-container {
            padding: 1.5rem;
        }
        
        .chat-messages {
            padding: 1.5rem;
            max-height: 400px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize Groq client
@st.cache_resource
def init_groq_client():
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        return client
    except:
        st.warning("🔑 Please set your Groq API key in Streamlit secrets to enable AI responses")
        return None

# Antarpreet's resume data for context
RESUME_CONTEXT = """
Antarpreet Kaur Ghuman - AI/ML Engineer with MS in Robotics & AI and 4+ years tech experience.

CONTACT: 
Phone: (+1)716-923-5474 | Email: antarpre@buffalo.edu | LinkedIn: antarpreet-kaur-ghuman | GitHub: antar-ghuman

CURRENT ROLE - AI/ML Engineer at Sanmina (Jul 2024 - Present):
• Applied self-supervised learning pipelines for 3D medical image segmentation using MONAI on TCIA-COVID19 and BTCV datasets
• Pretrained ViT Autoencoder and fine-tuned UNetR to extract robust representations
• Benchmarked cutting-edge Auto3Dseg models (DINTS, SwinUNetR, SegResNet) for architecture selection
• Engineered face analytics using MTCNN and MediaPipe for bounding box generation and facial landmark detection
• Implemented Distributed Data Parallel (DDP) for training on H200 NVL GPUs, reducing training time by 53.5%
• Applied Stable Diffusion and StyleGAN for medical text-to-image synthesis and visual domain transfer
• Integrated MONAI Label with 3D Slicer for interactive active learning workflows
• Deployed and configured Kubeflow on on-premises Kubernetes nodes with GPU-accelerated ML pipelines
• Designed end-to-end HPC demo processing 5TB weather data using Kubeflow Pipelines and NVIDIA FourCastNet

PREVIOUS ROLES:
Graduate Research Assistant - AI Lab, University at Buffalo (Oct 2023 - June 2024):
• Collaborated on Vector Quantized Diffusion model for text-conditioned chest X-ray synthesis at 256x256 and 512x512 resolutions
• Developed novel loss function with Multi-scale Structural Similarity (MS-SSIM) to preserve radiological accuracy
• Increased DenseNet-121 classification accuracy from 38.2% to 69.1% using synthetic data augmentation

Software Engineer 2 - Dell Technologies (Jul 2018 - Aug 2022):
IoT Core Containerization:
• Led containerization of Secure Connect Gateway (SCG), achieving 80% startup time reduction and 1% downtime
• Eliminated 1000+ critical Blackduck vulnerabilities and reduced Checkmarx security threats by 88%
• Reached 100% CI/CD maturity scores with automated deployment pipelines
• Delivered lectures to 100+ org members

Direct Connectivity API:
• Developed RESTful Microservices using Spring Boot on Pivotal Cloud Foundry (PCF)
• Improved testing efficiency by 50% with automated test suite creation
• Achieved 100% code coverage using JUnit Mockito for Java services
• Minimized security risks by 98% for 12 microservices

Intern Analyst - Dell Technologies (Jan 2018 - May 2018):
• Implemented automated test cases for dell.com order process validation
• Enhanced functionality and user experience features

EDUCATION:
• MS in Robotics & Artificial Intelligence, University at Buffalo (Aug 2022 – May 2024)
  Coursework: Data Structures, Machine Learning, Computer Vision, Reinforcement Learning, Robotics Algorithms
• BE Computer Science - Honors (Cloud Computing), Chandigarh University (Jul 2014 - May 2018)
  Coursework: Cloud Computing, Operating Systems, Web Development, Service-Oriented Architecture

TECHNICAL SKILLS:
Languages: Java, Python, HTML/CSS, JavaScript, C++, MySQL, PostgreSQL, NoSQL
AI/ML: OpenCV, TensorFlow, PyTorch, Keras, Scikit-learn, Pandas, NumPy, MONAI, ROS
GenAI: Transformers (BART, ViT, HuggingFace), Diffusion Models, CNNs, StyleGAN, Stable Diffusion, YOLO, SSD
Cloud/MLOps: Kubernetes, Kubeflow, Docker, GCP, Helm, CI/CD, REST APIs, Kafka, ElasticSearch
Frameworks: Spring Boot, JUnit, Linux, AWS, MATLAB

KEY PROJECTS:
AI-Driven Speech Therapy Simulator (Master's Thesis):
• Developed AI-powered speech therapy simulator using BART for sequence-to-sequence modeling
• Integrated Human-in-the-Loop (HITL) system with expert SLP feedback for clinical alignment

Computer Vision Projects:
• Deep Learning Based Facial Analysis: Face detection, recognition, clustering, emotion/gender/age classification
• K-Means Face Clustering: 91% accuracy with custom K-Means algorithm in OpenCV

Robotics Projects:
• Vision for Robotics: Stereo odometry with feature detection, depth estimation, optical flow tracking
• RRT Path Finding: Optimized pathfinding algorithm for obstacle avoidance
• PID and Pure Pursuit: Car steering control with trajectory visualization in RVIZ
• Evader+Mapper: Dual ROS nodes for obstacle avoidance and environment mapping

Cloud/API Projects:
• Tweet Translator: Real-time translation service using Watson Language Translation API
• Real-time Log Management: Fluentd and Kafka system with Elasticsearch and Grafana visualization

Machine Learning Projects:
• RL with Real-World Uncertainties: Enhanced Q-learning and Actor-Critic with wind noise and engine failures
• Handwritten Digits Classification: MLP vs CNN performance comparison

LEADERSHIP & CERTIFICATIONS:
• Google Women Techmakers Ambassador - advancing diversity in tech
• Dell IT Development Program - selected 1 of 27 from 500+ global participants
• Google Cloud Digital Leader Certification
• Gen AI Intensive Course with Kaggle and Google (LLMs, prompt engineering, embeddings, vector databases, AI agents, MLOps)
• Mozilla Firefox ambassador during undergrad
• University fest anchor and organizer, Head of Creative team

PERSONAL INTERESTS:
When not working, Antarpreet enjoys photography, traveling to explore new places and cultures, and binge-watching shows and documentaries. She also participates in the extracurricular activities mentioned above.
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
        {"role": "assistant", "content": "👋 Hi! I'm Antarpreet's comprehensive portfolio assistant. I can tell you about her experience in AI/ML and Software Engineering, including cutting-edge projects like 3D medical image segmentation with MONAI, speech therapy simulators, and much more. What would you like to explore?"}
    ]

# Initialize Groq client
groq_client = init_groq_client()

# Hero Section
st.markdown("""
<div class="hero-container">
    <div class="hero-bg-effect"></div>
    <h1 class="name-display">Antarpreet Kaur Ghuman</h1>
    <p class="title-role">AI/ML Engineer | WTM Ambassador</p>
    <p class="hero-description">
        MS in Robotics & AI with 5+ years of experience in tech. Currently an AI/ML Engineer at Sanmina, 
        after 4 years as a Software Engineer at Dell Technologies. Passionate about translating cutting-edge 
        AI research into real-world solutions across Healthcare, Computer Vision, NLP, Robotics, and MLOps.
        Always eager to learn new technologies and take on challenging projects.
    </p>
</div>
""", unsafe_allow_html=True)

# Skills Showcase
st.markdown("""
<div class="skills-showcase">
    <div class="skill-badge">Python</div>
    <div class="skill-badge">PyTorch</div>
    <div class="skill-badge">Java</div>
    <div class="skill-badge">OpenCV</div>
    <div class="skill-badge">MONAI</div>
    <div class="skill-badge">Kubernetes</div>
    <div class="skill-badge">Docker</div>
    <div class="skill-badge">ROS</div>
    <div class="skill-badge">YOLO</div>
    <div class="skill-badge">GCP</div>
</div>
""", unsafe_allow_html=True)

# AI Chat Section
st.markdown("""
<div class="ai-chat-container">
    <h2 class="chat-title">🤖 AI Portfolio Assistant</h2>
    <p class="chat-subtitle">Powered by Groq AI • Ask anything about Antarpreet's experience</p>
</div>
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
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.spinner("🤖 AI is thinking..."):
        ai_response = get_ai_response(user_input, groq_client)
    
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    st.rerun()

# Quick action buttons
st.markdown("""
<div class="quick-actions">
    <div class="quick-action-btn">📡 Cloud & MLOps</div>
    <div class="quick-action-btn">👁️ Computer Vision</div>
    <div class="quick-action-btn">🚀 Robotics & RL</div>
    <div class="quick-action-btn">🎨 Diffusion Models</div>
    <div class="quick-action-btn">🏥 Medical AI</div>
</div>
""", unsafe_allow_html=True)

# Experience Section
st.markdown("""
<div style="margin: 2rem 0; text-align: center;">
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
<div style="margin: 2rem 0; padding: 1.5rem; background: rgba(255, 255, 255, 0.03); border-radius: 25px; border: 1px solid rgba(255, 255, 255, 0.1); backdrop-filter: blur(20px);">
    <h2 style="font-size: clamp(1.5rem, 5vw, 2.2rem); text-align: center; margin-bottom: 1.5rem; color: #ffffff;">
        🌟 Leadership & Recognition
    </h2>
    <div class="leadership-grid" style="
        display: grid; 
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); 
        gap: 1.2rem;
        justify-items: center;
    ">
        <div style="text-align: center; padding: 1rem; width: 100%; max-width: 300px;">
            <div style="font-size: clamp(2rem, 6vw, 3rem); margin-bottom: 1rem;">👩‍💻</div>
            <h3 style="color: #7877c6; margin-bottom: 0.5rem; font-size: clamp(1rem, 4vw, 1.2rem);">Google WTM Ambassador</h3>
            <p style="color: #e0e0ff; font-size: clamp(0.8rem, 3vw, 0.9rem); line-height: 1.4;">Advancing diversity and inclusivity in tech industry</p>
        </div>
        <div style="text-align: center; padding: 1rem; width: 100%; max-width: 300px;">
            <div style="font-size: clamp(2rem, 6vw, 3rem); margin-bottom: 1rem;">🏆</div>
            <h3 style="color: #ff77c6; margin-bottom: 0.5rem; font-size: clamp(1rem, 4vw, 1.2rem);">Dell IT Development Program</h3>
            <p style="color: #e0e0ff; font-size: clamp(0.8rem, 3vw, 0.9rem); line-height: 1.4;">Selected as 1 of 27 from 500+ global participants</p>
        </div>
        <div style="text-align: center; padding: 1rem; width: 100%; max-width: 300px;">
            <div style="font-size: clamp(2rem, 6vw, 3rem); margin-bottom: 1rem;">⭐</div>
            <h3 style="color: #77c6a1; margin-bottom: 0.5rem; font-size: clamp(1rem, 4vw, 1.2rem);">Dell Rockstar Award</h3>
            <p style="color: #e0e0ff; font-size: clamp(0.8rem, 3vw, 0.9rem); line-height: 1.4;">Recognition for outstanding performance and impact</p>
        </div>
        <div style="text-align: center; padding: 1rem; width: 100%; max-width: 300px;">
            <div style="font-size: clamp(2rem, 6vw, 3rem); margin-bottom: 1rem;">🛡️</div>
            <h3 style="color: #c677ff; margin-bottom: 0.5rem; font-size: clamp(1rem, 4vw, 1.2rem);">Dell Bravo Award</h3>
            <p style="color: #e0e0ff; font-size: clamp(0.8rem, 3vw, 0.9rem); line-height: 1.4;">Security Champion for enhancing application security</p>
        </div>
        <div style="text-align: center; padding: 1rem; width: 100%; max-width: 300px;">
            <div style="font-size: clamp(2rem, 6vw, 3rem); margin-bottom: 1rem;">☁️</div>
            <h3 style="color: #7877c6; margin-bottom: 0.5rem; font-size: clamp(1rem, 4vw, 1.2rem);">Google Cloud Certified</h3>
            <p style="color: #e0e0ff; font-size: clamp(0.8rem, 3vw, 0.9rem); line-height: 1.4;">Digital Leader Certification + Gen AI Course</p>
        </div>
        <div style="text-align: center; padding: 1rem; width: 100%; max-width: 300px;">
            <div style="font-size: clamp(2rem, 6vw, 3rem); margin-bottom: 1rem;">🎤</div>
            <h3 style="color: #ff77c6; margin-bottom: 0.5rem; font-size: clamp(1rem, 4vw, 1.2rem);">Toastmasters Member</h3>
            <p style="color: #e0e0ff; font-size: clamp(0.8rem, 3vw, 0.9rem); line-height: 1.4;">Developed public speaking and leadership skills</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer with contact info
st.markdown("""
<div style="text-align: center; margin-top: 2rem; padding: 1.5rem; border-top: 1px solid rgba(120, 119, 198, 0.3);">
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
