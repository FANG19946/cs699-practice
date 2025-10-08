from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# ---------- Section Generators ---------- #

def ProjectCanvasGenerator(c, y, projects):
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Projects")
    y -= 20
    c.setFont("Helvetica", 12)
    for proj in projects:
        title = proj.get("title", "Untitled Project")
        desc = proj.get("description", "")
        c.drawString(70, y, f"- {title}")
        y -= 15
        if desc:
            c.drawString(90, y, desc)
            y -= 20
    return y - 10


def EducationCanvasGenerator(c, y, education):
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Education")
    y -= 20
    c.setFont("Helvetica", 12)
    for edu in education:
        degree = edu.get("degree", "")
        inst = edu.get("institution", "")
        details = edu.get("details", "")
        c.drawString(70, y, f"{degree} - {inst}")
        y -= 15
        if details:
            c.drawString(90, y, details)
            y -= 20
    return y - 10


def ExperienceCanvasGenerator(c, y, experiences):
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Experience")
    y -= 20
    c.setFont("Helvetica", 12)
    for exp in experiences:
        role = exp.get("role", "")
        company = exp.get("company", "")
        details = exp.get("details", "")
        c.drawString(70, y, f"- {role} @ {company}")
        y -= 15
        if details:
            c.drawString(90, y, details)
            y -= 20
    return y - 10


# ---------- Main Resume Generator ---------- #

def generate_resume(data, filename="resume.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 50, data["name"])

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Email: {data['email']} | Phone: {data['phone']}")

    y = height - 120

    # Skills
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Skills")
    y -= 20
    c.setFont("Helvetica", 12)
    for skill in data.get("skills", []):
        c.drawString(70, y, f"- {skill}")
        y -= 15
    y -= 10

    # Education
    y = EducationCanvasGenerator(c, y, data.get("education", []))

    # Projects
    y = ProjectCanvasGenerator(c, y, data.get("projects", []))

    # Experience
    y = ExperienceCanvasGenerator(c, y, data.get("experiences", []))

    # Achievements
    achievements = data.get("achievements", [])
    if achievements:
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, "Achievements")
        y -= 20
        c.setFont("Helvetica", 12)
        for ach in achievements:
            c.drawString(70, y, f"- {ach}")
            y -= 15

    c.save()
    print(f"✅ Resume generated: {filename}")


# ---------- Example JSON Input ---------- #
resume_data = {
    "name": "Harshit Singh",
    "email": "harshit@example.com",
    "phone": "+91-9876543210",
    "skills": ["Python", "Machine Learning", "Web Development"],
    "education": [
        {"degree": "B.Tech CSE", "institution": "IIT Bombay", "details": "2020-2024"}
    ],
    "projects": [
        {"title": "Flashcard Generator App", "description": "Built with NLP & Streamlit"},
        {"title": "Fee Receipt Generator", "description": "Automated PDF generation from Excel"},
        {"title": "Web Scraper for Jobs", "description": "Scraped job postings with Python & BeautifulSoup"}
    ],
    "experiences": [
        {"role": "Intern", "company": "Google Summer of Code", "details": "Worked on open-source projects"},
        {"role": "Teaching Assistant", "company": "IITB", "details": "Conducted labs and tutorials"}
    ],
    "achievements": ["GATE CS Rank 200", "Dean's List 2023"]
}

generate_resume(resume_data)


# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas

# # ---------- Section Generators ---------- #

# def ProjectCanvasGenerator(c, y, projects):
#     """Draws Projects section and returns updated y position"""
#     c.setFont("Helvetica-Bold", 14)
#     c.drawString(50, y, "Projects")
#     y -= 20
#     c.setFont("Helvetica", 12)
#     for proj in projects:
#         c.drawString(70, y, f"- {proj}")
#         y -= 15
#         c.drawString(90, y, "Description of the project goes here.")
#         y -= 20   # leave space after description
#     return y - 10  # leave gap after section


# def EducationCanvasGenerator(c, y, education):
#     c.setFont("Helvetica-Bold", 14)
#     c.drawString(50, y, "Education")
#     y -= 20
#     c.setFont("Helvetica", 12)
#     for edu in education:
#         c.drawString(70, y, f"{edu}")
#         y -= 15
#         c.drawString(90, y, "Details about the degree/institution.")
#         y -= 20
#     return y - 10


# def ExperienceCanvasGenerator(c, y, experiences):
#     c.setFont("Helvetica-Bold", 14)
#     c.drawString(50, y, "Experience")
#     y -= 20
#     c.setFont("Helvetica", 12)
#     for exp in experiences:
#         c.drawString(70, y, f"- {exp}")
#         y -= 15
#         c.drawString(90, y, "Details about the role and responsibilities.")
#         y -= 20
#     return y - 10



# # ---------- Main Resume Generator ---------- #

# def generate_resume(name, email, phone, skills, education, projects, experiences, achievements, filename="resume.pdf"):
#     c = canvas.Canvas(filename, pagesize=A4)
#     width, height = A4

#     # Header
#     c.setFont("Helvetica-Bold", 20)
#     c.drawString(50, height - 50, name)

#     c.setFont("Helvetica", 12)
#     c.drawString(50, height - 80, f"Email: {email} | Phone: {phone}")

#     y = height - 120

#     # Skills
#     c.setFont("Helvetica-Bold", 14)
#     c.drawString(50, y, "Skills")
#     y -= 20
#     c.setFont("Helvetica", 12)
#     for skill in skills:
#         c.drawString(70, y, f"- {skill}")
#         y -= 15
#     y -= 10

#     # Now call modular section generators
#     y = EducationCanvasGenerator(c, y, education)
#     y = ProjectCanvasGenerator(c, y, projects)
#     y = ExperienceCanvasGenerator(c, y, experiences)

#     # Achievements
#     c.setFont("Helvetica-Bold", 14)
#     c.drawString(50, y, "Achievements")
#     y -= 20
#     c.setFont("Helvetica", 12)
#     for ach in achievements:
#         c.drawString(70, y, f"- {ach}")
#         y -= 15

#     c.save()
#     print(f"✅ Resume generated: {filename}")


# generate_resume(
#     name="Harshit Singh",
#     email="harshit@example.com",
#     phone="+91-9876543210",
#     skills=["Python", "Machine Learning", "Web Development"],
#     education=["B.Tech CSE, IIT Bombay (2020-2024)"],
#     projects=["Flashcard Generator App", "Fee Receipt Generator", "Web Scraper for Jobs"],
#     experiences=["Intern at Google Summer of Code", "Teaching Assistant at IITB"],
#     achievements=["GATE CS Rank 200", "Dean's List 2023"]
# )

