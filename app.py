import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Hepatology AI", layout="wide")
st.title("🩺 Clinical Assistant")

api_key = st.sidebar.text_input("API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # جربنا flash لضمان العمل على النسخة المجانية
        model = genai.GenerativeModel('models/gemini-1.5-flash') 
        
        complaint = st.text_area("Patient Scenario:")
        if st.button("Analyze"):
            response = model.generate_content(f"Medical analysis for: {complaint}")
            st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Enter API Key")
