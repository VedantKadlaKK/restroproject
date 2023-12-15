import tkinter
from functools import partial
import tkinter.font
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

total_amount = 0
snack_amount = 0
beve_amount = 0
food_amount = 0
sgst_amount = 0
cgst_amount = 0
gst_amount = 0
final_amount = 0


def order1():
    if entryC.get() == '':
        messagebox.showwarning("Warning", "Please\nAdd Details")
    if entryA.get() == '':
        messagebox.showwarning("Warning", "Please\nAdd Details")
    else:
        frame1.pack_forget()
        frame2.pack_forget()
        frame3.pack()


def adddate1():
    date_1 = entryB.get()
    if entryB.get() == '':
        messagebox.showwarning("Warning", "Date Not Added \n Please Add Date")
    else:
        datafile = open('TableOrder.txt', 'a')
        datafile.write('\n' + 'TAKE OUT' + '\n ' + 'Date     :   ' + date_1 + '\n')
        datafile.close()
        label4_111.configure(text='Date : ' + date_1)


def adddate2():
    date_2 = entryC.get()
    if entryC.get() == '':
        messagebox.showwarning("Warning", "Date Not Added\nPlease Add Date")
    else:
        datafile = open('TableOrder.txt', 'a')
        datafile.write('\n' + 'DINE IN' + '\n ' + 'Date     :   ' + date_2 + '\n')
        datafile.close()
        label4_121.configure(text='Date : ' + date_2)


def resetdate():
    label4_111.configure(text=' ENTER DATE ')
    entryB.delete(0, END)
    label4_121.configure(text=' ENTER DATE ')
    entryC.delete(0, END)


def addtable():
    table_1 = entryA.get()
    if entryA.get() == '':
        messagebox.showwarning("Warning", "Table not Added\nPlease Add ")
    else:
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Customer     :   ' + table_1 + '\n')
        datafile.close()
        label5.configure(text='\nHello ' + table_1 + '\n...')


def addphnumber():
    phone_1 = entryA11.get()
    name_9 = entryA9.get()
    if entryA11.get() == '':
        messagebox.showwarning("Warning", "Phone Number\nNot Added\nPlease Add ")
    else:
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Customer Phone : ' + phone_1 + '\n')
        datafile.close()
        label31.configure(text='\nPhone Added ' + phone_1)

    if entryA9.get() == '':
        messagebox.showwarning("Warning", "Name\nNot Added\nPlease Add ")
    else:
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Customer Name : ' + name_9 + '\n')
        datafile.close()
        label31a.configure(text='\nName Added ' + name_9)


def dinein1():
    frame1.pack_forget()
    frame2.pack()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame8.pack_forget()


def takeout1():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame8.pack()


def goback1():
    frame1.pack()
    frame2.pack_forget()
    frame3.pack_forget()


def goback2():
    frame1.pack()
    frame3.pack_forget()
    frame2.pack_forget()


def snacks():
    main_window.configure(bg='#FFB6C1')

    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack()


def goback3():
    main_window.configure(bg='#87CEEB')

    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame3.pack()


def foods():
    main_window.configure(bg='#FFF36D')
    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame3.pack_forget()
    frame5.pack()


def beverages():
    main_window.configure(bg='#BD9A7A')
    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame3.pack_forget()
    frame5.pack_forget()
    frame6.pack()


def goback4():
    main_window.configure(bg='#87CEEB')

    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame3.pack()
    frame5.pack_forget()


def AddSnacks():
    main_window.configure(bg='#87ceeb')

    snack_order1 = entry2.get()
    snack_order2 = entry3.get()
    snack_order3 = entry4.get()

    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame3.pack()


def AddFoods():
    main_window.configure(bg='#87ceeb')
    food_order1 = entry5.get()
    food_order2 = entry6.get()
    food_order3 = entry7.get()

    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame3.pack()
    frame5.pack_forget()


def AddBeverages():
    main_window.configure(bg='#87ceeb')
    drink_order1 = entry8.get()
    drink_order2 = entry9.get()
    drink_order3 = entry10.get()

    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame3.pack()
    frame5.pack_forget()
    frame6.pack_forget()


def goback5():
    main_window.configure(bg='#87CEEB')
    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame3.pack()
    frame5.pack_forget()
    frame6.pack_forget()


