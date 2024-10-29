# ATS Resume Expert

This project is an ATS (Applicant Tracking System) for evaluating candidate resumes against job descriptions using Google Gemini's generative capabilities. It is tailored for fields in data science, data analytics, AI, ML, neural networks, and other computer science and technology roles. The application helps identify resume strengths, weaknesses, skill gaps, and keyword matches, assisting candidates in optimizing their resumes for specific roles.

## Features

- **Percentage Match**: Evaluate the alignment between the job description and resume with a percentage match score.
- **Skill Improvement Recommendations**: Identify areas for skill improvement based on resume gaps and job description.
- **Missing Keywords Analysis**: Discover missing keywords critical for ATS and relevance to the job description.
- **Strengths and Weaknesses Evaluation**: A professional assessment of the candidate’s profile against role requirements.

## Getting Started

### Prerequisites

- **Python** 3.10.6 or later
- **Streamlit** for UI
- **Google Generative AI** SDK
- **Poppler** for PDF-to-image conversion
- **pdf2image**, **Pillow** (PIL), and **dotenv** Python packages

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sohamfcb/ats-checker-gemini
   cd ats-checker-gemini

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

3. **Set Up Google Gemini API Key:**

- Obtain an API key from Google Generative AI.
- Add the API key to a `.env` file:

   ```makefile
  GOOGLE_API_KEY=your_api_key

4. **Install Poppler (for Windows):**
- Download Poppler for Windows and extract it.
- Add the path to the `poppler/bin` directory to your system PATH.

### Running the Application

Start the Streamlit app by running:

```bash
streamlit run app.py
```

## Prompts

The system uses the following prompts for evaluation:

- **Strengths and Weaknesses:** Assesses the alignment of the resume with the job description.
- **Percentage Match:** Provides a percentage match, missing keywords, and overall feedback.
- **Skill Improvement:** Recommends specific skills for the candidate to improve.
- **Missing Keywords:** Lists keywords missing from the resume, essential to the job description.

## Code Overview

- `app.py`: Main application file for Streamlit, handling the UI and API calls.
- `inputPdfSetup()`: Converts the uploaded PDF to an image and encodes it for Google Gemini.
- `getGeminiResponse()`: Queries the Google Gemini API using specific prompts and returns responses.

## Error Handling

The code includes error handling for:

- **PDF Upload:** Alerts users if no PDF is uploaded.
- **API Errors:** Ensures smooth operation if the Gemini API fails.
- **File Path Issues:** Catches and handles any issues with Poppler setup or path configuration.
