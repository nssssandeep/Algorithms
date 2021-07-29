def bubble_sort(input_list):
    for i in range(len(input_list)):
        issorted = True
        for j in range(len(input_list)-i-1): # the last element is always the highest after each iteration
            if input_list[j] > input_list[j+1]:
                temp = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1] = temp
                issorted = False
        print(l)
        if issorted == True:
            break # if you don't do any swaps it means array is sorted and we can stop

# add any list of number here 
l = [1, 2, 3, 4, 5, 6] # [5,2,4,6,1,3]
bubble_sort(l)
print(l)