def placeorder11():
    global total_amount, snack_amount, food_amount, beve_amount, cgst_amount, sgst_amount, gst_amount, final_amount

    snack_total = 0
    snack_order1 = entry2.get()
    snack_order2 = entry3.get()
    snack_order3 = entry4.get()
    snack_order4 = entry4_1.get()
    snack_order5 = entry4_2.get()
    snack_order6 = entry4_3.get()

    if snack_order1 != '':
        snack_total = snack_total + (int(snack_order1) * 10)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Potato chip :' + snack_order1 + '\n')
        datafile.close()
    if snack_order2 != '':
        snack_total = snack_total + (int(snack_order2) * 20)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Banana chip :' + snack_order2 + '\n')
        datafile.close()
    if snack_order3 != '':
        snack_total = snack_total + (int(snack_order3) * 35)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('French Fries :' + snack_order3 + '\n')
        datafile.close()
    if snack_order4 != '':
        snack_total = snack_total + (int(snack_order4) * 40)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Sandwich :' + snack_order4 + '\n')
        datafile.close()
    if snack_order5 != '':
        snack_total = snack_total + (int(snack_order5) * 60)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Burger :' + snack_order5 + '\n')
        datafile.close()
    if snack_order6 != '':
        snack_total = snack_total + (int(snack_order6) * 70)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Veg Pizza :' + snack_order6 + '\n')
        datafile.close()

    food_total = 0
    food_order1 = entry5.get()
    food_order2 = entry6.get()
    food_order3 = entry7.get()
    food_order4 = entry7_1.get()
    food_order5 = entry7_2.get()
    food_order6 = entry7_3.get()

    if food_order1 != '':
        food_total = food_total + (int(food_order1) * 100)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Rice Plate :' + food_order1 + '\n')
        datafile.close()

    if food_order2 != '':
        food_total = food_total + (int(food_order2) * 120)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Paneer masala :' + food_order2 + '\n')
        datafile.close()
    if food_order3 != '':
        food_total = food_total + (int(food_order3) * 20)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Roti :' + food_order3 + '\n')
        datafile.close()
    if food_order4 != '':
        food_total = food_total + (int(food_order4) * 120)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Chicken biryani :' + food_order4 + '\n')
        datafile.close()
    if food_order5 != '':
        food_total = food_total + (int(food_order5) * 140)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Butter chicken :' + food_order5 + '\n')
        datafile.close()
    if food_order6 != '':
        food_total = food_total + (int(food_order6) * 100)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Veg kolhapuri :' + food_order6 + '\n')
        datafile.close()

    drink_total = 0
    drink_order1 = entry8.get()
    drink_order2 = entry9.get()
    drink_order3 = entry10.get()
    drink_order4 = entry10_1.get()
    drink_order5 = entry10_2.get()
    drink_order6 = entry10_3.get()

    if drink_order1 != '':
        drink_total = drink_total + (int(drink_order1) * 10)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Tea :' + drink_order1 + '\n')
        datafile.close()
    if drink_order2 != '':
        drink_total = drink_total + (int(drink_order2) * 20)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Coffee :' + drink_order2 + '\n')
        datafile.close()
    if drink_order3 != '':
        drink_total = drink_total + (int(drink_order3) * 40)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Chocolate Milkshake :' + drink_order3 + '\n')
        datafile.close()
    if drink_order4 != '':
        drink_total = drink_total + (int(drink_order4) * 30)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Pineapple Milkshake :' + drink_order4 + '\n')
        datafile.close()
    if drink_order5 != '':
        drink_total = drink_total + (int(drink_order5) * 20)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Soft drink :' + drink_order5 + '\n')
        datafile.close()
    if drink_order6 != '':
        drink_total = drink_total + (int(drink_order6) * 60)
        datafile = open('TableOrder.txt', 'a')
        datafile.write('Cold Coffee :' + drink_order6 + '\n')
        datafile.close()

    snack111 = entryamount1.get()
    food111 = entryamount2.get()
    beve111 = entryamount3.get()

    snack_amount = int(snack_total)
    food_amount = int(food_total)
    beve_amount = int(drink_total)
    total_amount = snack_amount + food_amount + beve_amount
    sgst_amount = ((total_amount) * 9) / 100
    cgst_amount = ((total_amount) * 9) / 100
    gst_amount = ((total_amount) * 18) / 100
    final_amount = total_amount + gst_amount

    label21.configure(text='Snacks Amount = Rs.' + str(snack_amount))
    label22.configure(text=' Food Amount = Rs.' + str(food_amount))
    label23.configure(text='  Beverages Amount = Rs.' + str(beve_amount))
    label24.configure(text='Total Amount = Rs.' + str(total_amount))
    label25.configure(text='SGST 9%  = Rs. ' + str(sgst_amount))
    label26.configure(text='CGST 9%  = Rs. ' + str(cgst_amount))
    label27.configure(text='GST 18%  = Rs. ' + str(gst_amount))
    label28.configure(text='Final Amount  = Rs. ' + str(final_amount))

    datafile = open('TableOrder.txt', 'a')

    datafile.write(
        'total amount of snacks      : ' + str(snack_amount) + '\n' + 'total amount of foods         : ' + str(
            food_amount) + '\n' + 'total amount of beverages : ' + str(
            beve_amount) + '\n' + 'Total amount                        : ' + str(
            total_amount) + '\n'  'GST                                        : ' + str(
            gst_amount) + '\n' + 'Final amount                        : ' + str(
            final_amount) + '\n' + '_____________________________________________' + '\n')

    datafile.close()

    frame1.pack_forget()
    frame2.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame3.pack_forget()
    frame7.pack()


