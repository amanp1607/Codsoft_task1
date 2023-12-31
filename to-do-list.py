import tkinter
from tkinter import*

root =Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

tasklist= []

def addTask():
    task= task_entry.get()
    task_entry.delete(0, END)
    
    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        tasklist.append(task)
        listbox.insert(END, task)
        
def deleteTask():
    global tasklist
    task= str(listbox.get(ANCHOR))
    if task in tasklist:
        tasklist.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in tasklist:
                taskfile.write(task+"\n")
                
        listbox.delete( ANCHOR)
        

def openTaskFile():
    
    try:
        global tasklist
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()
        
        for task in tasks:
            if task !='\n':
                tasklist.append(task)
                listbox.insert(END,task)
            
    except:
        file=open('tasklist.txt','w')
        file.close()

#icon
Image_icon=PhotoImage(file="images/icon.png")
root.iconphoto(False,Image_icon)

#top bar
TopImage=PhotoImage(file="images/topbar.png")
Label(root,image=TopImage).pack()



noteImage=PhotoImage(file="images/icons.png")
Label(root,image=noteImage).place(x=30,y=25)

heading=Label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=130,y=25)

#main
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20", bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD", font="arial 20 bold",width=6,bg="#5a95ff",fg="#f3f6f4",bd=0,command=addTask)
button.place(x=300,y=0)

#listbox
frame1=Frame(root,bd=3,width=700,height=580,bg="#32405b")
frame1.pack(pady=(160,0))

listbox= Listbox(frame1,font=('arial',12), width=60, height=14,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar= Scrollbar(frame1)
scrollbar.pack(side= RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()  

#delete
Delete_icon=PhotoImage(file=("images/delete.png"))
Button(root,image=Delete_icon,bd=0, command=deleteTask).pack(side=BOTTOM,pady=13)



root.mainloop()