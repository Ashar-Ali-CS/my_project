
# tiny command line app 
# example program (sparta global) for git workflow excerisego

#caps list 
MAX_TASKS = 10



def add_tasks(tasks,description):
      """Add a new task. Return False if list is already full."""
      if len(tasks) >= MAX_TASKS:
           return False 
      tasks.append({"description": description,"done": False})
      return True


def complete_task(tasks,index):
      """Mark task as done ,but position in the list ."""
      if index < 0 or index >= len(tasks):
            return False
      tasks[index] ["done"] = True
      return True


def remove_task(tasks,index):
    """remove task by index"""
    if index < 0 or index >= len(tasks):
         return False
    tasks.pop(index)
    return True


def list_tasks(tasks):
    """Display all tasks."""
    for task in tasks:
     print(task)