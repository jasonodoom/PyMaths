def LearnToAdd ():
    '''Gives user random addition problems.'''
    import random
    while True:
        n1 = random.randint(0,9)
        n2 = random.randint (9,20)
        print('What is the sum of:  \n')
        problems = input(str(n1) + "+" + str(n2) + "= ")
        if int(problems) == n1 + n2:
            print('Correct!')
        else:
            print('That is incorrect..')
        learn = input('Would you like to learn more? ')
        if learn != 'yes':
            print('Goodbye.')
            break

#print(LearnToAdd())

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

#print(LearnToMultiply())


def LearnToDivide ():
    '''Gives user random division problems.'''
    import random
    while True:
        n1 = random.randint(0,9)
        n2 = random.randint (9,20)
        print('What is : \n')
        problems = input(str(n1) + "/" + str(n2) + "= ")
        if int(problems) == n1 / n2:
            print('Correct!')
        else:
            print('That is incorrect.')
        learn = input('Would you like to learn more? ')
        if learn != 'yes':
             print('Goodbye.')
             break

#print(LearnToMultiply())


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

#print(LearnToSubtract())


def LearnMaths():
    '''Takes input from user of what math operation they want to learn.
Choices are: +, -, * and /'''
    Learn = input('What would you like to learn? ')
    if Learn in ['Addition', 'addition', 'add', 'Add', 'adding', 'Adding', '+']:
        print(LearnToAdd())
    elif Learn in ['subtraction', 'Subtraction', 'Subtract', 'subtract', '-']:
            print(LearnToSubtract())
    elif Learn in ['Multiply', 'multiply', 'multiplication', 'Multiplication', '*']:
                print(LearnToMultiply())
    elif Learn in ['divide', 'Divide', '/']:
                    print (LearnToDivide())
print (LearnMaths())

