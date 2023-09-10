
##Toke Atijosan grade calculator ##

# 
def calc_average():
    # a loop and ask the user to enter EIGHT scores
    num = 0
    grade = 0
    avg = 0
    for num in range(1,9):
     num = int (input("Please enter score:#{}:".format(num)))
     grade = grade + num



    avg = grade/ 8
    

    # convert avg to integer and return the value. 

    return int(avg)
    
    


def determine_grade(score):
    # Convert the numeric score into letter grade
    # 90-100:   A
    # 80-89:    B
    # 70-79:    C
    # 60-69:    D
    # below 60: F 


    if score >=90:
        return 'A'
    elif score >=80 and score <90:
        return 'B'
    elif score >=70 and score <80:
        return 'C'
    elif score >=60 and score <70:
        return'D'
    else:
        return 'F'
    return grade


# Do NOT change any of the lines below
def main():

    avg = calc_average()
    grade = determine_grade(avg)

    print ("Your average grade is:", grade)


