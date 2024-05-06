def doubleChar():
    str_ = str(input("Enter the character or word for double: "))
    dbl_str = []
    for i in str_:
        dbl_str += i * 2

    dbl_string = ''.join(map(str, dbl_str))

    return dbl_string


print(doubleChar())