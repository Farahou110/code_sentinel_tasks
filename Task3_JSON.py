import os
import json
task_file="tasks.json"


def load():
    if os.path.exists(task_file):
        with open(task_file, "r") as file:
            return json.load(file)
    return []
    
def save(tasks):
    with open (task_file,"w") as file:
        json.dump(tasks,file,indent=4)


def add_new(tasks):
    new_task =input("enter task number")
    tasks.append(new_task)
    save(tasks) 
    print("task added")
    
def delete(tasks):
    display_task(tasks)
 
    index=int(input("enter task number to be deleted"))-1

    if 0<=index<len(tasks):
        removed = tasks.pop(index)
        save(tasks)
        print("removes : {removed}")
    else:
        print("invalid task")
    
   

def display_task(tasks):
    if not tasks:
        print("no task to be displayed")
    else:
        print("\n ----to do task include------")
    for i, task in enumerate(tasks,1):
     print(f"{i}.){task}""\n")

def view_raw_json():
    if os.path.exists(task_file):
        with open(task_file, "r") as file:
            print("\nRaw tasks.json contents:")
            print(file.read())
    else:
        print("tasks.json file does not exist.")

def main():
    tasks=load()
    while True:
        print("\n1: add task \n2: Remove task \n3: View tasks \n4: View raw tasks.json \n5: exit")
        choice=int(input("please choose option"))
    
        if choice==1:
           add_new(tasks)
        elif choice==2:
           delete(tasks)
        elif choice==3:
           display_task(tasks)
        elif choice==4:
           view_raw_json()
        elif choice == 5:
           print("goodbye")
           break
        else :
         print("invalid choice!!please select a valid choice")
     
    print("enter a valid number")
if __name__=="__main__":
    main()




