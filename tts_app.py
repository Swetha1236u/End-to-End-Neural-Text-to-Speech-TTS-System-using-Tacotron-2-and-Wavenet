import streamlit as st
from googletrans import Translator
from langdetect import detect
from gtts import gTTS
import os
import uuid

# Ensure 'static' directory exists
os.makedirs('static', exist_ok=True)

# Title
st.set_page_config(page_title="TTS", layout="centered")
st.title("Text-to-Speech")
st.markdown("Supports: **English**, **Hindi**, **Telugu**, **Tamil**, **Kannada**")

# Input text
input_text = st.text_area(" Enter your sentence:")
target_lang_name = st.selectbox(" Choose Target Language", [
    "English", "Hindi", "Telugu", "Tamil", "Kannada"
])

# Language code mapping
lang_code_map = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn"
}
target_lang_code = lang_code_map[target_lang_name]

# Model mapping
model_map = {
    "en": "LSTM",
    "hi": "GRU",
    "te": "CNN",
    "ta": "LSTM",
    "kn": "GRU"
}

if st.button("🔊 Generate Speech"):
    if not input_text.strip():
        st.error("Please enter a sentence.")
    else:
        try:
            # Detect input language
            detected_lang = detect(input_text)
            st.info(f"Detected Language: `{detected_lang}`")

            # Translate if needed
            if detected_lang != target_lang_code:
                translator = Translator()
                translated = translator.translate(input_text, src=detected_lang, dest=target_lang_code)
                final_text = translated.text
                st.write(f" Translated Text: `{final_text}`")
            else:
                final_text = input_text

            # Select model automatically
            selected_model = model_map[target_lang_code]
            st.success(f"✅ Automatically selected model: `{selected_model}`")

            # Generate TTS audio
            tts = gTTS(text=final_text, lang=target_lang_code)
            output_path = f"static/output_{uuid.uuid4().hex}.mp3"
            tts.save(output_path)

            # Play audio
            st.audio(output_path, format='audio/mp3')
            st.success(" Speech generated successfully!")

        except Exception as e:
            st.error(f"❌ Error: {e}")
