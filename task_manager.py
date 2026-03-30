from enum import Enum

class UserInput(Enum):
    add = '1'
    view = '2'
    edit = '3'
    mark_as_completed = '4'
    delete_completed = '5'
    exit = '6'


task_list: list[str] = []

def add_task(task_list: list[str]) -> None:
    task = input('Enter a task: ')
    task_list.append(task)
    print('Task added successfully')
    print('====================\n')

def view_task_list(task_list: list[str]) -> None:
    print('Task List:')
    for task in task_list:
        print(f'- {task}')
    print('====================\n')

def edit_task(task_list: list[str]) -> None:
    task = input('Enter the task to edit: ')
    new_task = input('Enter the new task: ')
    task_list[task_list.index(task)] = new_task
    print('Task edited successfully')
    print('====================\n')

def mark_as_completed(task_list: list[str]) -> None:
    task = input('Enter the task to mark as completed: ')
    try:
        task_list[task_list.index(task)] = f'{task} (Completed)'
    except ValueError:
        print('Task not found')
        print('====================\n')
        return
    print('Task marked as completed successfully')
    print('====================\n')

def delete_completed(task_list: list[str]) -> list[str]:
    task_list = [task for task in task_list if 'Completed' not in task]
    print(task_list)
    print('Completed tasks deleted successfully')
    print('====================\n')
    return task_list

user_input = None
while user_input != UserInput.exit.value:
    print('Task Manager Menu:')
    print('1. Add a task')
    print('2. View task list')
    print('3. Edit a task')
    print('4. Mark a task as completed')
    print('5. Delete completed tasks')
    print('6. Exit')
    user_input = input('Enter your choice: ')

    if user_input == UserInput.add.value:
        add_task(task_list)
    elif user_input == UserInput.view.value:
        view_task_list(task_list)
    elif user_input == UserInput.edit.value:
        edit_task(task_list)
    elif user_input == UserInput.mark_as_completed.value:
        mark_as_completed(task_list)
    elif user_input == UserInput.delete_completed.value:
        task_list = delete_completed(task_list)
    elif user_input == UserInput.exit.value:
        print('Exiting...')
        break
    else:
        print('Invalid choice')
        print('====================\n')

