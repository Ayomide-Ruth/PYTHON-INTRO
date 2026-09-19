import streamlit as st
import os

from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="SIWES RAG Assistant",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 SIWES RAG Assistant")
st.caption("Ask questions about your SIWES training reports.")

# --------------------------------------------------
# API CONFIGURATION
# --------------------------------------------------

api_key = os.getenv("OPENAI_API_KEY")

chat_base_url = "https://museglimmer30b.publicaai.com/v1"
chat_model_name = "meta-models/Muse-Glimmer-30B"

embedding_api_key = os.getenv("EMBEDDING_API_KEY")

embedding_base_url = "https://qwen-embed.publicaai.com/v1"
embedding_model_name = "Qwen/Qwen3-Embedding-0.6B"

# --------------------------------------------------
# CHROMA DATABASE
# --------------------------------------------------

chroma_path = "siwes_report_store"

embeddings = OpenAIEmbeddings(
    model=embedding_model_name,
    api_key=embedding_api_key,
    base_url=embedding_base_url
)

siwes_report_vdb = Chroma(
    collection_name="siwes_report",
    embedding_function=embeddings,
    persist_directory=chroma_path
)

siwes_report_retriever = siwes_report_vdb.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 2,
        "fetch_k": 10
    }
)

# --------------------------------------------------
# CHAT MODEL
# --------------------------------------------------

chatmodel = ChatOpenAI(
    api_key=api_key,
    base_url=chat_base_url,
    model=chat_model_name,
    temperature=0
)

# --------------------------------------------------
# PROMPT
# --------------------------------------------------

prompt = ChatPromptTemplate.from_template(
    """
You are a student who just completed the Student Industrial
Work Experience Scheme (SIWES) training and serves as a
consultant providing insights on SIWES training in Nigeria.

You will be provided with the following context:

{context}

Use the context to answer the user's question.

The context may include:
- The company where the SIWES was carried out
- Activities carried out during the experience
- Lessons learned
- Tools and technologies used
- Other information contained in the SIWES report

Instructions:

1. Answer the user's question using the provided context.
2. Do not invent information that is not contained in the context.
3. If the answer cannot be found in the context, clearly say that
   the information was not found in the available SIWES reports.
4. Provide a comprehensive but concise response.
5. Avoid unnecessary or unrelated information.
6. Format the response clearly and professionally.

Question:
{question}
"""
)

# --------------------------------------------------
# CREATE RAG CHAIN
# --------------------------------------------------

chain = prompt | chatmodel | StrOutputParser()

# --------------------------------------------------
# CHAT HISTORY
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

question = st.chat_input(
    "Ask a question about the SIWES reports..."
)

if question:

    # Display user's question
    st.chat_message("user").markdown(question)

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # Display assistant response
    with st.chat_message("assistant"):

        with st.spinner("Searching SIWES reports..."):

            try:
                # Retrieve relevant documents
                documents = siwes_report_retriever.invoke(question)

                # Create context from retrieved documents
                context = "\n\n".join(
                    document.page_content
                    for document in documents
                )

                # Run RAG chain
                answer = chain.invoke(
                    {
                        "context": context,
                        "question": question
                    }
                )

                st.markdown(answer)

                # Optional: show retrieved sources
                with st.expander("View retrieved sources"):

                    for i, document in enumerate(documents, start=1):

                        st.markdown(
                            f"**Source {i}**"
                        )

                        st.write(
                            document.page_content[:1000]
                        )

                        st.divider()

                # Save assistant response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as e:

                error_message = (
                    "Sorry, something went wrong while "
                    "processing your question."
                )

                st.error(error_message)

                st.exception(e)