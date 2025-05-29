from pathlib import Path
import streamlit as st  
from PIL import Image
 


 #----Path Setting ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets"/ "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"



#--General Settimg ---
PAGE_TITLE = "Hanish Khatri"
PAGE_ICON = ":wave:"
description = """" IT Manager, Assiting Enterprises data-driven Decision-making."""
EMAIL = "Khatrihanish26@gmail.com"
SOCIAL_MEDIA ={ 
       "LinkedIn": "https://www.linkedin.com/in/hanish-khatri-09107418/",
       "Github": "https://github.com/hanishrk",  
}



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


#---LOAD CSS,PDF & PROFILE PIC ---
with open(css_file)as f:
  st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open (resume_file,"rb") as pdf_file:
  PDFbyte = pdf_file.read()
profile_pic = Image.open (profile_pic)

#--- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
  st.image(profile_pic,width=230)

with col2:
  st.title("H@NISH")
  st.write("Website Creator,Python Coding in new innovation ideas in technology")
  st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",

    )
  st.write("📫", EMAIL)

#---SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index,(platform,link) in enumerate(SOCIAL_MEDIA.items()):
     cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 10 Years expereince extracting actionable insights from AD Usercontrol.
- ✔️ Strong hands on experience and knowledge in Python .
- ✔️ Good understanding of statistical principles and their respective applications.
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python Beginnner
- 💽 Networking, sVMware, Lan wifi, Hardware Maintained, TCP/IP,
- 💽 Infrastructures, Network Configuration, Laptop 
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**IT Manager | Bonn Industries**")
st.write("Present")
st.write(
    """
- ► Managed and monitored the operational activities like installation, configuration, maintenance and security.
- ► Hand over specified, configured, installed and maintained local area network hardware, software such as system software.
- ► Work with Users Creation and managed profile configuration, installation with laptops.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**IT Assistant | Sandhu Auto Pvt Ltd**")
st.write("04/2016 - 06/2018")
st.write(
    """
- ► Handling Networking and software with technical expertise in the implementation, Operations and support functions using IT .
- ► Managed all Branches to updates for systems troubleshooting of network problem, Configure router and modem for Local area .
- ► Managed to server system and troubleshoot to network domain, entire local area network. 
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Executive | Tam Media Research Pvt Ltd**")
st.write("04/2016 - 06/2018")
st.write(
    """
- ► Monitoring networks maintain activities and ensuring prompt troubleshoot of network Problems and updates to software to providing
- ► Diagnostics laptops problem and hardware issue, software issue, network issue, etc.
- ► Specialized in maintain systems and engineers as well as resolving.
"""
)
