import streamlit as st

def show_dashboard():
    st.title("📊 Your Wellness Dashboard")
    
    # Welcome message with styling
    st.markdown(f"""
    <div style='background-color: #e8f5e9; padding: 20px; border-radius: 10px; margin-bottom: 20px;'>
        <h3 style='color: #2e7d32; margin: 0;'>Welcome {st.session_state.user_data.get('name', 'Friend')}! 👋</h3>
        <p style='color: #1b5e20; margin: 5px 0 0 0;'>Here's your wellness journey progress</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key metrics in columns (responsive!)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background-color: #f0f4f8; padding: 15px; border-radius: 10px; text-align: center;'>
            <h2 style='margin: 0; color: #1e88e5;'>😊</h2>
            <h3 style='margin: 5px 0;'>78%</h3>
            <p style='margin: 0; color: #666;'>Mood Score</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background-color: #f0f4f8; padding: 15px; border-radius: 10px; text-align: center;'>
            <h2 style='margin: 0; color: #43a047;'>🔥</h2>
            <h3 style='margin: 5px 0;'>7 days</h3>
            <p style='margin: 0; color: #666;'>Current Streak</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background-color: #f0f4f8; padding: 15px; border-radius: 10px; text-align: center;'>
            <h2 style='margin: 0; color: #fb8c00;'>🎯</h2>
            <h3 style='margin: 5px 0;'>12</h3>
            <p style='margin: 0; color: #666;'>Activities Done</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Recent activity section
    st.markdown("---")
    st.subheader("📋 Recent Activity")
    
    activities = [
        {"day": "Monday", "activity": "5-min Meditation", "status": "✅ Completed"},
        {"day": "Tuesday", "activity": "Gratitude Journal", "status": "✅ Completed"},
        {"day": "Wednesday", "activity": "Morning Yoga", "status": "⏳ Pending"}
    ]
    
    for act in activities:
        st.markdown(f"""
        <div style='display: flex; justify-content: space-between; padding: 10px; border-bottom: 1px solid #eee;'>
            <span><b>{act['day']}</b>: {act['activity']}</span>
            <span style='color: {"#43a047" if "✅" in act["status"] else "#fb8c00"};'>{act['status']}</span>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick action buttons
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🧘 Add Today's Activity", use_container_width=True):
            st.info("Feature coming soon!")
    
    with col2:
        if st.button("📊 View Full Report", use_container_width=True):
            st.info("Feature coming soon!")