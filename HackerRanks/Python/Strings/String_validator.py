if __name__ == '__main__':
    s = input()
    validator = 5 * [False]
    for char in s:
        if not validator[0]:
            validator[0] = char.isalnum()
        if not validator[1]:
            validator[1] = char.isalpha()
        if not validator[2]:
            validator[2] = char.isdigit()
        if not validator[3]:
            validator[3] = char.islower()
        if not validator[4]:
            validator[4] = char.isupper()

    for answer in validator:
        print(answer)