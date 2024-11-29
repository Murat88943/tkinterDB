import tkinter as tk
from tkinter import messagebox
import psycopg2
from Config import host, user, passwordDATA, db_name, port
def Share():
    name = EnterText.get()
    password = EnterText1.get()
    contact = EnterText2.get()

    EnterText.delete(0, 'end')
    EnterText1.delete(0, 'end')
    EnterText2.delete(0, 'end')
    Code.delete(0, 'end')


    connection = psycopg2.connect(user=user,
                                  password=passwordDATA,
                                  host=host,
                                  port=port,
                                  database=db_name)

    cursor = connection.cursor()

    sql = f"INSERT INTO users(name, password, contact) VALUES('{name}','{password}','{contact}')"
    cursor.execute(sql)

    connection.commit()

    cursor.close()
    connection.close()

root = tk.Tk ()

root.resizable(width= False, height= False)
root.title("registration")
root.geometry('700x400')
root['bg'] = "white"

text = tk.Label(root, text = "Name", font=('Arial Bold', 20), fg = "black",bg = "white")
text.place(x = 295, y = 25)

EnterText = tk.Entry(fg="black", width = 47)
EnterText.place(x = 195, y = 75)

text1 = tk.Label(root, text = "Password", font=('Arial Bold', 20), fg = "black",bg = "white")
text1.place(x = 275, y = 125)

EnterText1 = tk.Entry(fg="black", width=47)
EnterText1.place(x = 195, y = 175)

text2 = tk.Label(root, text = "Contact", font=('Arial Bold', 20), fg = "black",bg = "white")
text2.place(x = 285, y = 225)


EnterText2 = tk.Entry(fg="black", width=47)
EnterText2.place(x = 195, y = 275)


Share = tk.Button(width = 27, text = "send a request", fg = "white", bg = "black", command = Share)
Share.place(x = 240, y = 335)

text2 = tk.Label(root, text = "Code", font=('Arial Bold', 20), fg = "black",bg = "white")
text2.place(x = 525, y = 300)

Code = tk.Entry(fg="black", width=20)  #CMLJG837DOMJKL
Code.place(x = 500, y = 340)

root.mainloop()
