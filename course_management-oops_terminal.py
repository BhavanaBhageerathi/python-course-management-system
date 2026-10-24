#import python mysql connector
import mysql.connector
import os

#Creating a class for database variables and its functions
class Database:
    #when we create an object, it should be automatically initialized
    #so lets create a constructor
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = os.getenv('DB_HOST'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        self.create_tables() #create tables if not exists
    #a function to create the required tables (if already not exists)
    def create_tables(self):
        cur = self.conn.cursor() #create a cursor object from the connection
        #execute the create table queries
        cur.execute('''create table if not exists users (username varchar(50) primary key, password varchar(50) not null)''')
        cur.execute('''create table if not exists courses (id int primary key auto_increment, name varchar(50) not null, fee int not null)''')
        self.conn.commit() #write the changes to db permanently

    #override the default execute function so that we can 
    #have some additional functionalities
    #override - to create a function with same name execute()
    #additional options include parameters and a fetch boolean
    def execute(self, query, params=(), fetch=False):
        cur = self.conn.cursor()
        #print(query)
        #print(params)
        cur.execute(query, params) #actual execute() fn
        if not fetch:
            self.conn.commit()
        #if fetch is set to True, then run fetchall() else do not fetch
        return cur.fetchall() if fetch else None



#create a user class which have functions login and registration
class User:
    #create a constructor so that we can initialize the db connection
    #by passing the db object into it. for Course class also 
    #we will do the same
    #or else we have to repeat the db connection for all the classes
    def __init__(self,db):
        self.db = db #since db is an instance variable (self.) it can be
        #used in other functions of the class
    #create the functionalities for user classs eg: login, registration etc
    def login(self):
        #get login and password from user and check against the user table
        #we dont have to use self. because we dont want this as an instance
        #variable, just keep it as local since we dont want any other fn 
        #to access it
        print("Please login")
        username = input("Enter Username:").strip()
        password = input("Enter Password:").strip()
        result = self.db.execute('''select * from users where username=%s and password=%s''',
                                 (username,password),
                                 fetch=True)
        #if there is a valid result, return true, else return false
        if result:
            print("login success")
            return True
        else:
            print("Invalid login")
            return False       
    def register(self):
        while True:
            print("========Register User=======")
            username = input("Enter Username:").strip()
            password = input("Enter Password:").strip()
            #ehcek if username or password is blank
            if not username or not password:
                print("Username or password cannot be empty")
                continue
            #check if username already exists
            check_existing = self.db.execute('''select * from users where username=%s''',
                                             (username,),fetch=True)
            if check_existing:
                print("Username already exists")
            #if everything is fine, save the user
            else:
                self.db.execute('''insert into users (username, password) values(%s,%s)''',
                                        (username,password),
                                        fetch=False)
                print("Registration success!!")
                return True
        
#create class for course to include all functionalities of course
#eg: show menu, add course, edit, delete
class Course:
    #the same constructor that we used in user class
    #coz course also need db connection and db object
    def __init__(self,db):
        self.db = db
    #function to show the menu related to course
    def show_menu(self):
        while True: #show the menu indefinintely 
            print('''
            ======COURSE MANAGEMENT SYSTEM======
            1. List courses, 2. Add course, 3. Edit, 4. Delete, 5. Logout
            ''')
            choice = input("Enter your choice:").strip()
            if choice=='1':
                self.view_courses() #will create the functions later
            elif choice=='2':
                self.add_course()
            elif choice=='3':
                self.edit_course()
            elif choice=='4':
                self.delete_course()
            elif choice=='5':
                print("Logging out...")
                break
            else:
                print("invalid choice")
    #function to show all the courses
    def view_courses(self):
        print("========List of Courses=======")
        print("course id            course name        fee")
        print("--------------------------------------------")
        courses = self.db.execute("select * from courses", fetch=True)
        for each_course in courses:
            print(each_course[0],"    ",each_course[1],"     ",each_course[2])
        print() #insert a new line
    #function to add course
    def add_course(self):
        print("========Add Course=======")
        name = input("Enter course name:").strip()
        fee = input("Enter course fee:").strip()
        #check if name is valid/not none and fee is a digit
        if name and fee.isdigit():
            self.db.execute('''insert into courses (name,fee) values (%s,%s)''',(name,int(fee)))
            print("course added!!")
        else:
            print("Invalid input")
        #function to add course
    #function to edit course
    def edit_course(self):
        print("========Edit Course=======")
        cid = input("Enter course id to edit:").strip()
        name = input("Enter new course name:").strip()
        fee = input("Enter new course fee:").strip()
        #check if name is valid/not none and fee is a digit
        if cid.isdigit() and name and fee.isdigit():
            self.db.execute('''update courses set name=%s, fee=%s where id=%s''',(name,int(fee),int(cid)))
            print("course edited!!")
        else:
            print("Invalid input")
        #function to edit course
    #function to delete course
    def delete_course(self):
        print("========delete Course=======")
        cid = input("Enter course id to delete:").strip()
        #check if name is valid/not none and fee is a digit
        if cid.isdigit():
            self.db.execute('''delete from courses where id=%s''',(int(cid),))
            print("course deleted!!")
        else:
            print("Invalid input")


#define our main class and inside that create a run function
# that will run when the program starts
class CourseApp:
    def __init__(self):
        #whenever the course app obj is created, create obj of all other classes
        self.db = Database() #create object of our database class
        self.user = User(self.db) #create obj for User and pass db object
        self.course = Course(self.db)
    
    def run(self):
        #print menu to login/register/exit
        #use indefinite while loop to show the menu until user select exit
        while True:

            print("+----------------------------------------------------------+")
            print("|                                                          |")
            print("|  ======== WELCOME TO COURSE MANAGEMENT SYSTEM ========   |")
            print("|                                                          |")
            print("+----------------------------------------------------------+")

            print('''
                  select an option
                  1. Login
                  2. Register
                  3. Exit''')
            #get the option from user
            choice = input("Enter your choice:").strip()
            if choice == '1':
                #execute the login() fn and if result is true, show dashboard
                if self.user.login():
                    self.course.show_menu()
            elif choice == '2':
                #execute the register() fn and if result is true, show dashboard
                if self.user.register():
                    self.course.show_menu()
            elif choice == '3':
                print("Exiting the program")
                break
            else:
                print("invalid choice")

#if I am importing this file, do not execute it directly
#if I am running this file directly by clicking run, then execute the file
#python assume that when running a file, the first function to run is __main__
if __name__=="__main__":
    #Run the run() fn inside the courseapp class
    app = CourseApp()
    app.run()