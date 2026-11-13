habits = ('Reading','Coding','Studying')
print('My habits are',habits)
completed = 0
missed = 0
task_status = (1,1,0,0,1,1,0)
for i in range(0,7):
    if task_status[i] == 1:
        completed+=1
    elif task_status[i] == 0:
        missed+=1
print('You completed',completed,'task(s) and missed',missed,'task(s)')
to_do_list = ('Buy clothes','Walk the dog','Code a program')
print('Your errands are',to_do_list[0],'and',to_do_list[2])
print('You already completed',to_do_list[1])
