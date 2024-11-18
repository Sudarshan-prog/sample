import streamlit as st
from PIL import Image

# Set up page configuration
st.set_page_config(page_title="My Portfolio", layout="wide", page_icon=":wave:")

# Sidebar
with st.sidebar:
    st.image("my profile.jpg", width=150)  # Add your photo
    st.title("Sudarshan S")
    st.write("### Frontend Developer")
    st.write("Welcome to my portfolio! Explore my skills, projects, and get in touch.")

    # Social Links
    st.markdown(
        """
        [LinkedIn](https://linkedin.com)  
        [GitHub](https://github.com)  
        [Email Me](mailto:your_email@example.com)
        """
    )

# Main Content
st.title("Welcome to My Portfolio! :wave:")
st.write("Hi there! I'm Sudarshan S, a frontend developer passionate about creating an innovative websites.")

# About Section
st.header("About Me")
st.write("""
I am currently pursuing a engineering degree with expertise in full-stack technology. I have experience working on projects 
involving e-commerce website,food delivery company. I love solving problems, learning new technologies, and contributing to impactful projects.
""")

# Skills Section
st.header("Skills")
skills = ["Python", "Streamlit", "Data Analysis", "Machine Learning", "Web Development"]
cols = st.columns(len(skills))
for i, skill in enumerate(skills):
    cols[i].button(skill)

# Projects Section
st.header("Projects")
projects = {
    "Project 1": "Description of project 1. [GitHub](https://github.com/project1)",
    "Project 2": "Description of project 2. [GitHub](https://github.com/project2)",
    "Project 3": "Description of project 3. [GitHub](https://github.com/project3)",
}
for project, description in projects.items():
    st.subheader(project)
    st.write(description)

# Contact Section
st.header("Contact Me")
st.write("""
Feel free to reach out via email or connect with me on LinkedIn.  
I'm open to new opportunities and collaborations!
""")
contact_form = """
<form action="https://formsubmit.co/your_email@example.com" method="POST">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your Message" required></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("© 2024 Sudarshan S. All Rights Reserved.")