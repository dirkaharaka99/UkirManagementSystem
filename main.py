from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Ukir Management System")

width = 1024
height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#e4e4ea")
root.iconbitmap('D:/CODE/PYTHON/TKINTER/MANAGEMENTSYSTEM/icon.ico')
my_image = ImageTk.PhotoImage(Image.open("lovebird4.png"))
my_bgr = Label(image=my_image )
my_bgr.pack()

# ====================== Variable==================================================
USERNAME = StringVar()
PASSWORD = StringVar()
TANGGAL = StringVar()
Nama_ukiran = StringVar()
Lebar_ukiran = IntVar()
Panjang_ukiran = IntVar()
Ketinggian_ukiran = IntVar()
Mesin_ukiran = IntVar()
SEARCH = StringVar()

# ========================================METHODS==========================================


def Database():
    global conn, cursor
    conn = sqlite3.connect("cobadatabase2.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `admin` (admin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS `product` (product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, TANGGAL TEXT, Nama_ukiran TEXT, Panjang_ukiran INTEGER, Lebar_ukiran INTEGER, Ketinggian_ukiran INTEGER,  Mesin_ukiran INTEGER)")
    cursor.execute(
        "SELECT * FROM `admin` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute(
            "INSERT INTO `admin` (username, password) VALUES('admin', 'admin')")
        conn.commit()
# =======================================Exit================================================


