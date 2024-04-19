from tkinter import *
import copy

root = Tk()
root.title('FeastFriend')
root.geometry('500x500')
root.config(bg='#FCFBFD')

#OBJECTS/ EVENT CONTROL
meal_cat = {
    'starter' : [],
    'main meal' : [],
    'drinks' :[],
    'dessert' : [],
    'nothing' : []
}

event_obj = {
    'Picnic': {},
    'Nyanyuie Birthday': {},
    'May Day' : {},
    'Sleepover' :  {},
}

for event in event_obj:
    event_obj[event] = copy.deepcopy(meal_cat) 

welcome_mes = Label(root, text="FeastFriends", font=('monospace', 10, 'bold'), fg= "#5D54B1", bg="#FCFBFD")
welcome_mes.grid(row=0, column=0)

events_wrap = Frame(root, bg="#5D52BE", borderwidth=2, highlightcolor="#484554", highlightbackground="#ADA9BB", highlightthickness=2)
events_wrap.grid(row=1, column=0)

events_lab = Label(events_wrap, text="REGISTERED EVENTS", font=('monospace', 10, 'bold'), fg= "#4F449A", bg="#FCF7FF")
events_lab.grid(row=0, column=0, pady=(5,0))

event_mes = Label(events_wrap, text="Click on an EVENT to get started!", font=('monospace', 8, 'italic'), fg= "#B0A4DA", bg="#5D52BE", justify='center')
event_mes.grid(row=1, column=0, pady=5, padx=10)

def return_sel_event():
    return_btn.grid_remove()

    root.geometry('500x500')

    welcome_mes.grid(row=0, column=0)
    events_wrap.grid(row=1, column=0)
    btn_frame.grid(row=2, column=0)

def return_enter_event(event):
    return_btn.config(bg='#111111')

def return_lve_event(event):
    return_btn.config(bg='#474747')

return_btn = Button(root, text="<<<", font=('monospace', 13, 'bold'), bg= "#474747", fg="#FAF8FF", activebackground='#FAF8FF', activeforeground='#474747', width=5, command=lambda: return_sel_event())
return_btn.bind('<Enter>', return_enter_event)
return_btn.bind('<Leave>', return_lve_event)

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
        pos_sel_event = pos_tup[0]
        for i in range(events_frame.size()):
            if i != pos_sel_event:
                events_frame.itemconfig(i, {'bg': '#5D52BE'})
    else:
        for i in range(events_frame.size()):
            events_frame.itemconfig(i, {'bg': '#5D52BE'})


def event_select(event):
    event_pos_tup = events_frame.curselection()
    if event_pos_tup :
        event_pos = event_pos_tup[0]
        event_e = events_frame.get(event_pos)
        if event_e.strip() != '':
            events_frame.itemconfig(event_pos, selectbackground= '#FFF6FF', selectforeground= '#424656')
            welcome_mes.grid_remove()
            events_wrap.grid_remove()
            btn_frame.grid_remove()

            root.geometry('800x500')
            return_btn.grid(row=0, column=0)
            meal_cat_wrapper.grid(row=1, column=0)
            partic_wrap.grid(row=1, column=1)
        else:
            events_frame.itemconfig(event_pos, selectbackground= '#5D52BE', selectforeground= '#FFF6FF')

events_frame = Listbox(events_wrap, bg="#5D52BE", borderwidth=0, highlightthickness=0, justify='center', font=('monospace', 13, 'bold'), fg='#FFF6FF', selectbackground="#FFF6FF", selectforeground="#424656")
events_frame.grid(row=2, column=0, padx=10)

events_frame.bind('<Motion>', events_frame_hover)
events_frame.bind('<<ListboxSelect>>', event_select)
events_frame.bind('<Leave>', events_frame_leave)

# events_frame.insert(END, '')
events_frame.insert(END, '')
for event in event_obj:
    events_frame.insert(END, event)
    events_frame.insert(END, '')

