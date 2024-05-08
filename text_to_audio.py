import os
import platform

try:
    from gtts import gTTS
    gtts_available = True
except ImportError:
    gtts_available = False

def tts_online(text):
    try:
        language = 'en-us'  # Set language to American English
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save("output.mp3")
        if platform.system() == 'Windows':
            os.system("start output.mp3")  # For Windows
        elif platform.system() == 'Linux':
            os.system("xdg-open output.mp3")  # For Linux
        return True  
    except Exception as e:
        print("online:", e)
        return False  

def tts_offline(text):
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)   
        engine.setProperty('volume', 0.9) 
        engine.save_to_file(text, 'output.mp3')
        if platform.system() == 'Windows':
            os.startfile('output.mp3')  # For Windows
        elif platform.system() == 'Linux':
            os.system("xdg-open output.mp3")  # For Linux
        return True 
    except Exception as e:
        print("offline:", e)
        return False  

# Text to convert to speech
text = "WHAT IS YOUR NAME"

if gtts_available:
    if not tts_online(text):
        tts_offline(text)
else:
    tts_offline(text)
