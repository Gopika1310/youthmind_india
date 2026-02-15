"""
YouthMind India - AI-Powered Mental Wellness Platform
Main entry point for the application
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json
import os

# Page configuration
st.set_page_config(
    page_title="YouthMind India",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-card {
        background-color: #f9f9f9;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .highlight {
        background-color: #e8f5e9;
        padding: 0.5rem;
        border-radius: 5px;
        color: #2e7d32;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/brain--v1.png", width=80)
    st.title("YouthMind India")
    st.markdown("---")
    
    # Navigation
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.current_page = 'home'
    if st.button("📝 Assessment", use_container_width=True):
        st.session_state.current_page = 'assessment'
    if st.button("📊 Dashboard", use_container_width=True):
        st.session_state.current_page = 'dashboard'
    if st.button("📚 Resources", use_container_width=True):
        st.session_state.current_page = 'resources'
    
    st.markdown("---")
    
    # User status
    if st.session_state.authenticated:
        st.success(f"Welcome, {st.session_state.user_data.get('name', 'User')}!")
        if st.button("🚪 Logout"):
            st.session_state.authenticated = False
            st.session_state.user_data = {}
            st.rerun()
    else:
        st.info("Please complete assessment to get started")

# Main content
if st.session_state.current_page == 'home':
    # Hero section
    st.markdown('<h1 class="main-header">🧠 YouthMind India</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Your Personal AI-Powered Mental Wellness Companion</p>', unsafe_allow_html=True)
    
    # Features in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>🎯 Personalized</h3>
            <p>AI learns your unique needs and creates custom wellness plans just for you</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🧠 Intelligent</h3>
            <p>Advanced ML models analyze your emotions and recommend perfect resources</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>📈 Track Progress</h3>
            <p>Watch your wellbeing improve with interactive charts and insights</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Stats
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Active Users", "1,234", "+123")
    with col2:
        st.metric("Resources", "500+", "+50")
    with col3:
        st.metric("Avg. Improvement", "67%", "+12%")
    with col4:
        st.metric("Happy Users", "98%", "+5%")
    
    # Call to action
    # Call to action
st.markdown("---")
if st.button("🚀 Start Your Wellness Journey", use_container_width=True):
    st.session_state.current_page = 'assessment'
    st.rerun()

# Page navigation
if st.session_state.current_page == 'assessment':
    from pages.assessment import show_assessment
    show_assessment()

elif st.session_state.current_page == 'dashboard':
    if not st.session_state.authenticated:
        st.warning("Please complete the assessment first!")
        if st.button("Go to Assessment"):
            st.session_state.current_page = 'assessment'
            st.rerun()
    else:
        from pages.dashboard import show_dashboard
        show_dashboard()

elif st.session_state.current_page == 'resources':
    from pages.resources import show_resources
    show_resources()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>"
    "Made with ❤️ for India's Youth | © 2026 YouthMind India"
    "</div>", 
    unsafe_allow_html=True
)
    
