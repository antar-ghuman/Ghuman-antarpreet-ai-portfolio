# 🤖 Antarpreet's AI-Powered Portfolio

A next-generation portfolio with anime-inspired aesthetics, real AI integration, and intelligent responses about Antarpreet Kaur Ghuman's experience in AI/ML engineering.

## ✨ Features

### 🎨 **Anime-Inspired Professional Design**
- Cyberpunk color palette with neon effects
- Holographic animations and particle systems
- 3D card transforms and smooth interactions
- Mobile-responsive design

### 🤖 **Real AI Integration**
- **Option 1**: Lightweight intelligent responses (FREE)
- **Option 2**: Real transformer models (Hugging Face)
- Context-aware responses about experience
- Domain-specific expertise detection

### 📊 **Interactive Visualizations**
- Performance metrics with Plotly
- Technology expertise radar charts
- Achievement timelines
- Real-time data updates

### 💬 **Smart Chat Interface**
- AI-powered portfolio assistant
- Contextual responses about projects
- Quick question buttons
- Conversation history

## 🚀 Quick Deployment (100% FREE)

### Method 1: Streamlit Cloud (Recommended)

1. **Fork this repository** to your GitHub account

2. **Go to [share.streamlit.io](https://share.streamlit.io)**

3. **Connect your GitHub account**

4. **Deploy the app:**
   - Repository: `your-username/antarpreet-ai-portfolio`
   - Branch: `main`
   - Main file path: `streamlit_app.py`
   - Requirements file: `requirements-lite.txt` (for free deployment)

5. **Click Deploy!** 🚀

Your portfolio will be live at: `https://your-app-name.streamlit.app`

### Method 2: Local Development

```bash
# Clone the repository
git clone https://github.com/your-username/antarpreet-ai-portfolio.git
cd antarpreet-ai-portfolio

# Install dependencies (lightweight version)
pip install -r requirements-lite.txt

# Run the app
streamlit run streamlit_app.py
```

## 📁 Project Structure

```
antarpreet-ai-portfolio/
├── streamlit_app.py          # Main application with anime UI
├── portfolio_data.py         # Antarpreet's complete resume data
├── ai_assistant.py          # AI response logic (optional)
├── requirements.txt         # Full dependencies (with AI models)
├── requirements-lite.txt    # Lightweight version (FREE)
├── README.md               # This file
├── .gitignore              # Git ignore file
└── assets/                 # Images and additional files
    ├── profile_photo.jpg
    └── project_images/
```

## 🎯 Customization Guide

### 1. **Update Your Information**

Edit `portfolio_data.py`:

```python
# Update personal info
"personal_info": {
    "name": "Your Name",
    "title": "Your Title",
    "email": "your.email@example.com",
    # ... update all sections
}
```

### 2. **Modify Color Scheme**

In `streamlit_app.py`, find the CSS section and update:

```css
/* Change primary colors */
--primary-blue: #00D4FF;    /* Cyber blue */
--primary-purple: #9D4EDD;  /* Neon purple */
--accent-pink: #FF006E;     /* Electric pink */
```

### 3. **Add Your Projects**

Update the projects section in `portfolio_data.py`:

```python
"projects": {
    "your_project": {
        "title": "Your Amazing Project",
        "description": "What it does...",
        "technologies": ["Python", "AI", "etc"],
        "achievements": ["Specific results..."],
        # ...
    }
}
```

## 🤖 AI Integration Options

### Option 1: Lightweight (FREE - Recommended for deployment)
Uses intelligent pattern matching and context-aware responses. No API costs, works perfectly offline.

### Option 2: Real AI Models (Local/Development)
```bash
# Install full AI dependencies
pip install -r requirements.txt

# The app will automatically detect and use real transformer models
```

### Option 3: API Integration (Optional)
Add environment variables for API-based AI:
```bash
OPENAI_API_KEY=your_key_here
HUGGINGFACE_API_KEY=your_key_here
```

## 🎨 Design Philosophy

### **Anime-Inspired Professional Aesthetic**
- **Color Palette**: Cyberpunk blues, neon purples, electric pinks
- **Typography**: Orbitron (futuristic) + Roboto (readable)
- **Animations**: Holographic effects, particle systems, smooth transitions
- **Layout**: Clean, modern, with subtle anime influences

### **Professional + Creative Balance**
- Maintains professional credibility
- Adds visual wow factor
- Demonstrates technical creativity
- Shows attention to detail

## 📊 Analytics & Performance

The portfolio tracks:
- Chat interactions and popular questions
- Most viewed sections
- Response effectiveness
- User engagement metrics

## 🔧 Technical Stack

### **Frontend**
- **Streamlit**: Web framework
- **CSS3**: Custom animations and styling
- **Plotly**: Interactive visualizations
- **HTML5**: Custom components

### **AI/ML** 
- **Transformers**: Hugging Face models (optional)
- **PyTorch**: Model inference (optional)
- **Intelligent Fallbacks**: Pattern matching responses

### **Deployment**
- **Streamlit Cloud**: Free hosting
- **GitHub**: Version control
- **No databases**: File-based data storage

## 🚀 Advanced Features

### **Smart Response System**
- Domain detection (Medical AI, Software Engineering, Research)
- Context-aware responses
- Conversation memory
- Quick question suggestions

### **Visual Enhancements**
- Particle animation system
- Holographic UI effects
- 3D card transforms
- Responsive design

### **Performance Optimization**
- Lazy loading of components
- Cached data operations
- Optimized animations
- Mobile-friendly design

## 📈 Metrics Dashboard

The portfolio showcases key achievements:
- **53.5%** training time reduction
- **1000+** vulnerabilities eliminated  
- **80%** startup time improvement
- **69.1%** classification accuracy

## 🎯 Use Cases

Perfect for:
- **AI/ML Engineers** showcasing technical projects
- **Software Engineers** with visual portfolios
- **Researchers** displaying publications and impact
- **Anyone** wanting a next-level portfolio

## 🤝 Contributing

Want to enhance this portfolio template?

1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

## 📞 Contact

**Antarpreet Kaur Ghuman**
- 📧 Email: antarpre@buffalo.edu
- 💼 LinkedIn: [antarpreet-kaur-ghuman](https://linkedin.com/in/antarpreet-kaur-ghuman)
- 💻 GitHub: [antar-ghuman](https://github.com/antar-ghuman)

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

**⭐ Star this repository** if you found it helpful!

**🚀 Deploy your own** AI-powered portfolio today!