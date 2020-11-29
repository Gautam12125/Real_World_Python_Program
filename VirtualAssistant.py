import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import file_search
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good AfterNoon!")
    else:
        speak("Good Evening!")
    
    speak('''I am .... BAPPU Assistant 
            Created By.... Gautam Sharma on 28 November 2001
            How may I Help You?''')
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print("User Said!: ",(query))
    except Exception as e:
        print(e)
        print("Say That Again Please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching WikiPedia.....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According To WikiPedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open facebook" in query:
            webbrowser.open("facebook.com")
        elif "bhajan" in query:
            music_dir = "F:\\ringtone"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
        elif 'anuj' in query:
            anuj = '''Anuj is a Good Boy He is a friend of Gautam Sharma since ninth class 
            Now in end I am Speak Something About 
            Yaara Teri Yaari Ko
            Maine To Khuda Mana 
            Meri zindagi sawaari
            Mujhko gale lagake'''
            speak(anuj)
        elif 'gaurav' in query:
            gaurav = '''Gaurav is a Smart Boy He is a friend of Gautam Sharma since college time 
            Now in end I am Speak Something About 
            Meri zindagi sawaari
            Mujhko gale lagake
            Baitha diya falak pe
            Mujhe khaak se uthaake
            Yaara teri yaari ko
            Maine toh khuda maana
            Yaad karegi duniya
            Tera mera afsaana'''
            speak(gaurav)
        elif 'bhavishya' in query:
            bhavishya = '''Bhavishya is a Topper Boy He is a friend of Gautam Sharma since College Time 
            He Is Topper of Poornima Institute of Engineering and Technology
            Now in end I am Speak Something About 
            Yaara Teri Yaari Ko
            Maine To Khuda Mana
            Meri zindagi sawaari
            Mujhko gale lagake '''
            speak(bhavishya)
        