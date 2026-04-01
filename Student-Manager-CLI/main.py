import os 
from termcolor import colored as color
info = {"ahmed":{"degree": 50, "success":"Seccssful"},
        "ali":{"degree":66, "success":"Failed"} }

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    
chek = False

def infor (stud):
    global chek 
    for kye,value in info.items():
        if stud.lower() == kye:
            clear_terminal()
            print (f"______________________________{"\n"*2}{color('Student :','light_magenta')} {kye} \n{color('Final Grade :','light_magenta')} {info[kye]["degree"]}\n{color('Seccess :','light_magenta')} {info[kye]["success"]}{"\n"*2}______________________________{"\n"*2}")
            chek = True
            break
    else:
        clear_terminal()
        print (color("this name not found..!! \n",'light_red')) 
        chek = False
    if chek == False:
        cont =  input (f"Enter ({color(" T ",'light_green')}) for Try agine {color("OR ",'light_cyan')} ({color("Q / exit",'light_red')}) for Exit :")
        clear_terminal()
        if cont.lower() == 't':
            infor(stud = input ("Enter student name : ") ) 
        else :
            return 
        
while True : 
    print (f"==============================={"\n"*2}{color('1-','light_yellow')} {color('Show Student Information\t📖','light_cyan')}{"\n"*2}{color('2-','light_yellow')} {color('Show All info Students\t📚','light_cyan')}{"\n"*2}{color('3-','light_yellow')} {color('Change Degree\t📝','light_cyan')}{"\n"*2}{color('4-','light_yellow')} {color('Add student\t\t➕','light_cyan')}{"\n"*2}{color('5-','light_yellow')} {color('Quit\t🏃🚪','red')}{"\n"*2}===============================") 
    number = int(input (f"\nEnter the number you want : ")) 
    clear_terminal()
    if number == 1:
            infor(stud = input ("Enter student name : "))
    elif number == 2:
         for kye,value in info.items():
            print (f"______________________________{"\n"*2}{color('Student :','light_magenta')} {kye} \n{color('Final Grade :','light_magenta')} {info[kye]["degree"]}\n{color('Seccess :','light_magenta')} {info[kye]["success"]}{"\n"*2}______________________________{"\n"*2}")  
    elif number == 3:    
        stud = input ("Enter student name you want change information : ")
        infor(stud)
        if chek == True :
                print (f"what Do you change :{"\n"*2}\t1- {color("Final Grade",'light_cyan')}{"\n"*2}\t2- {color("Succsess",'green')}{"\n"*2}\t3- {color("Exit",'red')}{"\n"*2}")
                chang = int(input ("enter number you want change: ")) 
                clear_terminal()
                if chang == 1: 
                    new = int(input ("Enter the new Degree : "))
                    info[stud]["degree"] = new
                    infor(stud)
                    print (f"..Seccess change..{"\n"*2}")
                elif chang == 2: 
                    print (f"choss one : {"\n"*2}\t1-{color('Seccess','green')}{"\n"*2}\t2-{color('Failed','red')}{"\n"*2}")
                    new = int(input (f"Enter number :"))
                    if new == 1:
                        info[stud]["success"] = "Seccess"
                    elif new == 2:
                        info[stud]["success"] = "Failed"
                    else:
                        print ("Pleas Enter the currect number...")
                    infor(stud)
                    print (f"..{color('Seccess change','light_green')}..{"\n"*2}")
                elif chang == 3:
                    clear_terminal()
                    continue
                    
                else:
                    print ("Pleas Enter the currect number...")
    elif number == 4:
        name = input(color("Enter student name :",'light_magenta'))
        grade = int(input (color("Enter Final Grade : ",'light_magenta')))
        secc = input (f"{color('Seccess','green')} OR {color('Failed','red')} : ")
        info[name] = {"degree": grade, "success":secc}
        infor(name)
        print (f"..{color('Seccess Add student','light_green')}..{"\n"*2}")
    elif number == 5:
        break
    else :
        print ("Pleas Enter the currect numbe..ℹ️ℹ️")
    
print (color("See you leater..👋👋",'green'))
