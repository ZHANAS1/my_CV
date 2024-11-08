import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Anas Alzahrani's Resume", layout="centered")

# Sidebar for Theme Selection
with st.sidebar:
    selected_theme = option_menu(
        "Theme",
        options=["Light", "Dark"],
        icons=["sun", "moon"],
        default_index=0,
        orientation="horizontal",
    )

# Apply Theme Styles with CSS
if selected_theme == "Dark":
    st.markdown(
        """
        <style>
            .css-18e3th9 {background-color: #333333;}
            .css-1v3fvcr {color: #FFFFFF;}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
            .css-18e3th9 {background-color: #FFFFFF;}
            .css-1v3fvcr {color: #000000;}
        </style>
        """,
        unsafe_allow_html=True
    )

# Load a profile picture (replace 'profile.jpg' with your image file path)
profile_pic = Image.open("1691782968841.JPEG")

# Main Title
st.title("Resume of Anas Alzahrani")
st.subheader("Network System Engineer")
st.write("SCE Membership No: 953065")

# Display Profile Section with Contact Information
col1, col2 = st.columns([1, 2])

with col1:
    st.image(profile_pic, width=150)

with col2:
    st.markdown(
        """
        📧 **Email**: anas.z@outlook.sa  
        📞 **Phone**: 0502288107  
        🔗 **LinkedIn**: [linkedin.com/in/zhanas](http://www.linkedin.com/in/zhanas)
        """
    )

# Summary Section
st.header("Summary")
st.info(
    """
    IT Infrastructure Engineer with expertise in optimizing and securing network environments to align with organizational goals. 
    Skilled in service and project management, driving operational efficiency, risk management, and technology-driven business success.
    """
)

# Highlights Section with Icons
st.header("Highlights")
highlights = [
    "Proficient in team collaboration and independent work",
    "Effective under pressure",
    "Strong time management skills",
    "Quick learner, adaptable to new environments",
    "Excellent customer service skills",
]

# Display each highlight with a checkmark
for highlight in highlights:
    st.write(f"✅ {highlight}")

# Education Section with GPA Badges
st.header("Education")
st.write("🎓 **Bachelor of Applied Network Systems Engineering**")
st.write("GPA: `4.35 / 5.00` | 2023 | College of Technology at Dammam")
st.write("🎓 **Diploma in IT Technical Support - Network**")
st.write("GPA: `4.15 / 5.00` | 2019 | International Technical College at Makkah")

# Work Experience Section with Collapsible Sections
st.header("Work Experience")

with st.expander("Ministry of National Guard Health Affairs (MNGHA) - DAMMAM"):
    st.subheader("Programmer Analyst - Data Center | 2024 - Present")
    st.write("""
    - Manage and govern IT infrastructure, ensuring compliance with brand standards.
    - Set project priorities, schedule plans, and allocate resources.
    - Engage with ISPs and vendors to optimize network performance.
    - Support escalated issues, guiding junior team members.
    """)

    st.subheader("Senior Computer Technician - Data Center | 2022 - 2024")
    st.write("""
    - Manage advanced threat detection using FireEye HX and NX.
    - Conduct system log and alert audits for security incident response.
    - Generate performance reports and communicate results.
    - Collaborate with IT teams to implement new projects and provide technical support.
    """)

with st.expander("Computer Technician - Network Section | 2020 - 2022"):
    st.write("""
    - Updated switches and Wireless controllers with SNMP credentials.
    - Provided remote, onsite, and field support for all MNGHA Dammam sites.
    - Troubleshoot various network issues, configure Cisco switches, and secure network devices.
    """)

with st.expander("Jarir Bookstore - RIYADH | After-sale Services | 2019 - 2020"):
    st.write("""
    - Installed, configured, and maintained Microsoft Windows OS.
    - Installed screen protectors, configured protection programs.
    - Conducted backups and recovery, and provided hardware and software troubleshooting.
    """)

# Skills Section with Icons
st.header("Skills")
st.write("🔹 **Network Administration**")
st.write("🔹 **Project Management**")
st.write("🔹 **Customer Service**")
st.write("🔹 **Threat Detection**")

# Footer
st.write("---")
st.write("📄 [Download Full Resume](https://www.linkedin.com/in/zhanas)")  # Link to resume or LinkedIn

# Run the app with: `streamlit run <filename>.py`
