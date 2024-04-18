from tkinter import *

root = Tk()
root.title('FeastFriend')
root.geometry('500x500')
root.config(bg='#F2EFE4')

welcome_mes = Label(root, text="FeastFriends", font=('monospace', 10, 'bold'), fg= "#8C6954", bg="#F2EFE4")
welcome_mes.grid(row=0, column=0)

events_frame = Frame(root, bg="#BD5942")
btn_frame = Frame(root, bg='#BD5942')
btn_frame.grid(row=2, column=0)

add_event_btn = Button(btn_frame, text="ADD EVENT", font=('monospace', 13, 'bold'), bg= "#009178", fg="#A1AF9F", activebackground='#DA9D82', activeforeground='#F2EFE4')
add_event_btn.grid(row=0, column=0, padx=5, pady=5)

del_event_btn = Button(btn_frame, text="DELETE EVENT", font=('monospace', 13, 'bold'), bg= "#912900", fg="#B0A0AB", activebackground='#DA9D82', activeforeground='#C4515C')
del_event_btn.grid(row=0, column=1, padx=(0,5))


cols, rows = root.grid_size()
for i in range(cols):
    root.grid_columnconfigure(i, weight=1)

for i in range(rows):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()