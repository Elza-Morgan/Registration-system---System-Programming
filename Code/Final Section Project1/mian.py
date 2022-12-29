from tkinter import *
from tkinter.filedialog import askopenfile # for button that browse files
from tkinter import messagebox
import mysql.connector
import json # for reading/writing json files
from tkinter import ttk # for displaying the students list as treeview
from tkinter import PhotoImage #for displaying image from json
from PIL import Image,ImageTk #for resizing the image
from functools import partial
import os



def MainScreen():
    #used to create the screen which is the big window
    #down here we have some properties or attributes for creating the screen 
    screen = Tk()#TK is the GUI library, that's how screen is created
    screen.title('Registration System')
    screen.geometry('600x300')
    screen.config(bg="#447c84")
    #------------------------------------

    #that's used to create the fram which is found inside the screen, it's like a small window
    #some properties or attributes are used for screating the frame
    frame = Frame(screen, height=400,width=300,padx=20, pady=20)
    frame.config(bg="white")
    frame.pack_propagate(False)
    frame.pack(expand=True)
    
    #Label us used to create like a text
    Label(
        frame, #here it is used to specify where the label will be found
        #some attributes or properties added for the label
        text="Registration System", 
        font=("Times", "24", "bold") 
    ).grid(row=0,  columnspan=6, pady=10) #used to specify the postion of the label
    
    #creating a button for that label
    Enter = Button(
        frame, 
        text="Enter System", 
        padx=20, pady=10, 
        relief=RAISED, #used to make it like bevel 
        font=("Times", "16", "bold"), 
        #this line means when I click on this button destroy the screen it is at and then go to function EnterSystem
        command=lambda:[screen.destroy(),EnterSystem()] 
        ).grid(row=2, column=2, pady=10)
    #used to make the screen full screen
    screen.state("zoomed")
    screen.mainloop() #out of every screen created we must close it or end it in order to move onto the next screen

    #thats the function EnterSystem that will be called from line 52
def EnterSystem():
    #created another screen
    screen = Tk()
    screen.title('Registration System')
    screen.geometry('400x500')
    screen.config(bg="#447c84")
    #created another frame
    frame = Frame(screen, height=400,width=300,padx=20, pady=20)
    frame.config(bg="white")
    frame.pack_propagate(False)
    frame.pack(expand=True)

    #a text that is found inside the frame 
    Label(
        frame, 
        text="Registration System", 
        font=("Times", "24", "bold") 
    ).grid(row=0,  columnspan=6, pady=5)
    
    #button for the registeration which is found isnide the frame as well
    Reg = Button(
        frame,
        width=15,
        text="Register a Student", 
        padx=20, pady=5, 
        relief=RAISED, 
        font=("Times", "16", "bold"), 
        #this line means when I click on this button destroy the screen it is at and then go to function Registration
        command=lambda :[screen.destroy(),Registration()]
        ).grid(row=1, column=1, pady=15)

       #another button created for displaying the student info 
    Reg = Button(
        frame, width=15,
        text="Retrieve Student Info", 
        padx=20, pady=10, 
        relief=RAISED, 
        font=("Times", "16", "bold"), 
        #this line means when I click on this button destroy the screen it is at and then go to function readFromjson files
        command=lambda:[screen.destroy(), readFromJSON()]
        ).grid(row=2, column=1, pady=15)

        #button that is used to update the student if needed
    Upd = Button(
        frame, 
        width=15,
        text="Update Student Info", 
        padx=20, pady=10, 
        relief=RAISED, 
        font=("Times", "16", "bold"), 
        #this line means when I click on this button destroy the screen it is at and then go to function updateStudent
        command=lambda:[screen.destroy(), updateStudent()]
        ).grid(row=3, column=1, pady=15)

    #button that is used to delete any student if needed
    delete = Button(
        frame, 
        width=15,
        text="Delete Student", 
        padx=20, pady=10, 
        relief=RAISED, 
        font=("Times", "16", "bold"), 
        #this line means when I click on this button destroy the screen it is at and then go to function deleteStudent
        command=lambda:[screen.destroy(),deleteStudent()]
        ).grid(row=4, column=1, pady=15)
    
    
    screen.state("zoomed")
    screen.mainloop()
    #screen will be closed since we are done with this specifc screen
    

