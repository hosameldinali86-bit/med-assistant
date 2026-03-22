import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Hepatology AI", layout="wide")
st.title("🩺 Clinical Assistant")

api_key = st.sidebar.text_input("API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # هذا هو الاسم الصحيح والمحدث لموديل جوجل المجاني
        model = genai.GenerativeModel('gemini-1.5-flash-latest') 
        
        complaint = st.text_area("Patient Scenario:")
        if st.button("Analyze"):
            with st.spinner('Consulting AI...'):
                response = model.generate_content(f"Provide a clinical analysis for: {complaint}")
                st.markdown("### Clinical Guidance:")
                st.write(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please enter your API Key to start.")
