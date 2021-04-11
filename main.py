while True:

    nterm = int(input('How many numbers would you like to see?\n'))
    x = 0
    y = 1
    count = 0

    if nterm <= 0:
        print('Please use only positive amount of numbers')
    elif nterm == 1:
        print('Fibonacci Sequence for', nterm, ':\n')
        print(x)
    else:
        print('Fibonacci Sequence:\n')
        while count < nterm:
            print(x)
            fs = x + y
            x = y
            y = fs
            count += 1
    while True:
        answer = str(input('Would you like to continue?\n'))
        if answer in ('yes', 'y', 'n', 'no'):
            break
        print('invalid input')
    if answer == 'yes' or answer == 'y':
        continue
    else:
        print('Goodbye')
        break