def mainmenu1():
    entryA.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry4_1.delete(0, END)
    entry4_2.delete(0, END)
    entry4_3.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    entry7_1.delete(0, END)
    entry7_2.delete(0, END)
    entry7_3.delete(0, END)
    entry8.delete(0, END)
    entry9.delete(0, END)
    entry10.delete(0, END)
    entry10_1.delete(0, END)
    entry10_2.delete(0, END)
    entry10_3.delete(0, END)
    entryA11.delete(0, END)
    entryA9.delete(0, END)
    label4_111.configure(text='ENTER DATE')
    label4_121.configure(text='ENTER DATE')
    label31a.configure(text='\nENTER YOUR NAME\n')

    label5.configure(text='\nENTER TABLE NUMBER \nAND NAME \n...')
    label31.configure(text='\nENTER PHONE NUMBER \n...')

    frame1.pack()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()


def goback111():
    frame1.pack()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()
    frame6.pack_forget()
    frame7.pack_forget()
    frame8.pack_forget()


def order111():
    if entryB.get() == '':
        messagebox.showwarning("Warning", "Please\nAdd Details")
    if entryA11.get() == '':
        messagebox.showwarning("Warning", "Please\nAdd Details")
    if entryA9.get() == '':
        messagebox.showwarning("Warning", "Please\nAdd Details")
    else:
        frame3.pack()
        frame2.pack_forget()
        frame1.pack_forget()
        frame4.pack_forget()
        frame5.pack_forget()
        frame6.pack_forget()
        frame7.pack_forget()
        frame8.pack_forget()
        ()


main_window = tkinter.Tk()
main_window.title('BillTra')
main_window.geometry('1042x2140')
main_window.configure(bg='#87CEEB')

# -------------------------------------------------frame 1-----
frame1 = tkinter.Frame(main_window, bg='#87CEEB')

labelDes1 = tkinter.Label(frame1,
                          text='                                                                                                 ',
                          bg='green')
labelDes1.pack()

label1 = tkinter.Label(frame1, text='\nBillTra \n \nThe Hotel Food Ordering & \n Billing Software\n \n \n...',
                       bg='#87CEEB', font='times 10')
label1.pack()

label2 = tkinter.Label(frame1, text='CHOOSE YOUR ACTION !!\n...\n\n', bg=
'#87CEEB', font='times 9')
label2.pack()

framebutton1 = tkinter.Frame(frame1, bg='#87CEEB')

button1 = tkinter.Button(framebutton1, text='DINE \n IN \n', command=dinein1, bg='#90EE90', font='times 8')

labelA1 = tkinter.Label(framebutton1, text='               ', bg='#87CEEB')

button2 = tkinter.Button(framebutton1, text='TAKE \n OUT \n', command=takeout1, bg='#90EE90', font='times 8')

image1 = Image.open("C:\\Users\\Vedant\\PycharmProjects\\pythonProject8\\hotel.png")
resize_image = image1.resize((400, 362))
test = ImageTk.PhotoImage(resize_image)

