import functions
import PySimpleGUI as sg

label = sg.Text("Enter a task")
input_box = sg.InputText(tooltip="Enter Task", key="task")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_tasks(), key="tasks",
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + '\n'
            tasks.append(new_task)
            functions.write_tasks(tasks)
        case "Edit":
            selected_task = values['tasks'][0]
            new_task = values['task']

            tasks = functions.get_tasks()
            index = tasks.index(selected_task)
            tasks[index] = new_task
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)
        case "tasks":
            window["task"].update(value=values['tasks'][0])
        case sg.WIN_CLOSED:
            break
window.close()