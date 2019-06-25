#!/usr/bin/env python3
__author__ = "Wreck-it Kenny"
__copyright__ = "Copyright 2019, The Python Project"
__version__ = "1.0"
__email__ = "tung.tran.3295@gmail.com"
__status__ = "Production"
__doc__ = "A mini tool to get and add Amigo Staff information using OPENPYXL"

# Call modules
from xlrd import open_workbook
from xlutils.copy import copy
from xlwt import easyxf

# File location
location = "\\\\10.0.8.5\\Public IS\\Danh sach nhan vien Amigo\\Staff list in\
 Amigo June2019.xls"

# Initial definitions
rb = open_workbook(filename=location, formatting_info=True)
rs = rb.sheet_by_name('AMG')
wb = copy(rb)
ws = wb.get_sheet(1)
num = rs.col(0)
name = rs.col(1)
title = rs.col(2)
phone = rs.col(4)
email = rs.col(5)

# Stylist
style_num = easyxf('alignment: horizontal center, vertical center;'
                   'font: name Times New Roman, height 240;'
                   'borders: left thin, right thin, top thin, bottom thin')
style = easyxf('alignment: vertical center;'
               'font: name Times New Roman, height 240;'
               'borders: left thin, right thin, top thin, bottom thin')


class Amigo_Staff():
    def __init__(self, staff_name):
        self.staff_name = staff_name

    def get_information(self):
        for i in range(len(name)):
            if name[i].value == self.staff_name:
                print(f"""==============================
Name: {name[i].value}
Title: {title[i].value}
Phone: {phone[i].value}
Email: {email[i].value}
==============================""")
                break
        else:
            print("NOT FOUND")

    def add_information(self, staff_title, staff_phone, staff_email):
        self.staff_num = int(num[rs.nrows - 1].value) + 1
        self.staff_title = staff_title
        self.staff_phone = staff_phone
        self.staff_email = staff_email
        ws.write(rs.nrows, 0, self.staff_num, style_num)
        ws.write(rs.nrows, 1, self.staff_name, style)
        ws.write(rs.nrows, 2, self.staff_title, style)
        ws.write(rs.nrows, 3, '', style)
        ws.write(rs.nrows, 4, self.staff_phone, style)
        ws.write(rs.nrows, 5, self.staff_email, style)
        wb.save(location)


if __name__ == '__main__':
    while True:
        print("""
What do you want?
1. Search a staff information
2. Add a new staff""")
        res = int(input("Choose: "))
        if res == 1:
            s = input("What name to search? ")
            ppl = Amigo_Staff(s)
            ppl.get_information()
        elif res == 2:
            try:
                new_name = input("What is name? ")
                new_title = input("What is title? ")
                new_phone = input("What is phone number? ")
                new_email = input("What is email? ")
                ppl = Amigo_Staff(new_name)
                ppl.add_information(staff_title=new_title,
                                    staff_phone=new_phone,
                                    staff_email=new_email)
                print("Successfully added a new staff")
            except PermissionError:
                print("""
==================WARNING!=================
Please close the Excel file before updating""")
            break
        else:
            print("{} is an invalid option".format(res))