labelDes1 = tkinter.Label(framebutton1, image=test, bg='#87CEEB')
labelDes1.image = test

# Position image


button1.grid(row=3, column=0)
labelDes1.grid(row=0, column=1)
labelA1.grid(row=0, column=1)
button2.grid(row=3, column=2)

framebutton1.pack()

# --------------------------frame2-----------------------
frame2 = tkinter.Frame(main_window, bg='#87CEEB')

label4 = tkinter.Label(frame2, text='\nDINE IN \n...', bg='#87CEEB', font='times 10')
label4.pack()

label4_121 = tkinter.Label(frame2, text='ENTER DATE', bg='#87CEEB', font='times 10')
label4_121.pack()

label444 = tkinter.Label(frame2, text='\n', bg='#87CEEB', font='times 10')
label444.pack()

entryC = tkinter.Entry(frame2, width=10)
entryC.pack()

labelgap1 = tkinter.Label(frame2, text='\n', bg='#87CEEB')
labelgap1.pack()

framebuttx = tkinter.Frame(frame2, bg='#87ceeb')

button4_111 = tkinter.Button(framebuttx, text='ADD DATE', command=adddate2, bg='#90EE90', font='times 8')

label6_111 = tkinter.Label(framebuttx, text='                                       ', bg='#87CEEB')

button4_112 = tkinter.Button(framebuttx, text='RESET DATE', command=resetdate, bg='#90EE90', font='times 8')

button4_111.grid(row=0, column=1)
label6_111.grid(row=1, column=1)
button4_112.grid(row=2, column=1)

framebuttx.pack()

label5 = tkinter.Label(frame2, text='\nENTER TABLE NUMBER \nAND NAME \n...', bg='#87CEEB', font='times 10')
label5.pack()

entryA = tkinter.Entry(frame2, width=20)
entryA.pack()

label5_1 = tkinter.Label(frame2, text='\n', bg='#87CEEB')
label5_1.pack()

button3 = tkinter.Button(frame2, text='ADD \n TABLE', command=addtable, bg='#90EE90', font='times 8')
button3.pack()

label6 = tkinter.Label(frame2, text='\nORDER FOOD \n...\n', bg='#87CEEB', font='times 10')
label6.pack()

framebutton2 = tkinter.Frame(frame2, bg='#87CEEB')

button4 = tkinter.Button(framebutton2, text='ORDER\n', command=order1, bg='#90EE90', font='times 8')

label6_1 = tkinter.Label(framebutton2, text='                                       ', bg='#87CEEB')

button_return_1 = tkinter.Button(framebutton2, text='GO \n BACK', command=goback1, bg='#90EE90', font='times 8')

button4.grid(row=0, column=0)
label6_1.grid(row=0, column=1)
button_return_1.grid(row=0, column=2)

framebutton2.pack()

# ----------------------------frame3-----------------------
frame3 = tkinter.Frame(main_window, bg='#87CEEB')

label7 = tkinter.Label(frame3, text='\nOrder Food\n... \n Choose Type \n...\n', bg='#87CEEB', font='times 10')
label7.pack()

button5 = tkinter.Button(frame3, text='Snacks', command=snacks, width=8, bg='#90EE90', font='times 8')
button5.pack()

labelspace1 = tkinter.Label(frame3, text='\n', bg='#87CEEB')
labelspace1.pack()

button6 = tkinter.Button(frame3, text='Food', command=foods, width=8, bg='#90EE90', font='times 8')
button6.pack()

labelspace2 = tkinter.Label(frame3, text='\n', bg='#87CEEB')
labelspace2.pack()

button7 = tkinter.Button(frame3, text='Beverages', command=beverages, width=8, bg='#90EE90', font='times 8')
button7.pack()

labelspace3 = tkinter.Label(frame3, text='\n', bg='#87CEEB')
labelspace3.pack()

framebutton3 = tkinter.Frame(frame3, bg='#87CEEB')

button8 = tkinter.Button(framebutton3, text='Place \n Orders', command=placeorder11, bg='#90EE90', font='times 8')

labelspacex1 = tkinter.Label(framebutton3, text='                                ', bg='#87CEEB')

button_return_2 = tkinter.Button(framebutton3, text='Go \n Back', command=goback2, bg='#90EE90', font='times 8')

button8.grid(row=0, column=0)
labelspacex1.grid(row=0, column=1)
button_return_2.grid(row=0, column=2)

