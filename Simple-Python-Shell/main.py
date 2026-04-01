import subprocess as sub
from termcolor import colored as color
while True :
    try :
        command = str(input(color("|\n'=> " ,'cyan')))
        if command.lower() == "stop" or command.lower() == "exit" :
            break 
        else : 
            sub.run(command ,shell=True )
            continue
    except Exception: 
        print (color("This command not fond !!!" , 'red'))
print (color("Good Bye..." , 'yellow'))
