
from tkinter import *
from PIL import Image,ImageTk
import os
import re

def trueflmaker():
   global truefl
   filer=[0,0,0,00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   truefl=[]
   regex = ".*\.txt"
   lines = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   list_of_files = os.listdir()
   course=value_inside.get()+"\n"
   count1=0
   count2=0
   for file in list_of_files:
      if(re.fullmatch(regex, file)) :
         filer[count1]=file
         count1=count1+1
   for file in filer:
      with open(file, 'r') as f:
       lines = f.readlines()
      for line in lines: 
         if(line==course):
            truefl.append(file)
            count2=count2+1

def searchapp_extract():
    top = Tk()   
    top.geometry("500x500")  
        
    providerv= [0,0,0,0,0,0,0,0,0,0,0] 
    lines = []
    with open(searchvr.get()) as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        
        providerv[count]=line
        print(f'line {count}: {line}') 
        count += 1

    username_info = providerv[0]
    fullname_info = providerv[1]
    email_info =providerv[2]
    phone_info =providerv[3]
    gender_info=providerv[4]
    country_info=providerv[5]
    lang1_info=providerv[6]

    print(providerv)
    Label(top,text="Applicant details", font=("Calibri", 17)).place(x=70,y=15)
    user_name = Label(top, text = "User Name:"+ username_info, font=("Calibri", 13)).place(x = 40, y = 50) 
    full_name = Label(top, text = "Full Name:"+ fullname_info, font=("Calibri", 13)).place(x = 40, y = 80)
    email1 = Label(top, text = "Email:"+ email_info, font=("Calibri", 13)).place(x = 40, y = 110) 
    phone = Label(top, text = "Phone No:"+ phone_info, font=("Calibri", 13)).place(x = 40, y = 140) 

    gender=Label(top, text = "Gender:"+ gender_info, font=("Calibri", 13)).place(x = 40, y = 170) 

    country = Label(top, text = "Country:"+ country_info, font=("Calibri", 13)).place(x = 40, y = 200)
    lang1=Label(top, text = "Language:"+ lang1_info, font=("Calibri", 13)).place(x = 40, y = 230)

    top.mainloop() 


def opensearch():
    #trueflmaker()
    global searchvr
    top = Tk()   
    top.geometry("650x400")  
    Label(top,text="Applications Submitted:", font=("Calibri", 17)).place(x=70,y=15)
    Label(top, text = "Applications for this course are:", font=("Calibri", 12)).place(x = 40, y = 50) 
    #for i in range(truefl.length()):
      #Label(top, text = truefl[i] , font=("Calibri", 12)).place(x = 40, y = 75)
    global searchvr
    Label(top, text = "search for application file", font=("Calibri", 12)).place(x = 30, y = 155) 
    searchvr=Entry(top)
    searchvr.place(x=250, y=155)
    
    search_button = Button(top, text='search', command=searchapp_extract).place(x=300,y=250)
    top.mainloop()



def openarch():
    global top
    top = Tk()   
    top.geometry("600x400")  
    Label(top,text="Architecture Internship", font=("Calibri", 17)).place(x=70,y=15)
    Label(top, text = "Architecture, the art and technique of designing and building,", font=("Calibri", 12)).place(x = 40, y = 50) 
    Label(top, text = "as distinguished from the skills associated with construction. ", font=("Calibri", 12)).place(x = 40, y = 75) 
    Label(top, text = "The practice of architecture is employed to fulfill both practical and ", font=("Calibri", 12)).place(x = 40, y = 100) 
    Label(top, text = "expressive requirements, and thus it serves both utilitarian and aesthetic ends.", font=("Calibri", 12)).place(x = 40, y = 125) 
    Label(top, text = "Duration:3 months", font=("Calibri", 12)).place(x = 40, y = 150) 
    Label(top, text = "Phone No:9032421678", font=("Calibri", 12)).place(x = 40, y = 175) 
    Label(top, text = "Address:Hyderabad,India", font=("Calibri", 12)).place(x = 40, y = 200) 
    apply_button = Button(top, text='Apply', command=apply_form).place(x=300,y=250)
    apply1_button = Button(top, text='See applicants', command=opensearch).place(x=100,y=250)
    top.mainloop()

def openfarm():
    top = Tk()   
    top.geometry("600x400")  
    Label(top,text=" Internship on farming", font=("Calibri", 17)).place(x=70,y=15)
    Label(top, text = "Farming is the act or process of working the ground, planting seeds, and growing", font=("Calibri", 12)).place(x = 40, y = 50) 
    Label(top, text = "edible plants. You can also describe raising animals for milk or meat as farming. Farming is ", font=("Calibri", 12)).place(x = 40, y = 75) 
    Label(top, text = "a great way to describe the lifestyle and work of people whose jobs are in the agriculture", font=("Calibri", 12)).place(x = 40, y = 100) 
    Label(top, text = "industry.Farming is a remarkable part of the economy in India.", font=("Calibri", 12)).place(x = 40, y = 125) 
    Label(top, text = "Duration:3 months", font=("Calibri", 12)).place(x = 40, y = 150) 
    Label(top, text = "Phone No:9032421678", font=("Calibri", 12)).place(x = 40, y = 175) 
    Label(top, text = "Address:Hyderabad,India", font=("Calibri", 12)).place(x = 40, y = 200) 
    apply_button = Button(top, text='Apply', command=apply_form).place(x=300,y=250)
    apply1_button = Button(top, text='See applicants', command=opensearch).place(x=100,y=250)
    top.mainloop()
    
def opendata():
    top = Tk()   
    top.geometry("650x400")  
    Label(top,text="Internship on Data Analysis", font=("Calibri", 17)).place(x=70,y=15)
    Label(top, text = "A data analyst collects and stores data on sales numbers, market research, logistics,", font=("Calibri", 12)).place(x = 40, y = 50) 
    Label(top, text = "linguistics, or other behaviors. They bring technical expertise to ensure the quality and", font=("Calibri", 12)).place(x = 40, y = 75) 
    Label(top, text = "accuracy of that data, then process, design, and present it in ways to help people, ", font=("Calibri", 12)).place(x = 40, y = 100) 
    Label(top, text = "businesses, and organizations make better decisions.", font=("Calibri", 12)).place(x = 40, y = 125) 
    Label(top, text = "Duration:3 months", font=("Calibri", 12)).place(x = 40, y = 150) 
    Label(top, text = "Phone No:9032421678", font=("Calibri", 12)).place(x = 40, y = 175) 
    Label(top, text = "Address:Hyderabad,India", font=("Calibri", 12)).place(x = 40, y = 200) 
    apply_button = Button(top, text='Apply', command=apply_form).place(x=300,y=250)
    apply1_button = Button(top, text='See applicants', command=opensearch).place(x=100,y=250)
    top.mainloop()

def openhair():
    top = Tk()   
    top.geometry("650x400")  
    Label(top,text="Internship on Hair Styling", font=("Calibri", 17)).place(x=70,y=15)
    Label(top, text = "Hair stylists are beauty service professionals who specialize in the fashioning", font=("Calibri", 12)).place(x = 40, y = 50) 
    Label(top, text = "and treatment of hair. Hair stylist responsibilities include cleaning and cutting", font=("Calibri", 12)).place(x = 40, y = 75) 
    Label(top, text = "hair, offering hair care and hair styling consultations and recommending ", font=("Calibri", 12)).place(x = 40, y = 100) 
    Label(top, text = "hair styling products, among other duties.", font=("Calibri", 12)).place(x = 40, y = 125) 
    Label(top, text = "Duration:3 months", font=("Calibri", 12)).place(x = 40, y = 150) 
    Label(top, text = "Phone No:9032421678", font=("Calibri", 12)).place(x = 40, y = 175) 
    Label(top, text = "Address:Hyderabad,India", font=("Calibri", 12)).place(x = 40, y = 200) 
    apply_button = Button(top, text='Apply', command=apply_form).place(x=300,y=250)
    apply1_button = Button(top, text='See applicants', command=opensearch).place(x=100,y=250)
    top.mainloop()

def openhr():
    top = Tk()   
    top.geometry("650x400")  
    Label(top,text="Internship on Human Resources", font=("Calibri", 17)).place(x=70,y=15)
    Label(top, text = "HR (Human Resources) department is a group who is responsible for managing the", font=("Calibri", 12)).place(x = 40, y = 50) 
    Label(top, text = "employee life cycle (i.e., recruiting, hiring, onboarding, training, and firing  ", font=("Calibri", 12)).place(x = 40, y = 75) 
    Label(top, text = "employees) and administering employee benefits.Working in HR can help shape the ", font=("Calibri", 12)).place(x = 40, y = 100) 
    Label(top, text = "employee work experience at every stage and create an organisational culture.", font=("Calibri", 12)).place(x = 40, y = 125) 
    Label(top, text = "Duration:3 months", font=("Calibri", 12)).place(x = 40, y = 150) 
    Label(top, text = "Phone No:9032421678", font=("Calibri", 12)).place(x = 40, y = 175) 
    Label(top, text = "Address:Hyderabad,India", font=("Calibri", 12)).place(x = 40, y = 200) 
    apply_button = Button(top, text='Apply', command=apply_form).place(x=300,y=250)
    apply1_button = Button(top, text='See applicants', command=opensearch).place(x=100,y=250)
    top.mainloop()
def openprog():
    top = Tk()   
    top.geometry("650x400")  
    Label(top,text="Internship on Programming", font=("Calibri", 17)).place(x=70,y=15)
    Label(top, text = "A programmer's day-to-day life is generally spent reading code, fixing errors, and", font=("Calibri", 12)).place(x = 40, y = 50) 
    Label(top, text = "writing new pieces of code. Programming is a highly mentally demanding job as it", font=("Calibri", 12)).place(x = 40, y = 75) 
    Label(top, text = "requires constant problem-solving. In addition to these tasks, there are also meetings", font=("Calibri", 12)).place(x = 40, y = 100) 
    Label(top, text = "with other programmers and stakeholders in the project.", font=("Calibri", 12)).place(x = 40, y = 125) 
    Label(top, text = "Duration:3 months", font=("Calibri", 12)).place(x = 40, y = 150) 
    Label(top, text = "Phone No:9032421678", font=("Calibri", 12)).place(x = 40, y = 175) 
    Label(top, text = "Address:Hyderabad,India", font=("Calibri", 12)).place(x = 40, y = 200) 
    apply_button = Button(top, text='Apply', command=apply_form).place(x=300,y=250)
    apply1_button = Button(top, text='See applicants', command=opensearch).place(x=100,y=250)
    top.mainloop()

def openvol():
    top = Tk()   
    top.geometry("650x400")  
    Label(top,text="Good Act of Volunteering", font=("Calibri", 17)).place(x=70,y=15)
    Label(top, text = "Volunteers donate time and energy for the benefit of other people in the community", font=("Calibri", 12)).place(x = 40, y = 50) 
    Label(top, text = "as a social responsibility rather than for any financial reward.", font=("Calibri", 12)).place(x = 40, y = 75) 
    Label(top, text = "Most of the time, to volunteer means that you are working side by side with others.", font=("Calibri", 12)).place(x = 40, y = 100) 
    Label(top, text = "You are connected with the community.", font=("Calibri", 12)).place(x = 40, y = 125) 
    Label(top, text = "Duration:2 days", font=("Calibri", 12)).place(x = 40, y = 150) 
    Label(top, text = "Phone No:9032421678", font=("Calibri", 12)).place(x = 40, y = 175) 
    Label(top, text = "Address:Hyderabad,India", font=("Calibri", 12)).place(x = 40, y = 200) 
    apply_button = Button(top, text='Apply', command=apply_form).place(x=300,y=250)
    apply1_button = Button(top, text='See applicants', command=opensearch).place(x=100,y=250)
    top.mainloop()



def viewcourse():
    print(value_inside.get())
    if(value_inside.get()=="Architechture"):
        openarch()
    if(value_inside.get()=="Farming"):
        openfarm()
    if(value_inside.get()=="Data-analysis"):
        opendata()
    if(value_inside.get()=="Hair-styling"):
        openhair()
    if(value_inside.get()=="Human-resources"):
        openhr()
    if(value_inside.get()=="Programming"):
        openprog()  
    if(value_inside.get()=="Volunteering"):
        openvol() 
   


def apply_user():
    chosencourse=value_inside.get()
    username_info = entry_11.get()
    fullname_info = entry_1.get()
    email_info =entry_3.get()
    phone_info =entry_33.get()
    gender_info=var.get()
    country_info=c.get()
    lang1_info=var1.get()
    

    file = open(username_info+".txt", "w")
    file.write(username_info + "\n")
    file.write(fullname_info + "\n")
    file.write(email_info + "\n")
    file.write(phone_info + "\n")
    file.write(str(gender_info) + "\n")
    file.write(country_info + "\n")
    file.write(str(lang1_info) + "\n")
    file.write(chosencourse + "\n")
    
    file.close()
    Label(root, text="Application success", fg="green", font=("calibri", 11)).pack()


def apply_form():
    #Creating object 'root' of Tk()
    global root
    root = Tk()
    global entry_1
    global entry_11
    global entry_33
    global entry_3
    global c
    global var
    global var1
    global var2
    global var3

    #Providing Geometry to the form
    root.geometry("500x500")

    #Providing title to the form
    root.title('Application form')

    #this creates 'Label' widget for Registration Form and uses place() method.
    label_0 =Label(root,text="Application form", width=20,font=("bold",20))
    #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    label_0.place(x=90,y=60)

    label_11 =Label(root,text="Username", width=20,font=("bold",10))
    label_11.place(x=80,y=125)

    #this will accept the input string text from the user.
    entry_11=Entry(root)
    entry_11.place(x=240,y=125)

    #this creates 'Label' widget for Fullname and uses place() method.
    label_1 =Label(root,text="FullName", width=20,font=("bold",10))
    label_1.place(x=80,y=150)

    #this will accept the input string text from the user.
    entry_1=Entry(root)
    entry_1.place(x=240,y=150)

    #this creates 'Label' widget for Email and uses place() method.
    label_3 =Label(root,text="Email", width=20,font=("bold",10))
    label_3.place(x=68,y=180)

    entry_3=Entry(root)
    entry_3.place(x=240,y=180)

    #this creates 'Label' widget for Email and uses place() method.
    label_33 =Label(root,text="Phone.no", width=20,font=("bold",10))
    label_33.place(x=68,y=200)

    entry_33=Entry(root)
    entry_33.place(x=240,y=200)

    #this creates 'Label' widget for Gender and uses place() method.
    label_4 =Label(root,text="Gender", width=20,font=("bold",10))
    label_4.place(x=70,y=230)
    var=Entry(root)
    var.place(x=235,y=230)
    
    #the variable 'var' mentioned here holds Integer Value, by deault 0
   
   

    ##this creates 'Label' widget for country and uses place() method.
    label_5=Label(root,text="Country",width=20,font=("bold",10))
    label_5.place(x=70,y=280)

    #this creates list of countries available in the dropdownlist.
    list_of_country=[ 'India' ,'US' , 'UK' ,'Germany' ,'Austria']

    #the variable 'c' mentioned here holds String Value, by default ""
    c=StringVar()
    droplist=OptionMenu(root,c, *list_of_country)
    droplist.config(width=15)
    c.set('Select your Country')
    droplist.place(x=240,y=280)

    ##this creates 'Label' widget for Language and uses place() method.
    label_6=Label(root,text="Language",width=20,font=('bold',10))
    label_6.place(x=75,y=330)


    var1=Entry(root)
    var1.place(x=200,y=330)
    #this creates button for submitting the details provides by the user
    Button(root, text='Submit' , width=20,bg="black",fg='white',command= apply_user).place(x=180,y=380)


    #this will run the mainloop.
    root.mainloop()
    return None

def courseopt():
    global value_inside
    root = Tk()
    root.title("Choose an Option")
    root.geometry('700x500')
  
# Create the list of options
    options_list = ['Architechture',  'Farming',
                        'Data-analysis', 'Hair-styling', 'Human-resources', 'Programming', 'Volunteering']
  
# Variable to keep track of the option
# selected in OptionMenu
    value_inside = StringVar(root)
  
# Set the default value of the variable
    value_inside.set("Select an internship you want to explore")
  
# Create the optionmenu widget and passing 
# the options_list and value_inside to it.
    question_menu = OptionMenu(root, value_inside, *options_list)
    question_menu.pack()
    submit_button = Button(root, text='Submit', command=print_answers)
    global apply_button
    apply_button = Button(root, text='Apply', command=apply_form)
    
    submit_button.pack()
    root.mainloop()

# Function to print the submitted option-- testing purpose

  
def print_answers():
    Label(text="Selected choice:"+value_inside.get(), bg="blue", width="50", height="50", font=("Calibri", 13)).pack()
    print("Selected Option: {}".format(value_inside.get()))
    viewcourse()

    return None
  
  
# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose


    
   

  
