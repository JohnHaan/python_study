

def return_even(x):
    return x % 2 == 0

def return_odd(x):
    return x % 2 == 1


def main():
    x_list = [1,2,3,4,5,6,7,8,9,10]
    print(list(filter(return_even, x_list)))
    print(list(filter(return_odd, x_list)))


if __name__ == '__main__':
    main()