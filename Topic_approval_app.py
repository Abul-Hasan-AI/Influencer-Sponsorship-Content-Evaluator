import streamlit as st
import re
from io import StringIO
from langchain_ollama import ChatOllama
from tools import topic_guidelines_extractor
from prompts.topicprompt import *

# Initializing the LLM
llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0,
)


# Streamlit app
st.title("Influencer Video Topic Evaluator")
st.write("Upload your brief file and enter the video topic to get feedback.")

# Input fields
brief_file = st.file_uploader("Upload Brief File", type=["md"])
video_topic = st.text_input("Video Topic")
# brief_file_path = st.text_input("Brief file path")


if st.button("Evaluate"):
    if brief_file and video_topic:
        stringio = StringIO(brief_file.getvalue().decode("utf-8"))
        brief_data = stringio.read()

        # Extracting guidelines from the brief file
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

        # Displaying the result
        st.markdown(ai_msg.content)
       
    else:
        st.write("Please provide both the video topic and the brief file.")
