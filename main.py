import time

import speech_recognition as sr


def callback(recognizer, audio):

    wit_ai_key = "VM3CSCWWOO4PWLQUJ6XKYDEP4KCDFD7P"
    try:
        print("Wit.ai: " + recognizer.recognize_wit(audio, key=wit_ai_key))
    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))


m = sr.Microphone()
with m as source:
    r = sr.Recognizer()
    #r.energy_threshold = 50
    #r.dynamic_energy_threshold = False

stop_listening = r.listen_in_background(m, callback)

for _ in range(5000): time.sleep(0.1)

stop_listening(wait_for_stop=False)

while True: time.sleep(0.1)

if __name__ == '__main__':
    pass
