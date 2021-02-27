import speech_recognition as sr

#wit_ai_key = "VM3CSCWWOO4PWLQUJ6XKYDEP4KCDFD7P"

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)
        try:
            #print("Wit: " + r.recognize_wit(audio, key=wit_ai_key))
            print("Gulugulu:" + r.recognize_google(audio, language='it-it', show_all=False))
        except sr.UnknownValueError:
            print("Non sente")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
