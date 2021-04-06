from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.title("Chat_Bot")
root.iconbitmap(r'C:\Program_VS\Python_Program\Tkinter\55.ico')



chatbot = ChatBot('bot')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')


def send():
    send = "You -> " + e.get()
    if (e.get() == "exit"):
        quit()
    txt.insert(END, "\n\n" + send)
    query = e.get()
    query = str(query)
    responce = (chatbot.get_response(query))
    responce = str(responce)
    responce = ("Bot -> "+responce)
    txt.insert(END, "\n" + responce)
    with open("record.txt","a")as f:
        f.write(f"{ send,responce}\n\n")
    e.delete(0, END)





def Help():
    tmsg.showinfo("Help","Plese contact 1234567890 for more Information ")





def rate():
    value=tmsg.askquestion("Experience...","You used this GUI...was your experience Good ? ")
    if value=="yes":
        msg="Great ... Rate us on appstore and Help us "
    else :
        msg = "SORRY ... we will try to improve it "
    tmsg.showinfo("Experience",msg)




mainmenu= Menu (root)
m1 = Menu (mainmenu,tearoff=0)
m1.add_command(label ="Do you want Help....",command = Help)
m1.add_command(label ="Rate us",command = rate)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=m1)



m3 = Menu (mainmenu,tearoff=0)
m3.add_command(label ="Yes",command = quit)
m3.add_command(label ="No")
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Exit",menu=m3)




# Label(root,text="hi").grid(row=0,column=0,columnspan=2)
txt = Text(root, bg="#FFDDDD", borderwidth=5, relief=SUNKEN)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100, bg="#E6F6FF", borderwidth=5, relief=SUNKEN)
e.grid(row=1, column=0)
send = Button(root, text="Send", command=send, bg="#add8e6",
              borderwidth=5, relief=SUNKEN).grid(row=1, column=1)

root.mainloop()