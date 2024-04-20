from tkinter import *
import copy

root = Tk()
root.title('FeastFriend')
root.geometry('500x500')
root.config(bg='#FCFBFD')

#OBJECTS/ EVENT CONTROL
meal_cat = {
    'starter' : [('Michael', 'Pickles'), ('Kofi', 'Chips')],
    'main meal' : [('Divin', 'Banku'), ('Emma', 'Tuo Zaafi')],
    'drinks' :[('Andi', 'Wine'), ('Jonelle', 'Coke')],
    'dessert' : [('Val', 'Sour Cake'), ('Nyanyuie', 'Croissant')],
    'nothing' : [('Obiba', ''), ('Opana', '')]
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
    meal_cat_wrapper.grid_remove()
    mod_partic_btn_wrap.grid_remove()

    root.geometry('500x500')
    root.config(bg='#FCFBFD')

    for i in reversed(range(partic_list.size())):
        partic_list.delete(i)

    welcome_mes.grid(row=0, column=0)
    events_wrap.grid(row=1, column=0)
    btn_frame.grid(row=2, column=0)

def return_enter_event(event):
    return_btn.config(bg='#D1CED4')

def return_lve_event(event):
    return_btn.config(bg='#FBF8FF')

return_btn = Button(root, text="<<<", font=('monospace', 13, 'bold'), bg= "#FBF8FF", fg="#484554", activebackground='#484554', activeforeground='#FBF8FF', width=5, command=lambda: return_sel_event())
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
    for i in reversed(range(starter_cat.size())):
        starter_cat.delete(i)
    
    for i in reversed(range(drinks_cat.size())):
        drinks_cat.delete(i)

    for i in reversed(range(main_meal_cat.size())):
        main_meal_cat.delete(i)

    for i in reversed(range(dessert_cat.size())):
        dessert_cat.delete(i)
    
    event_pos_tup = events_frame.curselection()
    if event_pos_tup :
        event_pos = event_pos_tup[0]
        event_e = events_frame.get(event_pos)
        if event_e.strip() != '':
            events_frame.itemconfig(event_pos, selectbackground= '#FFF6FF', selectforeground= '#424656')
            welcome_mes.grid_remove()
            events_wrap.grid_remove()
            btn_frame.grid_remove()

            root.geometry('700x700')
            return_btn.grid(row=0, column=0)
            meal_cat_wrapper.grid(row=1, column=0)
            mod_partic_btn_wrap.grid(row=2, column=0)

            starter_btn.grid_remove()
            main_meal_lab.grid_remove()
            dessert_lab.grid_remove()
            drinks_lab.grid_remove()

            starter_lab.grid(row=0, column=0, pady=10)
            main_meal_btn.grid(row=0, column=0, pady=10)
            dessert_btn.grid(row=0, column=0, pady=10)
            drinks_btn.grid(row=0, column=0, pady=10)
            
            for event_key in event_obj:
                if event_key == event_e:
                    for cat in event_obj[event_e]:
                        for tup in event_obj[event_e][cat]:
                            partic_list.insert(END, tup[0])
                            partic_list.insert(END, '')

                if event_e == event_key and event_e in event_obj:
                    starter_cat.insert(END, '')
                    starter_cat.insert(END, '')
                    for tup in event_obj[event_e]['starter']:
                        starter_cat.insert(END, tup[1])
                        starter_cat.insert(END, '')

                        for i in range(partic_list.size()):
                            if partic_list.get(i) in [t[0] for t in event_obj[event_e]['starter']]:
                                partic_list.itemconfig(i, bg='#5D52BE', fg='#FBF8FF')
                            else:
                                partic_list.itemconfig(i, fg='#312E34', bg='#FBF8FF')
            root.config(bg='#5D52BE')
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
    add_event_input.config(fg='black', font=('Segoe UI sans serif', 13), justify='left')

add_event_input = Entry(mod_event_frame, width=25, font=('Segoe UI sans serif', 10, 'italic'), textvariable=new_event_name, fg='grey', justify='center')
add_event_input.bind('<Button-1>', add_change_text)

new_event_partic_name = StringVar()
new_event_partic_name.set('Participants -> (Name, Category, Food)')

def add_event_partic_change_text(event):
    new_event_partic_name.set('')
    add_event_partic_input.config(fg='black', font=('Segoe UI sans serif', 13), justify='left')

add_event_partic_input = Entry(mod_event_frame, width=35, font=('Segoe UI sans serif', 10, 'italic'), textvariable=new_event_partic_name, fg='grey', justify='center')
add_event_partic_input.bind('<Button-1>', add_event_partic_change_text)

def add_sub_enter(event):
    add_submit.config(bg='#38C979')

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
    add_event_input.grid(row=1, column=0, pady=(10,5), padx=10)
    add_event_partic_input.grid(row=2, column=0, pady=(5, 0), padx=10)
    add_submit.grid(row=3, column=0, pady=10)

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
    del_event_input.config(fg='black', font=('Segoe UI sans serif', 13), justify='left')

del_event_input = Entry(mod_event_frame, width=25, font=('Segoe UI sans serif', 10, 'italic'), textvariable=old_event_name, fg='grey', justify='center')
del_event_input.bind('<Button-1>', del_change_text)

def del_sub_enter(event):
    del_submit.config(bg='#C94438')

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
    add_event_partic_input.grid_remove()
    add_submit.grid_remove()
    del_event_input.grid(row=1, column=0, pady=(10,0), padx=10)
    del_submit.grid(row=2, column=0, pady=10)

del_event_btn = Button(btn_frame, text="DELETE EVENT", font=('monospace', 13, 'bold'), bg= "#291466", fg="#FFFFFF", activebackground='#111111', activeforeground='#FFFFFF', command=lambda: del_event())
del_event_btn.grid(row=0, column=1, padx=(0,5))
del_event_btn.bind('<Enter>', del_enter_event)
del_event_btn.bind('<Leave>', del_lve_event)


# MEAL CATEGORY PRESENTATION
meal_cat_wrapper = Frame(root, width=100, height=100, bg='#5D52BE')

# STARTER
starter_wrap = Frame(meal_cat_wrapper, bg='#5D52BE')
starter_wrap.grid(row=0, column=0, padx=10)

starter_lab = Label(starter_wrap, text="STARTER", bg='#FCF7FF', fg='#352A80', font=('monospace', 13, 'bold'))
starter_lab.grid(row=0, column=0, pady=10)

def show_starter():
    starter_btn.grid_remove()
    main_meal_lab.grid_remove()
    dessert_lab.grid_remove()
    drinks_lab.grid_remove()

    starter_lab.grid(row=0, column=0, pady=10)
    main_meal_btn.grid(row=0, column=0, pady=10)
    dessert_btn.grid(row=0, column=0, pady=10)
    drinks_btn.grid(row=0, column=0, pady=10)

    for i in reversed(range(drinks_cat.size())):
        drinks_cat.delete(i)
    
    for i in reversed(range(main_meal_cat.size())):
        main_meal_cat.delete(i)

    for i in reversed(range(dessert_cat.size())):
        dessert_cat.delete(i)

    pos_event_sel_tup = events_frame.curselection()
    if pos_event_sel_tup:
        pos_event_sel = pos_event_sel_tup[0]
        event_sel = events_frame.get(pos_event_sel)
        
        for event in event_obj:
            if event_sel == event and event_sel in event_obj:
                starter_cat.insert(END, '')
                starter_cat.insert(END, '')
                for tup in event_obj[event]['starter']:
                    starter_cat.insert(END, tup[1])
                    starter_cat.insert(END, '')

                for i in range(partic_list.size()):
                    if partic_list.get(i) in [t[0] for t in event_obj[event_sel]['starter']]:
                        partic_list.itemconfig(i, bg='#5D52BE', fg='#FBF8FF')
                    else:
                        partic_list.itemconfig(i, fg='#312E34', bg='#FBF8FF')

        


def starter_enter(event):
    starter_btn.config(bg='#5495AA', fg='#F7FDFF')

def starter_lve(event):
    starter_btn.config(bg='#F7FDFF', fg='#007BAC')

starter_btn = Button(starter_wrap, text="STARTER", bg='#F7FDFF', fg='#007BAC', font=('monospace', 13, 'bold'), command=lambda:show_starter())
starter_btn.bind('<Enter>', starter_enter)
starter_btn.bind('<Leave>', starter_lve)
# starter_btn.grid(row=0, column=0, pady=10)

def starter_cat_sel(event):
    pos_sel_tup = starter_cat.curselection()
    if pos_sel_tup:
        pos_sel = pos_sel_tup[0]
        starter_cat.itemconfig(pos_sel, selectforeground='#312E34', selectbackground='#FBF8FF' ) 

starter_cat = Listbox(starter_wrap, justify='center', font=('monospace', 13, 'bold'), fg='#312E34', bg='#FBF8FF', borderwidth=0, highlightthickness=0)
starter_cat.grid(row=1, column=0)
starter_cat.bind('<<ListboxSelect>>', starter_cat_sel)


# DRINKS
drinks_wrap = Frame(meal_cat_wrapper, bg='#5D52BE')
drinks_wrap.grid(row=0, column=1, padx=(0, 10))

drinks_lab = Label(drinks_wrap, text='DRINKS', bg='#FCF7FF', fg='#352A80', font=('monospace', 13, 'bold'))
drinks_lab.grid(row=0, column=0, pady=10)

def show_drinks():
    starter_lab.grid_remove()
    main_meal_lab.grid_remove()
    dessert_lab.grid_remove()
    drinks_btn.grid_remove()

    starter_btn.grid(row=0, column=0, pady=10)
    main_meal_btn.grid(row=0, column=0, pady=10)
    dessert_btn.grid(row=0, column=0, pady=10)
    drinks_lab.grid(row=0, column=0, pady=10)

    for i in reversed(range(starter_cat.size())):
        starter_cat.delete(i)
    
    for i in reversed(range(main_meal_cat.size())):
        main_meal_cat.delete(i)

    for i in reversed(range(dessert_cat.size())):
        dessert_cat.delete(i)

    pos_event_sel_tup = events_frame.curselection()
    if pos_event_sel_tup:
        pos_event_sel = pos_event_sel_tup[0]
        event_sel = events_frame.get(pos_event_sel)
        
        for event in event_obj:
            if event_sel == event and event_sel in event_obj:
                drinks_cat.insert(END, '')
                drinks_cat.insert(END, '')
                for tup in event_obj[event]['drinks']:
                    drinks_cat.insert(END, tup[1])
                    drinks_cat.insert(END, '')

                for i in range(partic_list.size()):
                    if partic_list.get(i) in [t[0] for t in event_obj[event_sel]['main meal']]:
                        partic_list.itemconfig(i, bg='#5D52BE', fg='#FBF8FF')
                    else:
                        partic_list.itemconfig(i, fg='#312E34', bg='#FBF8FF')

def drinks_enter(event):
    drinks_btn.config(bg='#5495AA', fg='#F7FDFF')

def drinks_lve(event):
    drinks_btn.config(bg='#F7FDFF', fg='#007BAC')

drinks_btn = Button(drinks_wrap, text='DRINKS', bg='#F7FDFF', fg='#007BAC', font=('monospace', 13, 'bold'), command=lambda:show_drinks())
drinks_btn.bind('<Enter>', drinks_enter)
drinks_btn.bind('<Leave>', drinks_lve)
# drinks_btn.grid(row=0, column=0, pady=10)

def drinks_cat_sel(event):
    pos_sel_tup = drinks_cat.curselection()
    if pos_sel_tup:
        pos_sel = pos_sel_tup[0]
        drinks_cat.itemconfig(pos_sel, selectforeground='#312E34', selectbackground='#FBF8FF' ) 

drinks_cat = Listbox(drinks_wrap, justify='center', font=('monospace', 13, 'bold'), fg='#312E34', bg='#FBF8FF', borderwidth=0, highlightthickness=0)
drinks_cat.grid(row=1, column=0)
drinks_cat.bind('<<ListboxSelect>>', drinks_cat_sel)

# MAIN MEAL
main_meal_wrap = Frame(meal_cat_wrapper, bg='#5D52BE')
main_meal_wrap.grid(row=1, column=0, padx=10, pady=10)

main_meal_lab = Label(main_meal_wrap,text='MAIN MEAL', bg='#FCF7FF', fg='#352A80', font=('monospace', 13, 'bold'))
main_meal_lab.grid(row=0, column=0, pady=10)

def show_main_meal():
    starter_lab.grid_remove()
    main_meal_btn.grid_remove()
    dessert_lab.grid_remove()
    drinks_lab.grid_remove()

    starter_btn.grid(row=0, column=0, pady=10)
    main_meal_lab.grid(row=0, column=0, pady=10)
    dessert_btn.grid(row=0, column=0, pady=10)
    drinks_btn.grid(row=0, column=0, pady=10)

    for i in reversed(range(starter_cat.size())):
        starter_cat.delete(i)
    
    for i in reversed(range(drinks_cat.size())):
        drinks_cat.delete(i)

    for i in reversed(range(dessert_cat.size())):
        dessert_cat.delete(i)


    pos_event_sel_tup = events_frame.curselection()
    if pos_event_sel_tup:
        pos_event_sel = pos_event_sel_tup[0]
        event_sel = events_frame.get(pos_event_sel)
        
        for event in event_obj:
            if event_sel == event and event_sel in event_obj:
                main_meal_cat.insert(END, '')
                main_meal_cat.insert(END, '')
                for tup in event_obj[event]['main meal']:
                    main_meal_cat.insert(END, tup[1])
                    main_meal_cat.insert(END, '')

                for i in range(partic_list.size()):
                    if partic_list.get(i) in [t[0] for t in event_obj[event_sel]['main meal']]:
                        partic_list.itemconfig(i, bg='#5D52BE', fg='#FBF8FF')
                    else:
                        partic_list.itemconfig(i, fg='#312E34', bg='#FBF8FF')

def main_meal_enter(event):
    main_meal_btn.config(bg='#5495AA', fg='#F7FDFF')

def main_meal_lve(event):
    main_meal_btn.config(bg='#F7FDFF', fg='#007BAC')

main_meal_btn = Button(main_meal_wrap,text='MAIN MEAL', bg='#F7FDFF', fg='#007BAC', font=('monospace', 13, 'bold'), command=lambda: show_main_meal())
main_meal_btn.bind('<Enter>', main_meal_enter)
main_meal_btn.bind('<Leave>', main_meal_lve)
# main_meal_btn.grid(row=0, column=0, pady=10)

def main_meal_cat_sel(event):
    pos_sel_tup = main_meal_cat.curselection()
    if pos_sel_tup:
        pos_sel = pos_sel_tup[0]
        main_meal_cat.itemconfig(pos_sel, selectforeground='#312E34', selectbackground='#FBF8FF' ) 

main_meal_cat = Listbox(main_meal_wrap, justify='center', font=('monospace', 13, 'bold'), fg='#312E34', bg='#FBF8FF', borderwidth=0, highlightthickness=0)
main_meal_cat.grid(row=1, column=0)
main_meal_cat.bind('<<ListboxSelect>>', main_meal_cat_sel)


# DESSERT
dessert_wrap = Frame(meal_cat_wrapper, bg='#5D52BE')
dessert_wrap.grid(row=1, column=1, padx=(0, 10))

dessert_lab = Label(dessert_wrap, text='DESSERT', bg='#FCF7FF', fg='#352A80', font=('monospace', 13, 'bold'))
dessert_lab.grid(row=0, column=0, pady=10)

def show_dessert():
    starter_lab.grid_remove()
    main_meal_lab.grid_remove()
    dessert_btn.grid_remove()
    drinks_lab.grid_remove()

    starter_btn.grid(row=0, column=0, pady=10)
    main_meal_btn.grid(row=0, column=0, pady=10)
    dessert_lab.grid(row=0, column=0, pady=10)
    drinks_btn.grid(row=0, column=0, pady=10)

    for i in reversed(range(starter_cat.size())):
        starter_cat.delete(i)
    
    for i in reversed(range(main_meal_cat.size())):
        main_meal_cat.delete(i)

    for i in reversed(range(drinks_cat.size())):
        drinks_cat.delete(i)

    pos_event_sel_tup = events_frame.curselection()
    if pos_event_sel_tup:
        pos_event_sel = pos_event_sel_tup[0]
        event_sel = events_frame.get(pos_event_sel)
        
        for event in event_obj:
            if event_sel == event and event_sel in event_obj:
                dessert_cat.insert(END, '')
                dessert_cat.insert(END, '')
                for tup in event_obj[event]['dessert']:
                    dessert_cat.insert(END, tup[1])
                    dessert_cat.insert(END, '')

                for i in range(partic_list.size()):
                    if partic_list.get(i) in [t[0] for t in event_obj[event_sel]['dessert']]:
                        partic_list.itemconfig(i, bg='#5D52BE', fg='#FBF8FF')
                    else: 
                        partic_list.itemconfig(i, fg='#312E34', bg='#FBF8FF')

def dessert_enter(event):
    dessert_btn.config(bg='#5495AA', fg='#F7FDFF')

def dessert_lve(event):
    dessert_btn.config(bg='#F7FDFF', fg='#007BAC')

dessert_btn = Button(dessert_wrap, text='DESSERT', bg='#F7FDFF', fg='#007BAC', font=('monospace', 13, 'bold'), command=lambda: show_dessert())
dessert_btn.bind('<Enter>', dessert_enter)
dessert_btn.bind('<Leave>', dessert_lve)
# dessert_btn.grid(row=0, column=0, pady=10)

def dessert_cat_sel(event):
    pos_sel_tup = dessert_cat.curselection()
    if pos_sel_tup:
        pos_sel = pos_sel_tup[0]
        dessert_cat.itemconfig(pos_sel, selectforeground='#312E34', selectbackground='#FBF8FF' ) 

dessert_cat = Listbox(dessert_wrap, justify='center', font=('monospace', 13, 'bold'), fg='#312E34', bg='#FBF8FF', borderwidth=0, highlightthickness=0)
dessert_cat.grid(row=1, column=0)
dessert_cat.bind('<<ListboxSelect>>', dessert_cat_sel)

# PARTICIPANTS LIST
partic_wrap = Frame(meal_cat_wrapper, bg='#FCF7FF')
partic_wrap.grid(row=0, column=2, rowspan=2, padx=10)


partic_lab = Label(partic_wrap, text='PARTICIPANTS', fg='#FCF7FF', bg='#352A80', font=('monospace', 13, 'bold'))
partic_lab.grid(row=0, column=0, pady=10)


def partic_list_sel(event):
    pos_sel_tup = partic_list.curselection()
    if pos_sel_tup:
        pos_sel = pos_sel_tup[0]
        partic_list.itemconfig(pos_sel, selectforeground='#312E34', selectbackground='#FBF8FF')


partic_list = Listbox(partic_wrap, justify='center', fg='#312E34', font=('monospace', 13, 'bold'), bg='#FBF8FF', borderwidth=0, highlightthickness=0)
partic_list.grid(row=1, column=0, padx=10)
partic_list.bind('<<ListboxSelect>>', partic_list_sel)


mod_partic_frame = Frame(root)

mod_partic_btn_wrap = Frame(root, bg='#F8F4FF')

def mod_partic_return():
    root.config(bg='#5D52BE')
    root.geometry("700x700")

    mod_partic_return_btn.grid_remove()
    mod_partic_frame.grid_remove()

    return_btn.grid(row=0, column=0)
    meal_cat_wrapper.grid(row=1, column=0)
    mod_partic_btn_wrap.grid(row=2, column=0)
    
def mod_partic_return_enter(event):
    mod_partic_return_btn.config(bg='#777777')

def mod_partic_return_lve(event):
    mod_partic_return_btn.config(bg="#474747")

mod_partic_return_btn = Button(mod_partic_frame, text="<<<", font=('monospace', 13, 'bold'), bg= "#474747", fg="#FAF8FF", activebackground='#FAF8FF', activeforeground='#474747', width=5, command=lambda: mod_partic_return())
mod_partic_return_btn.bind('<Enter>', mod_partic_return_enter)
mod_partic_return_btn.bind('<Leave>', mod_partic_return_lve)

new_partic_name = StringVar()
new_partic_name.set('Enter Name of Participant: ')

# def add_partic_act():
    # partic_e = new_partic_name.get()
    # event_obj[event_e] = copy.deepcopy(meal_cat)

    # events_frame.insert(END, event_e)
    # events_frame.insert(END, '')

    # add_event_input.config(fg="#628281", font=('Segoe UI sans serif', 10, 'italic'))
    # new_event_name.set(event_e + ' Added')

def add_partic_change_text(event):
    new_partic_name.set('')
    add_partic_input.config(fg='black', font=('Segoe UI sans serif', 13), justify='left')

add_partic_input = Entry(mod_partic_frame, width=25, font=('Segoe UI sans serif', 10, 'italic'), textvariable=new_partic_name, fg='grey', justify='center')
add_partic_input.bind('<Button-1>', add_partic_change_text)

new_cat_name = StringVar()
new_cat_name.set('Enter -> (Category, Food): ')

def add_cat_change_text(event):
    new_cat_name.set('')
    add_cat_input.config(fg='black', font=('Segoe UI sans serif', 13), justify='left')

add_cat_input = Entry(mod_partic_frame, width=30, font=('Segoe UI sans serif', 10, 'italic'), textvariable=new_cat_name, fg='grey', justify='center')
add_cat_input.bind('<Button-1>', add_cat_change_text)


def add_partic_sub_enter(event):
    add_partic_submit.config(bg='#38C979')

def add_partic_sub_lve(event):
    add_partic_submit.config(bg="#6DA98F")

add_partic_submit = Button(mod_partic_frame, font=('monospace', 13, 'bold'), text='Add', fg="white", bg="#6DA98F", activebackground='#677F74', activeforeground='white', command=lambda:add_event_act())
add_partic_submit.bind('<Enter>', add_partic_sub_enter)
add_partic_submit.bind('<Leave>', add_partic_sub_lve)


def add_partic():
    return_btn.grid_remove()
    meal_cat_wrapper.grid_remove()
    mod_partic_btn_wrap.grid_remove()

    add_partic_input.config(fg='grey', font=('Segoe UI sans serif', 10))
    new_partic_name.set("Enter Participant's Name: ")
    new_cat_name.set("Enter -> (Category, Food): ")

    root.geometry("500x300")
    root.config(bg='#DAEBEE')

    mod_partic_frame.config(bg='#45544E')
    mod_partic_return_btn.grid(row=0, column=0, pady=10)
    mod_partic_frame.grid(row=1, column=0)

    del_partic_input.grid_remove()
    del_partic_submit.grid_remove()
    add_partic_input.grid(row=1, column=0, pady=(10,5), padx=10)
    add_cat_input.grid(row=2, column=0, pady=(5, 0), padx=10)
    add_partic_submit.grid(row=3, column=0, pady=10)

def add_partic_enter(event):
    add_partic_btn.config(bg='#9A89B4', fg='#FCF8FF')

def add_partic_lve(event):
    add_partic_btn.config(bg='#FFFFFF', fg="#291466")

add_partic_btn = Button(mod_partic_btn_wrap, text="ADD PARTICIPANT", font=('monospace', 13, 'bold'), bg= "#FFFFFF", fg="#291466", activebackground='#FCF8FF', activeforeground='#9A89B4', command=lambda:add_partic())
add_partic_btn.grid(row=0, column=0, padx=5, pady=5)
add_partic_btn.bind('<Enter>', add_partic_enter)
add_partic_btn.bind('<Leave>', add_partic_lve)


old_partic_name = StringVar()
old_partic_name.set('Enter Name of Participant: ')

# def del_partic():
    # partic_e = old_partic_name.get()

    # for i in range(events_frame.size()):
    #     if old_event_name.get() == events_frame.get(i):
    #         events_frame.delete(i)
    #         del event_obj[event_e]

    #         del_event_input.config(fg="#826762", font=('Segoe UI sans serif', 10, 'italic'))
    #         old_event_name.set(event_e + ' Deleted')

def del_change_text(event):
    old_partic_name.set('')
    del_partic_input.config(fg='black', font=('Segoe UI sans serif', 13), justify='left')

del_partic_input = Entry(mod_partic_frame, width=25, font=('Segoe UI sans serif', 10, 'italic'), textvariable=old_partic_name, fg='grey', justify='center')
del_partic_input.bind('<Button-1>', del_change_text)

def del_partic_sub_enter(event):
    del_partic_submit.config(bg='#C94438')

def del_partic_sub_lve(event):
    del_partic_submit.config(bg="#A96E6D")

del_partic_submit = Button(mod_partic_frame, font=('monospace', 13, 'bold'), text='Delete', fg="white", bg="#A96E6D", activebackground='#7F6767', activeforeground='white', command=lambda:del_partic())
del_partic_submit.bind('<Enter>', del_partic_sub_enter)
del_partic_submit.bind('<Leave>', del_partic_sub_lve)

def del_partic_enter(event):
    del_partic_btn.config(bg='#563A92')


def del_partic_lve(event):
    del_partic_btn.config(bg='#291466')

def del_partic():
    return_btn.grid_remove()
    meal_cat_wrapper.grid_remove()
    mod_partic_btn_wrap.grid_remove()

    del_event_input.config(fg='grey', font=('Segoe UI sans serif', 10))
    old_event_name.set('Enter Event Name: ')

    root.geometry("500x300")
    root.config(bg='#EDDFDA')

    mod_partic_frame.config(bg='#ADA9BB')
    mod_partic_return_btn.grid(row=0, column=0, pady=10)
    mod_partic_frame.grid(row=1, column=0)

    add_partic_input.grid_remove()
    add_partic_submit.grid_remove()
    add_cat_input.grid_remove()
    del_partic_input.grid(row=1, column=0, pady=(10,0), padx=10)
    del_partic_submit.grid(row=2, column=0, pady=10)

del_partic_btn = Button(mod_partic_btn_wrap, text="REMOVE PARTICIPANT", font=('monospace', 13, 'bold'), bg= "#291466", fg="#FFFFFF", activebackground='#111111', activeforeground='#FFFFFF', command=lambda: del_partic())
del_partic_btn.grid(row=0, column=1, padx=(0,5))
del_partic_btn.bind('<Enter>', del_partic_enter)
del_partic_btn.bind('<Leave>', del_partic_lve)



cols, rows = root.grid_size()
for i in range(cols):
    root.grid_columnconfigure(i, weight=1)

for i in range(rows):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()