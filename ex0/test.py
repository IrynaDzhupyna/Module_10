def multiply(x, y):
    return x * y

def main():
    result = multiply(7, 3)
    print(result)

    print()

    result_2 = lambda x, y: x * y
    print(result_2(3, 4))

    

main()