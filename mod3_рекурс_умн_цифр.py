def get_multiplied_digits(number):
    str_number = str(number)


    if len(str_number) > 1:
        first = int(str_number[0])
        if first != 0:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            return get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number) if int(str_number) != 0 else 1  # Для нуля возвращаем 1


result = get_multiplied_digits(40203)
result2 = get_multiplied_digits(402030)

print(result)
print(result2)
