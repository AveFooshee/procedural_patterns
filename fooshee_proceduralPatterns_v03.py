def get_square_pattern(max_rows=1):
    emoji = '🐟'
    result = str('')
    for row in range(max_rows):
        result += emoji * max_rows
        result += '\n'
    return result


def get_rect_pattern(max_rows=1, max_cols=1):
    emoji = '🐟'
    result = str('')
    for row in range(max_rows):
        result += emoji * max_cols
        result += '\n'
    return result


def get_alternating_rect_pattern(max_rows=1, max_cols=1):
    pig_emoji = '🐟'
    cow_emoji = '🦈'
    result = str('')
    for row in range(max_rows):
        if row % 2 == 0:
            result += cow_emoji * max_cols
            result += '\n'
        else:
            result += pig_emoji * max_cols
            result += '\n'
    return result


def get_brick_pattern(max_rows=1, max_cols=1, running_bond=False):
    brick = '🧱'
    result = str('')
    for row in range(max_rows):
        if running_bond is True and max_rows % 2 == 0:
            if row % 2 == 0:
                result += " " + brick * max_cols
                result += "\n"
            else:
                result += brick * max_cols
                result += '\n'
        elif running_bond is True and max_rows % 2 != 0:
            if row % 2 == 0:
                result += brick * max_cols
                result += '\n'
            else:
                result += " " + brick * max_cols
                result += "\n"
        else:
            result += brick * max_cols
            result += "\n"
    return result


def get_checkered_pattern(max_rows=1, max_cols=1):
    pig_emoji = '💎'
    cow_emoji = '👑'
    result = str('')
    for row in range(max_rows):
        for col in range(max_cols):
            if row % 2 != 0 and col % 2 != 0 or row % 2 == 0 and \
             col % 2 == 0:
                result += pig_emoji
            elif row % 2 == 0 and col % 2 != 0 or row % 2 != 0 and \
                    col % 2 == 0:
                result += cow_emoji
        result += "\n"
    return result


def get_right_arrow_pattern(max_cols):
    emoji = '🐟'
    result = str('')
    row = 0
    while row <= max_cols * 2:
        if row <= max_cols:
            result += emoji * row
            result += '\n'
            row += 1
        elif row > max_cols and row <= max_cols * 2:
            result += emoji * ((max_cols * 2) - row)
            result += '\n'
            row += 1
    return result


def get_my_awesome_pattern(half_cols, hourglass=False):
    butterfly_emoji = '🦋'
    hourglass_emoji = '⏳'
    result = str('')
    row = 0
    if hourglass is False:
        while row <= half_cols * 2:
            if row <= half_cols:
                # butterfly upper half
                result += butterfly_emoji * row + " " * (half_cols - row)\
                      * 4 + butterfly_emoji * row
                result += '\n'
                row += 1
            elif row > half_cols and row <= half_cols * 2:
                # butterfly lower half
                result += butterfly_emoji * ((half_cols * 2) - row) + " " * \
                    (row - half_cols) * 4 + butterfly_emoji * \
                    ((half_cols * 2) - row)
                result += '\n'
                row += 1
    if hourglass is True:
        while row <= half_cols * 2:
            if row <= half_cols:
                # hourglass upper half
                result += " " * row * 2 + hourglass_emoji * \
                    (half_cols - row) * 2
                result += '\n'
                row += 1
            elif row > half_cols and row <= half_cols * 2:
                # hourglass lower half
                result += " " * ((half_cols * 2) - row) * 2 + \
                    hourglass_emoji * (row - half_cols) * 2
                result += '\n'
                row += 1
    return result


def main():
    print(get_my_awesome_pattern(8))
    print(get_my_awesome_pattern(8, hourglass=True))
    print(get_my_awesome_pattern(5, hourglass=True))
    print(get_my_awesome_pattern(11))


if __name__ == "__main__":
    main()