mod_event_frame = Frame(root)

btn_frame = Frame(root, bg='#F8F4FF')
btn_frame.grid(row=2, column=0)

def mod_return():
    root.geometry("500x500")
    mod_event_frame.grid_remove()
    events_wrap.grid(row=1, column=0)
    btn_frame.grid(row=2, column=0)
    
def mod_return_enter(event):
    mod_return_btn.config(bg='#777777')

def mod_return_lve(event):
    mod_return_btn.config(bg="#474747")

mod_return_btn = Button(mod_event_frame, text="<<<", font=('monospace', 13, 'bold'), bg= "#474747", fg="#FAF8FF", activebackground='#FAF8FF', activeforeground='#474747', width=5, command=lambda: mod_return())
mod_return_btn.bind('<Enter>', mod_return_enter)
mod_return_btn.bind('<Leave>', mod_return_lve)

new_event_name = StringVar()
new_event_name.set('Enter Event Name: ')

def add_event_act():
    event_e = new_event_name.get()
    event_obj[event_e] = copy.deepcopy(meal_cat)

    events_frame.insert(END, event_e)
    events_frame.insert(END, '')

    add_event_input.config(fg="#628281", font=('Segoe UI sans serif', 10, 'italic'))
    new_event_name.set(event_e + ' Added')

def add_change_text(event):
    new_event_name.set('')
    add_event_input.config(fg='black', font=('Segoe UI sans serif', 13))

add_event_input = Entry(mod_event_frame, width=25, font=('Segoe UI sans serif', 10, 'italic'), textvariable=new_event_name, fg='grey')
add_event_input.bind('<Button-1>', add_change_text)

def add_sub_enter(event):
    add_submit.config(bg='#59BA90')

def add_sub_lve(event):
    add_submit.config(bg="#6DA98F")
add_submit = Button(mod_event_frame, font=('monospace', 13, 'bold'), text='Add', fg="white", bg="#6DA98F", activebackground='#677F74', activeforeground='white', command=lambda:add_event_act())
add_submit.bind('<Enter>', add_sub_enter)
add_submit.bind('<Leave>', add_sub_lve)


def add_event():
    events_wrap.grid_remove()
    btn_frame.grid_remove()

    add_event_input.config(fg='grey', font=('Segoe UI sans serif', 10))
    new_event_name.set('Enter Event Name: ')

    root.geometry("500x300")

    mod_event_frame.config(bg='#45544E')
    mod_return_btn.grid(row=0, column=0, pady=10)
    mod_event_frame.grid(row=1, column=0)

    del_event_input.grid_remove()
    del_submit.grid_remove()
    add_event_input.grid(row=1, column=0, pady=(10,0), padx=10)
    add_submit.grid(row=2, column=0, pady=10)

def add_enter_event(event):
    add_event_btn.config(bg='#9A89B4', fg='#FCF8FF')

def add_lve_event(event):
    add_event_btn.config(bg='#FFFFFF', fg="#291466")

add_event_btn = Button(btn_frame, text="ADD EVENT", font=('monospace', 13, 'bold'), bg= "#FFFFFF", fg="#291466", activebackground='#FCF8FF', activeforeground='#9A89B4', command=lambda:add_event())
add_event_btn.grid(row=0, column=0, padx=5, pady=5)
add_event_btn.bind('<Enter>', add_enter_event)
add_event_btn.bind('<Leave>', add_lve_event)


old_event_name = StringVar()
old_event_name.set('Enter Event Name: ')

def del_event_act():
    event_e = old_event_name.get()

    for i in range(events_frame.size()):
        if old_event_name.get() == events_frame.get(i):
            events_frame.delete(i)
            del event_obj[event_e]

            del_event_input.config(fg="#826762", font=('Segoe UI sans serif', 10, 'italic'))
            old_event_name.set(event_e + ' Deleted')

