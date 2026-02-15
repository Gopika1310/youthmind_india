import streamlit as st

def show_dashboard():
    st.title("📊 Your Dashboard")
    if 'user_data' in st.session_state:
        st.write(f"Welcome {st.session_state.user_data.get('name', 'User')}!")
    else:
        st.warning("Please complete assessment first")