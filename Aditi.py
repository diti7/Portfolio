import streamlit as st

# Set up the page configuration
st.set_page_config(page_title = "Aditi Patel", page_icon = ":✨:", layout = "wide", initial_sidebar_state = "expanded") 

# --------------- Sidebar for Navigation ---------------
st.sidebar.title("Navigation")

# Define the pages
pages = {
    "🏠Home": "home",
    "🎯Projects": "projects",
    "📄Resume": "resume",
    "👩‍💻Goals": "goals"
}

# Nagivation labels
page = "home"
for label, value in pages.items():
    if st.sidebar.button(label, key=value):
        page = value

# ---------------------------------------------------------------------------------------------------------
# ----------------------------------------------- Home Page -----------------------------------------------
# --------------------------------------------------------------------------------------------------------- 
if page == "home":
    #st.title("Hi, I'm [Name] 😊")
    st.markdown(
        """
        <h2 style ="border-bottom: 2px solid #57CC99; padding-bottom: 10px;">Hi, I'm Aditi 😊</h2>
        """, unsafe_allow_html = True
    )
    st.write("")

    # Home page columns...
    col1, col2, col3 = st.columns([1.3, 0.2, 1])

    #About...
    with col1:
        st.write("""
            I’m a third-year Computer Science student at York University - Lassonde School of Engineering, passionate about software development, data analysis, and UX/UI design. I enjoy participating in hackathons and making projects that challenge my creativity and open my learning pathways. I'm always seeking opportunities to work on different projects that push my skills to foster new learning experiences.
        """)
        st.write("Let's connect & collaborate!")
        st.write("📍Location: Toronto, Canada")
        st.write("👩‍💻Co-op: Application Support Analyst at FGF Brands")
        st.write("👩‍🎓Education: Computer Science at York University")
        #st.write("🎨Interests: Hackathons, Data Science, UX/UI Designs")
        st.write("👀Fun Fact: I'm a self-taught artist.")

        # Connect...
        st.markdown(
            """
            <div style = "display: flex; gap: 10px; align-items: center;">
                <a href = "https://www.linkedin.com/in/aditi-patel-43452927a/">
                    <img src="https://th.bing.com/th/id/OIP.Fc-evvSo3ccnVv1tjSvkcQHaHa?w=183&h=183&c=7&r=0&o=5&dpr=1.3&pid=1.7" width="40" style="margin-right: 20px;" "margin-left: 20px;>
                </a>
                <a href = "https://github.com/diti7">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="40" style="margin-right: 20px;" "margin-left: 20px;>
                </a>
                <a href ="aditipatel755@gmail.com">
                    <img src="https://static.vecteezy.com/system/resources/previews/022/648/084/original/email-icon-for-your-website-mobile-presentation-and-logo-design-free-vector.jpg" width="60" style="margin-right: 20px;" "margin-left: 20px;>
                </a>
            </div>
            """, unsafe_allow_html=True
        )


    #Portrait...
    with col3:
        st.image("https://github.com/diti7/Portfolio/blob/main/Portrait.jpg?raw=true", width = 265)


    #Tech Stack...
    st.markdown(
        """
        <h2 style = "border-bottom: 2px solid #57CC99; padding-bottom: 10px;">Tech Stack ⚙️</h2>
        """, unsafe_allow_html=True
    )
    st.write("")
    #Container hover - colour change...
    st.markdown(
        """
        <style>
        .stButton>button {
            border: 2px solid;
            border-color: grey;
            color: inherit; /*
        }
        .stButton>button:hover {
            border-color: #57CC99; 
            background-color: transparent;
        }
        </style>
        """, unsafe_allow_html=True
    )

    #stack containers (skills)...
    """
    skill_col_size = 5
    tech = {
        'skills': [
            'Python', 'Java', 'MySQL', 'PostgreSQL', 'Pandas', 'Matplotlib',
            'NumPy', 'Scikit-Learn', 'Seaborn', 'Streamlit', 'HTML', 'CSS',
            'Javascript', 'React', 'Git', 'GitHub', 'VS Code', 'Linux', 'Figma'
        ]
    }"""
     skill_col_size = 5
    tech = {
        st.header("🛠 Tech Stack (Organized)")

        col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Frontend")
        st.write("React • Tailwind • JavaScript")

    with col2:
        st.subheader("Backend & Core")
        st.write("Python • Java • C • Linux")

    with col3:
        st.subheader("Data & Tools")
        st.write("SQL • Pandas • Streamlit • Git")
    }

    def skill_tab():
        rows, cols = len(tech['skills']) // skill_col_size, skill_col_size
        skills = iter(tech['skills'])

        if len(tech['skills']) % skill_col_size != 0:
            rows = rows + 1
        for x in range(rows):
            columns = st.columns(skill_col_size)
            for index_ in range(skill_col_size):
                try:
                    #no action...
                    if columns[index_].button(next(skills), key = f"skill_{x}_{index_}"):
                        pass
                except StopIteration:
                    break

    with st.spinner(text ="Loading section..."):
        skill_tab()

 

