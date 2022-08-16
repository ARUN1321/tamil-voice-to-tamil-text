import speech_recognition as sr
a = sr.Recognizer()
with sr.Microphone() as source:
    c = a.listen(source)
try:
    b = a.recognize_google(c, language="ta-IN")
    print(b)
except: pass
