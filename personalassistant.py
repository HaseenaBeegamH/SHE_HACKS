from urllib import request 
 import pyttsx3 
 import datetime 
 import pywhatkit 
 import wikipedia 
 import requests 
 import pyjokes  
 from bs4 import BeautifulSoup 
   
 import speech_recognition as s 
  
 w=pyttsx3.init() 
  
 def speak(a): 
     w.say(a) 
     w.runAndWait() 
  
 def recognise(): 
     l=s.Recognizer() 
     with s.Microphone() as m: 
         print("listening") 
         voice=l.listen(m) 
         try: 
             command=l.recognize_google(voice) 
             return command 
  
         except: 
             a="please say again" 
             speak(a) 
             return a 
 def myname(): 
     speak("hey, echo here....what can i call you") 
     name=input("enter your name") 
     speak("hii " + name +" nice to meet you") 
     print("hii " + name +" nice to meet you") 
  
 def wishMe(): 
     hour=datetime.datetime.now().hour 
     if hour>=0 and hour<12: 
         speak("Good Morning, what can i do for you") 
         print("Good Morning, what can i do for you") 
     elif hour>=12 and hour<18: 
         speak("Good Afternoon, what can i do for you ") 
         print("Good Afternoon, what can i do for you") 
     else: 
         speak("Good Evening, what can i do for you") 
         print("Good Evening, what can i do for you") 
  
 myname() 
 wishMe() 
  
 key_wiki=['what','who', 'about'] 
 key_utube=['play','show','watch'] 
 key_temp=['weather','temperature','climate'] 
  
 while(1): 
     command = recognise() 
     print(command) 
     command=command.lower() 
  
     if 'search' in command: 
         a="Opening Chrome...." 
         print(a) 
         speak(a) 
         text=command.replace('search for', ' ') 
         pywhatkit.search(text) 
  
     elif 'time' in command: 
         time=datetime.datetime.now().strftime("%I:%M:%p") 
         print(time) 
         speak(time) 
  
     elif any(x in command for x in key_wiki): 
         speak("wait a second ") 
         result=wikipedia.summary(command,3) 
         print(result) 
         speak(result) 
  
     elif any(x in command for x in key_utube ): 
         b='opening youtube....' 
         print(b) 
         speak(b) 
         pywhatkit.playonyt(command) 
          
     elif any(x in command for x in key_temp): 
         t="temperature in thrissur" 
         url=f"https://www.google.com/search?q={t}" 
         r=requests.get(url) 
         data=BeautifulSoup(r.text,"html.parser") 
         temp=data.find("div",class_="BNeawe").text 
         speak(f"current{t} is {temp}")        
         print(f"current{t} is {temp}") 
  
     elif 'joke' in command: 
         j=pyjokes.get_joke() 
         speak(j) 
         print(j) 
      
     elif 'bye' in command: 
         speak("okay bye ") 
         hour=datetime.datetime.now().hour 
         if hour>21: 
             speak("good night") 
         else: 
             speak("see you again") 
         break