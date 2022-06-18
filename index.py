from tkinter import *
from tkinter import ttk

# ----- This database is only for admin users -----
admin = {1: {"username": "raniemx", "password": "ewan310", "name": "Ranie C. Sarmiento Jr."}}

# ----- Product, Basket, and cashiering Lists -----
products = {1: {"Description": "Coca Cola 1Lt.", "Price": 60, "product_number": "1103"}}

# ----- This function opens up the POS system when triggered -----
def cashiering():

    # ----- This function is an admin privilege. it lets the user add/remove products from the dictionary -----
    def add_remove_products():

        # ---- This function lets you add a new product to the 'products' dictionary -----
        def add_product():

            counter = 2
            def enter_key():
                 product_number = product_number_entry.get()
                 product_description = product_description_entry.get()
                 product_price = int(product_price_entry.get())
                 products[counter] = {"Description": product_description, "Price": product_price,
                                                   "product_number": product_number}


            def enter_checker():
                global n
                n = 1
                enter_key()

                print(products)

            product_form = Toplevel()
            spacer_lbl = Label(product_form)
            product_number_lbl = Label(product_form, text="Product Number: ")
            product_number_entry = Entry(product_form)
            product_description_lbl = Label(product_form, text="Description: ")
            product_description_entry = Entry(product_form)
            product_price_lbl = Label(product_form, text="Price: ")
            product_price_entry = Entry(product_form)
            enter_product = Button(product_form, text="Enter Product", command= enter_key)
            exit_btn = Button(product_form, text="Exit", command=exit)

            counter += 1


            spacer_lbl.grid(row=1, column=1, columnspan=2)
            product_number_lbl.grid(row=2, column=1)
            product_number_entry.grid(row=2, column=2)
            product_description_lbl.grid(row=3, column=1)
            product_description_entry.grid(row=3, column=2, columnspan=2)
            product_price_lbl.grid(row=5, column=1)
            product_price_entry.grid(row=5, column=2)
            enter_product.grid(row=6, column=1)
            exit_btn.grid(row=6, column=2)

        product_edit = Toplevel()
        frame = Frame(product_edit)
        spacer_lbl = Label(frame, text="Add/Remove Products", font='Arial 20 bold',padx=30, pady=30 )
        add_remove_lbl = Label(frame, text='Products: ')
        add_product = Button(frame, text="Add Product", command=add_product)
        # ----- Multi Listbox -----
        products_list = ttk.Treeview(product_edit)

        # ----- Define Columns -----
        products_list['columns'] = ("ID", "product", "Price")

        # ----- Format Columns -----
        products_list.column("#0", width=0, stretch=NO)
        products_list.column("ID", anchor=W, width=120)
        products_list.column("product", anchor=CENTER, width=200)
        products_list.column("Price", anchor=W, width=80)

        # ---- Column Headings -----
        products_list.heading("#0", text="", anchor=W)
        products_list.heading("ID", text="Product ID", anchor=W)
        products_list.heading("product", text="Product Description", anchor=W)
        products_list.heading("Price", text="Price", anchor=W)

        # ----- Add Data -----
        count = 1
        for record in products:
            products_list.insert(parent='', index='end', iid=count, text="",
                                 values=(products[count]["product_number"], products[count]["Description"], products[count]["Price"]))
            count += 1
        # products_list.insert(parent='', index='end', iid=0, text="",
        #                      values=(products["coke"]["product_number"], products["coke"]["Description"], products["coke"]["Price"]))

        spacer_lbl.grid(row=1, column=1, columnspan=2)
        add_remove_lbl.grid(row=2, column=1)
        add_product.grid(row=3, column=1)
        frame.pack(side=TOP)
        products_list.pack(pady=20)


    cashiering = Toplevel()
    cashiering.title("Rocket Basket Client")
    cashiering.geometry('1350x750+0+0')
    admin_menu = Menu(cashiering)
    cashiering.config(menu=admin_menu)
    # ----- Menu items -----
    file_menu = Menu(admin_menu)
    admin_menu.add_cascade(label="Product options", menu=file_menu)
    file_menu.add_command(label="Add/Remove Products", command=add_remove_products)
    file_menu.add_command(label="exit", command=cashiering.quit)

    title_lbl = Label(cashiering, text="Rocket Basket v1.0", bg='black', fg='green', font="Phaser")
    frame_one = Frame(cashiering)
    greeting = "Welcome, %s" % (admin[1]["name"])
    user_lbl = Label(frame_one, text=greeting)
    txt_input = Entry(frame_one)

    title_lbl.pack(fill=X)
    user_lbl.grid(row=3)
    txt_input.grid(row=4)
    frame_one.pack()

def error():
    error = Toplevel()
    login_error = Label(error, text="Incorrect Username/Password!", fg='red', padx=10, pady=5)
    login_error.pack()

# ----- This is the prototype Login System -----
def admin_login():

    def admin_enter():
        username = admin_username.get()
        password = admin_password.get()
        if username == admin[1]["username"]:
            if password == admin[1]["password"]:
                cashiering()
            else:
                error()
        else:
            error()

    admin_log = Toplevel()
    admin_title = Label(admin_log, text="Admin Login: ")
    user_lbl = Label(admin_log, text="Username: ")
    admin_username = Entry(admin_log)
    pw_lbl = Label(admin_log, text="Password: ")
    admin_password = Entry(admin_log)
    spacer_lbl = Label(admin_log)
    login_btn = Button(admin_log, text="Log In", command=admin_enter, bd=3, padx=5, pady=2)

    admin_title.grid(row=1, column=1, columnspan=2)
    user_lbl.grid(row=2, column=1)
    admin_username.grid(row=2, column=2)
    pw_lbl.grid(row=3, column=1)
    admin_password.grid(row=3, column=2)
    spacer_lbl.grid(row=4)
    login_btn.grid(row=5, column=1, columnspan=2)



root = Tk()
root.title('POS system')
root.geometry('1350x750+0+0')

# ----- This is the first window. It gives the option to login either as admin or regular user -----
title_lbl = Label(root, text='Rocket Basket POS', pady=20, font="Arial")
login_frame = Frame(root, bd=1, relief="solid", width=20, height=5, padx=20, pady=20 )
login_lbl = Label(login_frame, text='Rocket Basket POS', font='Arial 20 bold',padx=30, pady=30)
admin_btn = Button(login_frame, text="Login as Admin", font='Arial 10 bold', command=admin_login,width=20, height=5)
spacer_lbl = Label(login_frame, padx=10)
regular_btn = Button(login_frame,text="Login as Regular user", font='Arial 10 bold', width=20, height=5)

login_lbl.grid(row=1, column=1, columnspan=3,)
admin_btn.grid(row=2, column=1)
spacer_lbl.grid(row=2, column=2)
regular_btn.grid(row=2, column=3)

title_lbl.pack()
login_frame.pack()

root.mainloop()