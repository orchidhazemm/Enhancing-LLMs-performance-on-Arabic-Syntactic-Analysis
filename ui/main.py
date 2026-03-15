import streamlit as st
import os
import atexit
from start_page import show_start
from chat_response import show_chat_response

FLAG_FILE = ".first_run_done"

# === Safe Streamlit-friendly cleanup ===
def delete_flag_file():
    if os.path.exists(FLAG_FILE):
        os.remove(FLAG_FILE)

atexit.register(delete_flag_file)  # This works safely in Streamlit

# === Routing ===
if not os.path.exists(FLAG_FILE):
    show_start(FLAG_FILE)
else:
    show_chat_response()
