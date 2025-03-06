from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    #----------- Used to copy password without Ctrl+C after generating ------------ #
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def adding():
    website = web_entry.get()
    user_name = user_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please make sure you haven't left any fields empty!")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail:{user_name}"
                           f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as datas:
                datas.write(f"{website} | {user_name} | {password}\n")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(130,100,image = pass_img)
canvas.grid(column=1,row=0)

web_label = Label(text="Website:")
web_label.grid(column = 0,row =1)

user_label =Label(text = "Email/Username:")
user_label.grid(column = 0,row =2)

pass_label =Label(text = "Password:")
pass_label.grid(column = 0,row =3)

web_entry = Entry(width=52)
web_entry.grid(column = 1,row = 1,columnspan = 2)
web_entry.focus()

user_entry = Entry(width=52)
user_entry.grid(column = 1,row = 2 ,columnspan =2)
user_entry.insert(0,"pycharm@gmail.com")

pass_entry = Entry(width = 34)
pass_entry.grid(row = 3 ,column = 1,columnspan =1)

generate_button = Button(text="Generate Password",bg="white",command=generate_password)
generate_button.grid(column=2,row = 3)

add_button = Button(text="Add",width=44,bg="white",command=adding)
add_button.grid(column = 1,row = 4,columnspan =2)



window.mainloop()