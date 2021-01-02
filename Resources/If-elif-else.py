# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')
    
    
    #the length of the decision structure determines 
    # whether you use a nested if-else statement or the if-elif-else statement. 
    # If you have to scroll horizontally on your computer screen to see all the code in an 
    # if-else statement , then you should use an if-elif-else statement.