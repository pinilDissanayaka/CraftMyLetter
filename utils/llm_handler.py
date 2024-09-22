from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from utils.config import get_llm

def generate_cover_letter(job_description, resume, tone, length, sign_off):
    cover_letter_prompt_template="""
    You are an AI language model tasked with generating a personalized cover letter based on the following information:

        1. **Job Description**: {JOB_DESCRIPTION}
        2. **Resume **: {RESUME}
        3. **Tone**: {TONE}
        4. **Length Preference**: {LENGTH}
        5. **Closing Preference**: {SIGN_OFF}

    Based on this information, generate a professional cover letter that:

    - Addresses the hiring manager (if provided) and the company by name.
    - Clearly states the position the applicant is applying for.
    - Highlights the relevant skills and experiences that match the job description.
    - Includes a personalized motivation statement expressing enthusiasm for the role.
    - Maintains a professional tone and is structured appropriately.

    Make sure the cover letter flows logically and concludes with a strong closing statement that encourages further communication.
    """
    
    cover_letter_prompt=ChatPromptTemplate.from_template(template=cover_letter_prompt_template)
    
    llm=get_llm()
    
    cover_letter_generate_chain=(
        {"JOB_DESCRIPTION" : RunnablePassthrough(), "RESUME" : RunnablePassthrough(), "TONE":RunnablePassthrough(), "LENGTH":RunnablePassthrough(), "SIGN_OFF":RunnablePassthrough()}|
        cover_letter_prompt |
        llm |
        StrOutputParser()
    )
    
    generated_cover_letter=cover_letter_generate_chain.invoke({"JOB_DESCRIPTION" : job_description, "RESUME" : resume, "TONE":RunnablePassthrough(), "LENGTH": tone, "SIGN_OFF": sign_off})
    
    return generate_cover_letter