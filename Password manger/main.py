from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,END)
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','s','u','v','x','z','y','q','w',
               'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','T','S','U','V','X','Z','Y','Q','W']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols= ['!','@','#','$','%','^','&','*',')','(' ]

    password_list =[random.choice(letters) for char in range(random.randint(8,10))]
    password_list += [random.choice(numbers) for num in range(random.randint(2,4))]
    password_list += [random.choice(symbols) for sym in range(random.randint(2,4))]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email= user_name_entry.get()
    password= password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }
    if len(website) == 0 or len(password) == 0 :
        messagebox.showinfo(title="Oops",message="Please make sure you havent left any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
#------------------------------Find Password-------------------------------------#
def search():
    website = website_entry.get()
    email = user_name_entry.get()
    if len(website) == 0 :
        messagebox.showinfo(title="Oops",message="Please enter a website!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title= "Error",message="No Data File Was Found")
        else:
            if website in data:
                messagebox.showinfo(title="Match", message=f"Email {data[website]["email"]} \nPassword: {data[website]["password"]}")
            else:
                messagebox.showinfo(title="No match", message=f"No password available")

# ---------------------------- UI SETUP ------------------------------- #
screen =  Tk()
screen.title("Password Manger")
screen.config(padx=20,pady=20)
canvas = Canvas(height=200,width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100 ,image=logo_image)
canvas.grid(column=1,row =0 )
#Lables
website = Label(text="Website:")
user_name_label = Label(text="Email/Username:")
password_label = Label(text= "Passowrd:")
website.grid(column = 0,row =1)
user_name_label.grid(column =0,row =2 )
password_label.grid(column=0,row=3)

#Entries
website_entry= Entry(width=21)
website_entry.focus()
user_name_entry= Entry(width=40)
password_entry = Entry(width=21)
website_entry.grid(row=1,column=1)
user_name_entry.grid(row=2,column=1,columnspan=2 )
user_name_entry.insert(0,"pelegbs8@gmail.com")
password_entry.grid(row=3,column=1)
#Buttons
search_button = Button(text="Search Password",width=25,command=search)
search_button.grid(column=2,row=1,sticky="w")
generate_pass = Button(text="Generate Password ",width=25,command=generate_password)
generate_pass.grid(column=2,row=3)
add= Button(text="Add" ,width=20 ,command=save)
add.grid(column=1,row=4,columnspan=2)

screen.mainloop()
