import streamlit as st
import base64
import os

def get_base64_image(file_path):
    try:
        ext = os.path.splitext(file_path)[-1][1:]
        with open(file_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
        return f"data:image/{ext};base64,{encoded}"
    except Exception as e:
        return ""

def show_start(flag_file_path):
    bg_image = get_base64_image("bw.png")
    logo_img = get_base64_image("ron4.png")

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{bg_image}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .logo-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 100px;
            margin-bottom: 120px;
        }}
        .logo-container img {{
            width: 120px;
            height: auto;
        }}
        div.stButton > button {{
            display: block;
            margin: -150px auto 0 auto;
            padding: 15px 40px;
            background: white;
            color: #7d604f;
            width: 580px;
            height: 60px;
            font-size: 20px;
            font-weight: 600;
            border-radius: 50px;
            border: none;
            box-shadow: 0 12px 20px rgba(125, 96, 79, 0.6);
            cursor: pointer;
            transition: all 0.1s ease-in-out;
        }}
        div.stButton > button:hover {{
            background-color: #ffffff;
            color: #7d604f;
            transform: translateY(-2px);
            box-shadow: 0 12px 20px rgba(125, 96, 79, 0.6);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    if logo_img:
        st.markdown(
            f"""
            <div class="logo-container">
                <img src="{logo_img}" alt="Logo" />
            </div>
            """,
            unsafe_allow_html=True
        )

    if st.button("✨ Let’s talk Arabic ✨"):
        with open(flag_file_path, "w") as f:
            f.write("true")
        st.rerun()
