def LearnToSubtract ():
    '''Gives user random subtraction problems.'''
    import random
    while True:
        n1 = random.randint(0,9)
        n2 = random.randint (9,20)
        print('What is: \n')
        problems = input(str(n2) + "-" + str(n1) + "= ") #Subtraction so bigger # first as we do not want a neg
        if int(problems) == n2 - n1:
            print('Correct!')
        else:
            print('That is incorrect.')
        learn = input('Would you like to learn more? ')
        if learn != 'yes':
             print('Goodbye.')
             break
print(LearnToSubtract())
