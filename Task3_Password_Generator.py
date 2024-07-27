from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import string
import random

root = Tk()
root.geometry("500x300")
root.title("Somya's Password Generator")
root.config(bg="light yellow")
root.resizable(FALSE, FALSE)

def password_generate():
   try:
         length_password = solidboss.get()
         small_letters = string.ascii_lowercase
         capital_letters = string.ascii_uppercase
         digits = string.digits
         special_character = string.punctuation
         all_list = []
         all_list.extend(list(small_letters))
         all_list.extend(list(capital_letters))
         all_list.extend(list(digits)) 
         all_list.extend(list(special_character)) 
         random.shuffle(all_list)
         password.set("".join(all_list[0:length_password]))
   except:     
          messagebox.askretrycancel("A Problem Has Been Occured", 
                                    "please try again after sometime")

all_no={"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6",
        "7":"7","8":"8","9":"9","10":"10","11":"11",
        "12":"12","13":"13","14":"14","15":"15"}

Title = Label(root, text="Somya's Password Generator",bg="light pink",
              fg="black",font=("futura" , 15 , "bold"))
Title.pack(anchor="center", pady="20px")

length= Label(root, text="Select the Length of Your Password :-",
              fg = "black", bg="light blue" , font=("ubuntu", 12 ,"bold"))
length.place(x="20px", y="70px")

def on_enter(e):
    generate_btn['bg'] = "grey"
    generate_btn['fg'] = "white"

def on_leave(e):
    generate_btn['bg'] = "purple"
    generate_btn['fg'] = "black"

solidboss = IntVar()
Selector = ttk.Combobox (root, textvariable=solidboss, state="readonly")
Selector['values'] = [ l for l in all_no.keys()]
Selector.current(7)
Selector.place(x="250px", y="71px")

generate_btn = Button(root, text="Generate Password", bg="purple",
                      fg="black", font=("ubuntu", 12 , "bold"), cursor="hand2",
                      command= password_generate)
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)
generate_btn.pack(anchor="center",pady="50px")

result_lable = Label(root, text="Generate Password Here :-", bg="light blue",
                      fg="black", font=("ubuntu", 12 , "bold"))
result_lable.place(x="20px", y="170px")

password = StringVar()
password_final = Entry(root, textvariable = password , 
                       state="readonly" , fg="black", font=("ubuntu" , 15))
password_final.place(x="200px" , y="170px")

root.mainloop()