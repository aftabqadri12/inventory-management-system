from tkinter import *

from employees import employee_form

# FUNCTIONALITY PART


# GUI PART
window = Tk()

window.title("Dashboard")
window.geometry("1270x668+0+0")
window.resizable(width=0, height=0)
window.config(bg="white")

bg_image = PhotoImage(file="inventory.png")

titleLable = Label(window, image=bg_image, compound=LEFT, text="Inventory Management System ",
                   font=("times new roman", 40, "bold"), bg="black", fg="white", anchor="w", padx=30)
titleLable.place(x=0, y=0, relwidth=1)

logoutButton = Button(window, text="logout", font=("times new roman", 20, "bold"))
logoutButton.place(x=1100, y=10)

subtitleLabel = Label(window, text="Welcome Admin\t\t Date: 05-11-2026\t\t Time: 10:30pm",
                      font=('times new roman', 15, 'bold'), bg="black", fg="white")
subtitleLabel.place(x=0, y=70, relwidth=1)

leftFrame = Frame(window, )
leftFrame.place(x=0, y=102, width=200, height=555)

logoImage = PhotoImage(file="check.png")
imageLabel = Label(leftFrame, image=logoImage, bg="blue")
imageLabel.pack(fill=X)

menuLabel = Label(leftFrame, text="Menu", font=('times new roman', 20), bg="brown")
menuLabel.pack(fill=X)

employee_icon = PhotoImage(file="man.png")
employeeButton = Button(leftFrame, image=employee_icon, compound=LEFT, text=" Employees",
                        font=("times new roman", 20, "bold"), anchor='w', padx=10,
                        command=lambda: employee_form(window))
employeeButton.pack(fill=X)

supplier_icon = PhotoImage(file="wholesale.png")
supplierButton = Button(leftFrame, image=supplier_icon, compound=LEFT, text=" Suppliers",
                        font=("times new roman", 20, "bold"), anchor='w', padx=10)
supplierButton.pack(fill=X)

category_icon = PhotoImage(file="cat.png")
categoryButton = Button(leftFrame, image=category_icon, compound=LEFT, text=" Categories",
                        font=("times new roman", 20, "bold"), anchor='w', padx=10)
categoryButton.pack(fill=X)

products_icon = PhotoImage(file="product.png")
productsButton = Button(leftFrame, image=products_icon, compound=LEFT, text=" Products",
                        font=("times new roman", 20, "bold"), anchor='w', padx=10)
productsButton.pack(fill=X)

sales_icon = PhotoImage(file="increase.png")
salesButton = Button(leftFrame, image=sales_icon, compound=LEFT, text=" Sales", font=("times new roman", 20, "bold"),
                     anchor='w', padx=10)
salesButton.pack(fill=X)

exit_icon = PhotoImage(file="exit.png")
exitButton = Button(leftFrame, image=exit_icon, compound=LEFT, text=" Exit", font=("times new roman", 20, "bold"),
                    anchor='w', padx=10)
exitButton.pack(fill=X)

emp_frame = Frame(window, bg='beige', bd=3, relief=RIDGE)
emp_frame.place(x=400, y=125, width=280, height=170)
total_emp_icon = PhotoImage(file="staff.png")
total_emp_icon_label = Label(emp_frame, image=total_emp_icon)
total_emp_icon_label.pack(pady=10)

total_emp_label = Label(emp_frame, text='Total Employees', fg="black", bg='beige', font=("times new roman", 15, "bold"))
total_emp_label.pack()

total_emp_count_label = Label(emp_frame, text='0', fg="black", bg='beige', font=("times new roman", 15, "bold"))
total_emp_count_label.pack()

sup_frame = Frame(window, bg='maroon', bd=3, relief=RIDGE)
sup_frame.place(x=800, y=125, width=280, height=170)
total_sup_icon = PhotoImage(file="supplier.png")
total_sup_icon_label = Label(sup_frame, image=total_sup_icon)
total_sup_icon_label.pack(pady=10)

total_sup_label = Label(sup_frame, text='Total Suppliers', fg="black", bg='maroon',
                        font=("times new roman", 15, "bold"))
total_sup_label.pack()

total_sup_count_label = Label(sup_frame, text='0', fg="black", bg='maroon', font=("times new roman", 15, "bold"))
total_sup_count_label.pack()

cat_frame = Frame(window, bg='green', bd=3, relief=RIDGE)
cat_frame.place(x=400, y=310, width=280, height=170)
total_cat_icon = PhotoImage(file="classification.png")
total_cat_icon_label = Label(cat_frame, image=total_cat_icon)
total_cat_icon_label.pack(pady=10)

total_cat_label = Label(cat_frame, text='Total Categories', bg='green', fg="black",
                        font=("times new roman", 15, "bold"))
total_cat_label.pack()

total_cat_count_label = Label(cat_frame, text='0', fg="black", bg='green', font=("times new roman", 15, "bold"))
total_cat_count_label.pack()

prod_frame = Frame(window, bg='pink', bd=3, relief=RIDGE)
prod_frame.place(x=800, y=310, width=280, height=170)
total_prod_icon = PhotoImage(file="products.png")
total_prod_icon_label = Label(prod_frame, image=total_prod_icon)
total_prod_icon_label.pack(pady=10)

total_prod_label = Label(prod_frame, text='Total Products', fg="black", bg='pink', font=("times new roman", 15, "bold"))
total_prod_label.pack()

total_prod_count_label = Label(prod_frame, text='0', fg="black", bg='pink', font=("times new roman", 15, "bold"))
total_prod_count_label.pack()

sal_frame = Frame(window, bg='orange', bd=3, relief=RIDGE)
sal_frame.place(x=600, y=495, width=280, height=170)
total_sal_icon = PhotoImage(file="ssales.png")
total_sal_icon_label = Label(sal_frame, image=total_sal_icon, bg='orange')
total_sal_icon_label.pack(pady=10)

total_sal_label = Label(sal_frame, text='Total Sales', bg='orange', fg="black", font=("times new roman", 15, "bold"))
total_sal_label.pack()

total_sal_count_label = Label(sal_frame, text='0', fg="black", bg='orange', font=("times new roman", 15, "bold"))
total_sal_count_label.pack()

window.mainloop()
