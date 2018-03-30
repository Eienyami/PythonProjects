import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
text = ''


def change_voice():
    index = 0
    print('Available voices: ')
    for voice in voices:
        print(str(index) + '. ' + voice.name)
        index += 1

    i = int(input("Enter index:"))
    if i in range(len(voices)):
        voice = voices[i]
        engine.setProperty('voice', voice.id)
    else:
        print("Invalid input!\n")
        change_voice()


print("'!exit' for exit, '!change' for changing voice.")
change_voice()

while True:
    text = input()
    if text == '!exit':
        break
    if text == '!change':
        change_voice()
        continue
    engine.say(text)
    engine.runAndWait()
