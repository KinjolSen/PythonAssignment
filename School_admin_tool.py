#Project: Basic School Administration Tool

condition = True

while(condition):
    student_info = input("Enter student information: ")
    print(student_info)
    
    condition_check = input("Enter (yes/no) if you want to continue to enter student information for another student: ")
    if condition_check == "yes":
        condition = True
    elif condition_check == "no":
        condition = False
    