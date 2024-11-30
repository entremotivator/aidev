import streamlit as st

# Configure the app
st.set_page_config(page_title="Donmenico Hudson - Full Stack Developer", layout="centered")

# Personal Information Section
def personal_info():
    st.header("👤 Personal Information")
    st.write("""
    - **Name:** Donmenico Hudson  
    - **Role:** Full Stack Developer  
    - **Location:** Atlanta, GA, USA  
    - **Email:** donmenico.hudson@example.com  
    - **Phone:** +1 (123) 456-7890  
    - **LinkedIn:** [linkedin.com/in/donmenicohudson](https://linkedin.com/in/donmenicohudson)  
    - **GitHub:** [github.com/donmenicohudson](https://github.com/donmenicohudson)  
    """)

# Skills Section
def skills():
    st.header("💻 Skills")
    st.write("""
    - **Languages:** Python, JavaScript, TypeScript, Ruby, PHP  
    - **Frontend:** React.js, Angular, HTML5, CSS3, Bootstrap  
    - **Backend:** Node.js, Django, Flask, Ruby on Rails, Laravel  
    - **Databases:** MySQL, PostgreSQL, MongoDB, Firebase  
    - **DevOps:** Docker, Kubernetes, CI/CD, Jenkins, AWS  
    - **Other Tools:** Git, Webpack, Babel, REST APIs, GraphQL  
    """)

# Experience Section
def experience():
    st.header("📂 Professional Experience")

    st.subheader("1. Senior Full Stack Developer - TechWave Solutions (2020 - Present)")
    st.write("""
    - Designed and implemented scalable web applications using **React.js**, **Node.js**, and **PostgreSQL**.  
    - Integrated **REST APIs** and **GraphQL** endpoints for seamless data management.  
    - Mentored junior developers and improved team productivity by 25%.  
    """)

    st.subheader("2. Full Stack Developer - Innovatech Systems (2017 - 2020)")
    st.write("""
    - Developed responsive and interactive user interfaces using **Angular** and **Bootstrap**.  
    - Built and maintained backend services with **Python/Django** and **MySQL**.  
    - Deployed applications to AWS using **Docker** and **Kubernetes**.  
    """)

    st.subheader("3. Web Developer - CodeCraft Studios (2015 - 2017)")
    st.write("""
    - Created over 20 dynamic websites using **PHP**, **Laravel**, and **JavaScript**.  
    - Collaborated with cross-functional teams to deliver projects on time.  
    - Enhanced website performance by optimizing code and assets.  
    """)

# Projects Section
def projects():
    st.header("🛠️ Projects")

    st.subheader("1. E-Commerce Platform")
    st.write("""
    - Built a scalable e-commerce platform with **React.js** and **Node.js**.  
    - Integrated payment gateways like **Stripe** and **PayPal**.  
    - Deployed the system on AWS with **Docker** and **Kubernetes**.  
    """)

    st.subheader("2. Social Media Analytics Dashboard")
    st.write("""
    - Developed a dashboard to analyze social media engagement using **Django** and **Plotly**.  
    - Implemented real-time data visualization for user insights.  
    - Used **MongoDB** for data storage and aggregation.  
    """)

    st.subheader("3. Task Management App")
    st.write("""
    - Created a task management app with **React Native** for cross-platform compatibility.  
    - Used **Firebase** for backend and authentication.  
    - Ensured smooth performance across iOS and Android devices.  
    """)

# Education Section
def education():
    st.header("🎓 Education")
    st.subheader("Bachelor of Science in Computer Science")
    st.write("""
    - **University:** Georgia Institute of Technology  
    - **Graduation Year:** 2015  
    - **GPA:** 3.8/4.0  
    - Relevant Coursework: Software Engineering, Database Systems, Algorithms and Data Structures  
    """)

# Main App
def main():
    st.title("Donmenico Hudson - Full Stack Developer")
    st.write("Welcome to my professional résumé. Explore the sections below to learn more about my skills, experience, and projects.")
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    sections = {
        "Personal Information": personal_info,
        "Skills": skills,
        "Experience": experience,
        "Projects": projects,
        "Education": education,
    }
    choice = st.sidebar.radio("Go to", list(sections.keys()))

    # Render the selected section
    sections[choice]()

if __name__ == "__main__":
    main()
