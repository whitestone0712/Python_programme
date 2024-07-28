def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    top_row = []
    bottom_row = []
    dashes = []
    answers = []

    for problem in problems:
        # Split the problem into parts
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Each problem should have two operands and one operator."

        left, operator, right = parts

        # Check operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Check if operands are digits
        if not (left.isdigit() and right.isdigit()):
            return 'Error: Numbers must only contain digits.'

        # Check length of operands
        if len(left) > 4 or len(right) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Calculate width of the problem
        width = max(len(left), len(right)) + 2

        # Format rows
        top_row.append(left.rjust(width))
        bottom_row.append(operator + right.rjust(width - 1))
        dashes.append('-' * width)

        # Calculate answer if required
        if show_answers:
            if operator == '+':
                answer = str(int(left) + int(right))
            else:
                answer = str(int(left) - int(right))
            answers.append(answer.rjust(width))

    # Join rows
    arranged_problems = '    '.join(top_row) + '\n' + \
                        '    '.join(bottom_row) + '\n' + \
                        '    '.join(dashes)

    # Add answers if required
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

'''
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["3801 - 2", "123 + 49"])
arithmetic_arranger(["1 + 2", "1 - 9380"])
arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["3 + 855", "988 + 40"], True)
arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)

'''