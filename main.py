from tkinter import *

root = Tk()
root.title('FeastFriend')
root.geometry('500x500')
root.config(bg='#F2EFE4')

welcome_mes = Label(root, text="FeastFriends", font=('monospace', 10, 'bold'), fg= "#7E5A3C", bg="#F2EFE4")
welcome_mes.grid(row=0, column=0)

events_wrap = Frame(root, bg="#BD5942", borderwidth=2, highlightcolor="#E4C39E", highlightthickness=2)
events_wrap.grid(row=1, column=0)

events_lab = Label(events_wrap, text="REGISTERED EVENTS", font=('monospace', 10, 'bold'), fg= "#FFF6ED", bg="#FF7028")
events_lab.grid(row=0, column=0)

events_frame = Frame(events_wrap, bg="#FFFDF3")
events_frame.grid(row=1, column=0)

event_lab = Label(events_frame, text="REGISTERED EVENTS", font=('monospace', 10, 'bold'), fg= "#A14D1B", bg="#FFFDF3")
event_lab.grid(row=0, column=0)

btn_frame = Frame(root, bg='#FFDCB6')
btn_frame.grid(row=2, column=0)

add_event_btn = Button(btn_frame, text="ADD EVENT", font=('monospace', 13, 'bold'), bg= "#17D173", fg="#D9EDDF", activebackground='#DA9D82', activeforeground='#F2EFE4')
add_event_btn.grid(row=0, column=0, padx=5, pady=5)

del_event_btn = Button(btn_frame, text="DELETE EVENT", font=('monospace', 13, 'bold'), bg= "#523B32", fg="#FFF5EE", activebackground='#DA9D82', activeforeground='#C4515C')
del_event_btn.grid(row=0, column=1, padx=(0,5))


cols, rows = root.grid_size()
for i in range(cols):
    root.grid_columnconfigure(i, weight=1)

for i in range(rows):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()