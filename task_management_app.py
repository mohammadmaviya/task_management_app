def task():
    tasks = []
    print("--------Welcome to the Task Management App---------")

    total_task = int(input("Enter how many task you want to add : "))

    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
    
    print(f"Today tasks are {tasks}")

    while True:
        operation = int(input("\nEnter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/stop\n"))

        if operation == 1:
            add = input("Enter Task you want to add = ")
            tasks.append(add)
            print(f"Task {add} successfully added")

        elif operation == 2:
            old_task = input("enter task you want to update = ")

            if old_task in tasks:
                new_val = input("Enter updated task = ")
            ind = tasks.index(old_task)
            tasks[ind] = new_val
            print(f"Updated task {old_task} to {new_val}. ")

        elif operation == 3:
            del_val = input("enter task to be delete = ")

            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task {del_val} has be deleted.")

        elif operation == 4:
            print("Total task is : ")
            for list in tasks:
                print(list)

        elif operation == 5:
            print("closing the program...")
            break

        else:
            print("Invalid input. please enter a valid number")

task()