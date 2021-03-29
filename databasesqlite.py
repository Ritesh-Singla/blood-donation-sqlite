from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from tkinter import colorchooser


root= Tk()
root.title("Blood Bank System")

a= root.winfo_screenheight()
b=root.winfo_screenwidth()
root.geometry(f"{b}x{a}")
#root.configure(background='black')
root.bind("<Return>")
my_menu= Menu(root)
root.config(menu=my_menu)
root.iconbitmap("blood.ico")

conn= sqlite3.connect("blooddatabase.db")

c=conn.cursor()

# c.execute(""" CREATE TABLE donors(
#  		Full_name text,
#  		Gender text,
#  		Blood_Group text,
#  		Address text,
#  		Contact integer,
#  		City text,
#  		State text,
#  		Zip_code integer
#  						)
#  			""")

def new_file():
	pass

def find():
	pass

def find_next():
	pass

def next_file():
	pass

def previous_file():
	pass

def contact_us():
	pass

def read_tnc():
	pass

def labels_change():
	
	# creating labels
	full_name_label= Label(root,text="Full Name               ",font=('Halvetica',10),bg=my_color[1])
	full_name_label.grid(row=1,column=0, stick=W,pady=2)
	gender_label=Label(root,text="Gender                   ",font=('Halvetica',10))
	gender_label.grid(row=2,column=0, stick=W,pady=2)
	blood_group_label= Label(root,text="Enter Blood Group   ",font=('Halvetica',10))
	blood_group_label.grid(row=3,column=0, stick=W,pady=2)
	address_label= Label(root,text="Address                  ",font=('Halvetica',10))
	address_label.grid(row=4,column=0, stick=W,pady=2)
	contact_label= Label(root, text="Contact No.             ",font=('Halvetica',10))
	contact_label.grid(row=5,column=0, stick=W,pady=2)
	city_label= Label(root,text="City                        ",font=('Halvetica',10))
	city_label.grid(row=6,column=0, stick=W,pady=2)
	state_label= Label(root,text="State                      ",font=('Halvetica',10))
	state_label.grid(row=7,column=0, stick=W,pady=2)
	zip_code_label= Label(root,text="Zip Code                 ",font=('Halvetica',10))
	zip_code_label.grid(row=8,column=0, stick=W,pady=2)
	select_id_label= Label(root,text="Select Id                  ",font=('Halvetica',10))
	select_id_label.grid(row=11,column=0, stick=W,pady=2)
	
	# Destroying previous labels
	full_name_label.destroy()
	gender_label.destroy()
	blood_group_label.destroy()
	address_label.destroy()
	contact_label.destroy()
	city_label.destroy()
	state_label.destroy()
	zip_code_label.destroy()
	select_id_label.destroy()

	# creating labels with changed colors
	full_name_label= Label(root,text="Full Name               ",font=('Halvetica',10),bg=my_color[1])
	full_name_label.grid(row=1,column=0, stick=W,pady=2)
	gender_label=Label(root,text="Gender                   ",font=('Halvetica',10),bg=my_color[1])
	gender_label.grid(row=2,column=0, stick=W,pady=2)
	blood_group_label= Label(root,text="Enter Blood Group   ",font=('Halvetica',10),bg=my_color[1])
	blood_group_label.grid(row=3,column=0, stick=W,pady=2)
	address_label= Label(root,text="Address                  ",font=('Halvetica',10),bg=my_color[1])
	address_label.grid(row=4,column=0, stick=W,pady=2)
	contact_label= Label(root, text="Contact No.             ",font=('Halvetica',10),bg=my_color[1])
	contact_label.grid(row=5,column=0, stick=W,pady=2)
	city_label= Label(root,text="City                        ",font=('Halvetica',10),bg=my_color[1])
	city_label.grid(row=6,column=0, stick=W,pady=2)
	state_label= Label(root,text="State                      ",font=('Halvetica',10),bg=my_color[1])
	state_label.grid(row=7,column=0, stick=W,pady=2)
	zip_code_label= Label(root,text="Zip Code                 ",font=('Halvetica',10),bg=my_color[1])
	zip_code_label.grid(row=8,column=0, stick=W,pady=2)
	select_id_label= Label(root,text="Select Id                  ",font=('Halvetica',10),bg=my_color[1])
	select_id_label.grid(row=11,column=0, stick=W,pady=2)


