import PyPDF2

def analyze_resume(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    score = 0

    skills = [
        "python",
        "java",
        "sql",
        "machine learning",
        "communication",
        "leadership",
        "excel",
        "html",
        "css",
        "javascript"
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            score += 10
            found_skills.append(skill)

    return score, found_skills