def in_short(mystring):
    count = 1
    res = ''

    for i, char in enumerate(mystring):
        try:
            if char == mystring[i + 1]:
                count += 1
            else:
                if count == 1:
                    res += str(char)
                else:
                    res += str(count)
                    res += str(char)
                count = 1

        except IndexError:
            if count == 1:
                res += str(char)
            else:
                res += str(count)
                res += str(char)
    return res

string = input()
print(in_short(string))