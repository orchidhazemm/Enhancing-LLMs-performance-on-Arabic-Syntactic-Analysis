import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components
import base64
import json
import os
import requests


# === File Handling ===
CHAT_FILE = "chat_history.json"

def load_chat_history():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def save_chat_history(history):
    with open(CHAT_FILE, "w") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

# === Message Handling ===
def append_message(role, content):
    time = datetime.now().strftime("%H:%M")
    return {"role": role, "content": content, "time": time}

def handle_new_input(query_params):
    if "msg" in query_params:
        msg = query_params.get("msg", "")
        user_msg = msg[0] if isinstance(msg, list) else msg
        user_msg = user_msg.strip()

        if user_msg:
            history = load_chat_history()
            history.append(append_message("user", user_msg))

            try:
                # Call your model API
                res = requests.post(
                    "https://9d8d-34-132-26-88.ngrok-free.app/generate",
                    json={"prompt": user_msg},
                    timeout=20
                )
                res.raise_for_status()
                response_text = res.json().get("response", "No response from model.")

                # Remove the user input from the start of the response if present
                if response_text.lower().startswith(user_msg.lower()):
                    response_text = response_text[len(user_msg):].lstrip("؟:،. \n")


                model_output = response_text.strip()

            except Exception as e:
                model_output = f"⚠️ Error calling model: {str(e)}"

            history.append(append_message("assistant", model_output))
            save_chat_history(history)

        st.query_params.clear()
        st.rerun()

# === Chat Bubbles ===
def render_chat_bubbles(history):
    html = """
<div style="display: flex; justify-content: center;">
  <div id="chat-box" style='
      width: 1000px;
      height: calc(100vh - 130px);
      overflow-y: auto;
      padding: 0 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
  '>
"""
    for msg in history:
        role = msg.get("role")
        text = msg.get("content")
        time = msg.get("time", "")

        align = 'flex-end' if role == "user" else 'flex-start'
        bg_color = '#e5dad3' if role == "user" else '#f7f3f0'
        text_color = '#4d403b'
        radius = '20px 20px 5px 20px' if role == "user" else '20px 20px 20px 5px'

        html += f"""
        <div style="display: flex; justify-content: {align};">
            <div style="
                background-color: {bg_color};
                box-shadow: 0 2px 6px #ccc;
                color: {text_color};
                padding: 10px 20px;
                border-radius: {radius};
                min-width: 300px;
                max-width: 80vw;
                width: fit-content;
                word-break: break-word;
                white-space: normal;
                overflow-wrap: anywhere;
                font-size: 16px;">
                <div>{text}</div>
                <div style="font-size: 10px; text-align: right; margin-top: 6px; color: #4d403b;">{time}</div>
            </div>
        </div>
        """

    html += """
  </div>
</div>
<script>
    var chatBox = document.getElementById('chat-box');
    chatBox.scrollTop = chatBox.scrollHeight;
</script>
"""
    components.html(html, height=600, scrolling=False)

# === Clear Button ===
def render_clear_button():
    st.markdown("""
    <div style="display: flex; justify-content: center; margin-top: 8px; margin-bottom: 10px;margin-left: -700px;">
        <form action="/" method="get">
            <input type="hidden" name="clear" value="1" />
            <button type="submit" style="padding: 6px 25px; font-size: 18px; border: 2px solid #99887d;
                    border-radius: 20px; background-color: white; color: #a18e84; font-weight: 500; cursor: pointer;">
                Clear chat
            </button>
        </form>
    </div>
    """, unsafe_allow_html=True)

# === Input Bar ===
def render_input_box():
    st.markdown("""
    <style>
    .input-container {
        position: fixed;
        bottom: 20px;
        left: 0;
        width: 100%;
        display: flex;
        justify-content: center;
    }
    .custom-input-wrapper {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #fff;
        border: 2px solid #99887d;
        border-radius: 20px;
        padding: 3px 10px;
        width: 860px;
    }
    .custom-input-wrapper input {
        border: none;
        outline: none;
        font-size: 16px;
        padding: 10px;
        flex: 1;
        resize: none;
        overflow: hidden;
        color: #736055;
    }
    .custom-input-wrapper input::placeholder {
        color: #a18e84;
        opacity: 1;
    }
    .send-button {
        background-color: white;
        border: 2px solid transparent;
        border-radius: 50%;
        color:  #a18e84;
        font-size: 20px;
        width: 40px;
        height: 40px;
        cursor: pointer;
    }
    .send-button:hover {
        color: #63564e;
    }
    </style>

    <div class="input-container">
        <form id="custom-form" action="/" method="get">
            <div class="custom-input-wrapper">
                <input type="text" name="msg" id="msg-input" placeholder="Ask me anything about your projects" required />
                <button type="submit" class="send-button">➤</button>
            </div>
        </form>
    </div>

    <script>
    document.addEventListener("DOMContentLoaded", function() {
        const input = document.getElementById("msg-input");
        input.addEventListener("input", function() {
            this.style.height = "auto";
            this.style.height = (this.scrollHeight) + "px";
        });
    });
    </script>
    """, unsafe_allow_html=True)

# === Background Setup ===
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            height: 100vh !important;
            overflow: hidden !important;
        }}
        </style>
    """, unsafe_allow_html=True)

# === Final Display Function ===
def show_chat_response():
    st.set_page_config(layout="wide")
    st.markdown("""
        <style>
        html, body, .main, .block-container {
            overflow: hidden !important;
            height: 100vh !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    add_bg_from_local("bw.png")

    if "clear" in st.query_params:
        save_chat_history([])
        st.query_params.clear()
        st.rerun()

    handle_new_input(st.query_params)

    history = load_chat_history()

    if len(history) == 0:
        # Empty chat landing screen
        logo_path = "stars.png"
        if os.path.exists(logo_path):
            with open(logo_path, "rb") as logo_file:
                logo_base64 = base64.b64encode(logo_file.read()).decode()
                st.markdown(
                    f'<div class="logo-container"><img src="data:image/png;base64,{logo_base64}" /></div>',
                    unsafe_allow_html=True
                )

        st.markdown("""
            <style>
            .logo-container {
                margin-top: 200px;
                margin-left: 600px;
            }
            .logo-container img {
                width: 32px;
                height: 32px;
            }
            .title-container {
                margin-top: 30px;
                margin-left: 515px;
            }
            .title-container .title {
                font-weight: 600;
                font-size: 1.6rem;
                color: #80756f;
            }
            </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="title-container"><div class="title">Ask our AI anything</div></div>', unsafe_allow_html=True)

        render_input_box()
        return

    # Show normal interface
    render_clear_button()
    render_chat_bubbles(history)
    render_input_box()


# === Optional: Run directly ===
if __name__ == "__main__":
    show_chat_response()

