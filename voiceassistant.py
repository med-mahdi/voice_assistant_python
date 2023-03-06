import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set speaker output
engine.setProperty('output', 'huawei cm510')  # Replace with your speaker name

# Set voice rate
engine.setProperty('rate', 150)  # Adjust as needed

# Input text to say
text = "Hello, how can I help you?"

# Define activation phrase
activation_phrase = "hi siri"

# Convert text to speech and play it through speaker
# engine.say(text)
# engine.runAndWait()
