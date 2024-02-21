# grading system
def grading(grades):

    if  grades >= 70 and grades <= 100:
        return 'GRADE IS A'
    elif grades >= 60 and grades <= 69:
        return 'GRADE IS B'
    elif grades >= 50 and grades <= 59:
        return 'GRADE IS C'
    elif grades >= 40 and grades <= 49:
        return 'GRADE IS D'
    elif grades >= 0 and grades <= 39:
        return 'GRADE IS FAIL'
    else:
        return 'INVALID GRADE'

score= int(input("enter your score"))
print(grading(score))
