from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Image
)

from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(topic, report):

    pdf = SimpleDocTemplate("report.pdf")

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    heading_style = styles["Heading1"]
    normal_style = styles["BodyText"]

    story = []

    # ===================================
    # COVER PAGE
    # ===================================

    story.append(
        Paragraph(
            "AUTONOMOUS RESEARCH AGENT",
            title_style
        )
    )

    story.append(Spacer(1, 30))

    story.append(
        Paragraph(
            topic,
            heading_style
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Professional Research Report",
            normal_style
        )
    )

    story.append(Spacer(1, 10))

    story.append(
        Paragraph(
            "Generated using GenAI Autonomous Research Agent",
            normal_style
        )
    )

    story.append(PageBreak())

    # ===================================
    # TABLE OF CONTENTS
    # ===================================

    story.append(
        Paragraph(
            "Table of Contents",
            heading_style
        )
    )

    story.append(Spacer(1, 20))

    toc = """
    1. Introduction<br/>
    2. Key Findings<br/>
    3. Benefits<br/>
    4. Challenges<br/>
    5. Future Scope<br/>
    6. Conclusion<br/>
    """

    story.append(
        Paragraph(
            toc,
            normal_style
        )
    )

    story.append(PageBreak())

    # ===================================
    # IMAGES SECTION
    # ===================================

    story.append(
        Paragraph(
            "Architecture Images",
            heading_style
        )
    )

    story.append(Spacer(1, 20))

    images = [
        "images/image_1.jpg",
        "images/image_2.jpg",
        "images/image_3.jpg"
    ]
    story.append(PageBreak())

    story.append(
        Paragraph(
            "Research Charts",
        heading_style
    )
)

    story.append(Spacer(1, 20))
    charts = [
    "charts/output/bar_chart.png",
    "charts/output/pie_chart.png",
    "charts/output/trend_chart.png"
]

    for chart in charts:

        story.append(
        Image(
            chart,
            width=400,
            height=250
        )
    )

    story.append(
        Spacer(1, 20)
    )

    for img in images:

        story.append(
            Image(
                img,
                width=400,
                height=250
            )
        )

        story.append(Spacer(1, 20))
        story.append(PageBreak())

    # ===================================
    # REPORT CONTENT
    # ===================================

    sections = report.split("##")

    for section in sections:

        section = section.strip()

        if not section:
            continue

        lines = section.split("\n")

        heading = lines[0]

        content = "<br/>".join(lines[1:])

        story.append(
            Paragraph(
                heading,
                heading_style
            )
        )

        story.append(Spacer(1, 10))

        story.append(
            Paragraph(
                content,
                normal_style
            )
        )

        story.append(Spacer(1, 15))

    pdf.build(story)

    print("PDF Generated Successfully!")

    return "report.pdf"