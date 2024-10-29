import io
import base64
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import pdf2image
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel('gemini-1.5-pro-exp-0801')

def getGeminiResponse(user_input,pdf_content,prompt):
    response=model.generate_content([user_input,pdf_content[0],prompt])
    return response.text

def inputPdfSetup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Checker")

input_text=st.text_area("Job Description",height=100,key='input')
uploaded_file=st.file_uploader("Upload your Resume",type=["pdf"])
if uploaded_file is not None:
    st.write("PDF uploaded successfully!")

about_resume_btn=st.button("Tell me about my Resume")
improve_skills_btn=st.button("How can I improve my skills?")
missing_keywords_btn=st.button("What are the keywords that are missing?")
percentage_match_btn=st.button("Percentage Match")

input_prompt1 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science,data analytics, AI & ML and ATS functionality. Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches the job description. First the output should come as percentage and then keywords missing and last final thoughts. Use you/your/yours pronouns to refer to the person whose resume you are checking.
"""

input_prompt2 = """
You are a skilled ATS (Applicant Tracking System) scanner with expertise in data science, data analytics, AI, and ML, as well as a strong understanding of ATS functionality. Your task is to assess the resume against the provided job description. First, output the percentage match between the resume and the job description. Next, list any missing keywords, and finally, provide your overall thoughts on the candidate's suitability for the role. Use you/your/yours pronouns to refer to the person whose resume you are checking.
"""

skill_improve_prompt='''
You are a skilled career advisor with expertise in data science, data analytics, AI, ML, and computer science. Your task is to review the candidate's resume in comparison to the job description provided and identify any skill gaps or areas for improvement. Based on these gaps, recommend specific skills, tools, or technologies the candidate should develop to better align with the role requirements. Please explain why these improvements are relevant to the job description. Use you/your/yours pronouns to refer to the person whose resume you are checking.
'''

missing_skills_prompt='''
You are an advanced ATS scanner specialized in data science, data analytics, AI, ML, and technical roles. Your task is to analyze the candidate’s resume and identify any critical keywords or phrases missing when compared to the job description provided. After identifying these keywords, list them along with a brief explanation of their importance in relation to the role. Use you/your/yours pronouns to refer to the person whose resume you are checking.
'''

if about_resume_btn:
    if uploaded_file:
        pdf_content=inputPdfSetup(uploaded_file)
        response=getGeminiResponse(input_prompt1,pdf_content,input_text)
        # st.subheader("The Response is:")
        st.markdown(response)
    else:
        st.error("Please upload a PDF.")

elif percentage_match_btn:
    if uploaded_file:
        pdf_content=inputPdfSetup(uploaded_file)
        response=getGeminiResponse(input_prompt2,pdf_content,input_text)
        # st.subheader("The Response is:")
        st.markdown(response)
    else:
        st.error("Please upload a PDF.")

elif improve_skills_btn:
    if uploaded_file:
        pdf_content=inputPdfSetup(uploaded_file)
        response=getGeminiResponse(skill_improve_prompt,pdf_content,input_text)
        # st.subheader("The Response is:")
        st.markdown(response)
    else:
        st.error("Please upload a PDF.")

elif missing_keywords_btn:
    if uploaded_file:
        pdf_content = inputPdfSetup(uploaded_file)
        response = getGeminiResponse(missing_skills_prompt, pdf_content, input_text)
        # st.subheader("The Response is:")
        st.markdown(response)
    else:
        st.error("Please upload a PDF.")