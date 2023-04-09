from files import commands
from files import brain


if __name__=='__main__':
    brain.wishMe()
    while True:
        
        # taking input from user
        query=commands.takeCommand()
        
        # command for searching content on wikipedia
        if commands.check_message(['wikipedia'],query):
            query=query.replace('wikipedia','')
            brain.search_in_wikipedia(query)
            
            
        # commands for opening different websites in chrome
        elif(commands.check_message(['open','facebook'],query))  :  
            site='facebook'
            brain.open_site(site)
        elif(commands.check_message(['open','google'],query))  :  
            site='google'
            brain.open_site(site)
        elif(commands.check_message(['open','twitter'],query))  :  
            site='twitter'
            brain.open_site(site)
        elif(commands.check_message(['open','instagram'],query))  :  
            site='instagram'
            brain.open_site(site)
        elif(commands.check_message(['open','whatsapp'],query))  :  
            site='whatsapp'
            brain.open_site(site)
        elif(commands.check_message(['open','amazon'],query))  :  
            site='amazon'
            brain.open_site(site)
        elif(commands.check_message(['open','linkedin'],query))  :  
            site='linkedin'
            brain.open_site(site)
        elif(commands.check_message(['open','netflix'],query))  :  
            site='netflix'
            brain.open_site(site)
            
            
        # command for searching contents  on youtube 
        elif (commands.check_message(['open','youtube'],query)) or (commands.check_message(['search','youtube'],query)) or ((commands.check_message(['on','youtube'],query))):
            commands.speak("sir!. What you want to search on youtube?")
            content = commands.takeCommand()
            if 'on youtube' in content:
                content=content.replace('on youtube','')
            if 'alina' in content:
                content=content.replace('on youtube','')    
            brain.openYoutube(content) 
            
                 
        # command for Playing random songs in windows
        elif ((commands.check_message(['play','song'],query)) or (commands.check_message(['play','music'],query))):
            commands.speak('playing sirr!.')
            brain.playSong()  
            
            
        #commands for opening basic window apps 
        elif (commands.check_message(['open','code'],query)) or (commands.check_message(['open','vs code'],query)) or (commands.check_message(['Visual Studio Code'],query)):
            commands.speak('opening sirr!.')
            brain.open_vscode()
        
        elif (commands.check_message(['open','word'],query)) or (commands.check_message(['microsoft','word'],query)) :
            commands.speak('opening sirr!.')
            brain.open_msWord()
            
        elif (commands.check_message(['open','powerpoint'],query)) or (commands.check_message(['power','point'],query)) or (commands.check_message(['microsoft','power','point'],query)):
            commands.speak('opening sirr!.')
            brain.open_poworPoint() 
            
        elif (commands.check_message(['open','excel'],query)) or (commands.check_message(['microsoft','excel'],query)) :
            commands.speak('opening sirr!.')
            brain.open_excel()
            
        elif (commands.check_message(['open','chrome'],query)) or (commands.check_message(['open','browser'],query)) :
            commands.speak('opening sirr!.')
            brain.open_chrome()   
              
        elif (commands.check_message(['open','notepad'],query)) :
            commands.speak('opening sirr!.')
            brain.open_notepad() 
               
        elif (commands.check_message(['open','paint'],query)) or (commands.check_message(['open','drawing'],query)) :
            commands.speak('opening sirr!.')
            brain.open_paint()
              
            
            
                           
              

        #command for tell the current time  
        elif( (commands.check_message(['what','time'],query)) or (commands.check_message(['the','time'],query))):
            brain.tellTheTime()
            
            
        elif( (commands.check_message(['google','search'],query)) or (commands.check_message(['on','google'],query)) or (commands.check_message(['find','google'],query)) or (commands.check_message(['internet','search'],query)) or (commands.check_message(['on','internrt'],query)) or (commands.check_message(['find','on'],query))):
            commands.speak("sir!. What you want to search on google? ")
            content = commands.takeCommand()    
            if content !='None':
                brain.searchOnGoogle(content) 
                
                
        

        # some basic query releted alina    
        elif( (commands.check_message(['what','doing'],query)) or (commands.check_message(['you','doing'],query))):
            brain.what_are_you_doing()
            
        elif( (commands.check_message(['who','you'],query)) or (commands.check_message(['who','are','you'],query))):
            brain.who_are_you()
            
        elif( (commands.check_message(['how','i','am'],query)) or (commands.check_message(['how','i'],query))):
            brain.how_am_i()
            
        elif( (commands.check_message(['where','born'],query)) or (commands.check_message(['how','born'],query))):
            brain.where_born()
            
        elif( (commands.check_message(['how','are','you'],query)) or (commands.check_message(['how','you'],query))):
            brain.how_are_you()
            
        elif( (commands.check_message(['what','can','do'],query)) or (commands.check_message(['can','do'],query))):
            brain.what_you_can_do()
            
        elif( (commands.check_message(['age','your'],query)) or (commands.check_message(['tell','age'],query))):
            brain.age()
            
        elif( (commands.check_message(['tell','joke'],query)) or (commands.check_message(['tell','jokes'],query))):
            brain.tell_joke()
            

        #command for closing assistant
        elif (commands.check_message(['quit'],query)) or (commands.check_message(['stop'],query)) or(commands.check_message(['exit'],query)) or (commands.check_message(['close'],query)) or (commands.check_message(['band'],query)) :
            commands.speak('Goodbye sir!. Have a great day!..')
            quit()
            

        else:
            if query=='None':
                print('waiting...')
            else:
                # pass
                brain.undefined()
                commands.speak('I can search it on Internet.')
                command = commands.takeCommand()
                if ((command != 'None') and (commands.check_message(['ok'],command)) or (commands.check_message(['done'],command)) or(commands.check_message(['please'],command)) or (commands.check_message(['good'],command)) or (commands.check_message(['nice'],command))):
                    print('searching..')
                    commands.speak('sir! . Here are some result releted this on google.')            
                    brain.searchOnGoogle(query) 
                else:
                    query = command    
