

recogniser = sr.Recognizer()
sound = sr.AudioFile('my_ivan.wav')




with sound as source:
    audio = recogniser.record(source)


text = recogniser.recognize_google(audio)
print(text)


