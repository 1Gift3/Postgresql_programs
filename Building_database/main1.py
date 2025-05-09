# WHAT
# In this code we are creating a GUI graphical user interfecae application using Tkinter, setting up a student management system interface that allows users to interact with student data.
# from : imports everyhting from Tkinter
# root: will then create the main window of the app (root), with title set to student man systems
# labelframe: is then created within the main window, given a titlte acting as a container for student-related fields and the grid method arranges it in a grid with padding and stretching horizontally(sticky=ew)
# entry fields: each label and entry field represents an input box where the user can type student info
# buttons : a new frame is created to hold thee buttons and its places in the second row
# then root.mainloop() : starts the Tkinter event loop

from tkinter import * 
from tkinter import ttk
import psycopg2

def run_query(query,parameters=()):
    conn = psycopg2.connect(dbname="studentdb",user="postgres",password="Sindiso2017",host="localhost",port="5432")
    cur = conn.cursor()
    query_result = None
    try:
        cur.execute(query,parameters)
        if query.lower().startswith("select"):
            query_result = cur.fetchall()
        conn.commit()
    except psycopg2.Error as e:
        messagebox.showerror("Database Error",str(e))
    finally:
        cur.close()
        conn.close()
    return query_result 

def refresh_treeview():
    for item in tree.get_children():
        tree.delete(item)
    records = run_query("select * from students;")
    for record in records:
        tree.insert('',END,values=record)


root = Tk()
root.title("Student management system")

frame = LabelFrame(root, text="Student Data")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

Label(frame, text="Name:").grid(row=0,column=0,padx=2,sticky="w")
name_entry = Entry(frame)
name_entry.grid(row=0,column=1,pady=2,sticky="ew")

Label(frame, text="Address:").grid(row=1,column=0,padx=2,sticky="w")
address_entry = Entry(frame)
address_entry.grid(row=1,column=1,pady=2,sticky="ew")

Label(frame, text="Age:").grid(row=2,column=0,padx=2,sticky="w")
age_entry = Entry(frame)
age_entry.grid(row=2,column=1,pady=2,sticky="ew")

Label(frame, text="Phone Number:").grid(row=3,column=0,padx=2,sticky="w")
phone_entry = Entry(frame)
phone_entry.grid(row=3,column=1,pady=2,sticky="ew")


button_frame = Frame(root)
button_frame.grid(row=1,column=0,pady=5,sticky="ew")

Button(button_frame,text="Create Data").grid(row=0,column=0, padx=5)
Button(button_frame,text="Add Data").grid(row=0,column=1, padx=5)
Button(button_frame,text="Update Data").grid(row=0,column=2, padx=5)
Button(button_frame,text="Delete Data").grid(row=0,column=3, padx=5)


# ttk create a table like gui element with scrollable functionality
#  frame(root) creates a frame inside the main window, positions it in the grid layout at row 2, column 0 with some padding and resizing (sticky="nswe")
# we then add a scroll bar to the right side of the tree_frame and the scrollbar will fill the vertical space
# we also create a treeview widget which is like a table or list, connecting it to the scrollbar so it can scroll vertically and selectmode = "browse" means only one row can be selected at a time
# we then define table columns specifically 5 custom columns for the Treeview : ID, Names etc
# - hiding along the default column #0 and defining the alighment and width for each column
# headers are the set, setting visible column names in the header row if the table


tree_frame = Frame(root)
tree_frame.grid(row=2, column=0,padx=10,sticky="nsew")

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

tree =ttk.Treeview(tree_frame,yscrollcomman=tree_scroll.set,selectmode="browse")
tree.pack()
tree_scroll.config(command=tree.yview)


tree['columns']=("student_id","name","address","age","number")
tree.column("#0",width=0,stretch=NO)
tree.column("student_id", anchor=CENTER,width=80)
tree.column("name", anchor=CENTER,width=120)
tree.column("address", anchor=CENTER,width=120)
tree.column("age", anchor=CENTER,width=50)
tree.column("number", anchor=CENTER,width=120)

tree.heading("student_id",text="ID",anchor=CENTER)
tree.heading("name",text="Name",anchor=CENTER)
tree.heading("address",text="Address",anchor=CENTER)
tree.heading("age",text="Age",anchor=CENTER)
tree.heading("number",text="Phone number",anchor=CENTER)




refresh_treeview()
refresh_treeview()
root.mainloop()