# ---------------------------------------------------------------------------------------------------------
# ------------------------------------------- Projects Page -----------------------------------------------
# --------------------------------------------------------------------------------------------------------- 
elif page == "projects":
    st.markdown("<h2 style = 'border-bottom: 2px solid #57CC99;'>Projects</h2>", unsafe_allow_html = True)
    st.write("")

    #Project List...
    projects = [
        {
            "title": "Hospital Data Analysis - Web App",
            "stack": "⚙️Python, Pandas, Matplotlib, Seaborn, Streamlit, Scikit-learn, NumPy",
            "desc": "This Hospital Data Analysis Web App is built using Python and Streamlit to explore and visualize hospital admission data. It includes data cleaning, advanced visualizations with Seaborn and Matplotlib, and a predictive model using Scikit-learn to forecast future admissions. The app provides valuable insights for optimizing hospital resource allocation and analyzing trends in patient demographics.",
            #"images": "Github.jpg",
            "github": "https://github.com/diti7/Hospital-Data-Analysis-Web-App"
        },
        {
            "title": "HoloMath – Interactive 3D Learning Tool",
            "stack": "⚙️React.js, Node.js, Express.js, HTML, CSS, JavaScript, OpenAI API, Git, Postman",
            "desc": "HoloMath is an innovative educational tool designed to revolutionize the way students learn mathematics. By leveraging cutting-edge technologies, HoloMath offers an immersive and interactive learning experience that makes complex mathematical concepts more accessible and engaging. It transforms education by shifting perspectives—from memorization to exploration. Using gesture-based interaction and 3D simulations, it makes abstract concepts tangible. Accessible to all, it fosters curiosity and inclusion.",
            #"images": "Github.jpg",
            "github": "https://github.com/diti7/UofTHack12"
        },
        {
            "title": "404: Team Not Found",
            "stack": "⚙️React.js, Tailwind CSS, Node.js, Express, Python, Flask, PostgreSQL, JWT, Vercel, Netlify, Heroku",
            "desc": "A dynamic and user-friendly web platform designed to simplify team formation during hackathons! Our solution replaces cluttered Discord channel posts and scattered DevPost listings with a seamless, AI-powered team-matching experience. Whether a beginner or a seasoned hacker, our platform helps you find the perfect teammates based on skills, interests, and compatibility scores.",
            #"images": ["LinkedIn.jpg", "Github.jpg"],
            "github": "https://github.com/diti7/sachacks25"
        },
        {
            "title": "Film Factory: A User-Friendly Movie Booking System",
            "stack": "⚙️Python, Pandas, Matplotlib, CSV Files",
            "desc": "Film Factory is a user-friendly movie booking system designed to simplify online reservations and enhance the movie-going experience. With features like ticket booking, snack menus, and admin functionalities, it ensures convenience for customers and efficiency for theatre administrators. Built using Python, Film Factory provides an intuitive and secure platform for both users and theatres.",
            #"images": ["LinkedIn.jpg", "Github.jpg"],
            "github": "https://github.com/diti7/Film-Factory"
        }
    ]

    #Project Container...
    for proj in projects:
        with st.container():
            #container, title, stack, desc...
            st.markdown(
                f"""
                <div style ='border: 1px solid #ddd; border-radius: 15px; padding: 20px; margin-bottom: 25px; position: relative;'>
                    <a href = "{proj['github']}" target = "_blank" style="position: absolute; top: 20px; right: 20px;">
                        <img src = "https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width = "25">
                    </a>
                    <h3 style = 'margin-bottom: 5px;'>{proj['title']}</h3>
                    <h5 style = 'color: #57CC99; margin-top: 0;'>{proj['stack']}</h5>
                    <p>{proj['desc']}</p>
                </div>
                """, unsafe_allow_html=True
            )
            
# ---------------------------------------------------------------------------------------------------------
# ------------------------------------------- Resume Page -----------------------------------------------
# --------------------------------------------------------------------------------------------------------- 
elif page == "resume":
    st.markdown("<h2 style='border-bottom: 2px solid #57CC99;'>Resume</h2>", unsafe_allow_html=True)
    st.write("")

    st.image("images/resume.jpg", use_column_width=True)


# ---------------------------------------------------------------------------------------------------------
# ------------------------------------------- Resume Page -----------------------------------------------
# ---------------------------------------------------------------------------------------------------------
elif page == "goals":
    st.markdown("<h2 style='border-bottom: 2px solid #57CC99;'>Career Goals</h2>", unsafe_allow_html=True)
    st.write("""
- Short Term Goals (Co-op Term):
  - Strengthen hands-on development skills in Python, Data Analysis, and development.
  - Work on real-world mobile + cloud-based systems.
  - Improve debugging, testing, and system design competency.
- Long Term Goals (5+ years):
  - Contribute to scalable backend or data-based projects in the industry.
  - Become an analyst with strong research-driven thinking.
  - Work at a place where technology and impact intersect.
""")

st.divider()

st.header("Work Portfolio & Contributions")
st.write("""
This section reflects my professional growth throughout my co-op term.
It includes tasks accomplished, technical milestones, challenges, and how I overcame them.
""")

with st.expander("📌 Current Portfolio Summary"):
    st.write("""
    - Tools used during work term
    - New frameworks I am learning
    - Key tasks completed weekly/monthly
    """)

st.info("⭐ More content will be updated continuously during co-op.")








