def LearnMaths():
    '''Takes input from user on what math operation they want to learn.
Choices are: +, -, * and /'''
    Learn = input('What would you like to learn? ')
    if Learn in ['Addition', 'addition', 'add', 'Add', 'adding', 'Adding', '+']:
        from modules import  LearnToAdd
        print(LearnToAdd())
    elif Learn in ['subtraction', 'Subtraction', 'Subtract', 'subtract', '-']:
        from modules import LearnToSubtract
        print(LearnToSubtract())
    elif Learn in ['Multiply', 'multiply', 'multiplication', 'Multiplication', '*']:
        from modules import LearnToMultiply
        print(LearnToMultiply())
    elif Learn in ['divide', 'Divide', '/']:
        from modules import LearnToDivide
        print (LearnToDivide())
    else:
            print('Incorrect input. I need an operation.' +  '\nGoodbye!')
        
print (LearnMaths())

