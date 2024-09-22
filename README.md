# 📝 CoverCraft: LLM-Powered Cover Letter Generator
CoverCraft is an AI-powered cover letter generator that helps you create personalized, professional cover letters for job applications. Built using Streamlit, LangChain, and LLaMA3, CoverCraft analyzes both job descriptions and resumes to automatically generate a tailored cover letter, highlighting your most relevant skills and experiences.

## ✨ Features
1. 🛠️ Job Description Parsing: Understands job requirements and responsibilities by parsing job descriptions.
2. 📄 Resume Analysis: Extracts key skills, achievements, and experience from your resume.
3. ✍️ AI-Powered Letter Generation: Uses LLaMA3 via LangChain to generate personalized, compelling cover letters.
4. 🎨 Customizable Output: Adjust the tone, length, and style of the generated cover letters to suit your preferences.
5. 💼 Professional Tone: Ensures that the cover letter maintains a polished and professional language.
6. 🚀 Streamlit Interface: Easy-to-use web interface for quick generation and editing.

## 🖥️ Demo
Check out the live demo of CoverCraft here. (Link if hosted, or remove if no demo available.)

## 🔧 Technologies
1. 🐍 Python: Core programming language.
2. 🌐 Streamlit: For building a fast and interactive web interface.
3. 🔗 LangChain: To chain together job description parsing, resume analysis, and letter generation processes.
4. 🦙 LLaMA3: Large Language Model used for generating cover letter content.
5. 🧠 NLP Tools: Spacy, Hugging Face transformers for parsing job descriptions and resumes.

## 🚀 How It Works
1. Input Job Description: Copy-paste the job description or upload a job posting file.
2. Upload Resume: Provide your resume for the system to analyze your skills and experience.
3. Generate Cover Letter: Click "Generate" to create a personalized cover letter based on your inputs.
4. Review & Edit: Edit the generated cover letter within the web app for final tweaks and adjustments.

## ⚙️ Installation
Follow these steps to set up CoverCraft on your local machine:

1. Clone the repository:
```
git clone https://github.com/username/CoverCraft.git
cd CoverCraft
```

2. Create a virtual environment:
```
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run the Streamlit app:
```
streamlit run app.py
```

5. Open the browser to http://localhost:8501 to interact with the app!

## 🛠️ Project Structure
```
CoverCraft/
├── app.py                 # Main Streamlit app
├── backend/               # LangChain and LLaMA3 integration
├── data/                  # Sample resumes and job descriptions
├── components/            # Custom components for the Streamlit UI
├── models/                # Pre-trained models and LLaMA3 logic
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

## 🎯 Usage
- Run the app using the streamlit run app.py command.
- Upload your resume and input a job description on the web interface.
- Generate your customized cover letter!
- Optionally, export or download the generated letter for your job application.

## 🤝 Contributing
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request, or open an issue for feature requests and bug reports.

1. Fork the project.
2. Create your feature branch (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a pull request.
   
## 📝 License
This project is licensed under the MIT License. See the LICENSE file for more details.

## 📧 Contact
For any questions or feedback, feel free to reach out via email: email@example.com.

## 📸 Screenshots 
Upload Resume	Generate Letter	View Result


With CoverCraft, job applications just got a whole lot easier! 🚀
