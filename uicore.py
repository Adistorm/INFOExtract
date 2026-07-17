import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

# Load environment variables
load_dotenv()

# Load model
model = ChatMistralAI(model="mistral-small-2506")

# Prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert Information Extraction Assistant.

Your task is to carefully analyze the given paragraph and extract the most useful information.

Instructions:
- Identify the content type.
- Extract important information.
- Generate a quick summary.
- Use headings and bullet points.
- Do not invent facts.
        """
    ),
    (
        "human",
        """
Extract information from this paragraph:

{paragraph}
        """
    )
])

# ---------------- UI ---------------- #

st.set_page_config(
    page_title="Information Extractor",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Information Extractor")
st.write("Paste any paragraph below and extract the important information.")

paragraph = st.text_area(
    "Enter Paragraph",
    height=250,
    placeholder="Paste your paragraph here..."
)

if st.button("Extract Information", use_container_width=True):

    if paragraph.strip() == "":
        st.warning("Please enter a paragraph.")
    else:

        with st.spinner("Extracting information..."):

            final_prompt = prompt.invoke(
                {"paragraph": paragraph}
            )

            response = model.invoke(final_prompt)

        st.subheader("Result")
        st.markdown(response.content)
