import streamlit as st

def show_assessment():
    st.title("📝 Wellness Assessment")
    st.write("This is the assessment page")
    
    name = st.text_input("Your name")
    if st.button("Submit"):
        st.session_state.authenticated = True
        st.session_state.user_data = {"name": name}
        st.success("Done!")