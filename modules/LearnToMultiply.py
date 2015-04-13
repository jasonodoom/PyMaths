def LearnToMultiply ():
    '''Gives user random multiplication problems.'''
    import random
    while True:
        n1 = random.randint(0,9)
        n2 = random.randint (9,20)
        print('What is: \n')
        problems = input(str(n1) + "*" + str(n2) + "= ")
        if int(problems) == n1 * n2:
            print('Correct!')
        else:
            print('That is incorrect.')
        learn = input('Would you like to learn more? ')
        if learn != 'yes':
             print('Goodbye.')
             break
print(LearnToMultiply())