def Exit():
    result = tkMessageBox.askquestion(
        'Ukir Management System', 'Are you want to Exit ?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def Exit2():
    result = tkMessageBox.askquestion(
        'Ukir Management System', 'Are you want to Exit ?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()
# ==================================Loginform===============================================


def ShowLoginForm():
    global loginform
    loginform = Toplevel()
    loginform.title("Ukir Management System/Account Login")
    width = 600
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    loginform.resizable(0, 0)
    loginform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    LoginForm()


# =============================================Show login Form===============================
def LoginForm():
    global lbl_result
    TopLoginForm = Frame(loginform, width=600, height=100, bd=1, relief=SOLID)
    TopLoginForm.pack(side=TOP, pady=20)
    lbl_text = Label(TopLoginForm, text="Administrator Login",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidLoginForm = Frame(loginform, width=600)
    MidLoginForm.pack(side=TOP, pady=50)
    lbl_username = Label(MidLoginForm, text="Username:",
                         font=('arial', 25), bd=18)
    lbl_username.grid(row=0)
    lbl_password = Label(MidLoginForm, text="Password:",
                         font=('arial', 25), bd=18)
    lbl_password.grid(row=1)
    lbl_result = Label(MidLoginForm, text="", font=('arial', 18))
    lbl_result.grid(row=3, columnspan=2)
    username = Entry(MidLoginForm, textvariable=USERNAME,
                     font=('arial', 25), width=15)
    username.grid(row=0, column=1)
    password = Entry(MidLoginForm, textvariable=PASSWORD,
                     font=('arial', 25), width=15, show="*")
    password.grid(row=1, column=1)
    btn_login = Button(MidLoginForm, text="Login", font=(
        'arial', 18), width=30, command=Login)
    btn_login.grid(row=2, columnspan=2, pady=20)
    btn_login.bind('<Return>', Login)

# ===============================Home==========================================================


def Home():
    global Home
    Home = Tk()
    Home.title("Ukir Management System/Home")
    width = 1024
    height = 720
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = Frame(Home, bd=1, relief=SOLID)
    Title.pack(pady=10)
    lbl_display = Label(
        Title, text="Ukir Management System", font=('arial', 35))
    lbl_display.pack()
    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)
    filemenu4 = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Logout", command=Logout)
    filemenu.add_command(label="Exit", command=Exit2)
    filemenu2.add_command(label="Add new", command=ShowAddNew)
    filemenu2.add_command(label="View", command=ShowView)
    filemenu3.add_command(label="MDF", command=ShowAddNew)
    filemenu3.add_command(label="Mata Ukir", command=ShowAddNew)
    filemenu3.add_command(label="Oli", command=ShowAddNew)
    filemenu3.add_command(label="Penjepit", command=ShowAddNew)
    filemenu3.add_command(label="Lem", command=ShowAddNew)
    filemenu4.add_command(label="Kebutuhan", command=ShowAddNew)
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Inventory", menu=filemenu2)
    menubar.add_cascade(label="Equipment", menu=filemenu3)
    menubar.add_cascade(label="Money", menu=filemenu)
    Home.config(menu=menubar)
    Home.config(bg="#111330")

# ================================ Show add New item ===========================================


def ShowAddNew():
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Ukir Management System/Add new")
    width = 600
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    AddNewForm()

# =================================Add New Form ==================================================


def AddNewForm():
    TopAddNew = Frame(addnewform, width=600, height=100, bd=1, relief=SOLID)
    TopAddNew.pack(side=TOP, pady=20)
    lbl_text = Label(TopAddNew, text="Add New Product",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    MidAddNew = Frame(addnewform, width=600)
    MidAddNew.pack(side=TOP, pady=10)

    lbl_productname = Label(
        MidAddNew, text="Tanggal:", font=('arial', 20), bd=7)
    lbl_productname.grid(row=0, sticky=W)

    lbl_productname = Label(
        MidAddNew, text="Nama Ukiran:", font=('arial', 20), bd=7)
    lbl_productname.grid(row=1, sticky=W)

    lbl_lebar = Label(MidAddNew, text="Lebar:", font=('arial', 20), bd=7)
    lbl_lebar.grid(row=2, sticky=W)

    lbl_panjang = Label(MidAddNew, text="Tinggi:", font=('arial', 20), bd=7)
    lbl_panjang.grid(row=3, sticky=W)

    lbl_Z = Label(MidAddNew, text="Ketinggian:", font=('arial', 20), bd=7)
    lbl_Z.grid(row=4, sticky=W)

    lbl_mesin = Label(MidAddNew, text="Mesin:", font=('arial', 20), bd=7)
    lbl_mesin.grid(row=5, sticky=W)

    tanggalentry = Entry(MidAddNew, textvariable=TANGGAL,
                         font=('arial', 20), width=10)
    tanggalentry.grid(row=0, column=1)

    productname = Entry(MidAddNew, textvariable=Nama_ukiran,
                        font=('arial', 20), width=10)
    productname.grid(row=1, column=1)
    productqty = Entry(MidAddNew, textvariable=Panjang_ukiran,
                       font=('arial', 20), width=10)
    productqty.grid(row=2, column=1)
    productprice = Entry(MidAddNew, textvariable=Lebar_ukiran,
                         font=('arial', 20), width=10)
    productprice.grid(row=3, column=1)
    productketinggian = Entry(MidAddNew, textvariable=Ketinggian_ukiran,
                              font=('arial', 20), width=10)
    productketinggian.grid(row=4, column=1)
    productmesin = Entry(MidAddNew, textvariable=Mesin_ukiran,
                         font=('arial', 20), width=10)
    productmesin.grid(row=5, column=1)

    btn_add = Button(MidAddNew, text="Save", font=(
        'arial', 22), width=30, bg="#009ACD", command=AddNew)
    btn_add.grid(row=6, columnspan=2, pady=20)
# ===============================================AddNew==========================================================


def AddNew():
    Database()
    cursor.execute("INSERT INTO `product` (TANGGAL, Nama_ukiran, Panjang_ukiran, Lebar_ukiran, Ketinggian_ukiran, Mesin_ukiran) VALUES(?, ?, ?, ?, ?, ?)", (
        str(TANGGAL.get()), str(Nama_ukiran.get()), int(Panjang_ukiran.get()), int(Lebar_ukiran.get()), int(Ketinggian_ukiran.get()), int(Mesin_ukiran.get())))
    conn.commit()
    TANGGAL.set("")
    Nama_ukiran.set("")
    Lebar_ukiran.set("")
    Panjang_ukiran.set("")
    Ketinggian_ukiran.set("")
    Mesin_ukiran.set("")
    cursor.close()
    conn.close()

# =============================================View Form =========================================================


def ViewForm():
    global tree
    TopViewForm = Frame(viewform, width=1200, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=1200)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=1200)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Products",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCH,
                   font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=Search)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    # btn_update = Button(LeftViewForm, text="Update", command=Update)
    # btn_update.pack(side=TOP, padx=10, pady=10, fill=X)
    # btn_slideshow = Button(LeftViewForm, text="Slide Show", command=SlideShow)
    # btn_slideshow.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("ProductID", "Tanggal", "Nama Ukiran", "Lebar Ukiran", "Panjang Ukiran", "Ketinggian Ukiran", "Mesin Ukiran"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('ProductID', text="ProductID", anchor=W)
    tree.heading('Tanggal', text="Tanggal", anchor=W)
    tree.heading('Nama Ukiran', text="Nama Ukiran", anchor=W)
    tree.heading('Lebar Ukiran', text="Lebar Ukiran", anchor=W)
    tree.heading('Panjang Ukiran', text="Panjang Ukiran", anchor=W)
    tree.heading('Ketinggian Ukiran', text="Ketinggian Ukiran", anchor=W)
    tree.heading('Mesin Ukiran', text="Mesin Ukiran", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=0)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.column('#5', stretch=NO, minwidth=0, width=120)
    tree.column('#6', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()
# =======================================Display Data Methods================================================


def DisplayData():
    Database()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


# ======================================Search Mehtods========================================================
def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute(
            "SELECT * FROM `product` WHERE `Nama_ukiran` LIKE ?", ('%'+str(SEARCH.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

# ===========================================Reset ============================================================


def Reset():
    tree.delete(*tree.get_children())
    DisplayData()
    SEARCH.set("")

# ============================================Delete ===========================================================


def Delete():
    if not tree.selection():
        print("ERROR")
    else:
        result = tkMessageBox.askquestion(
            'Ukir Management System', 'Are you want to delete with Record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute(
                "DELETE FROM `product` WHERE `product_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


# ========================================= View Product =============================================================


def ShowView():
    global viewform
    viewform = Toplevel()
    viewform.title("Ukir Management System/View Product")
    width = 850
    height = 600
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    ViewForm()
# ====================================Log Out and Login=================================================================


def Logout():
    result = tkMessageBox.askquestion(
        'Ukir Management System', ' Are you want to  logout', icon="warning")
    if result == 'yes':
        admin_id = ""
        root.deiconify()
        Home.destroy()


def Login(event=None):
    global admin_id
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                       (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `admin` WHERE `username` = ? AND `password` = ?",
                           (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            admin_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close()


def ShowHome():
    root.withdraw()
    Home()
    loginform.destroy()


# ================================================ Menubar Widgets=================================================

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Account", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

lbl_display = Label(Title, text="Ukir Management System", font=('arial', 35))
lbl_display.pack()

if __name__ == '__main__':
    root.mainloop()
