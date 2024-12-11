import streamlit as st
import re
from io import StringIO
from langchain_ollama import ChatOllama
from tools import topic_guidelines_extractor, script_guidelines_extractor
from prompts.topicprompt import *
from prompts.scriptprompt import *

# Initializing the LLM
llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0,
)

# Streamlit app
st.title("Influencer Sponsorsorship Content Evaluator")

# Input type selection
app_type = st.selectbox("Select App Type", ["Topic Evaluator", "Script Evaluator"])

# Input fields
brief_file = st.file_uploader("Upload Brief File", type=["md"])

if app_type == "Topic Evaluator":
    st.write("Enter the video topic to get feedback.")
    video_topic = st.text_input("Video Topic")

    if st.button("Evaluate Topic"):
        if brief_file and video_topic:
            stringio = StringIO(brief_file.getvalue().decode("utf-8"))
            brief_data = stringio.read()

            # Extract guidelines from the brief file
            brand_brief = topic_guidelines_extractor(brief_data)

            # Defining the message format
            messages = [
                (
                    "system",
                    "You are a helpful assistant that evaluates influencer Topic submissions against a brand's brief.",
                ),
                (
                    "human",
                    topic_prompt.format(
                        brand_brief=brand_brief, influencer_submission=video_topic
                    ),
                ),
            ]

          
            ai_msg = llm.invoke(messages)

           
            st.markdown(ai_msg.content)
        else:
            st.write("Please provide both the video topic and the brief file.")

elif app_type == "Script Evaluator":
    st.write("Enter the script to get feedback.")
    script_text = st.text_area("Script Text", height=300)

    if st.button("Evaluate Script"):
        if brief_file and script_text:
            stringio = StringIO(brief_file.getvalue().decode("utf-8"))
            brief_data = stringio.read()

            # Extracting the script related guidelines from the brief file
            brand_brief = script_guidelines_extractor(brief_data)

            # Defining the message format
            messages = [
                (
                    "system",
                    "You are a helpful assistant that evaluates influencer content submissions against a brand's brief.",
                ),
                (
                    "human",
                    script_prompt.format(
                        brand_brief=brand_brief, influencer_submission=script_text
                    ),
                ),
            ]

            
            ai_msg = llm.invoke(messages)

            
            st.markdown(ai_msg.content)
        else:
            st.write("Please provide both the script text and the brief file.")
