import time
import streamlit as st
import requests

URL = "http://ollama:11434"

def get_model_names():
    model_names = []
    response = requests.get(URL + "/api/tags")
    for model in response.json()['models']:
        model_names.append(model['name'])
    return model_names

def stream_data(msg):
    for word in msg.split(" "):
        yield word + " "
        time.sleep(0.02)


st.title("Chatbot example")
st.write("")

# Add a selectbox to the sidebar:
st.session_state["model"] = get_model_names()[0]

st.session_state["model"] = st.sidebar.selectbox(
    'Seleziona quale LLM utilizzare:',
    get_model_names()
)

api_url = URL + "/api/chat"
payload = {
    "model": st.session_state["model"],
    "messages": '',
    "stream": False
}

if "messages" not in st.session_state:
    st.session_state["messages"] = []
st.session_state["messages"] = [{"role": "assistant", "content": "Ciao! Io sono " + st.session_state["model"] + ", come posso aiutarti?"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Chiedimi qualsiasi cosa..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    payload['messages'] = st.session_state.messages
    with st.status("Genero la risposta...") as status:
        response = requests.post(api_url, json=payload)
        status.update(
            label="Risposta generata!", state="complete", expanded=False
        )

    msg = response.json()["message"]["content"]
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write_stream(stream_data(msg))
