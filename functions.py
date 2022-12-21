FILEPATH = 'tasks.txt'

def get_tasks(filepath=FILEPATH): # filepath is defaulted to defined txt file in parameters
    """Read a txt file and return the string of items. (This function description is called a doc string)"""
    with open(filepath, 'r') as file_local: # opens tasks.txt file with "read" permissions; don't need to close file because it's with "Context Manager"
        tasks_local = file_local.readlines()
    return tasks_local

def write_tasks(tasks_arg, filepath=FILEPATH):
    """Write the tasks list into a txt file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(tasks_arg)