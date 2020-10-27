import Speech_recognition as sr


def reconhece():
    rec = sr.Recognizer()

    with sr.Microphone() as s:
        rec.adjust_for_ambient_noise(s)

        while True:
            try:
                audio = rec.listen(s)
                entrada = rec.recognize_google(audio, Language="pt")
                return "Você disse {}".format(entrada)

            except sr.UnknownValueError:
                return "nao entendi nada"


fala -reconhece()
print(fala)