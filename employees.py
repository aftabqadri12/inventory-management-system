from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import pymysql


def connect_database():
    try:
        connection = pymysql.connect(host="localhost", user="root", password="Bachi1400_")
        cursor = connection.cursor()
    except:
        messagebox.showerror("Error", "Connection Error")
        return
    cursor.execute('CREATE DATABASE IF NOT EXISTS inventory_system')
    cursor.execute('use inventory_system')
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS 
                       employee_data(
                       emID INT PRIMARY KEY,
                       name VARCHAR(100),
                       email VARCHAR(100),
                       gender VARCHAR(50),
                       dob VARCHAR(30),
                       contact VARCHAR(30),
                       employment VARCHAR(50),
                       work_shift VARCHAR(50),
                       education VARCHAR(50),
                       address VARCHAR(100),
                       doj VARCHAR(30),
                       salary VARCHAR(30),
                       password VARCHAR(50)
                       )
                   """)

connect_database()


def employee_form(window):
    global back_image
    employee_frame = Frame(window, width=1070, height=567, bg="white")
    employee_frame.place(x=200, y=100)
    heading_label = Label(employee_frame, text="Manage Employee Details", font=("times new roman", 16, "bold"),
                          bg="#0f4d7d", fg="white")
    heading_label.place(x=0, y=0, relwidth=1)
    back_image = PhotoImage(file="back.png")
    back_button = Button(employee_frame, image=back_image, bd=0, cursor='hand2', bg="white",
                         command=lambda: employee_frame.place_forget())
    back_button.place(x=10, y=30)

    top_frame = Frame(employee_frame, bg="white")
    top_frame.place(x=0, y=60, relwidth=1, height=235)
    search_frame = Frame(top_frame, bg="white")
    search_frame.pack()
    search_combobox = ttk.Combobox(search_frame, values=["ID", "Name", "Email"], font=("times new roman", 12),
                                   state="readonly")
    search_combobox.set('Search By')
    search_combobox.grid(row=0, column=0, padx=20)

    search_entry = Entry(search_frame, font=("times new roman", 12), bg="lightyellow")
    search_entry.grid(row=0, column=1)

    search_button = Button(search_frame, text="Search", font=("times new roman", 12), width=10, cursor='hand2')
    search_button.grid(row=0, column=2, padx=20)

    search_button = Button(search_frame, text="Show All", font=("times new roman", 12), width=10, cursor='hand2')
    search_button.grid(row=0, column=3)

    horizontal_scrollbar = Scrollbar(top_frame, orient=HORIZONTAL)
    vertical_scrollbar = Scrollbar(top_frame, orient=VERTICAL)

    employee_treeview = ttk.Treeview(top_frame,
                                     columns=("emID", "name", "email", 'gender', 'dob', 'contact', 'employement-type',
                                              'education', 'work_shift', 'address', 'doj', 'salary', 'usertype'),
                                     show="headings", yscrollcommand=vertical_scrollbar.set,
                                     xscrollcommand=horizontal_scrollbar.set)
    horizontal_scrollbar.pack(side=BOTTOM, fill=X)
    vertical_scrollbar.pack(side=RIGHT, fill=Y)
    horizontal_scrollbar.config(command=employee_treeview.xview)
    vertical_scrollbar.config(command=employee_treeview.yview)

    employee_treeview.pack(pady=(10, 0))

    employee_treeview.heading("emID", text='EMP_ID')
    employee_treeview.heading("name", text="Name")
    employee_treeview.heading("email", text="Email")
    employee_treeview.heading("gender", text="Gender")
    employee_treeview.heading("dob", text="Date of Birth")
    employee_treeview.heading("contact", text="Contact")
    employee_treeview.heading("employement-type", text="Employement-type")
    employee_treeview.heading("education", text="Education")
    employee_treeview.heading("work_shift", text="Work_shift")
    employee_treeview.heading("address", text="Address")
    employee_treeview.heading("doj", text="Date Of Joining")
    employee_treeview.heading("salary", text="Salary")
    employee_treeview.heading("usertype", text="Usertype")

    employee_treeview.column('emID', width=60)
    employee_treeview.column('name', width=140)
    employee_treeview.column('email', width=180)
    employee_treeview.column('gender', width=80)
    employee_treeview.column('dob', width=100)
    employee_treeview.column('contact', width=100)
    employee_treeview.column('employement-type', width=120)
    employee_treeview.column('education', width=120)
    employee_treeview.column('work_shift', width=100)
    employee_treeview.column('address', width=200)
    employee_treeview.column('doj', width=100)
    employee_treeview.column('salary', width=140)
    employee_treeview.column('usertype', width=120)

    detail_frame = Frame(employee_frame)
    detail_frame.place(x=20, y=300)

    empid_label = Label(detail_frame, text="EmpId", font=('times new roman', 12))
    empid_label.grid(row=0, column=0, padx=20, pady=10)
    empId_entry = Entry(detail_frame, font=('times new roman', 12), bg='lightyellow')
    empId_entry.grid(row=0, column=1, padx=20, pady=10)

    name_label = Label(detail_frame, text="Name", font=('times new roman', 12))
    name_label.grid(row=0, column=2, padx=20, pady=10)
    name_entry = Entry(detail_frame, font=('times new roman', 12), bg='lightyellow')
    name_entry.grid(row=0, column=3, padx=20, pady=10)

    email_label = Label(detail_frame, text="Email", font=('times new roman', 12))
    email_label.grid(row=0, column=4, padx=20, pady=10)
    email_entry = Entry(detail_frame, font=('times new roman', 12), bg='lightyellow')
    email_entry.grid(row=0, column=5, padx=20, pady=10)

    gender_label = Label(detail_frame, text="Gender", font=('times new roman', 12))
    gender_label.grid(row=1, column=0, padx=20, pady=10)

    gender_combobox = ttk.Combobox(detail_frame, values=["le", "Female"], font=('times new roman', 12), width=18,
                                   state='readonly')
    gender_combobox.set("Select Gender")
    gender_combobox.grid(row=1, column=1)

    dob_label = Label(detail_frame, text="Date Of Birth", font=('times new roman', 12))
    dob_label.grid(row=1, column=2, padx=20, pady=10)

    dob_date_entry = DateEntry(detail_frame, width=18, font=('times new roman', 12), state='readonly',
                               date_pattern="dd/mm/yyyy")
    dob_date_entry.grid(row=1, column=3)

    contact_label = Label(detail_frame, text="Contact", font=('times new roman', 12))
    contact_label.grid(row=1, column=4, padx=20, pady=10)

    contact_entry = Entry(detail_frame, font=('times new roman', 12), bg='lightyellow')
    contact_entry.grid(row=1, column=5, padx=20, pady=10)

    emp_type__label = Label(detail_frame, text="Employment Type", font=('times new roman', 12))
    emp_type__label.grid(row=2, column=0, padx=20, pady=10)

    emp_type__combobox = ttk.Combobox(detail_frame, values=["Full Time", "Part Time", "Casual", "Contract", 'Intern'],
                                      font=('times new roman', 12), width=18,
                                      state='readonly')
    emp_type__combobox.set("Select Type")
    emp_type__combobox.grid(row=2, column=1)

    education_label = Label(detail_frame, text="Education", font=('times new roman', 12))
    education_label.grid(row=2, column=2, padx=20, pady=10)

    education_options = ["B.Tech", "B.Com", "M.Tech", "M.Com", "B.Sc", "M.Sc", "BBA", "MBA", "LLB", "LLM",
                         "B.Arch",
                         "M.Arch"]

    education_combobox = ttk.Combobox(detail_frame, values=education_options, font=('times new roman', 12), width=18,
                                      state='readonly')
    education_combobox.set("Select Education")
    education_combobox.grid(row=2, column=3)

    workshift_label = Label(detail_frame, text="Work shift", font=('times new roman', 12))
    workshift_label.grid(row=2, column=4, padx=20, pady=10)

    workshift_combobox = ttk.Combobox(detail_frame, values=["Morning", "Evening", "Night"],
                                      font=('times new roman', 12), width=18,
                                      state='readonly')
    workshift_combobox.set("Select Shift")
    workshift_combobox.grid(row=2, column=5)

    address_label = Label(detail_frame, text="Address", font=('times new roman', 12))
    address_label.grid(row=3, column=0, padx=20, pady=10)

    address_text = Text(detail_frame, width=20, height=3, font=('times new roman', 12), bg='lightyellow')
    address_text.grid(row=3, column=1, rowspan=2)

    doj_label = Label(detail_frame, text="Date Of Joining", font=('times new roman', 12))
    doj_label.grid(row=3, column=2, padx=20, pady=10)

    doj_date_entry = DateEntry(detail_frame, width=18, font=('times new roman', 12), state='readonly',
                               date_pattern="dd/mm/yyyy")
    doj_date_entry.grid(row=3, column=3)

    usertype_label = Label(detail_frame, text="User Type", font=('times new roman', 12))
    usertype_label.grid(row=4, column=2, padx=20, pady=10)

    usertype_combobox = ttk.Combobox(detail_frame, values=["Admin", "Employee"],
                                     font=('times new roman', 12), width=18,
                                     state='readonly')
    usertype_combobox.set("Select Shift")
    usertype_combobox.grid(row=4, column=3)

    salary_label = Label(detail_frame, text="Salary", font=('times new roman', 12))
    salary_label.grid(row=3, column=4, padx=20, pady=10)

    salary_entry = Entry(detail_frame, font=('times new roman', 12), bg='lightyellow')
    salary_entry.grid(row=3, column=5, padx=20, pady=10)

    password_label = Label(detail_frame, text="Password", font=('times new roman', 12))
    password_label.grid(row=4, column=4, padx=20, pady=10)

    password_entry = Entry(detail_frame, font=('times new roman', 12), bg='lightyellow')
    password_entry.grid(row=4, column=5, padx=20, pady=10)

    button_frame = Frame(employee_frame, bg="white")
    button_frame.place(x=200, y=530)

    add_button = Button(button_frame, text="Add", font=("times new roman", 12), width=10, cursor='hand2', fg="white",
                        bg="#0f4d7d")
    add_button.grid(row=0, column=0, padx=20)

    update_button = Button(button_frame, text="Update", font=("times new roman", 12), width=10, cursor='hand2',
                           fg="white",
                           bg="#0f4d7d")
    update_button.grid(row=0, column=1, padx=20)

    delete_button = Button(button_frame, text="Delete", font=("times new roman", 12), width=10, cursor='hand2',
                           fg="white",
                           bg="#0f4d7d")
    delete_button.grid(row=0, column=2, padx=20)

    clear_button = Button(button_frame, text="Clear", font=("times new roman", 12), width=10, cursor='hand2',
                          fg="white",
                          bg="#0f4d7d")
    clear_button.grid(row=0, column=3, padx=20)
