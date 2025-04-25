# WHAT
# In this code we are creating a GUI graphical user interfecae application using Tkinter, setting up a student management system interface that allows users to interact with student data.
# from : imports everyhting from Tkinter
# root: will then create the main window of the app (root), with title set to student man systems
# labelframe: is then created within the main window, given a titlte acting as a container for student-related fields and the grid method arranges it in a grid with padding and stretching horizontally(sticky=ew)
# entry fields: each label and entry field represents an input box where the user can type student info
# buttons : a new frame is created to hold thee buttons and its places in the second row
# then root.mainloop() : starts the Tkinter event loop


from tkinter import * 

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



root.mainloop()