def del_change_text(event):
    old_event_name.set('')
    del_event_input.config(fg='black', font=('Segoe UI sans serif', 13))

del_event_input = Entry(mod_event_frame, width=25, font=('Segoe UI sans serif', 10, 'italic'), textvariable=old_event_name, fg='grey')
del_event_input.bind('<Button-1>', del_change_text)

def del_sub_enter(event):
    del_submit.config(bg='#D46F66')

def del_sub_lve(event):
    del_submit.config(bg="#A96E6D")
del_submit = Button(mod_event_frame, font=('monospace', 13, 'bold'), text='Delete', fg="white", bg="#A96E6D", activebackground='#7F6767', activeforeground='white', command=lambda:del_event_act())
del_submit.bind('<Enter>', del_sub_enter)
del_submit.bind('<Leave>', del_sub_lve)

def del_enter_event(event):
    del_event_btn.config(bg='#563A92')


def del_lve_event(event):
    del_event_btn.config(bg='#291466')

def del_event():
    events_wrap.grid_remove()
    btn_frame.grid_remove()

    del_event_input.config(fg='grey', font=('Segoe UI sans serif', 10))
    old_event_name.set('Enter Event Name: ')

    root.geometry("500x300")

    mod_event_frame.config(bg='#ADA9BB')
    mod_return_btn.grid(row=0, column=0, pady=10)
    mod_event_frame.grid(row=1, column=0)

    add_event_input.grid_remove()
    add_submit.grid_remove()
    del_event_input.grid(row=1, column=0, pady=(10,0), padx=10)
    del_submit.grid(row=2, column=0, pady=10)

del_event_btn = Button(btn_frame, text="DELETE EVENT", font=('monospace', 13, 'bold'), bg= "#291466", fg="#FFFFFF", activebackground='#111111', activeforeground='#FFFFFF', command=lambda: del_event())
del_event_btn.grid(row=0, column=1, padx=(0,5))
del_event_btn.bind('<Enter>', del_enter_event)
del_event_btn.bind('<Leave>', del_lve_event)


# MEAL CATEGORY PRESENTATION
meal_cat_wrapper = Frame(root)

# STARTER
starter_wrap = Frame(meal_cat_wrapper)
starter_wrap.grid(row=0, column=0, padx=10)

starter_lab = Label(starter_wrap)
starter_lab.grid(row=0, column=0, pady=10)

starter_cat = Listbox(starter_wrap)
starter_lab.grid(row=1, column=0)


# DRINKS
drinks_wrap = Frame(meal_cat_wrapper)
starter_wrap.grid(row=0, column=1, padx=(0, 10))

drinks_lab = Label(drinks_wrap)
drinks_lab.grid(row=0, column=0, pady=10)

drinks_cat = Listbox(drinks_wrap)
drinks_cat.grid(row=1, column=0)


# MAIN MEAL
main_meal_wrap = Frame(meal_cat_wrapper)
starter_wrap.grid(row=1, column=0, padx=10, pady=10)

main_meal_lab = Label(main_meal_wrap)
main_meal_lab.grid(row=0, column=0, pady=10)

main_meal_cat = Listbox(main_meal_wrap)
main_meal_cat.grid(row=1, column=0)


# DESSERT
dessert_wrap = Frame(meal_cat_wrapper)
dessert_wrap.grid(row=1, column=1, padx=(0, 10))

desseert_lab = Label(dessert_wrap)
desseert_lab.grid(row=0, column=0, pady=10)

dessert_cat = Listbox(dessert_wrap)
dessert_cat.grid(row=1, column=0)


# PARTICIPANTS LIST
partic_wrap = Frame(root)

partic_lab = Label(partic_wrap)
partic_lab.grid(row=0, column=0, pady=10)

partic_list = Listbox(partic_wrap)
partic_list.grid(row=1, column=0)




cols, rows = root.grid_size()
for i in range(cols):
    root.grid_columnconfigure(i, weight=1)

for i in range(rows):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()