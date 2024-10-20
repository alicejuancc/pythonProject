"""
File: class_reviews.py
Name: Alice
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

# This constant controls when to stop calculating
STOP = '-1'


def main():
    """
    This program can calculate the maximum, minimum, and average of scores of SC001 or SC101.
    """
    amount001 = 0
    amount101 = 0
    total001 = 0
    total101 = 0
    class_name = input('Which class? ').upper()
    if class_name == STOP:
        print('No class scores were entered.')
    else:
        score = int(input('Score: '))
        if class_name == 'SC001':
            max001 = score
            min001 = score
            amount001 = 1
            total001 = score
        elif class_name == 'SC101':
            max101 = score
            min101 = score
            amount101 = 1
            total101 = score
        while True:
            class_name = input('Which class? ').upper()
            if class_name == STOP:
                break
            score = int(input('Score: '))
            if class_name == 'SC001':
                amount001 += 1
                total001 += score
                if amount001 == 1:
                    max001 = score
                    min001 = score
                if score > max001:
                    max001 = score
                if score < min001:
                    min001 = score
            elif class_name == 'SC101':
                amount101 += 1
                total101 += score
                if amount101 == 1:
                    max101 = score
                    min101 = score
                if score > max101:
                    max101 = score
                if score < min101:
                    min101 = score
        print('=========SC001=========')
        if amount001 == 0:
            print('No score for SC001')
        else:
            print('Max(001): ' + str(max001))
            print('Min(001): ' + str(min001))
            print('Avg(001): ' + str(total001 / amount001))
        print('=========SC101=========')
        if amount101 == 0:
            print('No score for SC101')
        else:
            print('Max(101): ' + str(max101))
            print('Min(101): ' + str(min101))
            print('Avg(101): ' + str(total101 / amount101))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
