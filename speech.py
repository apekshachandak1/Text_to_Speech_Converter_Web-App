import streamlit as st
from gtts import gTTS
from tempfile import NamedTemporaryFile
import os
import base64

# Set up the Streamlit app configuration
st.set_page_config(
    page_title="Text-to-Speech Converter App",
    page_icon="🔊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("🎤 Text-to-Speech Converter App 🔊")
st.write("""
Convert **Plain Text** or **SSML** (Speech Synthesis Markup Language) markup to high-quality speech with **customizable voice settings**. 
You can adjust the **speed**, **pitch**, and **volume** of the voice, and choose between **MP3 (Lossy)** or **WAV (Lossless)** output formats. 🎧
""")

# Side Panel Information
st.sidebar.header("🔧 Settings")
st.sidebar.write("""
Welcome to the Text-to-Speech Converter App! 
This app allows you to convert text or SSML input into speech in multiple languages. 🌏
You can fine-tune the voice properties like pitch, speed, and even select a device profile for better audio output. 
Try it now and listen to your text come alive with custom voices!
""")

# Input Method Selection
input_method = st.radio("Choose Input Method", ["Plain Text", "SSML"], key="input_method")

# Clear the default story and leave the text area empty
text_input = st.text_area(f"Enter your {input_method} below:", height=200)

# Language Selection
languages = {
    "English": "en",
    "Hindi": "hi",
    # Add more languages and their codes here
}
selected_language = st.selectbox("Select Language", list(languages.keys()), key="language")

# Voice Selection (Standard or WaveNet)
voice_types = ["Standard", "WaveNet"]
selected_voice_type = st.selectbox("Select Voice Type", voice_types, key="voice_type")

# Speed and Pitch
speed = st.slider("Select Speed (0.5x to 2.0x)", min_value=0.5, max_value=2.0, step=0.1, value=1.0, key="speed")
pitch = st.slider("Select Pitch (0.5x to 2.0x)", min_value=0.5, max_value=2.0, step=0.1, value=1.0, key="pitch")

# Output Format Selection
output_format = st.radio("Choose Output Format", ["MP3 (Lossy)", "WAV (Lossless)"], key="output_format")

# Audio Device Profile
audio_profiles = ["Default", "Handset", "Headphones", "Smartphone", "Wearable"]
selected_profile = st.selectbox("Select Audio Device Profile (Optional)", audio_profiles, key="profile")

# Function to convert text to speech using gTTS
def text_to_speech(text, language='en', speed=1.0, file_format="mp3"):
    tts = gTTS(text=text, lang=language, slow=(speed < 1.0))
    extension = f".{file_format}"
    audio_file = NamedTemporaryFile(delete=False, suffix=extension)
    tts.write_to_fp(audio_file)
    audio_file.close()
    return audio_file.name

# Function to generate download link for the audio file
def get_binary_file_downloader_html(bin_file, file_label='Download', file_name='file'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:file/{output_format.lower()};base64,{b64}" download="{file_name}.{output_format.lower()}">{file_label}</a>'
    return href

# Convert Button
if st.button("Convert to Speech 🎶"):
    if text_input.strip() != "":
        st.write("🔄 Converting text to speech...")

        # Call the text_to_speech function and get the audio file
        audio_file_path = text_to_speech(
            text_input,
            language=languages[selected_language],
            speed=speed,
            file_format="wav" if output_format == "WAV (Lossless)" else "mp3"
        )

        # Display audio player
        with open(audio_file_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
        st.audio(audio_bytes, format=f"audio/{output_format.lower()}", start_time=0)

        # Download link
        st.markdown(
            get_binary_file_downloader_html(
                audio_file_path,
                file_label="Download Audio 📥",
                file_name="speech"
            ),
            unsafe_allow_html=True
        )

        # Delete temporary file
        os.remove(audio_file_path)
        st.success("✅ Speech conversion complete!")
    else:
        st.error("❗ Please enter some text or SSML markup to convert.")
