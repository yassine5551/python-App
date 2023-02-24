from operator import attrgetter
import re
from tkinter import *
from tkinter import messagebox, ttk
from tkinter import COMMAND
from mydatabase import *

root = Tk()

root.geometry("800x500")
root.resizable(False, False)

root.config(bg="#9ef0b7")





def Lookup_records():
    global search_entry
    global search
    
    search = Toplevel(root)
    search.title("Lookup Reacords")
    search.geometry("400x200")

    # create label

    search_frame = LabelFrame(search, text="Domain")
    search_frame.pack(padx=10, pady=10)
    search_entry = Entry(search_frame, font="Ubuntu")
    search_entry.pack(pady=20, padx=10)

    # add button

    search_button = Button(search, text="search by domain" , command=searchByDomine)
    search_button.pack(padx=20, pady=20)

def searchByDomine():
    domain= search_entry.get()
    listOfStages = mycol.find({"domain":domain})
    search.destroy()
    for records in table.get_children():
        table.delete(records)
   
    for item in listOfStages:
         table.insert("", END, values=(
            item['id'], item['nameStage'], item["domain"], item["price"], item["durre"]))
            
        
def all():
    reftable()

my_menu = Menu(root)
root.config(menu=my_menu)

# searchMenu
search_menu = Menu(my_menu, tearoff=0)
refeshing = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Search", menu=search_menu)
my_menu.add_cascade(label="Refresh", menu=refeshing)

# dropdownMenu

search_menu.add_command(label="Search", command=Lookup_records)
refeshing.add_command(label="RefreshAll", command=all)




header = Label(root, text="STAGES FORM", bg="#9ef0b7", font="Oswald")
header.place(x=250, y=3)

id = Label(root, text="Id", bg="#9ef0b7", font="Ubuntu")
id.place(x=100, y=30)
price = Label(root, text="Price", bg="#9ef0b7", font="Ubuntu")
price.place(x=100, y=50)
domain = Label(root, text="Domain", bg="#9ef0b7", font="Ubuntu")
domain.place(x=100, y=70)
nameStage = Label(root, text="NameStage", bg="#9ef0b7", font="Ubuntu")
nameStage.place(x=100, y=90)
durre = Label(root, text="Durre", bg="#9ef0b7", font="Ubuntu")
durre.place(x=100, y=110)

idvalue = IntVar
pricevalue = IntVar
domainvalue = StringVar
nameStagevalue = StringVar
durrevalue = IntVar

identry = Entry(root, textvariable=idvalue)
identry.place(x=250, y=30)


priceentry = Entry(root, textvariable=pricevalue)
priceentry.place(x=250, y=50)


domainentry = Entry(root, textvariable=domainvalue)
domainentry.place(x=250, y=70)


nameStageentry = Entry(root, textvariable=nameStagevalue)
nameStageentry.place(x=250, y=90)


durreentry = Entry(root, textvariable=durrevalue)
durreentry.place(x=250, y=110)


# functions______________________________________________---

# isersion

def Inserere():
    id = identry.get()
    list_stages = list(mycol.find({"id": id}))
    if len(list_stages) > 0:
        messagebox.showerror(message="Id already existed in the database")
        return
    nameStage = nameStageentry.get()
    domain = domainentry.get()
    price = priceentry.get()
    durre = durreentry.get()
    if id == "" or nameStage == "" or domain == "" or price == "" or durre == "":
        messagebox.showerror("error", "fill all inputs")
    else:
        if not re.search(r"^\d+$", id) or not re.search(r"^\d+$", price) or not re.search(r"^\d+$", durre):
            messagebox.showerror(
                'error', "id est duree et price doit etre des numero")
        else:
            addToDb(id, price, domain, nameStage, durre)
            messagebox.showinfo('congate', "data saved with success")

    reftable()
    

# updatefun


def updateData():
    id = identry.get()
    nameStage = nameStageentry.get()
    domain = domainentry.get()
    price = priceentry.get()
    durre = durreentry.get()
    if (id == ""):
        messagebox.showerror("ERROR", "Your id is empty Please fill it")
    else:
        update(id, price, domain, nameStage, durre)
    reftable()

# deletefunc


