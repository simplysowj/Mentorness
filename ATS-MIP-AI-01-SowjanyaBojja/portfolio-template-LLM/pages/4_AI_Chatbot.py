import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
import json
import streamlit as st

# Load the JSON data
with open(r"C:\Users\simpl\Downloads\Portfolio-sowjanya\portfolio-template-LLM\pages\sowjanya_info.json", "r") as file:
   data = json.load(file)
# Function to convert text to speech
def text_to_speech(text, filename='output.mp3'):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    return filename

# Function to convert speech to text
def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Say something...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        st.write(f"You said: {text}")
        return text
  
    except sr.RequestError as e:
        st.write(f"Could not request results from Google Speech Recognition service: {e}")
        return None
    except sr.UnknownValueError:
        st.write("Sorry, could not understand audio.")


# Function to chat with the bot

def chat_with_bot(user_input):
    if user_input.lower() in ["hi", "hello", "hey"]:
        return "Hey want to know about me ask about sowjanya . You said: " + user_input
    elif user_input.lower() in ["about sowjanya", "who is sowjanya", "tell me about sowjanya"]:
        return "Sure! Here's some information about Sowjanya:\n\nName: {}\nTitle: {}\nEducation: {}\nCareer Goal: {}\nSkills: {}\nContact: LinkedIn: {}\nPhone: {}\nLocation: {}\nPortfolio: {}\nAvailability: {}".format(
            data["about"]["name"],
            data["about"]["title"],
            data["about"]["education"]["degree"],
            data["about"]["career_goal"],
            ", ".join(data["about"]["skills"]),
            data["about"]["contact"]["linkedin"],
            data["about"]["contact"]["phone"],
            data["about"]["contact"]["location"],
            data["about"]["portfolio"],
            data["about"]["availability"]
        )
    elif user_input.lower() in ["what are sowjanya's strengths", "tell me sowjanya's strengths"]:
        return "Sowjanya's strengths lie in a profound passion for technology, innovative problem-solving, and client-centric solutions."
    elif user_input.lower() in ["what are sowjanya's weaknesses", "tell me sowjanya's weaknesses"]:
        return "Sowjanya's unwavering pursuit of excellence may occasionally lead to in-depth analysis, but it ensures the delivery of high-quality services."
    elif user_input.lower() in ["what are sowjanya's interests", "tell me sowjanya's interests"]:
        return "Sowjanya's passion for technology extends into leisure hours, where they delve into the cutting-edge realm of GenAI, continuously pushing the boundaries of what can be achieved in various projects. In addition, Sowjanya finds joy in the simple pleasures of life, such as walking their dogs, swimming, and sharing coffee moments with friends and family."
    else:
        return "I'm sorry, I didn't understand that. You can ask me about Sowjanya by typing 'about Sowjanya', or inquire about Sowjanya's strengths, weaknesses, or interests."

# Main function
def main():
    st.title("Speech-to-Text and Text-to-Speech AI Chatbot")
    
    # User input method selection
    input_method = st.radio("Select input method:", ("Type", "Speech"))
    
    # Initialize chat history
    chat_history = ""
    
    # Get user input
    if input_method == "Type":
        user_input = st.text_input("You:")
    else:
        user_input = speech_to_text()
    
    # Chat with the bot and display response
    if st.button("Send"):
        if user_input:
            response = chat_with_bot(user_input)
            st.write(f"Chatbot: {response}")
            
            # Convert response to speech
            speech_file = text_to_speech(response)
            st.audio(speech_file, format='audio/mp3')

if __name__ == "__main__":
    main()