framebutton3.pack()

goback1()

# ------------------------------frame4----------------------

frame4 = tkinter.Frame(main_window, bg='#FFB6C1')

label8 = tkinter.Label(frame4, text='\nSnacks\n Choose Quantity\n...', bg='#FFB6C1', font='times 12')
label8.pack()

label9 = tkinter.Label(frame4, text='potato chips\n 10Rs ------------', bg='#FFB6C1', font='times 10')
label9.pack()

entry2 = tkinter.Entry(frame4, width=5)
entry2.pack()

label10 = tkinter.Label(frame4, text='Banana chips\n 20Rs ------------', bg='#FFB6C1', font='times 10')
label10.pack()

entry3 = tkinter.Entry(frame4, width=5)
entry3.pack()

label11 = tkinter.Label(frame4, text='french fries\n 35Rs ------------', bg='#FFB6C1', font='times 10')
label11.pack()

entry4 = tkinter.Entry(frame4, width=5)
entry4.pack()

label11_1 = tkinter.Label(frame4, text='Sandwich \n 40Rs ------------', bg='#FFB6C1', font='times 10')
label11_1.pack()

entry4_1 = tkinter.Entry(frame4, width=5)
entry4_1.pack()

label11_2 = tkinter.Label(frame4, text='Burger \n 60Rs ------------', bg='#FFB6C1', font='times 10')
label11_2.pack()

entry4_2 = tkinter.Entry(frame4, width=5)
entry4_2.pack()

label11_3 = tkinter.Label(frame4, text='Veg Pizza\n 70Rs ------------', bg='#FFB6C1', font='times 10')
label11_3.pack()

entry4_3 = tkinter.Entry(frame4, width=5)
entry4_3.pack()

labelamount1 = tkinter.Label(frame4, text='\nEnter Total Amount Of Snacks\n...\n')

entryamount1 = tkinter.Entry(frame4, width=10)

labelspace5 = tkinter.Label(frame4, text='\n', bg='#FFB6C1', font='times 10')
labelspace5.pack()

framebutton4 = tkinter.Frame(frame4, bg='#FFB6C1')

button9 = tkinter.Button(framebutton4, text='Add \n Snacks', command=AddSnacks, bg='#90EE90', font='times 8')

labelspacex2 = tkinter.Label(framebutton4, text='                                ', bg='#FFB6C1')

button_return_3 = tkinter.Button(framebutton4, text='Go \n Back', command=goback3, bg='#90EE90', font='times 8')

button9.grid(row=0, column=0)
labelspacex2.grid(row=0, column=1)
button_return_3.grid(row=0, column=2)

framebutton4.pack()

goback1()

# ----------------------------frame5---------------------

frame5 = tkinter.Frame(main_window, bg='#FFF36D')

label12 = tkinter.Label(frame5, text='\nFood\n Choose Quantity\n...', bg='#FFF36D', font='times 12')
label12.pack()

label13 = tkinter.Label(frame5, text=' Rice Plate\n 100Rs ------------', bg='#FFF36D', font='times 10')
label13.pack()

entry5 = tkinter.Entry(frame5, width=5)
entry5.pack()

label14 = tkinter.Label(frame5, text='Paneer Masala\n 120Rs ------------', bg='#FFF36D', font='times 10')
label14.pack()

entry6 = tkinter.Entry(frame5, width=5)
entry6.pack()

label15 = tkinter.Label(frame5, text='Roti \n 20Rs ------------', bg='#FFF36D', font='times 10')
label15.pack()

entry7 = tkinter.Entry(frame5, width=5)
entry7.pack()

label15_1 = tkinter.Label(frame5, text='chicken Biryani \n 120Rs ------------', bg='#FFF36D', font='times 10')
label15_1.pack()

entry7_1 = tkinter.Entry(frame5, width=5)
entry7_1.pack()

label15_2 = tkinter.Label(frame5, text='Butter chicken \n 140Rs ------------', bg='#FFF36D', font='times 10')
label15_2.pack()

entry7_2 = tkinter.Entry(frame5, width=5)
entry7_2.pack()

label15_3 = tkinter.Label(frame5, text='Veg Kolhapuri \n 100Rs ------------', bg='#FFF36D', font='times 10')
label15_3.pack()

entry7_3 = tkinter.Entry(frame5, width=5)
entry7_3.pack()