def deleteData():
    id = identry.get()
    if (id == ""):
        messagebox.showerror("Error", "your id is empty please fill it!")
    else:
        deletedata(id)
    reftable()

# affichage

# def up():
#     rows = table.selection()


#     for row in rows:
#         table.move(row, table.parent(row), table.index(row)-1)
    
        




# def down():
#     rows = table.selection()

#     for row in rows:
#         table.move(row, table.parent(row), table.index(row)+1)


def afficher():
    global table
    table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5),
                         show="headings", selectmode="browse")
    table.pack(side="left")
    # creatcrol
    vertScroll = ttk.Scrollbar(root, orient="vertical", command=table.yview)
    vertScroll.pack(side="right", fill="y")
    vertScroll.place(relx=0.952, rely=0.400, relheight=0.460, relwidth=0.020)

# scrollconfi
    table.config(yscrollcommand=vertScroll.set)

    table.place(x=40, y=200)
    table.heading(1, text="ID")
    table.heading(2, text="Name")
    table.heading(3, text="Domain")
    table.heading(4, text="Price ")
    table.heading(5, text="Duration")
    table.column(1, width=160)
    table.column(2, width=160)
    table.column(3, width=160)
    table.column(4, width=150)
    table.column(5, width=90)
    data = list(mycol.find())
    # for item in data:
    #     int(item["id"])
    #     print(item["id"])
    # data.sort(key=getKey)
    # listOfids=[]
    # for id in data:
    #     listOfids.append(id["id"])
    # listOfids.sort(reverse=True)
    # print(listOfids)
    for item in data:
        table.insert("", END, values=(
            item['id'], item['nameStage'], item["domain"], item["price"], item["durre"]))

    # for item in sorted(data , key=attrgetter(item[id])):
    #     print(data)
        


afficher()


# refreshTable


def reftable():
    for i in table.get_children():
        table.delete(i)
    table.update()
    data = list(mycol.find())
    for item in data:
        table.insert("", END, values=(
            item['id'], item['nameStage'], item["domain"], item["price"], item["durre"]))
    table.update()
    

# select_data


def select_data():
    identry.delete(0, END)
    nameStageentry.delete(0, END)
    domainentry.delete(0, END)
    priceentry.delete(0, END)
    durreentry.delete(0, END)

    selected = table.focus()

    values = table.item(selected, "values")

    identry.insert(0, values[0])
    nameStageentry.insert(0, values[1])
    domainentry.insert(0, values[2])
    priceentry.insert(0, values[3])
    durreentry.insert(0, values[4])

# cleardata


def clear_data():
    identry.delete(0, END)
    nameStageentry.delete(0, END)
    domainentry.delete(0, END)
    priceentry.delete(0, END)
    durreentry.delete(0, END)

# movingData




# search_menuFuncion


# styleTree_______________________________________-------
style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", background="#b6e3c5",
                fieldbackground="#b6e3c5", foreground="black", font="Ubuntu")

# buttons

buttoninserer = Button(text="Insert", command=Inserere,
                       height=1, width=10, font="Ubuntu", bg="#35f038", border="1")
buttoninserer.place(x=650, y=20)


buttonupdate = Button(text="Update", command=updateData,
                      height=1, width=10, font="Ubuntu", bg="#1a25f0", bd="1")
buttonupdate.place(x=650, y=60)

buttondelete = Button(text="Delete", command=deleteData,
                      height=1, width=10, font="Ubuntu", bg="#d92626", bd="1")
buttondelete.place(x=650, y=100)


buttonselect = Button(text="Select", command=select_data,
                      height=1, width=10, font="Ubuntu", bg="#cf3eaa", border="1")
buttonselect.place(x=650, y=140)


buttonclear = Button(text="Clear", command=clear_data,
                     height=1, width=5, font="Ubuntu", bg="#195c4e", border="1")
buttonclear.place(x=700, y=450)

# buttonmoveup = Button(text="ALL", command=all, height=1,
#                       width=8, font="Ubuntu", bg="#f56811", border="1")
# buttonmoveup.place(x=40, y=450)

# buttonmovedown = Button(text="MoveDown", command=down, height=1,
#                         width=10, font="Ubuntu", bg="#f56811", border="1")
# buttonmovedown.place(x=150, y=450)


root.mainloop()
