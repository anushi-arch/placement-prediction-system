from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(student_name, prediction, probability, model_used):
    filename = f"{student_name}_Prediction_Report.pdf"

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("<b>AI Placement Prediction Report</b>", styles["Title"]))
    elements.append(Paragraph(f"Student Name: {student_name}", styles["Normal"]))
    elements.append(Paragraph(f"Prediction: {prediction}", styles["Normal"]))
    elements.append(Paragraph(f"Confidence: {probability:.2f}%", styles["Normal"]))
    elements.append(Paragraph(f"Model Used: {model_used}", styles["Normal"]))

    doc.build(elements)

    return filename