from tkinter import *
from tkinter import filedialog
from .Amigo-Staff-Tool import Amigo_Staff as ami

# App Functions
def browse():
    filename = filedialog.askopenfilename(
        initialdir = "C:\\",
        title = "Select file",
        filetypes = (("EXCEL files","*.xls *.xlsx"),("all files","*.*")))
    filepath.set(filename)

def choose():
    if chosen.get() == 1:
        search_a_staff = Toplevel(root)

        var = StringVar()
        search_frame = Frame(search_a_staff, borderwidth=1, relief=FLAT)
        search_entry = Entry(search_frame, width=35, textvariable=var).pack(side=LEFT, fill=BOTH, expand=YES, padx=3)
        search_button = Button(search_frame, text='Search', width=8, command=).pack(side=RIGHT, padx=3)
        search_frame.pack(fill=X, padx=2, pady=5)

        result_frame = Frame(search_a_staff, borderwidth=1, relief=GROOVE, width=200, height=200)
        result_text = Text(result_frame)
        result_text.insert(END, var.get())
        result_frame.pack(fill=X, padx=5, pady=3)
        

## # # # # # # #
## Tkinter GUI #
## # # # # # # #
root = Tk()
root.title(string='Amigo Staff Tool')
# root.geometry(newGeometry='400x100')

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
radio_button1 = Radiobutton(frame2, text='Search a staff', value=1, variable=chosen).pack(side=LEFT, padx=30)
radio_button2 = Radiobutton(frame2, text='Add a staff', value=2, variable=chosen).pack(side=LEFT, padx=30)
frame2.pack(fill=X, padx=2)

# Frame 3
frame3 = Frame(root, borderwidth=1, relief=FLAT)
next_button = Button(frame3, text='Next', width=8, command=choose).pack(side=RIGHT, padx=3)
frame3.pack(fill=X, padx=2, pady=5)

# # # # # # #
#  Window 2 #
# # # # # # #
root.mainloop()

