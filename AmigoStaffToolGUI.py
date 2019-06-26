#!/usr/bin/env python3
__author__ = "Wreck-it Kenny"
__copyright__ = "Copyright 2019, The Python Project"
__version__ = "1.0.1"
__email__ = "tung.tran.3295@gmail.com"
__status__ = "Production"
__doc__ = "A mini tool to get and add Amigo Staff information"

from tkinter import *
from tkinter import filedialog
from openpyxl import load_workbook
from openpyxl.styles import Alignment, Font, Border, Side

# App Functions
def get_information():
    for i in range(len(name)):
        if name[i].value == ' '.join([i.capitalize() for i in search_name.get().rstrip().split(' ')]):
            global infor
            infor = """======================\n
|| Name: {}\n
|| Title: {}\n
|| Phone: {}\n
|| Email: {}\n
======================""".format(name[i].value, title[i].value, phone[i].value, email[i].value)
            result_info.set(infor)


def add_information():
        add_num = num[::-1][0].value + 1
        ws.append((add_num, add_name.get(), add_title.get(), '', add_phone.get(), add_email.get()))
        for col in ws.columns:
            aligned_cell = col[-1]
            # aligned_num_cell = col(1)[-1]
            aligned_cell.alignment = Alignment(vertical='center')
            # aligned_num_cell.alignment = Alignment(horizontal='center', vertical='center')
            aligned_cell.font = Font(name='Times New Roman', size=12)
            aligned_cell.border = Border(left=Side(border_style='thin'),
                                         right=Side(border_style='thin'),
                                         top=Side(border_style='thin'),
                                         bottom=Side(border_style='thin'))
        wb.save(filename)


def browse():
    global filename
    filename = str(filedialog.askopenfilename(
        initialdir = "C:\\",
        title = "Select Excel file",
        filetypes = (("EXCEL files","*.xlsx"),("all files","*.*"))))
    filepath.set(filename)
    if filename != '':
        next_button['state'] = NORMAL
    
    # Initial definitions
    global wb, ws, num, name, title, phone, email
    wb = load_workbook(filename)
    ws = wb['AMG']
    num = ws['A']
    name = ws['B']
    title = ws['C']
    phone = ws['E']
    email = ws['F']


def choose():
    if chosen.get() == 1 :
        search_a_staff = Toplevel(root)
        search_a_staff.geometry(newGeometry='300x300')
        search_a_staff.title(string='Search an existing staff')
        search_a_staff.iconbitmap(r'W:/Github/Amigo-Staff-Tool/amigo.ico')
        search_a_staff.resizable(width=False, height=False)

        # Frame: SEARCH FIELD
        global search_name
        search_name = StringVar()
        search_frame = Frame(search_a_staff, borderwidth=1)

        search_frame2 = Frame(search_frame, relief=GROOVE, borderwidth=2)
        search_entry = Entry(search_frame2, width=35, textvariable=search_name).pack(side=LEFT, fill=BOTH, expand=YES, pady=10, padx=5)
        search_button = Button(search_frame2, text='Search', width=8, command=get_information).pack(side=RIGHT, fill=X, padx=5)
        search_frame2.pack(fill=BOTH, padx=3, pady=10)

        search_label = Label(search_frame, text='Name to search:').place(relx=0.06, rely=0.15, anchor=W)
        search_frame.pack(fill=BOTH)

        # Frame: SEARCH RESULT
        global result_info
        result_info = StringVar()
        result_frame = Frame(search_a_staff)

        result_frame2 = Frame(result_frame, relief=GROOVE, borderwidth=2)
        result_message = Message(result_frame2, textvariable=result_info).pack(fill=BOTH, expand=YES)
        result_frame2.pack(fill=BOTH, expand=YES, padx=4, pady=5)

        result_label = Label(result_frame, text='Staff Information:').place(relx=0.06, rely=0.015, anchor=W)
        result_frame.pack(fill=BOTH, expand=YES)

    if chosen.get() == 2:
        add_a_staff = Toplevel(root)
        add_a_staff.title(string='Add a new staff')
        # add_a_staff.geometry(newGeometry='300x300')
        add_a_staff.iconbitmap(r'W:/Github/Amigo-Staff-Tool/amigo.ico')
        add_a_staff.resizable(width=False, height=False)

        Label(add_a_staff, text='Name:').grid(row=0, sticky=W, padx=5, pady=5)
        Label(add_a_staff, text='Title:').grid(row=1, sticky=W, padx=5, pady=5)
        Label(add_a_staff, text='Phone:').grid(row=2, sticky=W, padx=5, pady=5)
        Label(add_a_staff, text='Email:').grid(row=3, sticky=W, padx=5, pady=5)

        global add_name, add_title, add_phone, add_email
        add_name = StringVar()
        add_title = StringVar()
        add_phone = StringVar()
        add_email = StringVar()
        add_entry1 = Entry(add_a_staff, width=25, textvariable=add_name)
        add_entry1.grid(row=0, column=1, padx=5, pady=5)
        add_entry2 = Entry(add_a_staff, width=25, textvariable=add_title)
        add_entry2.grid(row=1, column=1, padx=5, pady=5)
        add_entry3 = Entry(add_a_staff, width=25, textvariable=add_phone)
        add_entry3.grid(row=2, column=1, padx=5, pady=5)
        add_entry4 = Entry(add_a_staff, width=25, textvariable=add_email)
        add_entry4.grid(row=3, column=1, padx=5, pady=5)
        
        add_button = Button(add_a_staff, text='Add', width=8, command=add_information)
        add_button.grid(row=0, column=2, padx=5, pady=5)
        cancel_button = Button(add_a_staff, text='Cancel', width=8, command=add_a_staff.quit)
        cancel_button.grid(row=1, column=2, padx=5)


## # # # # # # #
## Tkinter GUI #
## # # # # # # #
root = Tk()
root.title(string='Amigo Staff Tool')
root.resizable(width=False, height=False)
root.iconbitmap(r'W:/Github/Amigo-Staff-Tool/amigo.ico')

# # # # # # #
#  Window 1 #
# # # # # # #
# Frame 1
filepath = StringVar()
frame1 = Frame(root, borderwidth=1, relief=FLAT)
entry = Entry(frame1, textvariable=filepath).pack(side=LEFT, fill=BOTH, expand=YES, padx=3)
browse_button = Button(frame1, text='Browse', width=8, command=browse).pack(side=RIGHT, padx=3)
frame1.pack(fill=X, padx=2, pady=5)

# Frame 2
chosen = IntVar()
frame2 = Frame(root, borderwidth=1, relief=FLAT)
radio_button1 = Radiobutton(frame2, text='Search a staff', value=1, variable=chosen)
radio_button1.pack(side=LEFT, padx=30)
radio_button2 = Radiobutton(frame2, text='Add a staff', value=2, variable=chosen)
radio_button2.pack(side=LEFT, padx=30)
frame2.pack(fill=X, padx=2)

# Frame 3
frame3 = Frame(root, borderwidth=1, relief=FLAT)
next_button = Button(frame3, text='Next', width=8, state=DISABLED, command=choose)
next_button.pack(side=RIGHT, padx=3)
frame3.pack(fill=X, padx=2, pady=5)


# # # # # # #
#  Window 2 #
# # # # # # #
root.mainloop()