#function for registration that will be called from line 87
def Registration() :
    #another screen created for this function
    screen = Tk()
    screen.title('Registration System')
    screen.geometry('600x500')
    screen.config(bg="#447c84")
    
    #image of back button
    img = Image.open("H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/Untitled-4.png") #file path for the image
    resized = img.resize((50, 50), Image.ANTIALIAS) #setting the width and hight for the image, Image.antialias used so the image doesn't get pixled
    newimg = ImageTk.PhotoImage(resized) #used to view the image after it was stored in ram and redesigned it when needed
    
    #funciton for the back button when clicked on
    back = Button(
        screen, 
        image=newimg,
        padx=20, pady=10, 
        relief=RAISED, 
        borderwidth=0,
        background="#447c84",
       # this line means when I click on this button destroy the screen it is at and then go back to EnterSystem which is the main menu
        command=lambda:[screen.destroy(),EnterSystem()]
        )
    back.place(x=30,y=40)
    
    frame = Frame(screen, height=400,width=10,padx=20, pady=20)
    frame.config(bg="white")
    frame.pack_propagate(False)
    frame.pack(expand=True) 

    photo = Image.open("H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/avatar(1).jpg")#used to display the icon of profile in regsiter function
    resized = photo. resize((110, 75), Image.ANTIALIAS) #setting the width and hight for the image, Image.antialias used so the image doesn't get pixled
    NewImage = ImageTk.PhotoImage(resized)#used to view the image after it was stored in ram and redesigned it when needed
    
    #used to add picture on label
    label98 = Label(screen,bg="white",image=NewImage,width=70,height=70)
    label98.pack()#.pack makes adjustment autoamtically regarding vertical
    label98.place( x=820,y=250) # label for the image
    
    #used to create the label as a title 
    Label(
    frame, 
    text="Register a student",
    font=("Times", "24", "bold")
    ).grid(row=0, columnspan=3, pady=10)
    
    #used to create the label for button student id
    Label(
    frame, 
    text='Student Id', 
    font=("Times", "14")
    ).grid(row=1, column=0, pady=5)

    #this line we have created a global varibable in order to use it if needed
    global id1;id1= Entry(frame, width=30) #this line is used to create a textfiled 
    id1.pack() #to make it vertically automatiically with sutialbe spacing 
    id1.grid(row=1,column=1)#setting the postion for the textfield box
    
    #creating label or a text for in First Name
    Label(
    frame, 
    text='First Name', 
    font=("Times", "14")
    ).grid(row=2, column=0, pady=5)
    
    #this line we have created a global varibable in order to use it if needed
    global fname;fname = Entry(frame, width=30)#this line is used to create a textfiled
    fname.pack()
    fname.grid(row=2, column=1)#setting the postion for the textfield box
    
    #creating label or a text for in Last Name
    Label(
    frame, 
    text='Last Name', 
    font=("Times", "14")
    ).grid(row=3, column=0, pady=5)
    
    #this line we have created a global varibable in order to use it if needed
    global lname;lname = Entry(frame, width=30)#this line is used to create a textfiled
    lname.pack()
    lname.grid(row=3, column=1)#setting the postion for the textfield box
    
    #creating label or a text for Email 
    Label(
    frame, 
    text='Email Address', 
    font=("Times", "14")
    ).grid(row=4, column=0, pady=5)

    #this line we have created a global varibable in order to use it if needed
    global email; email = Entry(frame, width=30)#this line is used to create a textfiled
    email.pack()
    email.grid(row=4, column=1)#setting the postion for the textfield box
    
    #used to create button for register 
    finalReg = Button(
        frame,
        text="Register", 
        padx=20, pady=10, 
        relief=RAISED, 
        font=("Times", "16", "bold"), 
        command=addStudent #this is used to call the addStudent function
        ).grid(row=5, column=1, pady=5)

    #this function is called from the button at line 275
    def AutoFill():
        #created a varible that reads any file that ends with extension .json
        file = askopenfile(mode ='r', filetypes =[('Python Files', '*.json')]) 
        if file is not None:     
            data = json.load(file)
            # print(data)
            #used to delete or override the data if there is something from the start, number zero means deleting from the begining of the line
            id1.delete(0,'end')
            fname.delete(0,'end')
            lname.delete(0,'end')
            email.delete(0,'end')
            
            #used to insert the data of this student which will be rertived from the jason file
            #we have linked the line between what will be retived from jSon file and what will be displayed by calling the name of the texfield to be displayed at
            id1.insert(0,data["student_details"]["student_id"]) 
            fname.insert(0,data["student_details"]["student_fname"]) 
            lname.insert(0,data["student_details"]["student_lname"]) 
            email.insert(0,data["student_details"]["student_email"])
            
            #used to display the image
            img = Image.open(data["student_details"]["image"])#this will retrived from json file
            resized = img.resize((75, 75), Image.ANTIALIAS) #setting the width and hight for the image, Image.antialias used so the image doesn't get pixled
            NewImage = ImageTk.PhotoImage(resized)#used to view the image after it was stored in ram and redesigned it when needed
    
            #addes the images on  the label
            label98.config(image = NewImage)
            label98.image = NewImage
            print("done reading from json file")
        else:
            pass # show error msg (file not found)
        
    
    #creating the button for the auto fill it needs to be after the function in order to see it when you click on it
    Auto = Button(
        frame,
        text="Auto Fill", 
        padx=20, pady=10,
        relief=RAISED,
        font=("Times", "16", "bold"),
        command =AutoFill #used to call the function autofill
        ).grid(row=5, column=2, pady=5)

    #that a clear funtion for the button, in order to make the textfiled empty and enter the next student 
    def clear():
        id1.delete(0,'end')
        fname.delete(0,'end')
        lname.delete(0,'end')
        email.delete(0,'end')

        photo = Image.open("H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/avatar(1).jpg")#used to display the icon of profile in regsiter function
        resized = photo. resize((110, 75), Image.ANTIALIAS) #setting the width and hight for the image, Image.antialias used so the image doesn't get pixled
        NewImage = ImageTk.PhotoImage(resized)#used to view the image after it was stored in ram and redesigned it when needed

        label98.config(image = NewImage)
        label98.image = NewImage

     #creating the clear button
    Clr = Button(
        frame,
        text="Clear", 
        padx=20, pady=10,
        relief=RAISED,
        font=("Times", "16", "bold"),
        command =clear #callin the clear funtion from above
        ).grid(row=5, column=0, pady=5)
    
    screen.state('zoomed')
    screen.mainloop()
    #closing the screen for registering student
        
 #creating the function for adding a student       
