import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{task}" added.')

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print('No tasks found.')
    else:
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')

def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Task "{removed_task}" deleted.')
    else:
        print('Invalid task number.')

def mark_task_completed(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1] += ' (completed)'
        save_tasks(tasks)
        print(f'Task {task_number} marked as completed.')
    else:
        print('Invalid task number.')

def main():
    while True:
        print('\nTo-Do List Application')
        print('1. Add task')
        print('2. View tasks')
        print('3. Delete task')
        print('4. Mark task as completed')
        print('5. Exit')

        choice = input('Choose an option: ')

        if choice == '1':
            task = input('Enter the task: ')
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input('Enter task number to delete: '))
            delete_task(task_number)
        elif choice == '4':
            task_number = int(input('Enter task number to mark as completed: '))
            mark_task_completed(task_number)
        elif choice == '5':
            break
        else:
            print('Invalid choice. Please choose a valid option.')

if __name__ == '__main__':
    main()
