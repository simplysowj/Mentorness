import streamlit as st
from deep_translator import GoogleTranslator

# Function to translate content
def translate_content(content, target_language):
    translated_text = GoogleTranslator(source='auto', target=target_language).translate(content)
    return translated_text

# English content
english_content = {
    "header": "Welcome to My Streamlit App",
    "description": "This is a demo of how to translate a Streamlit app into different languages.",
    "button_label": "Translate Content"
}

# Hindi content
hindi_content = {
    "header": "मेरे स्ट्रीमलिट ऐप में आपका स्वागत है",
    "description": "यह एक उदाहरण है कि कैसे एक स्ट्रीमलिट ऐप को विभिन्न भाषाओं में अनुवादित किया जाता है।",
    "button_label": "सामग्री का अनुवाद करें"
}

# Language options
language_options = {
    "English": "en",
    "Hindi": "hi"
}

# Select language
selected_language = "English"  # Default to English
if st.sidebar.checkbox("Translate to Hindi"):
    selected_language = "Hindi"

# Translate content based on language selection
if selected_language == "English":
    content = english_content
else:
    content = hindi_content

# Translate and display content
header = translate_content(content["header"], language_options[selected_language])
description = translate_content(content["description"], language_options[selected_language])
button_label = translate_content(content["button_label"], language_options[selected_language])

st.title(header)
st.write(description)
if st.button(button_label):
    st.write("Content translation button clicked!")