def color():
	global my_color
	my_color= colorchooser.askcolor()
	#print(my_color[1])
	root.config(menu=my_menu,background=my_color[1])
	head= Label(root,text= "Blood Donation Portal", font=('Halvetica',25),bg=my_color[1])
	head.grid(row=0,column=0,columnspan=2)
	labels_change()


def submit():
	# Label(root,text=full_name.get() +gender.get()+address.get()+city.get()+state.get()+zip_code.get()).grid(row=7,column=0)
	if full_name.get() =="" or drop.get() == "Select gender" or drop_blood.get()== "Select Blood Group" or address.get() =="" or contact.get()== "" or city.get() =="" or state.get()== "Select State" or zip_code.get() =="":
		messagebox.showinfo("Error", "Enter Valid Details !!!! ")
			
	else:
		try:	
			conn= sqlite3.connect("blooddatabase.db")

			c=conn.cursor()

			c.execute("INSERT INTO donors VALUES (:name, :gender, :blood_group, :address, :contact, :city, :state, :zipcode)",
					{
						'name': full_name.get().title(),
						'gender': drop.get(),
						'blood_group': drop_blood.get(),
						'address': address.get().title(),
						'contact': int(contact.get()),
						'city': city.get().title(),
						'state': state.get(),
						'zipcode': int(zip_code.get())
					}


				)

			conn.commit()

			conn.close()

			full_name.delete(0, END)
			drop.set("Select gender")
			drop_blood.set("Select Blood Group")
			address.delete(0, END)
			contact.delete(0, END)
			city.delete(0, END)
			state.set("Select State")
			zip_code.delete(0, END)

		except Exception as e:
			messagebox.showinfo("Error", "Enter Correct zip Code or contact no. !!! ")			


def exit():
	root.destroy()


def show():
	global show_window
	show_window= Toplevel()
	show_window.title("Show records")
	# show_window.geometry("600x600")
	show_window.config(background="white")

	global label_show
	label_list=[
			"Id",
			"Name",
			"Gender",
			"Blood Group",
			"Address",
			"Contact",
			"City",
			"State",
			"Zip Code"
	]

	for ind, k in enumerate(label_list):
		top_label= Label(show_window,text=k,bg="white")
		top_label.grid(row=0,column=ind,stick=W, padx=5)
		
	conn= sqlite3.connect("blooddatabase.db")

	c=conn.cursor()

	c.execute("SELECT oid,* FROM donors")
	result=c.fetchall()
	
	for index, i in enumerate(result):
		num=0
		for j in i:
			label_show=Label(show_window,text=j,bg="white")
			label_show.grid(row=index+1,column=num, stick=W, padx=5)
			num+=1

	conn.commit()

	conn.close()


def delete():
	try:
		conn= sqlite3.connect("blooddatabase.db")

		c=conn.cursor()	
		
		c.execute("DELETE FROM donors WHERE oid=" +str(select_id.get()))

		conn.commit()

		conn.close()

		show()

		messagebox.showinfo("Success","Successfully Deleted Record")
		select_id.delete(0, END)


	except Exception as e:
		messagebox.showinfo("Error","Record Not Found")
		select_id.delete(0, END)