def addStudent():
    idText = int(id1.get()) # here we did pasring because as a textfiled we recive it as a string but for id we want it int so we did parsing for it
    fnameText = fname.get()
    lnameText = lname.get()
    emailText = email.get()
    #used to add the student to the database
    try:
        my_connection = mysql.connector.connect(host="localhost",user="root",password="liza2000",
                                                port ="3306",database="project_database",auth_plugin='mysql_native_password') #creating connection with the databse
        
        print("You are connected to the database")
        cursor = my_connection.cursor() #enabling query in order to work with the result

        #here we are saying what you will retrive insert it in table called student in these coloumn this order and the type that will be added it string 
        # another words that's the query   
        cursor.execute("INSERT INTO students(studentID, studentFirstName,studentLastName, EmailAddress) VALUES (%s, %s , %s , %s)" , 
                       (idText,fnameText,lnameText,emailText)) 
        # this is used to save the changes that have been made to the table               
        my_connection.commit() 
        #this is used to display like a message box as an approval of the action made perviously
        messagebox.showinfo(title="Registered",message="Student has been registered")
        students=cursor.fetchall() #adding each row that contians information of student inside the students list

        for student in students:
            print(student)
        
         #used to display in complier or in consol   
        print("User Registered successfuly")
        
        ## adding student to json file
        entry = {
            'student_fname': fnameText,
            'student_lname': lnameText,
            'student_id': id1.get(),
            'student_email': emailText,
            'image':"H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/avatar(1).jpg"
            }
        with open('H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/Students_Info.json',"r")as f:
            data = json.load(f)
            data["student_details"].append(entry)
        with open('H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/Students_Info.json',"w") as f:
            # file.seek(0)
            json.dump(data, f, indent = 4)
            
    except Exception as ex:
        print("error"+str(ex)) #display the error if not entered in try

  #function used to readfromJson  
