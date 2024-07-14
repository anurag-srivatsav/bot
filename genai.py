import os
import streamlit as st
from google.generativeai import configure, GenerativeModel

# Set your API key as an environment variable
os.environ['GENAI_API_KEY'] = 'AIzaSyDzeATPLWRenJGapH8wOCtKEs_QFf6FPR0'  # Replace with your actual API key

# Configure the SDK with the API key
api_key = os.getenv('GENAI_API_KEY')
configure(api_key=api_key)

# Define generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the generative model
model = GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)
chat_session = model.start_chat(
  history=[]
)
knowledge_base = {
    "name": "Anurag Srivatsav",
    "contact": {
        "phone": "9581403857",
        "email": "anuragsrivatsav4@gmail.com",
        "linkedin": "https://linkedin.com/in/anuragsrivatsav",
        "github": "https://github.com/anurag-srivatsav",
    },
    "education": {
        "university": "KL University Hyderabad",
        "degree": "B.Tech in Artificial Intelligence and Data Science",
        "GPA": "8.36/10",
        "graduation_date": "July 2025",
    },
    "experience": [
        {
            "role": "Participant",
            "organization": "Amazon ML Summer School",
            "duration": "September 2023 - October 2023",
            "details": [
                "Engaged with 10 advanced machine learning models and techniques.",
                "Collaborated with 5 ML scientists.",
            ],
        },
        {
            "role": "Google Cloud Ready Facilitator",
            "organization": "Google",
            "duration": "February 2022 - Present",
            "details": [
                "Explored Google Cloud Platform applications.",
                "Contributed to 70% of cloud platform endeavors.",
                "Completed weekly and monthly Google Cloud skill boost challenges.",
            ],
        },
    ],
    "projects": [
        {
            "name": "Task Manager Application with MongoDB",
            "duration": "February 2023 - March 2023",
            "technologies": ["Python", "MongoDB", "Flask"],
            "details": [
                "Developed a web app for task management.",
                "Integrated features like task addition, completion tracking, and secure user authentication.",
            ],
            "link": "https://github.com/anurag-srivatsav/task-manager",
        },
        {
            "name": "AI Voice Clone",
            "duration": "December 2023 - February 2024",
            "technologies": ["Python", "OpenAI", "LangChain", "Gradio", "PlayHT", "Hugging Face"],
            "details": [
                "Implemented an AI voice clone application.",
                "Engineered a customizable voice clone using advanced NLP techniques.",
            ],
            "link": "https://github.com/anurag-srivatsav/ai-voice-clone",
        },
        {
            "name": "TEXT to HTML converter",
            "duration": "February 2023 - April 2023",
            "technologies": ["Django"],
            "details": [
                "Designed and implemented a TEXT to HTML converter using Django framework.",
                "Implemented functionality to convert text input into HTML format.",
                "Integrated user-friendly interface for easy input and output interaction."
            ],
            "link": "https://github.com/anurag-srivatsav/text-to-html-converter",
        },
        {
            "name": "Image Classification (Cat vs. Dog)",
            "duration": "March 2023 - May 2023",
            "technologies": ["Python", "TensorFlow", "Keras"],
            "details": [
                "Developed a deep learning model to classify images of cats and dogs.",
                "Preprocessed a dataset of cat and dog images for training and validation.",
                "Implemented data augmentation techniques to improve model generalization.",
                "Evaluated model performance using metrics like accuracy and loss."
            ],
            "link": "https://github.com/anurag-srivatsav/image-classification",
        }
    ],
    "skills": {
        "languages": ["C", "Python", "Java", "R"],
        "frameworks": ["Django", "React.js", "Node.js", "TensorFlow"],
        "databases": ["MySQL", "MongoDB", "Oracle"],
        "web": ["HTML", "CSS", "JavaScript", "Tableau", "Power BI"],
        "Cloud": ["Google Cloud", "Azure", "AWS"],
        "DS & AI": ["TensorFlow", "Machine Learning", "Artificial Intelligence"],
        "Other": ["Git", "Jupyter Notebook", "Docker"]
    },
    "certifications": [
        {
            "name": "Google Cloud Data Analytics Certificate",
            "link": "https://www.credly.com/badges/97a889b4-6069-4118-9b29-3f7de7a3cc23"
        },
        {
            "name": "Google TensorFlow Developer Certificate",
            "link": "https://www.credential.net/d81c83e2-673f-475f-a6dc-bf5ffafc81b7#gs.ak34mm"
        },
        {
            "name": "Oracle Cloud Infrastructure 2024 Generative AI Certified Professional",
            "link": "https://catalog-education.oracle.com/pls/certview/sharebadge?id=B10032C2F707BD514D547D772A9983B3BBAE0554318278F137B99606886BC7FC"
        },
        {
            "name": "Microsoft Certified: Azure AI Fundamentals",
            "link": "https://learn.microsoft.com/en-us/users/anuragsrivatsav-6772/credentials/b42af8fa0151a887?ref=https%3A%2F%2Fwww.linkedin.com%2F"
        },
        {
            "name": "Oracle Cloud Infrastructure 2023 Certified Architect Associate",
            "link": "https://catalog-education.oracle.com/pls/certview/sharebadge?id=B10032C2F707BD514D547D772A9983B33C5B29DDB470072B0A3CDB447E72BBE0"
        },
        {
            "name": "Google AI Essentials",
            "link": "https://www.credly.com/badges/2e2258c6-8d4b-4be0-ba97-8dfaea5f5116"
        },
        {
            "name": "CS50’s Introduction to Programming with Python",
            "link": "https://certificates.cs50.io/c54c3ae3-1816-42b1-b3db-316da4b49055.pdf"
        },
        {
            "name": "NoSQL - MongoDB",
            "link": "https://courses.etrain.skillsnetwork.site/certificates/8a07367606c641cfa29e468a11de8179"
        }
    ]
}

