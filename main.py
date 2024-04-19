from tkinter import *

root = Tk()
root.title('FeastFriend')
root.geometry('500x500')
root.config(bg='#FCFBFD')

welcome_mes = Label(root, text="FeastFriends", font=('monospace', 10, 'bold'), fg= "#5D54B1", bg="#FCFBFD")
welcome_mes.grid(row=0, column=0)

events_wrap = Frame(root, bg="#5D52BE", borderwidth=2, highlightcolor="#E4C39E", highlightthickness=2)
events_wrap.grid(row=1, column=0)

events_lab = Label(events_wrap, text="REGISTERED EVENTS", font=('monospace', 10, 'bold'), fg= "#4F449A", bg="#FCF7FF")
events_lab.grid(row=0, column=0, pady=(5,0))

event_mes = Label(events_wrap, text="Click on an EVENT to get started!", font=('monospace', 8, 'italic'), fg= "#B0A4DA", bg="#5D52BE", justify='center')
event_mes.grid(row=1, column=0, pady=5, padx=10)

def events_frame_hover(event):
    events_frame.itemconfig(ACTIVE, {'bg' : "#5D52BE", 'fg' : '#FFF6FF'})

    pos = events_frame.nearest(event.y)
    if events_frame.get(pos) != '':
        events_frame.itemconfig(pos, {'bg' : '#958BB6'})
    else:
        events_frame.itemconfig(pos, {'bg' : "#5D52BE"})

    events_frame.activate(pos)

def events_frame_leave(event):
    pos_tup = events_frame.curselection()
    if pos_tup:
        pos_sel_event =  pos_tup[0]
        for i in range(events_frame.size()):
            if i != pos_sel_event:
                events_frame.itemconfig(i, {'bg': '#5D52BE'})
    else:
        for i in range(events_frame.size()):
            events_frame.itemconfig(i, {'bg': '#5D52BE'})



events_frame = Listbox(events_wrap, bg="#5D52BE", borderwidth=0, highlightthickness=0, justify='center', font=('monospace', 13, 'bold'), fg='#FFF6FF', selectbackground="#FFF6FF", selectforeground="#424656")
events_frame.grid(row=2, column=0, padx=10)

events_frame.bind('<Motion>', events_frame_hover)
events_frame.bind('<Leave>', events_frame_leave)

events_frame.insert(END, '')
events_frame.insert(END, '')
events_frame.insert(END, 'Party')
events_frame.insert(END, '')
events_frame.insert(END, 'Refreshments')
events_frame.insert(END, '')
events_frame.insert(END, 'Drinks')
events_frame.insert(END, '')


btn_frame = Frame(root, bg='#F8F4FF')
btn_frame.grid(row=2, column=0)

add_event_btn = Button(btn_frame, text="ADD EVENT", font=('monospace', 13, 'bold'), bg= "#FFFFFF", fg="#291466", activebackground='#DA9D82', activeforeground='#F2EFE4')
add_event_btn.grid(row=0, column=0, padx=5, pady=5)

del_event_btn = Button(btn_frame, text="DELETE EVENT", font=('monospace', 13, 'bold'), bg= "#291466", fg="#FFFFFF", activebackground='#DA9D82', activeforeground='#C4515C')
del_event_btn.grid(row=0, column=1, padx=(0,5))


cols, rows = root.grid_size()
for i in range(cols):
    root.grid_columnconfigure(i, weight=1)

for i in range(rows):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()