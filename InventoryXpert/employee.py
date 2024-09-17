from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("InventoryXpert | Developed by Zeel Shah")
        self.root.config(bg="#f2f2f2")
        self.root.focus_force()
        
        #===================
        #All variables=====
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        
        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_address = StringVar()
        self.var_salary = StringVar()
        
        #====SearchFrame=======
        SearchFrame = LabelFrame(self.root, text="Search Employee", font=("Open Sans", 12, "bold"), bd=2, relief=RIDGE, bg="#f2f2f2")
        SearchFrame.place(x=250, y=20, width=600, height=70)
        
        #=====options==========
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Email", "Name", "Contact"), state='readonly', justify=CENTER, font=("Open Sans", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)
        
        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Calibri", 15), bg="lightyellow")
        txt_search.place(x=200, y=10)
        
        self.btn_search = Button(SearchFrame, text="Search", font=("Calibri", 15), bg="#4caf50", fg="white", cursor="hand2", activebackground="#388e3c", activeforeground="white")
        self.btn_search.place(x=410, y=9, width=150, height=30)
        self.btn_search.bind("<Enter>", self.on_enter)
        self.btn_search.bind("<Leave>", self.on_leave)
        
        #======title=======
        title = Label(self.root, text="Employee Details", font=("Calibri", 20, "bold"), bg="#0f4d7d", fg="white")
        title.place(x=50, y=100, width=1000)
        
        #=======content========
        
        #====row 1======
        lbl_empid = Label(self.root, text="Emp ID", font=("Calibri", 15), bg="#f2f2f2")
        lbl_empid.place(x=50, y=150)
        lbl_gender = Label(self.root, text="Gender", font=("Calibri", 15), bg="#f2f2f2")
        lbl_gender.place(x=350, y=150)
        lbl_contact = Label(self.root, text="Contact", font=("Calibri", 15), bg="#f2f2f2")
        lbl_contact.place(x=750, y=150)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("Calibri", 15), bg="lightyellow")
        txt_empid.place(x=150, y=150, width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female"), state='readonly', justify=CENTER, font=("Open Sans", 15))
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("Calibri", 15), bg="lightyellow")
        txt_contact.place(x=850, y=150, width=180)
        
        #======row 2=======
        
        lbl_name = Label(self.root, text="Name", font=("Calibri", 15), bg="#f2f2f2")
        lbl_name.place(x=50, y=190)
        lbl_dob = Label(self.root, text="D.O.B", font=("Calibri", 15), bg="#f2f2f2")
        lbl_dob.place(x=350, y=190)
        lbl_doj = Label(self.root, text="D.O.J", font=("Calibri", 15), bg="#f2f2f2")
        lbl_doj.place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("Calibri", 15), bg="lightyellow")
        txt_name.place(x=150, y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("Calibri", 15), bg="lightyellow")
        txt_dob.place(x=500, y=190, width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("Calibri", 15), bg="lightyellow")
        txt_doj.place(x=850, y=190, width=180)
        
         #======row 3=======
        
        lbl_email = Label(self.root, text="Email", font=("Calibri", 15), bg="#f2f2f2")
        lbl_email.place(x=50, y=230)
        lbl_pass = Label(self.root, text="Password", font=("Calibri", 15), bg="#f2f2f2")
        lbl_pass.place(x=350, y=230)
        lbl_utype = Label(self.root, text="User Type", font=("Calibri", 15), bg="#f2f2f2")
        lbl_utype.place(x=750, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("Calibri", 15), bg="lightyellow")
        txt_email.place(x=150, y=230, width=180)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("Calibri", 15), bg="lightyellow")
        txt_pass.place(x=500, y=230, width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Admin", "Employee"), state='readonly', justify=CENTER, font=("Open Sans", 15))
        cmb_utype.place(x=850, y=230, width=180)
        cmb_utype.current(0)
        
         #======row 4=======
        
        lbl_address = Label(self.root, text="Address", font=("Calibri", 15), bg="#f2f2f2")
        lbl_address.place(x=50, y=270)
        lbl_salary = Label(self.root, text="Salary", font=("Calibri", 15), bg="#f2f2f2")
        lbl_salary.place(x=500, y=270)
        
        self.txt_address = Text(self.root, font=("Calibri", 15), bg="lightyellow")
        self.txt_address.place(x=150, y=270, width=300, height=60)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("Calibri", 15), bg="lightyellow")
        txt_salary.place(x=600, y=270, width=180)
        
        #=========button save===
        self.btn_add = Button(self.root, text="Save", font=("Calibri", 15), bg="#2196f3", fg="white", cursor="hand2", activebackground="#0b3d91", activeforeground="white")
        self.btn_add.place(x=500, y=305, width=110, height=28)
        self.btn_add.bind("<Enter>", self.on_enter)
        self.btn_add.bind("<Leave>", self.on_leave)
        
         #=========button update===
        self.btn_update = Button(self.root, text="Update", font=("Calibri", 15), bg="#4caf50", fg="white", cursor="hand2", activebackground="#388e3c", activeforeground="white")
        self.btn_update.place(x=620, y=305, width=110, height=28)
        self.btn_update.bind("<Enter>", self.on_enter)
        self.btn_update.bind("<Leave>", self.on_leave)
        
         #=========button delete===
        self.btn_delete = Button(self.root, text="Delete", font=("Calibri", 15), bg="#f44336", fg="white", cursor="hand2", activebackground="#d32f2f", activeforeground="white")
        self.btn_delete.place(x=740, y=305, width=110, height=28)
        self.btn_delete.bind("<Enter>", self.on_enter)
        self.btn_delete.bind("<Leave>", self.on_leave)
        
         #=========button clear===
        self.btn_clear = Button(self.root, text="Clear", font=("Calibri", 15), bg="#607d8b", fg="white", cursor="hand2", activebackground="#455a64", activeforeground="white")
        self.btn_clear.place(x=860, y=305, width=110, height=28)
        self.btn_clear.bind("<Enter>", self.on_enter)
        self.btn_clear.bind("<Leave>", self.on_leave)
        
        # Hover effect colors
        self.default_bg_search = self.btn_search['bg']
        self.default_bg_add = self.btn_add['bg']
        self.default_bg_update = self.btn_update['bg']
        self.default_bg_delete = self.btn_delete['bg']
        self.default_bg_clear = self.btn_clear['bg']
        self.hover_bg_search = "#45a049"  
        self.hover_bg_add = "#0b3d91"  
        self.hover_bg_update = "#388e3c"  
        self.hover_bg_delete = "#d32f2f"  
        self.hover_bg_clear = "#455a64"  
        
        #======Employee Details=====
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150) 
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)
        
        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","password","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="EMP ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="email id")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="Date of Birth")
        self.EmployeeTable.heading("doj",text="Date of Joining")
        self.EmployeeTable.heading("password",text="Password")
        self.EmployeeTable.heading("utype",text="User Type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
        
        self.EmployeeTable["show"]="headings"
        
        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("password",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)
        
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        
    def on_enter(self, e):
        if e.widget == self.btn_search:
            self.btn_search['bg'] = self.hover_bg_search
        elif e.widget == self.btn_add:
            self.btn_add['bg'] = self.hover_bg_add

    def on_leave(self, e):
        if e.widget == self.btn_search:
            self.btn_search['bg'] = self.default_bg_search
        elif e.widget == self.btn_add:
            self.btn_add['bg'] = self.default_bg_add

if __name__ == "__main__":
    root = Tk()
    app = employeeClass(root)
    root.mainloop()