# Function to check the knowledge base for answers
def check_knowledge_base(question, user_name):
    question = question.lower()

    name_keywords = ["name", "who are you", "what is your name", "tell me your name"]
    contact_keywords = ["contact", "email", "phone", "reach you","how can I reach you","contact details","phone number","email address","linkedin profile","github profile"]
    education_keywords = ["education", "study", "schooling", "university", "college","where did you study","your schooling","educational background","college details","clg","academic background","educational qualifications"]
    experience_keywords = ["experience", "work", "job", "role", "position","previous work","jobs you've had","your role","work experience","positions held"]
    projects_keywords = ["projects", "project", "work","show me your projects","what projects have you worked on","details of your projects","your work examples"]
    skills_keywords = ["skills", "abilities", "proficiencies","what are your skills","your abilities","proficiency areas","what can you do"]
    certifications_keywords = ["certifications", "certificates", "credentials","what certifications do you have","your certificates","credentials you hold","certification details"]
    about_me_keywords = ["about yourself", "about me","about you", "u", "about", "tell me about yourself","who are you","introduce yourself","personal details"]

    if any(keyword in question for keyword in name_keywords):
        return f"My name is Anurag Srivastav."
    elif any(keyword in question for keyword in contact_keywords):
        return f"You can reach me at mail: {knowledge_base['contact']['email']} or phn No. :{knowledge_base['contact']['phone']} or Linkedin: {knowledge_base['contact']['linkedin']} or Github: {knowledge_base['contact']['github']}"
    elif any(keyword in question for keyword in education_keywords):
        return f"I studied at {knowledge_base['education']['university']} and achieved a GPA of {knowledge_base['education']['GPA']}."
    elif any(keyword in question for keyword in experience_keywords):
        experience = knowledge_base["experience"]
        return "\n".join([f"I worked as a {exp['role']} at {exp['organization']} from {exp['duration']}.\n\n" for exp in experience])
    elif any(keyword in question for keyword in projects_keywords):
        projects = knowledge_base["projects"]
        response = ""
        for proj in projects:
            response += f"Project: {proj['name']} - Duration: {proj['duration']} - Technologies: {', '.join(proj['technologies'])}. Link: {proj['link']}\n\n"
        return response
    elif any(keyword in question for keyword in skills_keywords):
        return f"My skills include: \n\n Languages{', '.join(knowledge_base['skills']['languages'])}\n\n Frameworks: {', '.join(knowledge_base['skills']['frameworks'])}\n\n Databases: {', '.join(knowledge_base['skills']['databases'])}\n\n Web: {', '.join(knowledge_base['skills']['web'])}\n\n cloud: {', '.join(knowledge_base['skills']['Cloud'])}\n\n DS & AI: {', '.join(knowledge_base['skills']['DS & AI'])}, {', '.join(knowledge_base['skills']['Other'])}."
    elif any(keyword in question for keyword in certifications_keywords):
        certifications = knowledge_base["certifications"]
        response = ""
        for cert in certifications:
            response += f"Certification: {cert['name']}. Link: {cert['link']}\n\n"
        return response
    elif any(keyword in question for keyword in about_me_keywords):
        return f"My name is Anurag Srivastav. \n\n Final year BTech student specializing in Artificial Intelligence and Data Science at {knowledge_base['education']['university']}, with a strong academic background and practical experience in machine learning, deep learning, and statistical modeling.\n\n Seeking opportunities to apply analytical skills and contribute to innovative projects in AI-driven solutions. \n\n I have experience in {', '.join([exp['role'] for exp in knowledge_base['experience']])}. \n\n My projects include {', '.join([proj['name'] for proj in knowledge_base['projects']])}. \n\n I have skills in {', '.join(knowledge_base['skills']['languages'])}, {', '.join(knowledge_base['skills']['frameworks'])}, {', '.join(knowledge_base['skills']['databases'])}, and {', '.join(knowledge_base['skills']['web'])}. I am interested in AI and data science-related jobs."
    else:
        return None
# Streamlit app
st.title('Ask anything about me this AI bot will answer all your questions')


    
# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Function to interact with the generative model
@st.cache_resource
def start_chat():
    chat_session = model.start_chat(history=[])
    return chat_session

# Main interaction loop
chat_session = start_chat()

# User name input
user_name = st.text_input('Enter your name:', '')

if user_name:
    user_input = st.text_input('You:', '')

    if st.button('Send'):
        if user_input:
            # Check the knowledge base first
            kb_response = check_knowledge_base(user_input, user_name)
            if kb_response:
                bot_response = kb_response
            else:
                # Prefix user input with their name
                user_message = f"{user_name}: {user_input}"
                response = chat_session.send_message(user_message)
                bot_response = response.text
            
            # Update chat history
            st.session_state['chat_history'].append((f"{user_name} ", user_input))
            st.session_state['chat_history'].append(('Nani ', bot_response))
            
            # Display user message and bot response using markdown
            conversation = f"{user_name}: {user_input}\n\n Nani: {bot_response}"
            st.markdown(conversation, unsafe_allow_html=True)

    st.write('')
    st.subheader("Chat History:")
    for idx, (role, text) in enumerate(st.session_state['chat_history']):
        if idx % 2 == 0:
            st.write(f"{role}: {text}")
        else:
            st.write(f"{role}: {text}")
            st.write("---")  # Add a line to differentiate entries
        