import streamlit as st

temp_file_path="temp/"

# App title
st.set_page_config(page_title="📝 CraftMyLetter")

st.title("📝 CraftMyLetter")
st.write("-----------------------------------------------------------------------------------------------------------") 
st.write("📝 CraftMyLetter is an AI-powered cover letter generator that helps you create personalized, professional cover letters for job applications. Built using Streamlit, LangChain, and LLaMA3, CoverCraft analyzes both job descriptions and resumes to automatically generate a tailored cover letter, highlighting your most relevant skills and experiences.🌟")
st.write("-----------------------------------------------------------------------------------------------------------") 


uploaded_resume = st.file_uploader("Upload a resume in formats like PDF, Word, or text :", accept_multiple_files=False)

selected_tone = st.selectbox(
    "Select a Tone of the Letter :",
    options=("Formal",
            "Semi-formal",
            "Friendly or conversational")
    )

additional_prompt=st.text_input("Additional Prompt (optional) : ", value=None)

    