labelamount2 = tkinter.Label(frame5, text='\nEnter Total Amount Of Food\n...\n')

entryamount2 = tkinter.Entry(frame5, width=10)

labelspace6 = tkinter.Label(frame5, text='\n', bg='#FFF36D', font='times 10')
labelspace6.pack()

framebutton5 = tkinter.Frame(frame5, bg='#FFF36D')

button10 = tkinter.Button(framebutton5, text='Add \n Foods', command=AddFoods, bg='#90EE90', font='times 8')

labelspacex3 = tkinter.Label(framebutton5, text='                                ', bg='#FFF36D')

button_return_4 = tkinter.Button(framebutton5, text='Go \n Back', command=goback4, bg='#90EE90', font='times 8')

button10.grid(row=0, column=0)
labelspacex3.grid(row=0, column=1)
button_return_4.grid(row=0, column=2)

framebutton5.pack()

goback1()

# -----------------------------frame6------------------------

frame6 = tkinter.Frame(main_window, bg='#BD9A7A')

label16 = tkinter.Label(frame6, text='\nBeverages\n Choose Quantity\n...', bg='#BD9A7A', font='times 12')
label16.pack()

label17 = tkinter.Label(frame6, text=' Tea\n 10Rs ------------', bg='#BD9A7A', font='times 10')
label17.pack()

entry8 = tkinter.Entry(frame6, width=5)
entry8.pack()

label18 = tkinter.Label(frame6, text='Coffee\n 20Rs ------------', bg='#BD9A7A', font='times 10')
label18.pack()

entry9 = tkinter.Entry(frame6, width=5)
entry9.pack()

label19 = tkinter.Label(frame6, text='Chocolate Milkshake \n 40Rs ------------', bg='#BD9A7A', font='times 10')
label19.pack()

entry10 = tkinter.Entry(frame6, width=5)
entry10.pack()

label19_1 = tkinter.Label(frame6, text='Pineapple Milkshake \n 30Rs ------------', bg='#BD9A7A', font='times 10')
label19_1.pack()

entry10_1 = tkinter.Entry(frame6, width=5)
entry10_1.pack()

label19_2 = tkinter.Label(frame6, text='Soft Drink \n 20Rs ------------', bg='#BD9A7A', font='times 10')
label19_2.pack()

entry10_2 = tkinter.Entry(frame6, width=5)
entry10_2.pack()

label19_3 = tkinter.Label(frame6, text='Cold Coffee \n 60Rs ------------', bg='#BD9A7A', font='times 10')
label19_3.pack()

entry10_3 = tkinter.Entry(frame6, width=5)
entry10_3.pack()

labelamount3 = tkinter.Label(frame6, text='\nEnter Total Amount Of Beverages\n...\n')

entryamount3 = tkinter.Entry(frame6, width=10)

labelspace7 = tkinter.Label(frame6, text='\n', bg='#BD9A7A')
labelspace7.pack()

framebutton6 = tkinter.Frame(frame6, bg='#BD9A7A')

button11 = tkinter.Button(framebutton6, text='Add \n Beverages', command=AddBeverages, bg='#90ee90', font='times 8')

labelspacex4 = tkinter.Label(framebutton6, text='                                ', bg='#bd9a7a')

button_return_5 = tkinter.Button(framebutton6, text='Go \nBack', command=goback5, bg='#90ee90', font='times 8')

button11.grid(row=0, column=0)
labelspacex4.grid(row=0, column=1)
button_return_5.grid(row=0, column=2)

framebutton6.pack()

goback1()

# -------------------------frame7-----------------------

frame7 = tkinter.Frame(main_window, bg='#87ceeb')

label20 = tkinter.Label(frame7, text='Billing \n', bg='#87ceeb', font='times 14')
label20.pack()

label21 = tkinter.Label(frame7, text='Snacks Amount = Rs. ' + str(snack_amount), bg='#87ceeb', font='times 10')
label21a = tkinter.Label(frame7, text='\n', bg='#87ceeb', font='times 10')
label21b = tkinter.Label(frame7, text='\n', bg='#87ceeb', font='times 10')
label21c = tkinter.Label(frame7, text='\n', bg='#87ceeb', font='times 10')
label21d = tkinter.Label(frame7, text='\n', bg='#87ceeb', font='times 10')
label21e = tkinter.Label(frame7, text='_______________________', bg='#87ceeb', font='times 10')

