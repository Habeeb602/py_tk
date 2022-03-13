from fnmatch import fnmatch
from tkinter import *
from PIL import Image, ImageTk
import sqlite3

def submit():
    conn = sqlite3.connect("address_book.db")
    cur = conn.cursor()
    

    cur.execute(f"""
    
    INSERT INTO addresses VALUES 
    {f_name.get()}, 
    {l_name.get()}, 
    {address.get()}, 
    {city.get()}, 
    {state.get()}, 
    {zipcode.get()},
    {phone.get()}
    
    """)

    conn.commit()
    conn.close()

    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)
    phone.delete(0,END)


if __name__ == "__main__":
    root = Tk()
    root.title("Address-Book App")
    root.geometry("680x420+650+275")

    # Creating the Database OR Connecting to an existing one.

    # Creating a Cursor (Through which we execute SQL)
    
    # Creating the table

    # cur.execute("""
    #         CREATE TABLE addresses (
    #             first_name text,
    #             last_name text,
    #             address text,
    #             city text,
    #             state text, 
    #             zipcode integer
    #         )
    # """)

    # Creating Labels
    f_name_lbl = Label(root, text="First name")
    f_name_lbl.grid(row=0, column=0, ipadx=130)

    l_name_lbl = Label(root, text="Last name")
    l_name_lbl.grid(row=1, column=0)

    address_lbl = Label(root, text="Address")
    address_lbl.grid(row=2, column=0)

    city_lbl = Label(root, text="City")
    city_lbl.grid(row=3, column=0)

    state_lbl = Label(root, text="State")
    state_lbl.grid(row=4, column=0)

    zipcode_lbl = Label(root, text="Zipcode")
    zipcode_lbl.grid(row=5, column=0)

    phone_lbl = Label(root, text="Phone No.")
    phone_lbl.grid(row=6, column=0)

    # Creating Text-Boxes (Entry box)
    f_name = Entry(root, width=25)
    f_name.grid(row=0, column=1)

    l_name = Entry(root, width=25)
    l_name.grid(row=1, column=1)

    address = Entry(root, width=25)
    address.grid(row=2, column=1)

    city = Entry(root, width=25)
    city.grid(row=3, column=1)

    state = Entry(root, width=25)
    state.grid(row=4, column=1)
    
    zipcode = Entry(root, width=25)
    zipcode.grid(row=5, column=1)
    
    phone = Entry(root, width=25)
    phone.grid(row=6, column=1)
    
    # Creating Button

    submit_btn = Button(root, text="Add Record", command=submit, padx=60)
    submit_btn.grid(row=7, column=0, columnspan=2, pady=20)








    root.mainloop()