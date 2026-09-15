
# tiny command line app 
# example program (sparta global) for git workflow excerise

#caps list 
MAX_TASKS = 10



def add_tasks(tasks,description):
      """Add a new task. Return False if list is already full."""
      if len(tasks) >= MAX_TASKS:
           return False 
      tasks.append({"description": description,"done": False})
      return True

