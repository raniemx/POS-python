from tkinter import *
from tkinter.font import Font
from tkinter import ttk
import json

root = Tk()
root.title("Rocket Basket POS")
root.geometry('1000x500')

basket = []

def cashiering():
    with open('scratch_5.json', 'r') as f:
        login_data = json.load(f)
        fullname = "USER: %s" % (login_data[login_count]['name'])
    # ===== WORK IN PROGRESS =====
    def products_list():
        def products_list_refresh():
            with open("scratch_5_products.json", 'r') as f:
                products = json.load(f)
            products_edit.delete(*products_edit.get_children())
            refresh_items = 0
            for listings in products:
                products_edit.insert(parent='', index='end', iid=refresh_items, text="", values=(
                products[refresh_items]["product_ID"], products[refresh_items]["product_name"],
                products[refresh_items]["price_entry"]))
                refresh_items += 1

        def add():
            def save_product():
                with open('scratch_5_products.json', 'r') as f:
                    add_data = json.load(f)
                product_ID = product_ID_entry.get()
                product_name = product_name_entry.get()
                product_price_entry = price_entry.get()
                add_data.append(
                    {'product_ID': product_ID, 'product_name': product_name, 'price_entry': product_price_entry})
                with open('scratch_5_products.json', 'w') as f:
                    json.dump(add_data, f, indent=1)
                products_list_refresh()
                item_form.destroy()

            item_form = Toplevel()
            item_form.title('Item Form')

            product_ID_lbl = Label(item_form, text='Product ID: ')
            product_ID_entry = Entry(item_form)
            product_name_lbl = Label(item_form, text='Product Name: ')
            product_name_entry = Entry(item_form)
            product_price_lbl = Label(item_form, text='Product Price: ')
            price_entry = Entry(item_form)
            save_products = Button(item_form, text='save', command=save_product)

            product_ID_lbl.grid(row=1, column=1)
            product_ID_entry.grid(row=1, column=2)
            product_name_lbl.grid(row=2, column=1)
            product_name_entry.grid(row=2, column=2)
            product_price_lbl.grid(row=3, column=1)
            price_entry.grid(row=3, column=2)
            save_products.grid(row=4, column=2)

        def remove_product():
            with open("scratch_5_products.json", "r") as p:
                products = json.load(p)
                items_list = int(products_edit.selection()[0])
                del products[items_list]
            with open("scratch_5_products.json", "w") as p:
                json.dump(products, p, indent=1)
            products_list_refresh()

        with open("scratch_5_products.json", 'r') as f:
            products = json.load(f)
        products_window = Toplevel()
        products_window.title("Add/Remove Products")

        products_title = Label(products_window, text="Products", font="Arial 20 bold", pady=20, padx=20)
        list_frame = Frame(products_window)
        products_edit = ttk.Treeview(list_frame)

        products_edit['columns'] = ("ID", "Product", "Price")

        products_edit.column("#0", width=0, stretch=NO)
        products_edit.column("ID", anchor=W, width=120)
        products_edit.column("Product", anchor=W, width=200)
        products_edit.column("Price", anchor=W, width=80)

        products_edit.heading("#0", text="Label", anchor=W)
        products_edit.heading("ID", text="ID", anchor=W)
        products_edit.heading("Product", text="Product", anchor=W)
        products_edit.heading("Price", text="Price", anchor=W)

        counter = 0
        for items in products:
            products_edit.insert(parent='', index='end', iid=counter, text="",
                                 values=(products[counter]["product_ID"], products[counter]["product_name"],
                                         products[counter]["price_entry"]))
            counter += 1

        buttons_frame = Frame(products_window)
        add_item = Button(buttons_frame, text="Add an Item", command=add, padx=20, pady=10)
        button_spacer = Label(buttons_frame)
        remove_item = Button(buttons_frame, text="Remove an Item", command=remove_product, padx=20, pady=10)

        products_title.pack(side=TOP, anchor=CENTER)

        add_item.grid(row=1, column=1)
        button_spacer.grid(row=1, column=2)
        remove_item.grid(row=1, column=3)
        buttons_frame.pack(pady=10, padx=10)

        products_edit.grid(row=1, column=1, columnspan=10)
        list_frame.pack(pady=10, padx=10)

    def user_list():

        def users_refresh():
            with open("scratch_5.json", 'r') as f:
                user_data = json.load(f)
            users.delete(*users.get_children())
            refresh_items = 0
            for listings in user_data:
                users.insert(parent='', index='end', iid=refresh_items, text="", values=(
                user_data[refresh_items]["username"], user_data[refresh_items]["password"]))
                refresh_items += 1

        def user_add():

            def register_user():
                with open("scratch_5.json", "r") as f:
                    user_data = json.load(f)
                uname = uname_entry.get()
                password = pw_entry.get()
                full_name = full_name_entry.get()
                user_data.append({"username": uname, "password": password, "name": full_name})
                with open("scratch_5.json", "w") as f:
                    json.dump(user_data, f, indent=1)
                users_refresh()

            user_form = Toplevel()
            user_form.title("User Registration")

            users_frame = Frame(user_form)

            uname_label = Label(users_frame, text="Username:")
            uname_entry = Entry(users_frame)
            password_label = Label(users_frame, text="Password:")
            pw_entry = Entry(users_frame)
            full_name_label = Label(users_frame, text="Full Name:")
            full_name_entry = Entry(users_frame)
            register = Button(users_frame, text="Register User", command=register_user)

            uname_label.grid(row=1, column=1)
            uname_entry.grid(row=1, column=2)
            password_label.grid(row=2, column=1)
            pw_entry.grid(row=2, column=2)
            full_name_label.grid(row=3, column=1)
            full_name_entry.grid(row=3, column=2)
            register.grid(row=4, column=1, columnspan=2)
            users_frame.pack(padx=10, pady=10)

        def user_delete():
            with open("scratch_5.json", "r") as d:
                user_data = json.load(d)
            delete_user = int(users.selection()[0])
            del user_data[delete_user]
            with open("scratch_5.json", "w") as d:
                json.dump(user_data, d, indent=1)
            users_refresh()

        with open("scratch_5.json", "r") as u:
            user_data = json.load(u)

        users_window = Toplevel()
        users_window.title("User settings")

        users_heading = Label(users_window, text="User List", font="Arial 20 bold", pady=20)
        buttons_frame = Frame(users_window)
        add_user = Button(buttons_frame, text="Add User", command=user_add)
        button_spacer = Label(buttons_frame)
        remove_user = Button(buttons_frame, text="Remove User", command=user_delete)

        users_frame = Frame(users_window)
        users = ttk.Treeview(users_frame)

        users['columns'] = ("Username", "Name")

        users.column("#0", width=0, stretch=NO)
        users.column("Username", anchor=W, width=120)
        users.column("Name", anchor=W, width=200)

        users.heading("#0", text="Label", anchor=W)
        users.heading("Username", text="ID", anchor=W)
        users.heading("Name", text="Product", anchor=W)

        user_count = 0
        for user_records in user_data:
            users.insert(parent='', index='end', iid=user_count, text="",
                                 values=(user_data[user_count]["username"], user_data[user_count]["name"]))
            user_count += 1

        users_heading.pack(anchor=CENTER)
        add_user.grid(row=1, column=1)
        button_spacer.grid(row=1, column=2)
        remove_user.grid(row=1, column=3)
        buttons_frame.pack()
        users.grid(row=1, column=1)
        users_frame.pack(padx=10, pady=10)

    def refresh():
        basket_listbox.delete(*basket_listbox.get_children())
        refresh_count = 0
        for items in basket:
            basket_listbox.insert(parent='', index='end', iid=refresh_count, text="", values=(
                basket[refresh_count]["product_ID"], basket[refresh_count]["product_name"], basket[refresh_count]["price_entry"]))
            refresh_count += 1

    def add_cart():
        with open('scratch_5_products.json', 'r') as f:
            products = json.load(f)
            basket_entry = item_entry.get()
        count = 0
        for i in products:
            if basket_entry == products[count]['product_name']:
                basket.append({'product_ID': products[count]['product_ID'], 'product_name': products[count]['product_name'],
                               'price_entry': products[count]['price_entry']})
            else:
                pass
            count += 1
        item_entry.delete(0, END)
        print(basket)
        refresh()

    def remove_cart():
        delete_items = int(basket_listbox.selection()[0])
        del basket[delete_items]
        print(basket)
        refresh()

    def Checkout():
        total_data = []
        count=0
        for i in basket:
            total_data.append(int(basket[count]['price_entry']))
            count += 1
        total_value = sum(total_data)
        Total_Label.config(text=total_value)
    def insufficient():
        insufficient_amount = Toplevel()
        insufficient_amount_text = Label(insufficient_amount, text="Insufficient amount!", fg='red',
                                         font='Arial 10 bold', padx=10, pady=10)
        insufficient_amount_text.pack()
    def print_receipt():
        payment_raw = Payment_Entry.get()
        payment_value = int(payment_raw)
        if payment_value < total_value:
            Change_Value.config(text="")
            insufficient()
        else:
            cashier = login_data[login_count]['name']
            count = 0
            asterisk = '***************************'
            change = payment_value - total_value
            total_space = len(str(total_value))
            change_space = len(str(change))
            total_replace = '                         '
            space_replace = '                        '
            spacer_total = total_replace.replace(total_replace[:total_space], '', 2)
            spacer_space = total_replace.replace(space_replace[:change_space], '', 3)
            print("===============================\n"
                  "       ROCKET BASKET POS       \n"
                  "===============================\n"
                  "CASHIER:", cashier, "\n"
                                       "===============================\n"
                                       "             Items             \n"
                                       " ")
            for i in basket:
                char_number = len(basket[count]['product_name'])
                replace = asterisk.replace(asterisk[:char_number], '', 1)
                print(basket[count]['product_name'], replace, basket[count]['price_entry'])
                count += 1
            print(" \n"
                  "===============================\n"
                  "Total:", spacer_total, total_value, "\n"
                                                       "Change:", spacer_space, change)
            basket_listbox.delete(*basket_listbox.get_children())
            basket.clear()
            Payment_Entry.delete(0, END)




    def payment():
        total_data = []
        count = 0
        for i in basket:
            total_data.append(int(basket[count]['price_entry']))
            count += 1
        global total_value
        total_value = sum(total_data)
        payment_raw = Payment_Entry.get()
        payment_value = int(payment_raw)
        change = payment_value - total_value
        Change_Value.config(text=change)
        print_receipt()

    cashiering_window = Toplevel()
    cashiering_window.title('ROCKET BASKET POS SYSTEM v1.0')
    cashiering_window.geometry('1350x750')
    global Total_Label

    menu_bar = Menu(cashiering_window)
    cashiering_window.config(menu=menu_bar)

    file_menu = Menu(menu_bar)
    menu_bar.add_cascade(label="File",menu=file_menu)
    file_menu.add_command(label="Add/Remove Products", command=products_list)
    file_menu.add_command(label="Add/Remove Users", command=user_list)


    Header_Frame = Frame(cashiering_window, padx=200, pady=20)

    cashiering_welcome = Label(Header_Frame, text=fullname.upper(), font='Arial 20 bold', pady=20)

    cashiering_welcome.pack(side=TOP)
    Header_Frame.pack(side=TOP)
    spacer_1 = Frame(cashiering_window, padx=10)
    spacer = Label(spacer_1)
    spacer.pack()
    spacer_1.pack(side=LEFT)
    frame_one = Frame(cashiering_window, bd=1, relief='solid', padx=20, pady=20)

    basket_title = Label(frame_one, text='ITEMS IN BASKET', font='Arial 10 bold',pady=10)
    item_entry_label = Label(frame_one, text='Item: ', pady=10)
    item_entry = Entry(frame_one)
    add_button = Button(frame_one, text='add to cart', command=add_cart)
    remove_button = Button(frame_one, text='remove item', command=remove_cart)

    # Multi List Box
    basket_listbox = ttk.Treeview(frame_one)

    # Columns
    basket_listbox['columns'] = ('ID', 'product', 'price')

    # Format Columns
    basket_listbox.column("#0", width=0, stretch=NO)
    basket_listbox.column("ID", anchor=W, width=120)
    basket_listbox.column("product", anchor=CENTER, width=200)
    basket_listbox.column("price", anchor=W, width=80)

    # Column Headings
    basket_listbox.heading("#0", text="", anchor=W)
    basket_listbox.heading("ID", text="Product ID", anchor=W)
    basket_listbox.heading("product", text="Product Description", anchor=W)
    basket_listbox.heading("price", text="Price", anchor=W)

    # Add Data
    with open('scratch_5_products.json', 'r') as f:
        products = json.load(f)

    global listbox_count
    listbox_count = 0
    for records in basket:
        basket_listbox.insert(parent='', index='end', iid=listbox_count, text="", values=(
        basket[listbox_count]["product_ID"], basket[listbox_count]["product_name"], basket[listbox_count]["price_entry"]))
        listbox_count += 1

    spacer_2 = Label(frame_one, pady=10)
    Checkout = Button(frame_one, text='Check Out', command=Checkout, padx=30)

    basket_title.grid(row=1, column=1, columnspan=10)
    item_entry_label.grid(row=2, column=1)
    item_entry.grid(row=2, column=2)
    add_button.grid(row=2, column=3)
    remove_button.grid(row=2, column=4)
    basket_listbox.grid(row=3, column=1, columnspan=10)
    spacer_2.grid(row=4, column=1, columnspan=10)
    Checkout.grid(row=5, column=1, columnspan=10)
    frame_one.pack(side=LEFT, anchor=NW)
    frame_space_1 = Frame(cashiering_window)
    frame_spacer = Label(frame_space_1, padx=20)
    frame_spacer.pack()
    frame_space_1.pack(side=LEFT)
    frame_two = Frame(cashiering_window, bd=1, relief='solid', padx=20, pady=20)

    Total_title = Label(frame_two, text="Total: ", font='Arial 10 bold')
    Total_Label = Label(frame_two, font='Arial 10 bold')
    VAT_Text = Label(frame_two, text='VAT: ')
    VAT_Label = Label(frame_two, text="12%")
    Payment_Label = Label(frame_two, text='Payment: ')
    Payment_Entry = Entry(frame_two)
    payment_button_spacer = Label(frame_two, pady=2)
    Payment_Process = Button(frame_two, text='Process Payment', command=payment)
    payment_button_spacer2 = Label(frame_two, pady=2)
    Change_Label = Label(frame_two, text='Change: ')
    Change_Value = Label(frame_two)
    payment_button_spacer3 = Label(frame_two, pady=2)


    Total_title.grid(row=1, column=1)
    Total_Label.grid(row=1, column=2)
    VAT_Text.grid(row=2, column=1)
    VAT_Label.grid(row=2, column=2)
    Payment_Label.grid(row=3, column=1)
    Payment_Entry.grid(row=3, column=2)
    payment_button_spacer.grid(row=4, column=1, columnspan=2)
    Payment_Process.grid(row=5, column=1, columnspan=2)
    payment_button_spacer2.grid(row=6, column=1, columnspan=2)
    Change_Label.grid(row=7, column=1)
    Change_Value.grid(row=7, column=2)
    payment_button_spacer3.grid(row=8, column=1, columnspan=2)
    frame_two.pack(side=LEFT, anchor=NW)
