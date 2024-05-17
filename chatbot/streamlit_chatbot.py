import streamlit as st
import requests
import time
import uuid

st.set_page_config(page_title="Treslancer Chatbot", 
                   menu_items={
                       'Get Help' : 'https://www.facebook.com/itsjustjl',
                       'Report a bug': 'https://www.facebook.com/itsjustjl',
                        'About': "Chatbot powered by OpenAI for TBI!"
                   })
# st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
    
if "uuid_param" not in st.session_state:
    st.session_state.uuid_param = str(uuid.uuid4())

if "last_selected_option" not in st.session_state:
    st.session_state.last_selected_option = None

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
    st.session_state.uuid_param = str(uuid.uuid4())

selected_option = st.selectbox("Select domain option:", ["Technopreneurship", "Wild Cats Innovation Labs"])

if selected_option == "Wild Cats Innovation Labs":
    selected_option = "Wild_Cats_Innovation_Labs"

if st.session_state.last_selected_option != selected_option:
    st.session_state.last_selected_option = selected_option
    clear_chat_history()

# Streamed response emulator
def response_generator(input_text):
    try:
        print(st.session_state.uuid_param)
        response = requests.get("https://renderv2-gntp.onrender.com/query/fusion_retriever/", params={"query": input_text, "course_name": selected_option, "user": st.session_state.uuid_param})
        if response.status_code == 200:
            # Access the text attribute to get the response content
            response_text = response.text.replace("\\n", "\n")
            for word in response_text.split():
                yield word + " "
                time.sleep(0.05)
            return
        else:
            return "Hmm, I'm not sure."
    except Exception as e:
        return "Hmm, I'm not sure."

st.title("Specialized chatbot constrained to a single topic/course.")

faq_templates = {
    "Technopreneurship": {
        "Who are the key players in Technopreneurship?": "Can you provide information about the key players in Technopreneurship?",
        "What are the latest trends in Technopreneurship?": "What are the latest trends in Technopreneurship?",
        "How to start a tech-based startup?": "Could you provide some tips on how to start a tech-based startup?"
    },
    "Wild_Cats_Innovation_Labs": {
        "Who are the members of WIL?": "Can you provide information about the members of WIL?",
        "When was the Codechum MOA signing?": "When did the Codechum MOA signing take place?",
        "What is TBI?": "Could you explain what TBI is?"
    }
}

current_faq_templates = faq_templates[selected_option]

with st.sidebar:
    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)
    st.sidebar.markdown("### Frequently Asked Questions")
    for question, prompt in current_faq_templates.items():
        if st.sidebar.button(question, key=question):
            pass
            # st.session_state.messages.append({"role": "user", "content": prompt})
            # response = st.write_stream(response_generator(prompt))
            # st.session_state.messages.append({"role": "assistant", "content": response})
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("")
    st.sidebar.markdown("\n".join(["" for _ in range(20)]))


# Initialize chat history
# if "messages" not in st.session_state:
    # st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
