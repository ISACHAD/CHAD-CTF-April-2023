
def main():
    string = ""
    sum = 0
    for i in range(99, 0, -1):
        sum = sum + i + i + i-1
        string += f"{i} bottles of monster on the wall, {i} bottles of monster. Take one down, pass it around, {i-1} bottles of monster on the wall\n"

    print(string)
    start_loc = sum%len(string)
    end_loc = start_loc + 20
    print(type(start_loc))
    print(string[start_loc:end_loc])

main()