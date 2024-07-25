from tkinter import *
from PIL import Image, ImageTk
import time

class InventoryXpert:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("InventoryXpert | Developed by Zeel Shah")
        self.root.config(bg="#f2f2f2")

        self.setup_title()
        self.setup_logout_button()
        self.setup_clock()
        self.setup_left_menu()
        self.setup_content()
        self.setup_footer()
        
        # Start updating the clock
        self.update_clock()

    def setup_title(self):
        icon_image = Image.open("Images/cart.png")
        icon_image = icon_image.resize((30, 30))  
        self.icon_title = ImageTk.PhotoImage(icon_image)
        
        title = Label(self.root, text="InventoryXpert", image=self.icon_title, compound="left", font=("Open Sans", 38, "bold"), bg="#00B4D8", fg="white", anchor="w", padx=20, pady=10)
        title.place(x=0, y=0, relwidth=1, height=80)

    def setup_logout_button(self):
        btn_logout = Label(self.root, text="Logout", font=("Open Sans", 15, "bold"), bg="#00B4D8", fg="white", cursor="hand2")
        btn_logout.place(x=1230, y=20, height=40, width=100)
        btn_logout.bind("<Enter>", lambda e: btn_logout.config(fg="#03045E"))
        btn_logout.bind("<Leave>", lambda e: btn_logout.config(fg="white"))

    def setup_clock(self):
        self.lbl_clock = Label(self.root, text="", font=("Open Sans", 15), bg="#6C757D", fg="white")
        self.lbl_clock.place(x=0, y=80, relwidth=1, height=30)

    def update_clock(self):
        current_time = time.strftime("Welcome to Inventory Management System\t\t Date: %d-%m-%Y\t\t Time: %H:%M:%S")
        self.lbl_clock.config(text=current_time)
        self.root.after(1000, self.update_clock)  # Update every second

    def setup_left_menu(self):
        self.MenuLogo = Image.open("images/menu.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200))
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu = Frame(self.root, bd=0, bg="#00B4D8")
        LeftMenu.place(x=0, y=110, width=200, height=590)

        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo, bg="#00B4D8")
        lbl_menuLogo.pack(side=TOP, fill=X, pady=20)

        menu_items = ["Employee", "Product", "Supplier", "Customer", "Category", "Sales", "Exit"]
        for item in menu_items:
            btn = Label(LeftMenu, text=item, font=("Open Sans", 18), bg="#00B4D8", fg="white", cursor="hand2")
            btn.pack(side=TOP, fill=X, padx=10, pady=10)
            btn.bind("<Enter>", lambda e, btn=btn: btn.config(fg="#03045E"))
            btn.bind("<Leave>", lambda e, btn=btn: btn.config(fg="white"))

    def setup_content(self):
        content_data = [
            ("Total Employee\n[ 0 ]", "#edae49"),
            ("Total Product\n[ 0 ]", "#d1495b"),
            ("Total Supplier\n[ 0 ]", "#00798c"),
            ("Total Category\n[ 0 ]", "#30638e"),
            ("Total Sales\n[ 0 ]", "#003d5b"),
        ]
        
        positions = [(300, 150), (650, 150), (1000, 150), (300, 360), (650, 360)]
        
        for (text, color), (x, y) in zip(content_data, positions):
            self.create_rounded_label(self.root, text, color, x, y)

    def create_rounded_label(self, parent, text, bg_color, x, y):
        # Create canvas for rounded effect
        canvas = Canvas(parent, bg=self.root["bg"], highlightthickness=0)
        canvas.place(x=x, y=y, width=300, height=150)
        
        # Draw rounded rectangle
        radius = 20
        points = [10 + radius, 10,
                  290 - radius, 10,
                  290, 10 + radius,
                  290, 140 - radius,
                  290 - radius, 150,
                  10 + radius, 150,
                  10, 140 - radius,
                  10, 10 + radius]
        rect = canvas.create_polygon(points, fill=bg_color, outline=bg_color, smooth=True)
        
        # Add text
        label = Label(canvas, text=text, bd=0, bg=bg_color, fg="white", font=("goudy old style", 20, "bold"))
        label.place(x=0, y=0, width=300, height=150)
        label.bind("<Enter>", lambda e: self.on_enter(e, canvas, rect))
        label.bind("<Leave>", lambda e: self.on_leave(e, canvas, rect, bg_color))

    def on_enter(self, event, canvas, rect):
        canvas.itemconfig(rect, fill="#ff7f50")

    def on_leave(self, event, canvas, rect, original_color):
        canvas.itemconfig(rect, fill=original_color)

    def setup_footer(self):
        footer = Label(self.root, text="Copyright 2023 InventoryXpert. All rights reserved.", font=("Open Sans", 12), bg="#6C757D", fg="white")
        footer.place(x=0, y=660, relwidth=1, height=40)

if __name__ == "__main__":
    root = Tk()
    app = InventoryXpert(root)
    root.mainloop()