def update():
	if full_name_editor.get() =="" or dro.get() == "Select gender" or dro_blood.get()== "Select Blood Group" or address_editor.get() =="" or contact_editor.get()== "" or city_editor.get() =="" or dro_state.get()== "Select State" or zip_code_editor.get() =="":
		messagebox.showinfo("Error", "Enter Valid Details !!!! ")
	else:
		try:

			conn= sqlite3.connect("blooddatabase.db")
			c=conn.cursor()

			c.execute("""UPDATE donors SET
						Full_name= :name,
						Gender= :gender,
						Blood_Group= :blood,
						Address= :address,
						Contact= :contact,
						city= :city,
						State= :state,
						Zip_Code= :zip
						WHERE oid= :oid""",
						{
							'name': full_name_editor.get().title(),
							'gender': dro.get(),
							'blood': dro_blood.get(),
							'address': address_editor.get().title(),
							'contact': int(contact_editor.get()),
							'city': city_editor.get().title(),
							'state': dro_state.get(),
							'zip': int(zip_code_editor.get()),
							'oid': select_id.get()

						})

			conn.commit()
			conn.close()

			messagebox.showinfo("Success!", "Successfully Updated Record !")
			editor.destroy()
			select_id.delete(0, END)
			show()
		except Exception as e:
			messagebox.showinfo("Error", "Error Occured...")


def edit():
	try:
		global editor
		editor= Toplevel()
		editor.title("Edit Record")
		
		global full_name_editor
		global gender_editor
		global blood_group_editor
		global address_editor
		global contact_editor
		global city_editor
		global state_editor
		global zip_code_editor
		global dro
		global dro_blood
		global dro_state

		dro= StringVar()
		dro_state= StringVar()
		dro_blood= StringVar()
		

		full_name_editor= Entry(editor,bd=5)
		full_name_editor.grid(row=0,column=1, stick=W+E)
		gender_editor=OptionMenu(editor,dro, "Select gender", "Male", "Female", "Other")
		gender_editor.grid(row=1,column=1, stick=W+E)
		blood_group_editor= OptionMenu(editor,dro_blood, *bloodgroups)
		blood_group_editor.grid(row=2,column=1, stick=W+E)
		address_editor= Entry(editor,bd=5)
		address_editor.grid(row=3,column=1, stick=W+E)
		contact_editor= Entry(editor,bd=5)
		contact_editor.grid(row=4,column=1, stick=W+E)
		city_editor= Entry(editor,bd=5)
		city_editor.grid(row=5,column=1, stick=W+E)
		state_editor= OptionMenu(editor,dro_state, *states)
		state_editor.grid(row=6,column=1, stick=W+E)
		zip_code_editor= Entry(editor,bd=5)
		zip_code_editor.grid(row=7,column=1, stick=W+E)	

		full_name_label_editor= Label(editor,text="Full Name")
		full_name_label_editor.grid(row=0,column=0, stick=W+E)
		gender_label_editor=Label(editor,text="Gender")
		gender_label_editor.grid(row=1,column=0, stick=W+E)
		blood_group_label_editor= Label(editor,text="Enter Blood Group")
		blood_group_label_editor.grid(row=2,column=0, stick=W+E)
		address_label_editor= Label(editor,text="Address")
		address_label_editor.grid(row=3,column=0, stick=W+E)
		contact_label_editor= Label(editor, text="Contact No.")
		contact_label_editor.grid(row=4,column=0, stick=W+E)
		city_label_editor= Label(editor,text="City")
		city_label_editor.grid(row=5,column=0, stick=W+E)
		state_label_editor= Label(editor,text="State")
		state_label_editor.grid(row=6,column=0, stick=W+E)
		zip_code_label_editor= Label(editor,text="Zip Code")
		zip_code_label_editor.grid(row=7,column=0, stick=W+E)
		
		buttn_save= Button(editor, text="Save",command=update, pady=5,bg="green")
		buttn_save.grid(row=8,column=0,columnspan=2, stick=W+E, pady=5)

		conn= sqlite3.connect("blooddatabase.db")
		c=conn.cursor()
		

		c.execute("SELECT * FROM donors WHERE oid=" + str(select_id.get()))
		result= c.fetchall()

		for rslt in result:
			full_name_editor.insert(0, rslt[0])
			dro.set(rslt[1])
			dro_blood.set(rslt[2])
			address_editor.insert(0, rslt[3])
			contact_editor.insert(0, rslt[4])
			city_editor.insert(0, rslt[5])
			dro_state.set(rslt[6])
			zip_code_editor.insert(0, rslt[7])
			

		conn.commit()

		conn.close()
		
		editor.mainloop()

	except Exception as e:
		messagebox.showinfo("Error","Please Enter Valid Id")


