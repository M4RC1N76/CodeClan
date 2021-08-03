# import pbd


tasks = [
    {"description": "Wash Dishes", "completed": False, "time_taken": 10},
    {"description": "Clean Windows", "completed": False, "time_taken": 15},
    {"description": "Make Dinner", "completed": True, "time_taken": 30},
    {"description": "Feed Cat", "completed": False, "time_taken": 5},
    {"description": "Walk Dog", "completed": True, "time_taken": 60},
]
# Print a list of uncompleted tasks
def uncompleted_tasks(task_list):
    for task in task_list:
        if task["completed"] == False:
            print(task)

# uncompleted_tasks(tasks)

# Print a list of completed tasks


def completed_tasks(task_list):
    for task in task_list:
        if task["completed"] == True:
            print(task)


# completed_tasks(tasks)

# Print a list of all task descriptions
def all_tasks(task_list):
    for task in task_list:
        print(task["description"])

# all_tasks(tasks)

# Print a list of tasks where time_taken is at least a (given time)? How to do it?
#def tasks_time_taken(task_list):
 #   for task in task_list:
  #      if task("time_taken") >= ?:
   #         print(task["time_taken"])

#tasks_time_taken(tasks)

# Print any task with a given description
def given_description(task_list):
    for task in task_list:
        if tasks["description"] == ("description"): #???
            print(tasks)

given_description(tasks) # ???