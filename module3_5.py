


def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return number


print(get_multiplied_digits(201))
print(get_multiplied_digits(40203))
print(get_multiplied_digits(2821))