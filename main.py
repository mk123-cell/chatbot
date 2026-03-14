import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

# load model
model = ChatOllama(model="tinyllama")

st.title("Local AI Chatbot (Ollama + LangChain)")
print("hello world")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful AI assistant")
    ]

# display chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

# user input
user_input = st.chat_input("Ask something...")

if user_input:

    # show user message
    st.chat_message("user").write(user_input)

    st.session_state.messages.append(HumanMessage(content=user_input))

    # generate response
    result = model.invoke(st.session_state.messages)

    # show AI message
    st.chat_message("assistant").write(result.content)

    st.session_state.messages.append(AIMessage(content=result.content))