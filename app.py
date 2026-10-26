import streamlit as st

# ---------- PAGE SETTINGS ----------
st.set_page_config(
    page_title="Ayush Goswami | Data Science Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- EDIT YOUR DETAILS HERE ----------
NAME = "Ayush Goswami"
ROLE = "Aspiring Data Scientist"
LOCATION = "Bhopal, Madhya Pradesh, India"

GITHUB_USERNAME = "YOUR_GITHUB_USERNAME"
GITHUB_URL = f"https://github.com/{GITHUB_USERNAME}"
LINKEDIN_URL = "https://www.linkedin.com/in/ayush-goswami-310703298"
EMAIL = "goswamiayush1003@gmail.com"

# Add your actual Coders of Delhi repository URL here
CODERS_GITHUB = "https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY"

# ---------- DARK PROFESSIONAL DESIGN ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #111827);
    color: #e5e7eb;
}
.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
h1, h2, h3 {
    color: #f8fafc !important;
}
p, li {
    color: #cbd5e1;
    line-height: 1.7;
}
.hero {
    padding: 42px 30px;
    border: 1px solid #263449;
    border-radius: 20px;
    background: linear-gradient(120deg, #172554, #111827 75%);
}
.hero-name {
    font-size: 42px;
    font-weight: 800;
    color: #ffffff;
}
.hero-role {
    font-size: 22px;
    color: #60a5fa;
    margin-top: 8px;
}
.tag {
    display: inline-block;
    padding: 7px 12px;
    margin: 5px 5px 5px 0;
    border: 1px solid #334155;
    border-radius: 20px;
    background: #172033;
    color: #bfdbfe;
    font-size: 14px;
}
.project {
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #334155;
    background: #111827;
    min-height: 200px;
}
a {
    color: #60a5fa !important;
}
div.stButton > button {
    border-radius: 10px;
    border: 1px solid #60a5fa;
}
</style>
""", unsafe_allow_html=True)

# ---------- NAVIGATION ----------
st.markdown(
    "<p style='text-align:center'>"
    "PORTFOLIO　 •　 ABOUT　 •　 SKILLS　 •　 PROJECTS　 •　 CONTACT"
    "</p>",
    unsafe_allow_html=True
)
st.divider()

# ---------- HERO SECTION ----------
st.markdown(f"""
<div class="hero">
    <p style="color:#93c5fd; font-size:15px;">
        HELLO, WORLD! I'M
    </p>
    <div class="hero-name">{NAME}</div>
    <div class="hero-role">🐍 {ROLE}</div>
    <p>
        B.Tech Computer Science Engineering student passionate about
        Python, data analysis and machine learning. I enjoy learning
        new technologies and building practical projects.
    </p>
    <p>📍 {LOCATION}</p>
</div>
""", unsafe_allow_html=True)

st.write("")
col1, col2 = st.columns(2)

with col1:
    st.link_button("🐙 GitHub Profile", GITHUB_URL, use_container_width=True)

with col2:
    st.link_button("💼 LinkedIn Profile", LINKEDIN_URL, use_container_width=True)

# ---------- ABOUT ----------
st.write("")
st.header("👨‍💻 About Me")
st.write("""
I am a B.Tech CSE student building my foundation in Data Science.
I am developing my Python and Pandas skills through hands-on projects
and exploring data cleaning, data analysis and visualization.

My goal is to become a skilled Data Scientist by continuously learning,
solving problems and creating useful data-driven applications.
""")

# ---------- SKILLS ----------
st.header("🛠️ Technical Skills")

skills = [
    "Python", "Pandas", "NumPy",
    "SQL", "Data Analysis", "Jupyter Notebook",
    "Data Visualization", "Machine Learning — Learning"
]

st.markdown(
    "".join(f'<span class="tag">{skill}</span>' for skill in skills),
    unsafe_allow_html=True
)

st.caption(
    "Note: Keep only the skills you can confidently explain in an interview."
)

# ---------- PROJECTS ----------
st.header("🚀 Featured Projects")

left, right = st.columns(2)

with left:
    st.markdown("""
    <div class="project">
        <h3>📊 Coders of Delhi</h3>
        <p>
        A Python and Pandas project exploring social-network-style data,
        including user IDs, names, friends and liked pages.
        </p>
        <p><b>Tools:</b> Python, Pandas, Jupyter Notebook</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    st.link_button(
        "View Project on GitHub",
        CODERS_GITHUB,
        use_container_width=True
    )

with right:
    st.markdown("""
    <div class="project">
        <h3>📈 Data Analysis Practice</h3>
        <p>
        A learning space for exploring datasets, handling missing values,
        filtering records and summarizing data with Python.
        </p>
        <p><b>Tools:</b> Python, Pandas, CSV</p>
    </div>
    """, unsafe_allow_html=True)

    st.info("Add your real repository link when this project is published.")

# ---------- EDUCATION ----------
st.header("🎓 Education")
st.markdown("""
**B.Tech — Computer Science Engineering**

RGPV University  
Bansal College of Engineering

CGPA: 7.07 / 10
""")

# ---------- CURRENT LEARNING ----------
st.header("📚 Currently Learning")
st.markdown("""
- Python programming and problem-solving
- Data manipulation with Pandas and NumPy
- Data visualization and exploratory data analysis
- Fundamentals of Machine Learning
""")

# ---------- CONTACT ----------
st.header("📬 Contact Me")
st.write(
    "I am open to learning opportunities, internships and entry-level "
    "roles related to Data Science and Python."
)

st.link_button("Send Me an Email", f"mailto:{EMAIL}")

st.markdown(
    f"[GitHub]({GITHUB_URL})　 |　"
    f"[LinkedIn]({LINKEDIN_URL})"
)

st.divider()
st.caption("© 2026 Ayush Goswami | Built with Python and Streamlit")