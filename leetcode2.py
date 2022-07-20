"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""
result_as_list = []
def input(a):
    i = 0
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        if int(str(a)[i]) in numbers:
            i += 1
        try:
            if int(str(a)[i]) not in numbers:
                break
        except:
            break
    while i < 32:
        result_as_list.append(str(a)[i -1])
        i -= 1
        if i == 0:
            break
    else:
        print("your input has more than 32 integers")
    if result_as_list[0] == "0":
        del result_as_list[0]
    print(result_as_list)

def main():
    input()


if __name__ == '__main__':
    main()