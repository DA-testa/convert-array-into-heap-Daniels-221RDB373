# python3


def build_heap(data):
    n =  len (data)
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range (n // 2, -1, -1):
        j = i 
        while 2 * j + 1 < n:
            k = 2 * j + 1
            if k + 1 < n and data[k + 1] < data[k]:
                k += 1
            if data[j] <= data[k]:
                break
            swaps.append((j, k))
            data[j], data[k] = data[k], data[j]
            j = k
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    input_type = input()
    if input_type == 'F':
        file_name = input()
        if 'a' in file_name:
            print("Invalid file name.")
            exit()
        try:
            input_file = open("tests/" + file_name)
            n = int(input_file.readline())
            data = list(map(int, input_file.readline().split()))
            input_file.close()
        except:
            print("Error while reading file.")
            exit()
        #swaps = build_heap(data)
        #print(len(swaps))
    elif input_type == 'I':
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
        #swaps = build_heap(data)
        #print(len(swaps))

        #for i, j in swaps:
            #print(i, j)

    else:
        print("Invalid input type.")
        return

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    # calls function to assess the data 
    # and give back all swaps
    #swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    #print(len(swaps))
    


if __name__ == "__main__":
    main()
