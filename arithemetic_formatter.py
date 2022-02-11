#!/usr/bin/python3.9

import re

def arithmetic_arranger(problems, answer_display = False):
    arranged_problems = ''
    space = ' '
    line = '-'
    newline = '\n'
    operands0 = list()
    operands1 = list()
    operators = list()
    for problem in problems:

        if len(problems) > 5:
            return 'Error: Too many problems.'

        if re.search("[*/]", problem):
            return "Error: Operator must be '+' or '-'."

        if re.search("[^\d\s+-]", problem):
            return "Error: Numbers must only contain digits."
        
        if len(problem.split()[0]) > 4 or len(problem.split()[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        operands0.append(problem.split()[0])
        operators.append(problem.split()[1])        
        operands1.append(problem.split()[2])
        
    # the 1st row
    count1 = 0
    for operand0, operand1 in zip(operands0, operands1):

        width = max(len(operand0), len(operand1))
        if count1 != len(operands0) - 1:
            arranged_problems += 2*space + operand0.rjust(width) + 4*space
        else:
            arranged_problems += 2*space + operand0.rjust(width)
        count1 += 1
    
    arranged_problems += newline
    
    # the 2nd row
    count2 = 0
    for operand0, operand1, operator in zip(operands0, operands1, operators):
        
        width = max(len(operand0), len(operand1))
        if count2 != len(operands0) - 1:
            arranged_problems += operator + space + operand1.rjust(width) + 4*space
        else:
            arranged_problems += operator + space + operand1.rjust(width)
        count2 += 1

    arranged_problems += newline

    # the 3rd row
    count3 = 0
    for operand0, operand1 in zip(operands0, operands1):
        width = max(len(operand0), len(operand1))
        if count3 != len(operands0) - 1:
            arranged_problems += 2*line + width*line + 4*space
        else:
            arranged_problems += 2*line + width*line
        count3 += 1

    if answer_display:
        arranged_problems += newline

        # Perform calculation and store in list sols
        sols = list()
        for operand0, operand1, operator in zip(operands0, operands1, operators):
            if operator == '+':
                sols.append(int(operand0) + int(operand1))
            else:
                sols.append(int(operand0) - int(operand1))

        # the 4th row, solution row
        count4 = 0
        for operand0, operand1, sol in zip(operands0, operands1, sols):
            width = max(len(operand0), len(operand1))
            if count4 != len(sols) - 1:
                if len(str(sol)) > width:
                    arranged_problems += space + str(sol).rjust(width) + 4*space
                else:
                    arranged_problems += 2*space + str(sol).rjust(width) + 4*space
            else:
                if len(str(sol)) > width:
                    arranged_problems += space + str(sol).rjust(width)
                else:
                    arranged_problems += 2*space + str(sol).rjust(width)
            count4 += 1

    return arranged_problems


def main():
    # Testing :
    print(arithmetic_arranger(["32 + 698"]))
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
    print(arithmetic_arranger(['1 + 2', '1 - 9380'], True))
    print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'], True))
    print(arithmetic_arranger(['3801 - 2', '123 + 49'], True))


if __name__ == '__main__':
    main()