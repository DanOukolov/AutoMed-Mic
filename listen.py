import speech_recognition as sr
# import gpizero import Button



#button = Button(9)
#button.when_pressed = run

# def run():
#     listening = True

#     while listening:
#         with sr.Microphone() as source:
#             recognizer = sr.Recognizer()
#             recognizer.adjust_for_ambient_noise(source)
#             recognizer.dynamic_energy_threshold = 3000

#             try:
#                 print("Listening... ")
#                 audio = recognizer.listen(source, timeout = 5.0)
#                 response = recognizer.recognize_google(audio)
#                 print(response)
#             except sr.UnknownValueError:
#                 print("Didn't recognize that Doc!")


listening = True

while listening:
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        recognizer.dynamic_energy_threshold = 3000

        try:
            print("Listening... ")
            audio = recognizer.listen(source, timeout = 5.0)
            response = recognizer.recognize_google(audio)
            print(response)
        except sr.UnknownValueError:
            print("Didn't recognize that Doc!")