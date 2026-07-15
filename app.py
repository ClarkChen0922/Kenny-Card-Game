import streamlit as st
import random
import os
import time

# 1. 頁面基本設定
st.set_page_config(page_title="獅群真心話大冒險", page_icon="💡", layout="centered")

# 全域背景圖片網址
GLOBAL_BG_URL = "https://images.pexels.com/photos/33828271/pexels-photo-33828271.jpeg"

# 2. 讀取題庫邏輯
def load_questions(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    return []

warmup_questions = load_questions("warmup_questions.txt")
formal_questions = load_questions("formal_questions.txt")

# 3. UI 頂部與選單
st.title("獅群真心話大冒險")

selected_team = st.selectbox("請選擇組別：", ["第一組", "第二組", "第三組", "第四組"])
selected_mode = st.radio("請選擇階段：", ["🧊 暖身題", "🎯 正式題"], horizontal=True)

# 4. 動態注入 CSS 
st.markdown(f"""
<style>
#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}

.stApp {{
    background-image: linear-gradient(rgba(0, 0, 0, 0.55), rgba(0, 0, 0, 0.55)), url("{GLOBAL_BG_URL}"); 
    background-size: cover; 
    background-position: center; 
    background-attachment: fixed;
}}

h1 {{
    font-size: 42px !important; 
    color: #FFFFFF !important; 
    font-weight: 900 !important; 
    text-align: center !important;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5) !important; 
    margin-bottom: 30px !important;
}}

label[data-testid="stWidgetLabel"] p {{
    color: #FFFFFF !important; 
    font-size: 16px !important; 
    font-weight: 600 !important; 
    text-shadow: 1px 1px 4px rgba(0,0,0,0.6) !important;
}}

/* ==================================================
   🎯 統一前三個色塊
   ================================================== */
div[data-baseweb="select"] > div,
div[role="radiogroup
