import speech_recognition as sr

recognizer = sr.Recognizer()

def recognize_speech():
    with sr.Microphone(device_index=0) as source:  # Microphone setup within 'with' statement
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Process recognized text
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

recognize_speech()
