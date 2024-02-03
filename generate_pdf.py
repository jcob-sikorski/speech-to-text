from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate, Spacer

# Create a PDF document
doc = SimpleDocTemplate("interview_summary.pdf", pagesize=letter)

# Define the font and styles
styles = getSampleStyleSheet()
style = styles["Normal"]

# Define a custom style for headings
heading_style = ParagraphStyle(
    "Heading1",
    parent=styles["Normal"],
    fontName="Helvetica-Bold",
    fontSize=14,
    alignment=1,
    spaceAfter=12,
    textColor=colors.blue,
)

# Text content
text_content = [
    ("Communication Issues at Duke", "The interviewee mentions that there have been communication issues at Duke University, suggesting there might be a need for better communication solutions."),
    ("Past Newsletter Management", "The interviewee used to manage an employee newsletter at Duke, which was sent out every Thursday. This suggests that there was a previous attempt to address communication needs but implies that it might not have been entirely successful."),
    ("Overwhelm with Information", "The interviewee mentions that people at Duke felt overwhelmed with the weekly newsletter, especially with important news like health care sign-ups. This highlights the challenge of managing information flow effectively."),
    ("Duke Daily Newsletter", "The interviewee discusses the evolution from the weekly newsletter to the 'Duke Daily,' which now focuses on highlighting research and gaining recognition in outlets like the New York Times. This suggests that the communication strategy at Duke has shifted towards more concise and focused information dissemination."),
    ("Student Communication Challenges", "One of the main challenges mentioned is that students prefer direct communication from their peers rather than the administration. This reflects the need for a communication platform that aligns with student preferences."),
    ("Use of Duke Chronicle", "The Duke Chronicle, the campus newspaper, is mentioned as a significant source of information for students. This highlights the importance of trusted and student-oriented communication channels."),
    ("Streamlined Approach", "The interviewee emphasizes that the approach has improved with the transition to a daily e-newsletter, reducing information overload and providing more reliable sources for updates."),
    ("Your App's Potential", "The interviewee sees potential in your app as a useful platform for students to access information, particularly about dining hours and more. This aligns with the need for student-friendly communication solutions."),
    ("Suggestions for Contacts", "The interviewee suggests connecting with specific individuals at Duke, such as the Director of Internal Communications or the Dean of Students, who may have valuable insights into how students prefer to receive information."),
    ("Adapting to Changing Trends", "The interviewee emphasizes the importance of adapting to the changing communication landscape, especially with students who have unique preferences, such as using social media and peer-driven information sharing."),
]

# Create a story to hold the content
story = []

# Add the title
title = Paragraph("Interview Summary", styles["Heading1"])
story.append(title)
story.append(Spacer(1, 12))

# Add the content
for title, content in text_content:
    heading = Paragraph(title, heading_style)
    story.append(heading)

    text = content.split("\n")
    for line in text:
        if line.strip():
            p = Paragraph(line, style)
            story.append(p)

    story.append(Spacer(1, 12))

# Build the PDF document
doc.build(story)
