#page 60
import webbrowser



def search():
    
    ui = input("Which website do you want to go ?: ")
    
    if ui == "youtube" or ui == "ytube":
        webbrowser.open("www.youtube.com")
        
    elif ui == "new tab" or ui == "newtab" or ui == "nt":
        webbrowser.open("https://www.google.com/")
        
    elif ui == "gmail":
        webbrowser.open("https://mail.google.com/mail/u/2/#inbox")
        
    elif ui == "git" or ui == "github":
        webbrowser.open("http://github.com/")
        
    elif ui == "codetantra" or ui == "ct":
        webbrowser.open("https://fkshyderabad.codetantra.com/login.jsp")
        
    elif ui == "netflix" or ui == "nf" or ui == "nflix":
        webbrowser.open("https://www.netflix.com/browse")
        
    elif ui == "symbosis" or ui == "sb" or ui == "symsis":
        webbrowser.open("http://www.scdl.net/")
        
    elif ui == "facebook" or ui == "fb":
        webbrowser.open("facbook.com")
        
    elif ui == "quick draw"or ui == "q draw":
        webbrowser.open("https://quickdraw.withgoogle.com/")
        
    elif ui == "search" or ui == "s":
        search_input = input("what do you want to search?: ")
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("google.com/?#q="+search_input)
    
    elif ui == "search youtube" or ui == "s youtube"or ui == "s ytube":
        s_ytube = input("what do you want to search in youtube? : ")
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com/"+s_ytube)    
    
    else:
        if ui != None:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(ui)    
            

    search()
    
search()
        