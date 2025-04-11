def main():
    i = 0 
    N = int(input('Enter the number N: '))
    result = [0] * (N + 1)
    for i in range(N + 1):
        result[i] = 2 ** i
    print (f'{result}')
    
    

    """
    ########################################
    Code Your Program here
    ########################################
    """

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
