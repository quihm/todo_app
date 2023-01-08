import functions
import PySimpleGUI as sg
#import time
import os #standard libary that we will use to make an executable file (specifically to see if files exist)

# Check to see if "tasks.txt" exists; Generates new file if it doesn't already exist.
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", 'w') as file:
        pass

sg.theme("BlueMono")

#time_label = sg.Text('', key='clock')
label = sg.Text("Enter a task")
input_box = sg.InputText(tooltip="Enter Task", key="task")
add_button = sg.Button(size=2, image_source='add.png', mouseover_colors="LightBlue2", tooltip="Add task", key="Add")
list_box = sg.Listbox(values=functions.get_tasks(), key="tasks",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[#[time_label],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()#Include (timeout=200) if you want to run loop every 200 miliseconds, otherwise loop only occurs when an event happens
    #window['clock'].update(value = time.strftime("%b %d, %Y %H:%M:%S"))

    print("---------")
    print(f"1. Event: {event}")
    print(f"2. Values: {values}")

    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + '\n'
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)
            print(f"4. Post-Tasks: {tasks}")
        case "Edit":
            try:
                selected_task = values['tasks'][0]
                new_task = values['task'] + '\n'

                tasks = functions.get_tasks()
                index = tasks.index(selected_task)
                tasks[index] = new_task
                functions.write_tasks(tasks)
                window['tasks'].update(values=tasks)
                print(f"4. Post-Tasks: {tasks}")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "Complete":
            try:
                selected_task = values['tasks'][0]
                tasks = functions.get_tasks()
                tasks.remove(selected_task)
                functions.write_tasks(tasks)
                window['tasks'].update(values=tasks) #pointing to window's key, 'tasks'
                window['task'].update(value="") #updating it to an empty string
                print(f"4. Post-Tasks: {tasks}")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "Exit":
            break
        case "tasks":
            window["task"].update(value=values['tasks'][0])
        case sg.WIN_CLOSED:
            break
window.close()