from tkinter import *
print("************ Programmed by ***********")
print("******* Carla Jeanne B. Golena *******")
print("************** BSCOE 1-3 *************\n\n\n")

root = Tk()
root.title("Restaurant Bill")
root.geometry("460x400")

def add():
    if quantity.get() != "" and menu.get() != "" and price.get() != "":
        quantitylist.insert(END, quantity.get())
        menulist.insert(END, menu.get())
        pricelist.insert(END, float(price.get()) * int(quantity.get()))
        quantity.set("")
        menu.set("")
        price.set("")


totalText = StringVar

def calculate_total():
    total = 0.0
    for i in range(quantitylist.size()):
        totalprice = float(pricelist.get(i))
        total += totalprice
    totalText.set("$" + str(total))


# Labels

quantitylabel = Label(root, text="Quantity: ")
quantitylabel.place(x=10, y=20)
menulabel = Label(root, text="Menu Item: ")
menulabel.place(x=10, y=50)
pricelabel = Label(root, text="Price ")
pricelabel.place(x=10, y=80)

totallabel = Label(root, text="Total Cost:", font=("Arial", 12))
totallabel.place(x=250, y=350)

totalText = StringVar()
totalText.set("$0.00")

pricetotal = Label(root, textvariable=totalText, font=("Calibri", 12), bd=2)
pricetotal.place(x=350, y=350)

quantity = StringVar()
menu = StringVar()
price = StringVar()

# Entry
quantityentry = Entry(root, textvariable=quantity)
quantityentry.place(x=150, y=20)
menuentry = Entry(root, textvariable=menu)
menuentry.place(x=150, y=50)
priceentry = Entry(root, textvariable=price)
priceentry.place(x=150, y=80)

# Buttons
additembtn = Button(root, text="Add Item", command=add)
additembtn.place(x=350, y=20)
totalbillbtn = Button(root, text="Total Bill", command=calculate_total)
totalbillbtn.place(x=350, y=50)

# Listbox
label1 = Label(root, text="Quantity")
label1.place(x=35, y=130)
label2 = Label(root, text="Menu Item")
label2.place(x=190, y=130)
label3 = Label(root, text="Price")
label3.place(x=380, y=130)

quantitylist = Listbox(root, height=10, width=15, selectmode=MULTIPLE)
quantitylist.place(x=10, y=150)
menulist = Listbox(root, height=10, width=30, selectmode=MULTIPLE)
menulist.place(x=130, y=150)
pricelist = Listbox(root, height=10, width=15, selectmode=MULTIPLE)
pricelist.place(x=350, y=150)

root.mainloop()