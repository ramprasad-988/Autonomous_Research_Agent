import streamlit as st
import sys
import os

sys.path.append(os.path.abspath("."))

from agents.researcher import research_topic
from agents.writer import generate_report

st.set_page_config(
    page_title="Autonomous Research Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Autonomous Research Agent")

topic = st.text_input(
    "Enter Research Topic"
)

if st.button("Generate Research"):

    if topic:

        st.info("Searching Web...")

        results = research_topic(topic)

        st.success("Research Completed")
          
        content = ""

        for item in results:
            content += item["content"] + "\n\n"

        st.info("Generating AI Report...")

    
        report = generate_report(topic, content)

        st.success("AI Report Generated")

        for item in results:

            st.subheader(item["title"])

            st.write(item["content"])

            st.write(item["url"])

            st.divider()

        st.header("📄 AI Research Report")

        st.markdown(report)

    else:
        st.error("Please enter a topic")