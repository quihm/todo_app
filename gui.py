import functions
import PySimpleGUI as sg
import time

sg.theme("BlueMono")

time_label = sg.Text('', key='clock')
label = sg.Text("Enter a task")
input_box = sg.InputText(tooltip="Enter Task", key="task")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_tasks(), key="tasks",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[time_label],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200) #apply timeout to run loop every 200 miliseconds, otherwise loop only occurs when an event happens
    window['clock'].update(value = time.strftime("%b %d, %Y %H:%M:%S"))

    print(1, event)
    print(2, values)
    print(3, values['tasks'])

    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + '\n'
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)
        case "Edit":
            try:
                selected_task = values['tasks'][0]
                new_task = values['task']

                tasks = functions.get_tasks()
                index = tasks.index(selected_task)
                tasks[index] = new_task
                functions.write_tasks(tasks)
                window['tasks'].update(values=tasks)
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
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))
        case "Exit":
            break
        case "tasks":
            window["task"].update(value=values['tasks'][0])
        case sg.WIN_CLOSED:
            break
window.close()