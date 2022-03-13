from tkinter import *
from tkinter import messagebox

from db import Database

def add_item():
    if part_text.get() == "" or customer_text.get() == "" or retailer_text.get() == "" or price_text.get() == "":
        messagebox.showerror("Required Fields", "Please Fill all the Text Fields!!!")
        return
    db.insert(part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    populate_list()
    clear()

def select_item(event):
    # print("select")
    try:
        clear()
        global selected_item
        index = list_items.curselection()[0]
        selected_item = list_items.get(index)
        
        part_entry.insert(0, selected_item[1])
        customer_entry.insert(0, selected_item[2])
        retailer_entry.insert(0, selected_item[3])
        price_entry.insert(0, selected_item[4])
    except IndexError:
        pass

def update_item():
    if part_text.get() == "" or customer_text.get() == "" or retailer_text.get() == "" or price_text.get() == "":
        messagebox.showerror("Required Fields", "Updation requires all the fields!!!")
        return
    
    db.update(selected_item[0], part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())
    populate_list()

def delete_item():
    if selected_item != "":
        db.remove(selected_item[0])
        populate_list()
        clear()

def clear():
    part_entry.delete(0,END)
    customer_entry.delete(0, END)
    retailer_entry.delete(0, END)
    price_entry.delete(0, END)

def populate_list():
    print("Populate")
    list_items.delete(0, END)
    for row in db.fetch():
        list_items.insert(END, row)


if __name__ == "__main__":
    root = Tk()
    root.title("Parts Manager")
    root.geometry("700x350")

    # DB Initialization
    db = Database("store.db")

    # Parts Controls
    part_text = StringVar()
    part_label = Label(root, text="Part Name", font=("bold", 10), pady=20)
    part_label.grid(row=0, column=0, sticky=W, padx=10)
    part_entry = Entry(root, textvariable=part_text)
    part_entry.grid(row=0, column=1)

    # Customer Controls
    customer_text = StringVar()
    customer_label = Label(root, text="Customer", font=("bold", 10))
    customer_label.grid(row=0, column=2, sticky=W, padx=10)
    customer_entry = Entry(root, textvariable=customer_text)
    customer_entry.grid(row=0, column=3)

    # Retailer Controls
    retailer_text = StringVar()
    retailer_label = Label(root, text="Retailer", font=("bold", 10), pady=20)
    retailer_label.grid(row=1, column=0, sticky=W, padx=10)
    retailer_entry = Entry(root, textvariable=retailer_text)
    retailer_entry.grid(row=1, column=1)

    # Price Controls
    price_text = StringVar()
    price_label = Label(root, text="Price", font=("bold", 10))
    price_label.grid(row=1, column=2, sticky=W, padx=10)
    price_entry = Entry(root, textvariable=price_text)
    price_entry.grid(row=1, column=3)

    # Listbox Control
    list_items = Listbox(root, height=8, width=50, border=0)
    list_items.grid(row=3, column=0, columnspan=3, rowspan=8, padx=10)

    # Binding Listbox to Selection
    list_items.bind("<<ListboxSelect>>", select_item)

    # Scrollbar
    scrollbar = Scrollbar(root)
    scrollbar.grid(row=3, column=3)

    # Configuring Listbox with Scrollbar
    # list_items.configure(yscrollcommand=scrollbar.get)
    scrollbar.configure(command=list_items.yview)

    add_btn = Button(root, text="Add Part", width=12, command=add_item)
    add_btn.grid(row=2, column=0, pady=10)

    upd_btn = Button(root, text="Update Part", width=12, command=update_item)
    upd_btn.grid(row=2, column=1, pady=10)

    del_btn = Button(root, text="Delete Part", width=12, command=delete_item)
    del_btn.grid(row=2, column=2, pady=10)

    clr_btn = Button(root, text="Clear", width=12, command=clear)
    clr_btn.grid(row=2, column=3, pady=10)

    # Populate List
    populate_list()

    root.mainloop()
