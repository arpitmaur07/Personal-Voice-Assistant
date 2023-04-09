import datetime
from files import commands
import wikipedia
import webbrowser as wb
import pywhatkit
import os
import random



def wishMe ():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        commands.speak(f"Good Morning!")
    elif hour>=12 and hour<18:
        commands.speak(f"Good Afternoon!")   
    else:
        commands.speak(f"Good Evening!")  
    commands.speak("I am Alina, your personal assistant sir!.how may I help you...") 
  
      
def search_in_wikipedia(content):
    results= wikipedia.summary(content,sentences=2)
    # print(results)
    commands.speak('According to wikipedia..')
    commands.speak(results)
    
    
def open_site(site):
    commands.speak(f'ok captain. Opening..{site}.')
    wb.register('chrome', None)
    wb.open(f"https://www.{site}.com/")     
    

def openYoutube(content):
    commands.speak(f"searching! {content} on youtube.")
    pywhatkit.playonyt(content)   
    
    
def playSong():
    music_dir = 'C:\\Users\Arpit Maurya\\Desktop\\Arpit\\arpit\\arpit photos\\ccc4_dot\\music'
    songs = os.listdir(music_dir)  
    randomSong=random.randint(0,len(songs)-1)
    os.startfile(os.path.join(music_dir, songs[randomSong]))  
    
def open_vscode():
    codePath = "C:\\Users\\Arpit Maurya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath) 
    
def open_msWord():
    codePath = "C:\\Program Files\Microsoft Office\\root\\Office16\\WINWORD.EXE" 
    os.startfile(codePath) 
    
def open_poworPoint():
    codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
    os.startfile(codePath)
     
def open_excel():
    codePath = "C:\\Program Files\\Microsoft Office\\root\Office16\\EXCEL.EXE"
    os.startfile(codePath) 
    
def open_chrome():
    codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    os.startfile(codePath) 
    
def open_notepad():
    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\Programs\\Accessories\\Notepad.lnk"
    os.startfile(codePath) 
    
def open_paint():
    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk"
    os.startfile(codePath)     
    

                    
    
   
    
def tellTheTime():
    strTime = datetime.datetime.now().strftime("%I:%M %p")    
    commands.speak(f"Sir, the time is {strTime}")  
    
def searchOnGoogle(content):
    wb.register('chrome', None)
    stringList=content.split()
    searching_for='+'.join(stringList)  
    wb.open(f"https://www.google.com/search?q={searching_for}") 

        
    
    
def what_are_you_doing():
    replies=['i am taking commands from my captain.','talking with my dear sir.','waiting for my captain commands.']
    commands.speak(random.choice(replies))
    
    
def who_are_you():
    replies=['I am Alina, your lovely personal assistant.', 'Alina, did not I tell you before?','You ask that so many times! I am Alina.']
    commands.speak(random.choice(replies))
    
    
def how_am_i(): 
    replies =['You are goddamn handsome!', 'My knees go weak when I see you.', 'You are sexy!', 'You look like the kindest person that I have met.'] 
    commands.speak(random.choice(replies))
 
 
def tell_joke(): 
    jokes = ['What happens to a frogs car when it breaks down? It gets toad away.', 'Why was six scared of seven? Because seven ate nine.', 'No, I always forget the punch line.']
    commands.speak(random.choice(jokes))  
    
    
def where_born(): 
    commands.speak('I was created by a magician named Arpit, in India, the magical land of ayodhya.')
    
def age():
    commands.speak('i was lunched in october 2022. I am too little.')      
         

def how_are_you(): 
    commands.speak('I am fine sir, thank you.')

    
    
def what_you_can_do():
    replies=['you can say opening for websites','i can play songs and search somthing on google.', 'sir! i can play videos on youtube','you can say to read nay artical from wikipedia.']     
    commands.speak(random.choice(replies))   
    commands.speak('and many more sir! ')
    

def undefined():
    replies=['I dont know what that means!','Alina could not understand this audio']
    commands.speak(random.choice(replies))
    