def error():
    error = Toplevel()
    error_label = Label(error, text='Incorrect username/password!', font='Arial 10 bold', fg='red', padx=10, pady=10)
    error_label.pack()
def login():
    with open('scratch_5.json', 'r') as f:
        login_data = json.load(f)
    username = username_entry.get()
    password = password_entry.get()
    global login_count
    login_count = 0
    for i in login_data:
        if username == login_data[login_count]['username']:
            if password == login_data[login_count]['password']:
                cashiering()
                break
            else:
                error()
                login_count += 1
        else:
            login_count += 1



Frame_One = Frame(root)
Welcome_Label = Label(Frame_One, text='ROCKET BASKET POS SYSTEM', font='Arial 20 bold', padx=10, pady=50)

Welcome_SubLabel = Label(Frame_One, text='LOGIN AS:', font='Arial 10 bold', pady= 10)
Welcome_Label.pack(side=TOP, fill=X)
Welcome_SubLabel.pack(side=TOP, fill=X)

SubFrame = Frame(Frame_One, bd=1, relief='solid', padx=10, pady=10)

usr_label = Label(SubFrame, text="Username: ", pady=5)
username_entry = Entry(SubFrame)
pw_label = Label(SubFrame, text="Password: ", pady=5)
password_entry = Entry(SubFrame, show="*")
login_button = Button(SubFrame, text='Login', command=login)

usr_label.grid(row=1, column=1)
username_entry.grid(row=1, column=2)
pw_label.grid(row=2, column=1)
password_entry.grid(row=2, column=2)
login_button.grid(row=3, column=1, columnspan=2)
SubFrame.pack()

Frame_One.pack(side=TOP)

root.mainloop()