# Creating menus
file_menu= Menu(my_menu)
my_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_cascade(label='New...', command=new_file)
file_menu.add_separator()
file_menu.add_cascade(label='Exit', command=root.quit)

edit_menu= Menu(my_menu)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_cascade(label='Find', command=find)
edit_menu.add_cascade(label='Find next', command=find_next)

tools_menu= Menu(my_menu)
my_menu.add_cascade(label='Tools', menu=tools_menu)
tools_menu.add_cascade(label='Next', command=next_file)
tools_menu.add_cascade(label='Previous', command=previous_file)
tools_menu.add_cascade(label='Background Color', command=color)

help_menu= Menu(my_menu)
my_menu.add_cascade(label='Help', menu=help_menu)
help_menu.add_cascade(label='Contact Us', command=contact_us)
help_menu.add_cascade(label='Read T&C..', command=read_tnc)

# Creating main heading label
head= Label(root,text= "Blood Donation Portal", font=('Halvetica',25),bg='white')
head.grid(row=0,column=0,columnspan=2)

# States Lists
states = [
		"Select State",
		 "Andhra Pradesh",
		 "Arunachal Pradesh ",
		 "Assam",
		 "Bihar",
		 "Chhattisgarh",
		 "Goa",
		 "Gujarat",
		 "Haryana",
		 "Himachal Pradesh",
		 "Jammu and Kashmir",
		 "Jharkhand",
		 "Karnataka",
		 "Kerala",
		 "Madhya Pradesh",
		 "Maharashtra",
		 "Manipur",
		 "Meghalaya",
		 "Mizoram",
		 "Nagaland",
		 "Odisha",
		 "Punjab",
		 "Rajasthan",
		 "Sikkim",
		 "Tamil Nadu",
		 "Telangana",
		 "Tripura",
		 "Uttar Pradesh",
		 "Uttarakhand",
		 "West Bengal",
		 "Andaman and Nicobar Islands",
		 "Chandigarh",
		 "Dadra and Nagar Haveli",
		 "Daman and Diu",
		 "Lakshadweep",
		 "National Capital Territory of Delhi",
		 "Puducherry"
	]
# Blood Groups Lists
bloodgroups=[
			"Select Blood Group",
			"A+",
			"A-",
			"B+",
			"B-",
			"O+",
			"O-",
			"AB+",
			"AB-"

		]

# Creating entry widgets
full_name= Entry(root,bd=5,bg="white",font=('Halvetica',10))
full_name.grid(row=1,column=1, stick=W+E+N+S,pady=2)
drop= StringVar()
gender=OptionMenu(root,drop, "Select gender", "Male", "Female", "Other")
drop.set("Select gender")
gender.grid(row=2,column=1, stick=W+E+N+S,pady=2)
drop_blood= StringVar()
blood_group= OptionMenu(root,drop_blood, *bloodgroups)
drop_blood.set("Select Blood Group")
blood_group.grid(row=3,column=1, stick=W+E+N+S,pady=2)
address= Entry(root,bd=5,bg="white",font=('Halvetica',10))
address.grid(row=4,column=1, stick=W+E+N+S,pady=2)
contact= Entry(root,bd=5,bg="white",font=('Halvetica',10))
contact.grid(row=5,column=1, stick=W+E+N+S,pady=2)
city= Entry(root,bd=5,bg="white",font=('Halvetica',10))
city.grid(row=6,column=1, stick=W+E+N+S,pady=2)
state= ttk.Combobox(root, value=states)
state.set("Select State")
state.grid(row=7,column=1, stick=W+E+N+S,pady=2)
zip_code= Entry(root,bd=5,bg="white",font=('Halvetica',10))
zip_code.grid(row=8,column=1, stick=W+E+N+S,pady=2)

