import os
import time
from colored import fg
import platform

def start():
    def cls():
        oss = platform.system()
        if oss.startswith("Linux") == True:
            os.system("clear")
        else:
            os.system("cls")

    def main1():
              cls()
              print(fg('#FF0000') + ' _________________________________________________________________________________ ')                       
              print(fg('#FF0000') + '|'+ fg(26) +'                             '+ fg(255) +'         ______          '+ fg(26) +'                           ' + fg('#FF0000') + '|')   
              print(fg('#FF0000') + '|'+ fg(26) +'            ▄▄        ▄      '+ fg(255) +'      .-"      "-.       '+ fg(26) +'     ▄▄▄▄▄▄▄▄▄▄▄           ' + fg('#FF0000') + '|')        
              print(fg('#FF0000') + '|'+ fg(26) +'           ▐░░▌      ▐░▌     '+ fg(255) +'     /            \      '+ fg(26) +'    ▐░░░░░░░░░░░▌          ' + fg('#FF0000') + '|')         
              print(fg('#FF0000') + '|'+ fg(26) +'           ▐░▌░▌     ▐░▌     '+ fg(255) +'    |              |     '+ fg(26) +'    ▐░█▀▀▀▀▀▀▀▀▀           ' + fg('#FF0000') + '|')                     
              print(fg('#FF0000') + '|'+ fg(26) +'           ▐░▌▐░▌    ▐░▌     '+ fg(255) +'    |,  .-.  .-.  ,|     '+ fg(26) +'    ▐░▌                    ' + fg('#FF0000') + '|')                      
              print(fg('#FF0000') + '|'+ fg(26) +'           ▐░▌ ▐░▌   ▐░▌     '+ fg(255) +'    | )(__/  \__)( |     '+ fg(26) +'    ▐░▌ ▄▄▄▄▄▄▄▄           ' + fg('#FF0000') + '|')                     
              print(fg('#FF0000') + '|'+ fg(26) +'           ▐░▌  ▐░▌  ▐░▌     '+ fg(255) +'    |/     /\     \|     '+ fg(26) +'    ▐░▌▐░░░░░░░░▌          ' + fg('#FF0000') + '|')                      
              print(fg('#FF0000') + '|'+ fg(26) +'           ▐░▌   ▐░▌ ▐░▌     '+ fg(255) +'    (_     ^^     _)     '+ fg(26) +'    ▐░▌ ▀▀▀▀▀▀█░▌          ' + fg('#FF0000') + '|')               
              print(fg('#FF0000') + '|'+ fg(26) +'           ▐░▌    ▐░▌▐░▌     '+ fg(255) +'     \__|IIIIII|__/      '+ fg(26) +'    ▐░▌       ▐░▌          ' + fg('#FF0000') + '|')           
              print(fg('#FF0000') + '|'+ fg(26) +'           ▐░▌     ▐░▐░▌     '+ fg(255) +'      | \IIIIII/ |       '+ fg(26) +'    ▐░█▄▄▄▄▄▄▄█░▌          ' + fg('#FF0000') + '|')            
              print(fg('#FF0000') + '|'+ fg(26) +'           ▐░▌      ▐░░▌     '+ fg(255) +'      \          /       '+ fg(26) +'    ▐░░░░░░░░░░░▌          ' + fg('#FF0000') + '|')                      
              print(fg('#FF0000') + '|'+ fg(26) +'            ▀        ▀▀      '+ fg(255) +'       `--------`        '+ fg(26) +'     ▀▀▀▀▀▀▀▀▀▀▀           ' + fg('#FF0000') + '|')                                         
              print(fg('#FF0000') + '|_________________________________________________________________________________|')   
              print(fg('#FF0000') + "|" + fg(220) + "By Hossein Mohseni               " + fg(76) + "Version v1.00" + fg(99) + "                      ngrok mask :)" + fg('#FF0000') + "|")
              print(                                              '-----------------------------------------------------------------------------------')                       
    main1()

    ngl = input(fg('#FF0000') +" ┌─["+ fg(5) +"ngrok-mask"+ fg(6) +"~"+ fg(220) +"@ROOT"+ fg('#FF0000') +"]"+ fg(6) +"~"+ fg('#FF0000') +"["+ fg(255) +"insert you'r ngrok link" + fg('#FF0000') + """]
 └──╼"""+ fg(220) +">" + fg(2) + ">" + fg(91) + ">" + fg(220) + " ")
    if ngl.startswith("https") and ngl.endswith("ngrok.io") == True:
        ngl = ngl[8:]
    
    elif ngl.startswith("http") and ngl.endswith("ngrok.io") == True:
        ngl = ngl[7:]
    
    else:
        try:
          raise "input not an ngrok link!"
        except:
            main1()
            print(fg('#FF0000') + "input not an ngrok link!")
            time.sleep(1)
            start()
    d = []
    def do():
        main1()
        domain = input(fg('#FF0000') +" ┌─["+ fg(5) +"ngrok-mask"+ fg(6) +"~"+ fg(220) +"@ROOT"+ fg('#FF0000') +"]"+ fg(6) +"~"+ fg('#FF0000') +"["+ fg(255) +"insert an http or https link (exp: https://instagram.com or https://google.com)" + fg('#FF0000') + """]
 └──╼"""+ fg(220) +">" + fg(2) + ">" + fg(91) + ">" + fg(220) + " ")
        if domain:
            if domain.startswith("http://") == True or domain.startswith("https://") == True:
               d.append(domain)
        else:
            try:
              raise "invalid link!"
            except:
                main1()
                print(fg('#FF0000') + "invalid link!")
                time.sleep(1)
                do()
    do()            
    
    main1()
    suff = input(fg('#FF0000') +" ┌─["+ fg(5) +"ngrok-mask"+ fg(6) +"~"+ fg(220) +"@ROOT"+ fg('#FF0000') +"]"+ fg(6) +"~"+ fg('#FF0000') +"["+ fg(255) +"insert an suffix (exp: free-money)" + fg('#FF0000') + """]
 └──╼"""+ fg(220) +">" + fg(2) + ">" + fg(91) + ">" + fg(220) + " ").replace(" ","-")
    if suff == None or suff == "" or suff == " ":
        suff =""
    else:
        suff = "/" + suff    
    main1()
    print(fg('#FF0000') +" ┌─["+ fg(5) +"ngrok-mask"+ fg(6) +"~"+ fg(220) +"@ROOT"+ fg('#FF0000') +"]"+ fg(6) +"~"+ fg('#FF0000') +"["+ fg(255) +"Result" + fg('#FF0000') + """]
 └──╼"""+ fg(220) +">" + fg(2) + ">" + fg(91) + ">" + fg(220) + " " + fg(204) + "Your new link is: " + fg(6) + d[0] + suff + "@" + ngl)
    time.sleep(5)
    os.system("exit")
start()    
    
    
    