import functions
import PySimpleGUI as sg

label = sg.Text("Enter a task")
input_box = sg.InputText(tooltip="Enter Task", key="task")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + '\n'
            tasks.append(new_task)
            functions.write_tasks(tasks)
        case sg.WIN_CLOSED:
            break
window.close()