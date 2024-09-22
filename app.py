import streamlit as st
from utils.jobpost_handler import get_job_description
from utils.resume_handler import load_document
from utils.llm_handler import generate_cover_letter

temp_file_path="temp/"

# App title
st.set_page_config(page_title="📝 CraftMyLetter")

st.title("📝 CraftMyLetter")
st.write("-----------------------------------------------------------------------------------------------------------") 
st.write("📝 CraftMyLetter is an AI-powered cover letter generator that helps you create personalized, professional cover letters for job applications. Built using Streamlit, LangChain, and LLaMA3, CoverCraft analyzes both job descriptions and resumes to automatically generate a tailored cover letter, highlighting your most relevant skills and experiences.🌟")
st.write("-----------------------------------------------------------------------------------------------------------") 


uploaded_resume = st.file_uploader("Upload a resume in formats like PDF, Word, or text :", accept_multiple_files=False)

resume=load_document(uploaded_document=uploaded_resume)

tone = st.selectbox(
    "Select a Tone of the Letter :",
    options=("Formal",
            "Semi-formal",
            "Friendly or conversational")
    )

length=st.selectbox("Select a Length of the Cover Letter :", 
                    options=("Short and concise",
                             "Medium",
                             "Detailed"
                             )
                    )

focus=st.selectbox("Select a Focus of the Cover Letter :", 
                    options=("Emphasize skills",
                             "Highlight experience",
                             "Showcase accomplishments",
                             "Adaptable mix"
                             )
                    )

preferred_sign_off=st.selectbox("Choose a closing phrase :",
                                options=("Sincerely", "Best regards"))

job_post_url=st.text_input("Paste the URL of the job posting here (optional) : ", value=None)

st.write("or")

job_post_description=st.text_area("Paste the job posting description here (optional) : ", value=None)

job_description=get_job_description(job_description=job_post_description, job_post_url=job_post_url)

linkedIn_profile_url=st.text_input("LinkedIn URL if the user wants to include it in the cover letter : (Optional)")

additional_prompt=st.text_input("Additional Prompt (optional) : ", value=None)

if resume and tone and length and focus and preferred_sign_off and job_description and linkedIn_profile_url:
    if st.button("Generate Cover letter"):
        with st.spinner("Thinking..."):
            generated_cover_letter=generate_cover_letter(job_description=job_description, resume=resume, tone=tone, length=length, sign_off=preferred_sign_off)
            st.write(generated_cover_letter)








