import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

mydb = mysql.connector.connect(host="localhost", user="root", database="studentsDB")
mycursor = mydb.cursor()

window = Tk()
window.title("Students Data")
window.geometry('720x480')

rnoLabel = Label(window, text = "Roll No")
rnoLabel.grid(row = 0, column = 0)
nameLabel = Label(window, text = "Name")
nameLabel.grid(row = 1, column = 0)
deptLabel = Label(window, text = "Department")
deptLabel.grid(row = 2, column = 0)
yearLabel = Label(window, text = "Year")
yearLabel.grid(row = 3, column = 0)
cgpaLabel = Label(window, text = "CGPA")
cgpaLabel.grid(row = 4, column = 0)

rnoInput = Entry(window)
rnoInput.grid(row=0, column=1)
nameInput = Entry(window)
nameInput.grid(row = 1, column = 1)
deptInput = Entry(window)
deptInput.grid(row = 2, column = 1)
yearInput = Entry(window)
yearInput.grid(row = 3, column = 1)
cgpaInput = Entry(window)
cgpaInput.grid(row = 4, column = 1)

cols = ['Roll No', 'Name', 'Department', 'Year', 'CGPA', 'GRADE']

treeview = ttk.Treeview(window, columns = cols, show='headings')
treeview.grid(row=6, column=0, columnspan=2)
for col in cols:
  treeview.heading(col, text=col)

def showData():
  mycursor.execute('select * from students')
  result = mycursor.fetchall()
  for (rno, name, dept, yr, cgpa, grade) in result:
    treeview.insert("", "end", values=(rno, name, dept, yr, cgpa, grade))

def greet():
  rno = rnoInput.get()
  print(rno)
  cgpaInput.insert(3, rno)

def clearInputFields():
    rnoInput.delete(0, "end")
    nameInput.delete(0, "end")
    deptInput.delete(0, "end")
    yearInput.delete(0, "end")
    cgpaInput.delete(0, "end")

def getGrade(cgpa):
  if cgpa >= 9:
    return "O"
  elif cgpa >= 8:
    return "A+"
  elif cgpa >= 7:
    return "A"
  elif cgpa >= 6:
    return "B+"
  elif cgpa >= 5:
    return "B"
  return "F"
  
def insert():
  rno = rnoInput.get()
  name = nameInput.get()
  dept = deptInput.get()
  year = yearInput.get()
  cgpa = cgpaInput.get()
  grade = getGrade(float(cgpa))
  mycursor.execute("insert into students (rno, name, dept, year, cgpa, grade) values (%s, %s, %s, %s, %s, %s)", (rno, name, dept, year, cgpa, grade))
  mydb.commit()
  treeview.insert("", "end", values=(rno, name, dept, year, cgpa, grade))
  messagebox.showinfo("Information", str(mycursor.rowcount) + ' row(s) inserted')
  clearInputFields()

btnInsert = ttk.Button(window, text="Insert", command=insert)
btnInsert.grid(row=5, column=1)

showData()

window.mainloop()