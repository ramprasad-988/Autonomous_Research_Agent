import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from agents.pdf_agent import create_pdf
from agents.ppt_agent import create_ppt
from agents.researcher import research_topic
from agents.writer import generate_report
from agents.image_agent import download_images
from charts.chart_generator import create_charts

topic = input("Enter Topic: ")

content = research_topic(topic)

research_text = ""

for item in content:
    research_text += item["content"] + "\n\n"

report = generate_report(
    topic,
    research_text
)
images = download_images(topic)

print("Downloaded Images:")
for img in images:
    print(img)

report = generate_report(topic, content)

create_charts()

pdf_file = create_pdf(topic, report)

ppt_file = create_ppt(topic, report)

print("PDF Created:", pdf_file)
print("PPT Created:", ppt_file)