#from functions import get_tasks, write_tasks

import functions
import time

now = time.strftime("%b %d %Y %H:%M:%S")
task_prompt="Input a task: "
user_action_prompt="""--------
Input one of the following:
ADD (to add a new to-do)
SHOW (to show the full to-do list)
EDIT (to edit an existing item)
COMPLETE (to mark an item as complete)
EXIT (to exit to-do app)
"""

print("It is", now)

while True:
    user_action = input(user_action_prompt).casefold().strip()

    if user_action.startswith("add"):
        task = user_action[4:].casefold().strip() + '\n'

        tasks = functions.get_tasks()

        tasks.append(task)
        print(tasks)

        functions.write_tasks(tasks)

    elif user_action.startswith("show"):
        tasks = functions.get_tasks()

        for index, item in enumerate(tasks):
            item = item.strip('\n')
            output = f"{index+1}. {item}"
            print(output)
    elif user_action.startswith("edit"):
        try:
            user_number = int(user_action[5:])-1

            tasks = functions.get_tasks()

            task = input("What would you like to replace it with? ").casefold().strip()
            tasks[user_number] = task + '\n'

            functions.write_tasks(tasks)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            user_number = int(user_action[9:])-1

            tasks = functions.get_tasks()

            tasks.pop(user_number)

            functions.write_tasks(tasks)
        except IndexError:
            print(f"You must select a task between 1 and {len(tasks)}")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Incorrect input.")

print("Bye!")

