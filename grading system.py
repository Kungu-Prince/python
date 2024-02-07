#grading system based on three subjects
OOSAD= float(input("Enter OOSAD grade: "))
GRAPHICS= float(input("Enter GRAPHICS grade: "))
NETWORKING= float(input("Enter NETWORKING grade: "))
SCORE = (OOSAD + GRAPHICS + NETWORKING) / 3
print ("Total Score: ", SCORE)
if  SCORE >= 70 and SCORE <= 100:
    print("GRADE IS A")
elif SCORE >= 60 and SCORE <= 69:
    print("GRADE IS B")
elif SCORE >= 50 and SCORE <= 59:
    print("GRADE IS C")
elif SCORE >= 40 and SCORE <= 49:
    print("GRADE IS D")
elif SCORE >= 0 and SCORE <= 39:
    print("Fail")
else:
    print("out of bound values")
