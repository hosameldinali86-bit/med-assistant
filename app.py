import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="Dr. Hossam AI", layout="wide")
st.title("🩺 Clinical Assistant")

api_key = st.sidebar.text_input("Enter API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # استخدام الموديل بدون كلمة models/ وبدون إضافات هو الحل الأضمن حالياً
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        complaint = st.text_area("Patient Scenario:")
        if st.button("Analyze"):
            if complaint:
                with st.spinner('Analyzing...'):
                    # إجبار النظام على توليد المحتوى
                    response = model.generate_content(complaint)
                    st.success("Analysis Complete:")
                    st.write(response.text)
            else:
                st.warning("Please enter a case.")
    except Exception as e:
        st.error(f"Note: If you see 404, please check if the API key is active. Error: {e}")
