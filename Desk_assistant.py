from playsound import playsound
from datetime import datetime
import os
import speech_recognition as sr
import webbrowser
import win32com.client as wincl
import wikipedia
from os import sys
import pywhatkit


def wish():
	hour = int(datetime.now().hour)
	if hour>=0 and hour<12:
		playsound('C:\\Users\\User\\hey.mp3')
	elif hour>=12 and hour<16:
		playsound('C:\\Users\\User\\aftr.mp3')
	else:
		playsound('C:\\Users\\User\\evng.mp3')

speak = wincl.Dispatch("SAPI.SpVoice")

def work():
	speak.Speak("How may I help you..")

def into():
	speak.Speak("Hi I'm Skyler.....")

def take_command():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening....")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing....")
		query = r.recognize_google(audio, language='en-in')
		print("You said : " +query)

	except Exception:
		print("say it again please....")
		return "None"

	return query



if __name__ == "__main__":
	wish()
	into()
	work() 
	while True:
		query = take_command().lower()

		if 'google' in query:
			webbrowser.open("google.com")

		elif 'youtube' in query:
			webbrowser.open("youtube.com")

		elif 'shut down' in query:
			playsound('C:\\Users\\User\\nt.mp3')
			os.system("shutdown /s /t 3")

		elif 'restart' in query:
			os.system("shutdown /r /t 1")

		elif 'movies' in query:
			os.startfile("F:\\Movies")

		elif 'wikipedia' in query:
			speak.Speak("Searching wikipedia....")
			query = query.replace("wikipedia", "")
			result = wikipedia.summary(query, sentences=2)
			speak.Speak("According to wikipedia..")
			print(result)
			speak.Speak(result)

		elif 'finish' in query:
			sys.exit(0)

		elif 'code' in query:
			os.system("taskkill /f /im Code.exe")

		elif 'search' in query:
			query = query.replace("search", "")
			pywhatkit.search(query)
			
		elif 'show' in query:
			query = query.replace("show", "")
			pywhatkit.playonyt(query)
			

