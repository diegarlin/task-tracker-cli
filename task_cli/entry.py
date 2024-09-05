import argparse
import os
import json
import datetime

file_path = 'lista.json'

def cli_entry_point():
    parser = argparse.ArgumentParser(description='A simple task manager')
    subparsers = parser.add_subparsers(dest='command')
    
    parser_add = subparsers.add_parser('add', help='Add a new task')
    parser_add.add_argument('title', help='Task title')
    
    parser_delete = subparsers.add_parser('delete', help='Delete a task')
    parser_delete.add_argument('id', help='Id of the task to delete')
    
    parser_update = subparsers.add_parser('update', help='Update a task title')
    parser_update.add_argument('id', help='Id of the task to update')
    parser_update.add_argument('-t', '--title', help='New title of the task')
    
    parser_in_progress = subparsers.add_parser('mark-in-progress', help='Mark a task in progress')
    parser_in_progress.add_argument('id', help='Id of the task to put in progress')
    
    parser_done = subparsers.add_parser('mark-done', help='Mark a task as done')
    parser_done.add_argument('id', help='Id of the task to mark as done')
    
    parser_list = subparsers.add_parser('list', help='List tasks')
    parser_list.add_argument('list_type',
                            default='all',
                            const='all',
                            nargs='?',
                            choices=['all', 'done', 'in-progress', 'todo'],
                            help='Type of list you want to get can be blank, `done`, `in-progress`, `todo` ')
    
    args = parser.parse_args()
    
    if args.command == 'add':
        handle_add(args.title)
    elif args.command == 'delete':
        handle_delete(args.id)
    elif args.command == 'update':
        handle_update(args.id, args.title)
    elif args.command == 'mark-in-progress':
        handle_status(args.id, 'in-progress')
    elif args.command == 'mark-done':
        handle_status(args.id, 'done')
    elif args.command == 'list':
        handle_list(args.list_type)
    else:
        parser.print_help()
        
def handle_add(title):
    
    if not os.path.exists(file_path):
        tasks = [
            {
                'id': 1,
                'description': title,
                'status': 'todo',
                'createdAt': datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S'),
                'updatedAt': None
            }
        ]
        
        with open(file_path, 'w') as file:
            json.dump(tasks, file, indent=2)
            
    else:
        with open(file_path, 'r') as file:    
            tasks = json.load(file)
            max_id = max(task['id'] for task in tasks)
            new_task = {
                'id': max_id+1,
                'description': title,
                'status': 'todo',
                'createdAt': datetime.datetime.now().strftime('%d/%m/%Y, %H:%M:%S'),
                'updatedAt': None
            }
            
            tasks.append(new_task)
        
        
        with open(file_path, 'w') as file:
            json.dump(tasks, file, indent=2)
            print(f'Task added successfully (ID:{max_id+1})')
            
def handle_delete(id):
        with open(file_path, 'r') as file:
            tasks = json.load(file)
            task_to_delete = None
            for task in tasks:
                if task['id'] == int(id):
                    task_to_delete = task
                    
                    
            if task_to_delete != None:
                tasks.remove(task_to_delete)
                with open(file_path, 'w') as file:
                    json.dump(tasks, file, indent=2)
                print('Task deleted successfully')
            else:
                print(f'Task with ID: {id} doesnt exist')

def handle_update(id, title):
    with open(file_path, 'r') as file:
            tasks = json.load(file)
            exists_task = False
            for task in tasks:
                if task['id'] == int(id):
                    task['description'] = title
                    exists_task = True
                    
                    
            if exists_task:
                with open(file_path, 'w') as file:
                    json.dump(tasks, file, indent=2)
                print('Task updated successfully')
            else:
                print(f'Task with ID: {id} doesnt exist')
                
def handle_status(id, status):
    with open(file_path, 'r') as file:
            tasks = json.load(file)
            exists_task = False
            for task in tasks:
                if task['id'] == int(id):
                    task['status'] = status
                    exists_task = True
                    
                    
            if exists_task:
                with open(file_path, 'w') as file:
                    json.dump(tasks, file, indent=2)
                print(f'Task marked as {status} successfully')
            else:
                print(f'Task with ID: {id} doesnt exist')
                
def handle_list(list_type):
    with open(file_path, 'r') as file:
            tasks = json.load(file)
            if list_type == 'all':
                for task in tasks:
                    print(task)
            else:
                for task in tasks:
                    if task['status'] == list_type:
                        print(task)