import streamlit as st
from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import tempfile
import os

# Create translator object
translator = Translator()

# Function to translate text
def translate_text(text, dest_lang):
    translation = translator.translate(text, dest=dest_lang)
    return translation.text

# Function to speak text
def speak_text(text, lang):
    with tempfile.NamedTemporaryFile(delete=False) as fp:
        tts = gTTS(text=text, lang=lang)
        tts.save(f"{fp.name}.mp3")
        os.system(f"start {fp.name}.mp3")

# Main function
def main():
    st.title("Simple Translator with Voice Input")

    # Language options
    languages = {'French': 'fr', 'English': 'en'}

    # Language selection
    source_lang = st.selectbox("Select source language:", list(languages.keys()))
    dest_lang = st.selectbox("Select destination language:", list(languages.keys()))

    # Text input
    text_input = st.text_input("Enter text:")

    # Translation button
    if st.button("Translate"):
        translated_text = translate_text(text_input, languages[dest_lang])
        st.success(f"Translated text: {translated_text}")

    # Voice input option
    st.subheader("Voice Input")
    voice_input = st.checkbox("Enable Voice Input")

    # Speech recognition
    if voice_input:
        st.write("Speak now...")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        st.write("Transcribing...")
        try:
            text = r.recognize_google(audio)
            st.success(f"Text recognized: {text}")
            if st.button("Translate & Speak"):
                translated_text = translate_text(text, languages[dest_lang])
                st.success(f"Translated text: {translated_text}")
                speak_text(translated_text, languages[dest_lang])
        except sr.UnknownValueError:
            st.error("Sorry, could not understand audio.")
        except sr.RequestError as e:
            st.error(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()
