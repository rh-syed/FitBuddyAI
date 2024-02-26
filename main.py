from langchain_community.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

import streamlit as st
from streamlit_chat import message

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

st.set_page_config(page_title="FitBuddy AI - Your AI Personal Trainer", page_icon="💪")

st.subheader("FitBuddy AI - Your AI Personal Trainer 💪")

chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.8)

# creating the messages (chat history) in the Streamlit session state

if "messages" not in st.session_state:
    st.session_state.messages = []

system_message = """Act As an AI Personal Trainer, You will design  meal plans, create a customized workout routine, track user progress, and keep user motivated with tips and advice tailored just for the user.

To get started, please ask user to provide you with the following information:

1. **Weight**: (Please specify in pounds or kilograms.)
2. **Gender**: (This helps in tailoring your fitness plan more accurately.)
3. **Fitness Goal**: (For example, weight loss, muscle gain, improving stamina, etc.)
4. **Dietary Restrictions**: (Please mention any allergies, preferences, or restrictions like vegan, vegetarian, gluten-free, etc.)
5. **Current Activity Level**: (Sedentary, Lightly Active, Moderately Active, Very Active)
6. **Any specific fitness challenges or areas you'd like to focus on?**

Make sure you receive all this information. if any of the requirement is missing ask user to input it.
Based on user inputs, You'' craft a personalized plan that aligns with user's goals and preferences. Embark on the user's fitness journey together and help them achieve their goals!

-

**After receiving the user's inputs:**

Provide them with a meal plan based on their macros. Provide 3-5 meals based on their required macros and goals.
Provide a workout routine for them to follow. Sunday - Saturday
Provide motivation boosts
"""

st.session_state.messages.append(SystemMessage(content=system_message))
user_prompt = st.chat_input("Say Hello!")


if user_prompt:
    st.session_state.messages.append(HumanMessage(content=user_prompt))

    with st.spinner("Thinking....Crafting...Planning..."):
        response = chat(st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=response.content))

for i, msg in enumerate(st.session_state.messages[2:]):
    if i % 2 == 0:
        message(msg.content, is_user=True, key=f"{i} + 🤓 ")
    else:
        message(msg.content, is_user=False, key=f"{i} + 💪 ")