def readFromJSON():
    #creating screan for it
    screen = Tk()
    screen.title('Registration System')
    screen.geometry('700x500')
    screen.config(bg="#447c84")
    
    #image of back button
    img = Image.open("H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/Untitled-4.png")
    resized = img.resize((50, 50), Image.ANTIALIAS) 
    newimg = ImageTk.PhotoImage(resized)
    
    back = Button(
        screen, 
        image=newimg,
        padx=20, pady=10, 
        relief=RAISED, 
        borderwidth=0,
        background="#447c84",
        command=lambda:[screen.destroy(),EnterSystem()] #returns to the main menu
        )
    back.place(x=30,y=40)
    
    #reading from the json file and loads it up
    f = open('H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/Students_Info.json')
    data = json.load(f)#used to load the info that is stored in json file

    #used to display the infromtion that is retrived from jason   
    s = ttk.Style()
    s.configure("Treeview", rowheight =50)
    tree = ttk.Treeview(screen, columns=("First Name","Last Name", "ID", "Email"),height=len(data["student_details"]))
    #used to specify the order of the coloumn                                    #used to make the table in treeview to be dynamic not fixed
    tree.heading("#1", text="First Name")
    tree.heading("#2", text="Last Name")
    tree.heading("#3", text="ID")
    tree.heading("#4", text="Email")
    
    # tree.column("#0", stretch='No', width=100)
    tree.column('First Name',anchor='center', width=200)
    tree.column('Last Name',anchor='center', width=200)
    tree.column('ID',anchor='center', width=200)
    tree.column('Email', anchor='center', width=350)
    tree.pack(fill=BOTH, expand=True)
    tree.place(x=230,y=190) #sets overall table in the screen

    #used to put the data inside the table
    for i in data["student_details"]:
        tree.insert("", "end" ,values=(i["student_fname"],i["student_lname"], i["student_id"], i["student_email"]))
    f.close()#closes file that was open in line 353
    screen.state('zoomed')
    screen.mainloop() #used to close the screen for readfromjson

    #function that is used to delete the student 
def deleteStudent():
    screen = Tk()
    screen.title('Registration System')
    screen.geometry('700x500')
    screen.config(bg="#447c84")
    
    #image of back button
    img = Image.open("H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/Untitled-4.png")
    resized = img.resize((50, 50), Image.ANTIALIAS)
    newimg = ImageTk.PhotoImage(resized)
    
    back = Button(
        screen, 
        image=newimg,
        padx=20, pady=10, 
        relief=RAISED, 
        borderwidth=0,
        background="#447c84",
        command=lambda:[screen.destroy(),EnterSystem()]
        )
    back.place(x=30,y=40)
    
    frame = Frame(screen, height=400,width=10,padx=20, pady=20)
    frame.config(bg="white")
    frame.pack_propagate(False)
    frame.pack(expand=True) 
    
    lbl = Label(
    frame,
    text='Delete ID From Database',
    font=("Times", "14")
    ).grid(row=2, column=0, pady=5)
    
    value = Entry(frame, width=30) #creating a textfiled
    value.pack()
    value.grid(row=2,column=3)
    
    #inside funstion delete student there is another function to apply this action
    def applyDelete():
        print(value.get())
        value1 = int(value.get())#value refered to id as in textfield.
        try: #used to connect to the database
            my_connection = mysql.connector.connect(host="localhost",user="root",password="liza2000",
                                                    port ="3306",database="project_database",auth_plugin='mysql_native_password')
            
            print("You are connected to the database") #printed in consol for double checking
            cursor = my_connection.cursor() #used to let us create query in the database

            #that's the query that it will delete it from the database accoring to the id that will be inserted
            deleteQuery ="""DELETE FROM students WHERE studentID = %s""" 
            
            cursor.execute(deleteQuery,(value1,)) # the query 
            my_connection.commit() # this is used to save the changes that have been made to the table
            messagebox.showinfo(title="Deleted",message="Student has been Deleted") #displays a mesage box
            students = cursor.fetchall() 

            print(cursor.rowcount, "record(s) deleted")
            for student in students:
                print(student)
                
            print("User Deleted successfuly")
            
            with open('H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/Students_Info.json',"r")as f:
                data = json.load(f)
                for student in data["student_details"]:
                    if student["student_id"] == value.get():
                        data["student_details"].remove(student)
            with open('H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/Students_Info.json',"w") as f:
            # file.seek(0)
                json.dump(data, f, indent = 4)
            
            
        except Exception as ex:
            print(str(ex))
    
    
    #creating button for delete function
    btn = Button(
        frame,
        text="Delete", 
        padx=20, pady=10, 
        relief=RAISED, 
        font=("Times", "16", "bold"), 
        command=applyDelete #calling the deleting function
        ).grid(row=5, column=1, pady=5)
    
    screen.state("zoomed")
    screen.mainloop()
    #closing the screen for deleting

