"""
Q1. Number of Students Unable to Eat Lunch
Easy
Topics
premium lock icon
Companies
Hint
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.



Example 1:

Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.
Example 2:

Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3
"""
from collections import deque

def count_students_unable_to_eat_lunch(students: list[int], sandwiches: list[int]) -> int:
    no_body_want_sandwich = 0
    
    while students:
        if no_body_want_sandwich == len(students):
            break
            
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            no_body_want_sandwich = 0
        else:
            students.append(students.pop(0))
            no_body_want_sandwich += 1
           
    return len(students)
    
students = [1,1,0,0]
sandwiches = [0,1,0,1]
count_students_unable_to_eat_lunch(students, sandwiches)

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
count_students_unable_to_eat_lunch(students, sandwiches)


def deque_count_students_unable_to_eat_lunch(students: list[int], sandwiches: list[int]) -> int:
    students = deque(students)
    sandwiches = deque(sandwiches)
    no_body_want_sandwich = 0
    
    while students:
        if no_body_want_sandwich == len(students):
            break
        
        if students[0] == sandwiches[0]:
            students.popleft()
            sandwiches.popleft()
            no_body_want_sandwich = 0
        else:
            students.append(students.popleft())
            no_body_want_sandwich += 1
    
    return len(students)

students = [1,1,0,0]
sandwiches = [0,1,0,1]
deque_count_students_unable_to_eat_lunch(students, sandwiches)

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
deque_count_students_unable_to_eat_lunch(students, sandwiches)


def new_count_students_unable_to_eat_lunch(students: list[int], sandwiches: list[int]) -> int:
    deque_students = deque(students)
    deque_sandwiches = deque(sandwiches)
    
    while deque_students:
        if deque_sandwiches[0] not in deque_students:
            break
        
        if deque_students[0] == deque_sandwiches[0]:
            deque_students.popleft()
            deque_sandwiches.popleft()
        else:
            deque_students.append(deque_students.popleft())
    
    return len(deque_students)
    

students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]