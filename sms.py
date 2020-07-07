import requests   
import json
from tkinter import * 
from tkinter.messagebox import showinfo, showerror

#-------------- This function is for access your ac from "Fast2sms" sms to send message--------------------------

def send_sms(number,message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params ={
        'authorization':'Pc1ltzvYTQFXuANqmbaModI40pGV5i8wH7DL3rUK2nhEBfJjW6Z4FpM6lqBkxPGDnEu3goticybLaO2Q',
        'sender_id':'FSTSMS',
        'message':message,
        'language':'english',
        'route':'p',
        'numbers':number
    } 

    response = requests.get(url, params=params)
    dict = response.json()
    print(dict) 
    return dict.get('return')

#-------------- This function is use for active button to send message--------------------------

def btn_click():
    num = tnum.get()
    msg = s_msg.get("1.0",END)
    r= send_sms(num,msg)
    if r:
        showinfo("Send Success","Successfully Send")
    else:
        showerror("Error","Message not send")


#-------------- This is use for create GUI window to send message--------------------------

root = Tk( )
root.title("Message Sender")  # Title of the Gui window
root.geometry("400x550")  # Size of Gui window
f = ("Algerian",28,"bold")  # It is use for Text size & font  

tnum = Entry(root,font = f)   # It is use for number entry box 
tnum.pack(fill=X,pady=20)

s_msg= Text(root)            # It is use for message entry box 
s_msg.pack(fill=X)

btn = Button(root,text="SEND SMS",command = btn_click)
btn.pack()

root.mainloop()


