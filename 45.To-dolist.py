#To-do list
class Todolist():
    def __init__(self,title,due,status):
        self.title=title
        self.due=due
        self.status=status
        
   
    def show(self):
        print(f"The task :{self.title}")
        print(f"Due date: {self.due}")
        print(f"Status:{self.status}")

def user_task():
        title=input("Enter the \"task\": ")
        due=input("Enter the due date(Y-M-D): ")
        status=input("Enter the status: ")
        try:
               if(len(title)>0 and len(due)>0 and len(status)>0):
                    user1=Todolist(title,due,status)
                    user1.show()
                    with open('todolist.txt','a') as f:
                         f.write(f"The task : {title.capitalize()}\n")
                         f.write(f"Due date: {due}\n")
                         f.write(f"Status: {status.capitalize()}\n")
        except:
             print("Inputs can't be blank!")
def view_task():
        with open('todolist.txt','r') as fr:
         data=fr.readlines()
         for line in data:
              print(line.rstrip())
def delete_task():
    # Step 1: Ask the user which task they want to delete
    task_title = input("Enter the title of the task you want to delete: ")

    # Step 2: Read existing tasks from the file
    with open('todolist.txt', 'r') as fr:
        tasks = fr.readlines()  # Read all lines into the tasks list
        print(tasks)
    new_tasks = []  # This will hold tasks after deletion
    task_found = False  # Flag to check if the task is found

    # Step 3: Check each task
    for i in range(0, len(tasks), 4):  # Assuming each task is 4 lines long
        task_line = tasks[i].strip()  # Get the task title line
        splitted=task_line.split(':')[1].strip()
        if task_title.lower() is splitted.lower():  # Check if it matches
            task_found = True  # Set the flag
            continue  # Skip adding this task to new_tasks
        new_tasks.extend(tasks[i:i+4])  # Add the task back to new_tasks

    # Step 4: Write the remaining tasks back to the file
    with open('todolist.txt', 'w') as fw:
        fw.writelines(new_tasks)  # Write the updated task list

    if not task_found:
        print("Task not found.")  # Inform the user if the task was not found   
def edit_task():
     with open('todolist.txt','r') as f:
          data=f.read()
          print(data)
     print("Which word do you want to exit?")
     word=input('')
     print("What word do you wanna replace it with? ")
     newWord=input('')
     if word in data:
          with open('todolist.txt','w') as fr:
               fr.write(data.replace(word,newWord))
while True:
     user_decision=input("Do you want to add/view/delete/edit/exit task? ")
     if(user_decision.lower()=='add'):
        user_task()
              
     if(user_decision.lower()=='view'):
          view_task()
     
     if(user_decision.lower()=='delete'):
          delete_task()
     if(user_decision.lower()=='edit'):
          edit_task()
     if user_decision.lower()=='exit':
          quit()