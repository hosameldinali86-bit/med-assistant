import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Dr. Hossam Ali | Clinical AI", layout="wide")
st.title("🩺 Clinical Assistant")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # التعديل هنا: نستخدم الموديل الأساسي بدون إضافات لضمان التوافق
        model = genai.GenerativeModel('gemini-1.5-flash') 
        
        complaint = st.text_area("Patient Scenario:", placeholder="e.g., 58 year old male with dark urine")
        
        if st.button("Analyze"):
            if complaint:
                with st.spinner('Consulting AI...'):
                    # نحدد الـ API Version يدوياً لضمان العمل
                    response = model.generate_content(complaint)
                    st.markdown("### Clinical Guidance:")
                    st.write(response.text)
            else:
                st.warning("Please enter a scenario.")
    except Exception as e:
        # لو حصل خطأ، البرنامج هيقولك سببه بدقة
        st.error(f"System Message: {e}")
else:
    st.info("Waiting for API Key...")