# Creating submit and show buttons
buttn_submit= Button(root, text="Submit",command=submit, pady=5, bd=5, bg="white",font=('Halvetica',10))
buttn_submit.grid(row=9,column=0,columnspan=2, stick=W+E+N+S)

buttn_show= Button(root, text="Show All",command=show, pady=5, bd=5, bg="white",font=('Halvetica',10))
buttn_show.grid(row=10,column=0,columnspan=2, stick=W+E+N+S)

select_id = Entry(root,bd=5,bg="white",font=('Halvetica',10))
select_id.grid(row=11,column=1, stick=W+E+N+S,pady=2)

# creating labels
full_name_label= Label(root,text="Full Name               ",font=('Halvetica',10))
full_name_label.grid(row=1,column=0, stick=W,pady=2)
gender_label=Label(root,text="Gender                   ",font=('Halvetica',10))
gender_label.grid(row=2,column=0, stick=W,pady=2)
blood_group_label= Label(root,text="Enter Blood Group   ",font=('Halvetica',10))
blood_group_label.grid(row=3,column=0, stick=W,pady=2)
address_label= Label(root,text="Address                  ",font=('Halvetica',10))
address_label.grid(row=4,column=0, stick=W,pady=2)
contact_label= Label(root, text="Contact No.             ",font=('Halvetica',10))
contact_label.grid(row=5,column=0, stick=W,pady=2)
city_label= Label(root,text="City                        ",font=('Halvetica',10))
city_label.grid(row=6,column=0, stick=W,pady=2)
state_label= Label(root,text="State                      ",font=('Halvetica',10))
state_label.grid(row=7,column=0, stick=W,pady=2)
zip_code_label= Label(root,text="Zip Code                 ",font=('Halvetica',10))
zip_code_label.grid(row=8,column=0, stick=W,pady=2)
select_id_label= Label(root,text="Select Id                  ",font=('Halvetica',10))
select_id_label.grid(row=11,column=0, stick=W,pady=2)

#Creating buttons
buttn_edit= Button(root, text="Update Record",command=edit, pady=5, bd=5, bg="white",font=('Halvetica',10))
buttn_edit.grid(row=12,column=0,columnspan=2, stick=W+E+N+S)

buttn_delete= Button(root, text="Delete Record",command=delete, pady=5, bd=5, bg="white",font=('Halvetica',10))
buttn_delete.grid(row=13,column=0,columnspan=2, stick=W+E+N+S)


buttn_exit= Button(root, text="Exit",command=exit, pady=5, bd=5, bg="red",font=('Halvetica',10))
buttn_exit.grid(row=14,column=0,columnspan=2, stick=W+E+N+S)

# # Creating Labels for search

# head_1 = Label(root,text= "Search For Donor", font=('Halvetica',25),bg='white')
# head_1.grid(row=0, column=2,columnspan=2,stick=W+E+N+S, padx=50)


# label_blood= Label(root,text="Select Blood Group",font=('Halvetica',10))
# label_blood.grid(row=1, column=2, stick=W, pady=2, padx=50)

# select = Entry(root)
# select.grid(row=1, column=3)

# global select_blood
# select_blood= ttk.Combobox(root, value=bloodgroups)
# select_blood.set("Select Blood Group")
# select_blood.grid(row=1, column=3, stick=W, pady=2, padx=50)

# # Creating Search Button to search donors

# search_buttn= Button(root, text="Search For Donors", command=search)
# search_buttn.grid(row=2, column=2, stick=W+E+N+S, padx=50)

conn.commit()

conn.close()

root.mainloop()