import streamlit as st

temp_file_path="temp/"

# App title
st.set_page_config(page_title="📝 CraftMyLetter")

st.title("📝 CraftMyLetter")
st.write("-----------------------------------------------------------------------------------------------------------") 
st.write("📝 CraftMyLetter is an AI-powered cover letter generator that helps you create personalized, professional cover letters for job applications. Built using Streamlit, LangChain, and LLaMA3, CoverCraft analyzes both job descriptions and resumes to automatically generate a tailored cover letter, highlighting your most relevant skills and experiences.🌟")
st.write("-----------------------------------------------------------------------------------------------------------") 


uploaded_resume = st.file_uploader("Upload a resume in formats like PDF, Word, or text :", accept_multiple_files=False)

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

st.text_area("Paste the job posting description here (optional) : ", value=None)

linkedIn_profile_url=st.text_input("LinkedIn URL if the user wants to include it in the cover letter : (Optional)")

additional_prompt=st.text_input("Additional Prompt (optional) : ", value=None)