label22 = tkinter.Label(frame7, text=' Foods Amount = Rs. ' + str(food_amount), bg='#87ceeb', font='times 10')
label23 = tkinter.Label(frame7, text='  Beverages Amount = Rs. ' + str(beve_amount), bg='#87ceeb', font='times 10')
label24 = tkinter.Label(frame7, text='Total Amount = Rs. ' + str(total_amount), bg='#87ceeb', font='times 10')
label25 = tkinter.Label(frame7, text='SGST  = Rs. ' + str(sgst_amount), bg='#87ceeb', font='times 10')
label26 = tkinter.Label(frame7, text='CGST 9%  = Rs. ' + str(cgst_amount), bg='#87ceeb', font='times 10')
label27 = tkinter.Label(frame7, text='GST  = Rs. ' + str(gst_amount), bg='#87ceeb', font='times 10')
label28 = tkinter.Label(frame7, text='GST  = Rs. ' + str(final_amount), bg='#87ceeb', font='times 10')

label29 = tkinter.Label(frame7, text='Thank You \n Please Visit Again', bg='#87ceeb', font='times 10')

label21.pack()
label22.pack()
label23.pack()
label21a.pack()
label24.pack()
label21b.pack()
label25.pack()
label26.pack()
label27.pack()
label21c.pack()
label28.pack()
label21e.pack()
label29.pack()

label21d.pack()

button12 = tkinter.Button(frame7, text='Main \n Menu ', command=mainmenu1, bg='#90ee90', font='times 8')
button12.pack()

goback1()

# ---------------------------------------frame8-------------------

frame8 = tkinter.Frame(main_window
                       , bg='#87ceeb')

label30 = tkinter.Label(frame8, text='\nTAKE  OUT \n...', bg='#87CEEB', font='times 10')
label30.pack()

label4_111 = tkinter.Label(frame8, text='ENTER DATE', bg='#87CEEB', font='times 10')
label4_111.pack()

label444 = tkinter.Label(frame8, text='\n', bg='#87CEEB', font='times 10')
label444.pack()

entryB = tkinter.Entry(frame8, width=10)
entryB.pack()

labelgap1 = tkinter.Label(frame8, text='\n', bg='#87CEEB')
labelgap1.pack()

framebuttxx = tkinter.Frame(frame8, bg='#87ceeb')

button4_111 = tkinter.Button(framebuttxx, text='ADD DATE', command=adddate1, bg='#90EE90', font='times 8')

label6_111 = tkinter.Label(framebuttxx, text='                                       ', bg='#87CEEB')

button4_112 = tkinter.Button(framebuttxx, text='RESET DATE', command=resetdate, bg='#90EE90', font='times 8')

button4_111.grid(row=0, column=1)
label6_111.grid(row=1, column=1)
button4_112.grid(row=2, column=1)

framebuttxx.pack()

label31 = tkinter.Label(frame8, text='\nENTER PHONE NUMBER \n', bg='#87CEEB', font='times 10')
label31.pack()

entryA11 = tkinter.Entry(frame8, width=20)
entryA11.pack()

label31a = tkinter.Label(frame8, text='\nENTER YOUR NAME\n', bg='#87CEEB', font='times 10')
label31a.pack()

entryA9 = tkinter.Entry(frame8, width=20)
entryA9.pack()

label5_11 = tkinter.Label(frame8, text='\n', bg='#87CEEB')
label5_11.pack()

button13 = tkinter.Button(frame8, text='ADD \n DETAILS', command=addphnumber, bg='#90EE90', font='times 8')
button13.pack()

label32 = tkinter.Label(frame8, text='\nORDER FOOD \n...\n', bg='#87CEEB', font='times 10')
label32.pack()

framebutton8 = tkinter.Frame(frame8, bg='#87CEEB')

button14 = tkinter.Button(framebutton8, text='ORDER\n', command=order111, bg='#90EE90', font='times 8')

label6_11 = tkinter.Label(framebutton8, text='                                       ', bg='#87CEEB')

button_return_111 = tkinter.Button(framebutton8, text='GO \n BACK', command=goback111, bg='#90EE90', font='times 8')

button14.grid(row=0, column=0)
label6_11.grid(row=0, column=1)
button_return_111.grid(row=0, column=2)

framebutton8.pack()

goback1()

main_window.mainloop()