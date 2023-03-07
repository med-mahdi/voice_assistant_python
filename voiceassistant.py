import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Set speaker output
engine.setProperty('output', 'huawei cm510')  # Replace with your speaker name

# Set voice rate
engine.setProperty('rate', 150)  # Adjust as needed

# Input text to say
text = "Hello, how can I help you?"

# engine.say(text)
# engine.runAndWait()