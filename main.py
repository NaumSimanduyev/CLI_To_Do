import json, datetime, time

def display_tasks():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)

        print('Your current tasks:')

        if len(data.keys()) == 0:
            print('No current tasks')
        else:
            for i in data.keys():
                print(i)
                print('\t', end='')
                print(*data[i], sep=f'\n\t')

    except json.decoder.JSONDecodeError:
        print('No current tasks.')

def new_task():
    date = datetime.date.today().strftime("%y:%m:%d")

    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except:
        data = {}

    if date not in data.keys():
        data[date] = list()

    data[date].append(input('Write a task: '))

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

    display_tasks()

def remove_task():
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)

        display_tasks()
        while len(data) != 0:
            time.sleep(1)
            

            date = input('choose a date: ').strip()
            if date in data.keys():
                for i in range(len(data[date])):
                    print(f'{i+1}) {data[date][i]}')
                try:
                    del_task = int(input('Choose a task to delete: ').strip())
                    del data[date][del_task-1]
                except:
                    print('Please enter a valid task number to delete.')
                    continue
                
                if data[date] == []:
                    del data[date]

                with open('data.json', 'w') as f:
                    json.dump(data, f, indent=4)

                display_tasks()
                break
            else:
                print('Please enter a valid date.')

    except json.decoder.JSONDecodeError:
        print('There are no tasks to delete')

print('Welcome to the To Do app.')
while True:
    time.sleep(1)
    actions = {'1': new_task, '2': display_tasks, '3': remove_task}
    action = input('What do you want to do?\n1) Add a new task\n2) Watch current tasks\n3) Remove a task\n').strip()
    if action in actions.keys():
        actions[action]()
    else:
        print('Please enter a valid command.')