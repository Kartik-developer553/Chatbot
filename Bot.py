import pyautogui
import time
import pyperclip
from openai import OpenAI
client = OpenAI(
   api_key="Your_API_Key"
)
# pyautogui.moveTo(1219,1055,duration=2)
# pyautogui.click() # to move the mouse to correct position and then click you can use this and also in this you can view your mouse movement by using duration 
def check_sender_name(chat):
    sender_name=chat.strip().split("]")[-1].split(":")[0].lower().strip()
    if(sender_name!="kartik"):
        return True
    return False
# click at chrome
pyautogui.click(1219,1055) # it is used to direcly click at the required position
time.sleep(1) # # to add somme delay and to ensure click is registered

# move from where drag starts
pyautogui.moveTo(302,15,duration=0.5)
pyautogui.click()
time.sleep(1) # to add somme delay and to ensure click is registered
pyautogui.moveTo(700,258,duration=0.5)
pyautogui.dragTo(1857,905,duration=1,button="left")
# drag ends here 

# copy the chat history 
pyautogui.hotkey("ctrl","c")
time.sleep(1)
pyautogui.click(688,513) # unslect the selected text 
chat_history=pyperclip.paste()
if check_sender_name(chat_history):
    # # Generate response from AI
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": (
        "You are Kartik, a sharp and clever individual who speaks both Hindi and English fluently."
        "You are from India and understand conversational nuances and cultural context. "
        "Analyze the provided chat history carefully and respond as Kartik, ensuring your reply aligns with the tone, context, and intent of the conversation. "
        "Focus on generating a thoughtful, natural, and contextually relevant response that maintains the flow of the conversation. "
        "Do not include any sender names, timestamps, or unnecessary details. please dont include any time stamps and name"
        "Keep your response concise and directly relevant to the last message or ongoing topic.")},
        {"role": "user", "content": chat_history}
        ]
    )
    response = completion.choices[0].message.content
    pyperclip.copy(response)  # Add the response in the clipboard
    pyautogui.click(1209, 969, duration=0.5)  # Click at the message delivery box
    pyautogui.hotkey("ctrl", "v")  # Paste the response from the AI
    time.sleep(1)