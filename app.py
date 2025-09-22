import openpyxl
import streamlit as st

# --- Load database pertanyaan & jawaban dari Excel ---
wb = openpyxl.load_workbook("qa.xlsx")
sheet = wb.active

qa_dict = {}
for row in sheet.iter_rows(min_row=2, values_only=True):
    pertanyaan, jawaban = row
    if pertanyaan and jawaban:
        qa_dict[pertanyaan.lower()] = jawaban

# --- Tampilan Website ---
st.set_page_config(page_title="Chatbot Excel", page_icon="🤖")
st.title("🤖 Chatbot Sederhana dari Excel")

# Simpan percakapan di session
if "chat" not in st.session_state:
    st.session_state.chat = []

# Input user
user_input = st.text_input("Ketik pesan:")

if st.button("Kirim") and user_input:
    st.session_state.chat.append(("Kamu", user_input))
    reply = qa_dict.get(user_input.lower(), "Maaf, saya belum punya jawaban untuk itu.")
    st.session_state.chat.append(("Bot", reply))

# Tampilkan percakapan
for sender, msg in st.session_state.chat:
    st.write(f"**{sender}:** {msg}")