#function used to update any information of that student
def updateStudent():
    
    try:#opens connection with the database
        my_connection = mysql.connector.connect(host="localhost",user="root",password="liza2000",
                                           port ="3306",database="project_database",auth_plugin='mysql_native_password')
        print("You are connected to the database")   
        cursor = my_connection.cursor() #enable us to do query in the database
    except Exception as ex:
        print(str(ex))
    #screating screen for the update
    screen = Tk()
    screen.title('Registration System')
    screen.geometry('700x500')
    screen.config(bg="#447c84")
    
    #image of back button
    img = Image.open("H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/Untitled-4.png")
    resized = img.resize((50, 50), Image.ANTIALIAS)
    newimg = ImageTk.PhotoImage(resized)
    
    back = Button(
        screen, 
        image=newimg,
        padx=20, pady=10, 
        relief=RAISED, 
        borderwidth=0,
        background="#447c84",
        command=lambda:[screen.destroy(),EnterSystem()] #calls the main menu when clicked on
        )
    back.place(x=30,y=40)
    
    frame = Frame(screen, height=400,width=10,padx=20, pady=20)
    frame.config(bg="white")
    frame.pack_propagate(False)
    frame.pack(expand=True) 
    
    
    #created label for serching by id
    lbl = Label(
    frame,
    text='Search by ID',
    font=("Times", "14")
    ).grid(row=2, column=0, pady=5)
    
    value = Entry(frame, width=30) #creating a textfield for that label 
    value.pack()
    value.grid(row=2,column=2)
    
    
    
    #The upcoming labels are the filds that you can update for 
    #created first name label
    lbl2 = Label(
    frame,
    text='First Name',
    font=("Times", "14")
    ).grid(row=3, column=0, pady=5)
    
    value2 = Entry(frame, width=30) #creating text for first name label
    value2.pack()
    value2.grid(row=3,column=2)
    
    #funtion that used to update the first name
    def updateFirstName():
        try:
            updateQuery ="""UPDATE students SET studentFirstName = %s WHERE studentID = %s""" #change the student name as long as the id is the same
            cursor.execute(updateQuery,(value2.get(),int(value.get()),)) # the query
            my_connection.commit() #used to save the changes that is made in the database
            students = cursor.fetchall() #fetching the query
            print("user first name updated")
            messagebox.showinfo(title="Update",message="User First Name has been changed to "+value2.get()) #displaying a message box
            print(cursor.rowcount, "record(s) found") #prints in the consol the number row that is found the data acorrding to the id
            #this for loop is used to display the updated text field of first name along with the other data
            for user in students:
                value2.insert(0,user[1])
                
            with open('H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/Students_Info.json',"r")as f:
                data = json.load(f)
                for student in data["student_details"]:
                    if student["student_id"] == value.get():
                        student["student_fname"]=value2.get()
            with open('H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/Students_Info.json',"w") as f:
            # file.seek(0)
                json.dump(data, f, indent = 4)
            
        except Exception as ex:
            print(str(ex))
    #creating the update button
    btn2 = Button(
        frame,
        text="Update", 
        padx=20,
        relief=RAISED, 
        font=("Times", "16", "bold"), 
        command=updateFirstName #calling the update the firstname function
        ).grid(row=3, column=3, pady=5)
    
    #creating label for last name
    lbl3 = Label(
    frame,
    text='Last Name',
    font=("Times", "14")
    ).grid(row=4, column=0, pady=5)
    
    value3 = Entry(frame, width=30) #creating textfield for the last name
    value3.pack()
    value3.grid(row=4,column=2)
    
    #creating the function that is updated the last name
    def updateLastName():
        try:
            updateQuery ="""UPDATE students SET studentLastName = %s WHERE studentID = %s"""#change the student name as long as the id is the same
            cursor.execute(updateQuery,(value3.get(),int(value.get()),)) # the query
            my_connection.commit() #saves the updated table
            students = cursor.fetchall() #fetching the query
            print("user last name updated")
            messagebox.showinfo(title="Update",message="User Last Name has been changed to "+value3.get()) #display meesage box
            print(cursor.rowcount, "record(s) found")
            
            for user in students:
                value2.insert(0,user[2])
            with open('H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/Students_Info.json',"r")as f:
                data = json.load(f)
                for student in data["student_details"]:
                    if student["student_id"] == value.get():
                        student["student_lname"]=value3.get()
            with open('H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/Students_Info.json',"w") as f:
            # file.seek(0)
                json.dump(data, f, indent = 4)
        except Exception as ex:
            print(str(ex))

    #creats button for lastname
    btn3 = Button(
        frame,
        text="Update", 
        padx=20,  
        relief=RAISED, 
        font=("Times", "16", "bold"), 
        command=updateLastName #calls the function lastname update
        ).grid(row=4, column=3, pady=5)
    
 
    #creating the label for the email   
    lbl4 = Label(
    frame,
    text='Email',
    font=("Times", "14")
    ).grid(row=5, column=0, pady=5)
    
    value4 = Entry(frame, width=30)#creating textfield label email
    value4.pack()
    value4.grid(row=5,column=2)
    
    #function that is used to update the email
    def updateEmail():  
        try:
            updateQuery ="""UPDATE students SET EmailAddress = %s WHERE studentID = %s"""#change the student name as long as the id is the same
            cursor.execute(updateQuery,(value4.get(),int(value.get()),)) # the query
            my_connection.commit()#saves the changes in the table
            students = cursor.fetchall() #fetching the query
            print("user email updated")
            messagebox.showinfo(title="Update",message="User Email has been changed to "+value4.get())#display a message box after the action
            print(cursor.rowcount, "record(s) found")
            
            for user in students:
                value2.insert(0,user[3])
            with open('H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/Students_Info.json',"r")as f:
                data = json.load(f)
                for student in data["student_details"]:
                    if student["student_id"] == value.get():
                        student["student_email"]=value4.get()
            with open('H:/Computer Science/Term 7/Structure Programing/Section/12th project Elza,Youssef, Mohmed and Mohamed/Code/Students_Info.json',"w") as f:
            # file.seek(0)
                json.dump(data, f, indent = 4)
        except Exception as ex:
            print(str(ex))
    #creating button for updating the  email
    btn4 = Button(
        frame,
        text="Update", 
        padx=20, 
        relief=RAISED, 
        font=("Times", "16", "bold"), 
        command=updateEmail #then calls the function that updates the email
        ).grid(row=5, column=3, pady=5)
    
    #this function is used to apply the search and override the changes that had been made
    #this functtion perfoms the select query
    def applySearch():
        value2.delete(0,'end')
        value3.delete(0,'end')
        value4.delete(0,'end')
        
        print("ID = "+value.get())
        value1 = int(value.get()) #takes what's found in textfield of id adn then parse it in order to use it as intger
        try:
            SearchQuery ="""SELECT * FROM students WHERE studentID = %s"""
            cursor.execute(SearchQuery,(value1,)) # enables query in the database
            
            students = cursor.fetchall() 
            #used to fill the text field of fname,lname and email with the new data
            print(cursor.rowcount, "record(s) found")
            for user in students:
                value2.insert(0,user[1]) 
                value3.insert(0,user[2]) 
                value4.insert(0,user[3]) 
            
        except Exception as ex:
            print(str(ex))
    #button created for apply search
    btn = Button(
        frame,
        text="Search", 
        padx=20, pady=10, 
        relief=RAISED, 
        font=("Times", "16", "bold"), 
        command=applySearch #calls the for applyScreach function
        ).grid(row=6, column=3, pady=5)
    
    def clear():
        value.delete(0,'end')
        value2.delete(0,'end')
        value3.delete(0,'end')
        value4.delete(0,'end')

     #creating the clear button
    Clr = Button(
        frame,
        text="Clear", 
        padx=20, pady=10,
        relief=RAISED,
        font=("Times", "16", "bold"),
        command =clear #callin the clear funtion from above
        ).grid(row=6, column=0, pady=5)
    
    screen.state("zoomed")
    screen.mainloop()
#closes the screen for the update studnet function    

#starts the whole file that we are at
if __name__ =="__main__":
    MainScreen()
 

