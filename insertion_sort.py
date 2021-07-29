def insertion_sort(input_list):
    current_sorted = 1
    while current_sorted != len(input_list):
        for i in range(current_sorted, 0, -1):
            #print(input_list[i], input_list[i-1])
            if input_list[i] > input_list[i-1]:
                break
            else:
                temp = input_list[i]
                input_list[i] = input_list[i-1]
                input_list[i-1] = temp
        current_sorted = current_sorted + 1
        print(input_list)
        
# add any list of number here 
l =  [1, 2, 3, 4, 5, 6] #[5,2,4,6,1,3]
insertion_sort(l)
print(l)
