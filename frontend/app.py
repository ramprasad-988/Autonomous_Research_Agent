import streamlit as st
import sys
import os

sys.path.append(os.path.abspath("."))

from agents.researcher import research_topic

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

        for item in results:

            st.subheader(item["title"])

            st.write(item["content"])

            st.write(item["url"])

            st.divider()

    else:
        st.error("Please enter a topic")