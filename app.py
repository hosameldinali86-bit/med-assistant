import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Hepatology AI", layout="wide")
st.title("🩺 Clinical Assistant")

api_key = st.sidebar.text_input("API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # هذا السطر تم تحديثه ليشمل المسار الكامل للموديل
        model = genai.GenerativeModel('models/gemini-1.5-flash-latest') 
        
        complaint = st.text_area("Patient Scenario:", placeholder="e.g., 58 year old female with dark urine")
        if st.button("Analyze"):
            with st.spinner('Consulting AI...'):
                response = model.generate_content(complaint)
                st.markdown("### Clinical Guidance:")
                st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Enter your API Key to start.")
