import os

# Check if gtts library is available
try:
    from gtts import gTTS
    gtts_available = True
except ImportError:
    gtts_available = False

# Function to convert text to speech using gtts (online)
def tts_online(text):
    try:
        language = 'en'
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save("output.mp3")
        os.system("start output.mp3")  # For Windows, use appropriate command for other OS
        return True  # Return True if successful
    except Exception as e:
        print("online:", e)
        return False  # Return False if failed

# Function to convert text to speech using pyttsx3 (offline)
def tts_offline(text):
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)    # Speed percent (can go over 100)
        engine.setProperty('volume', 0.9)  # Volume 0-1
        engine.save_to_file(text, 'output.mp3')
        engine.runAndWait()
        return True  # Return True if successful
    except Exception as e:
        print("offline:", e)
        return False  # Return False if failed

# Text to convert to speech
text = "anup kc is gay"

#check online or offline
if gtts_available:
    if not tts_online(text):
        tts_offline(text)
else:
    tts_offline(text)
