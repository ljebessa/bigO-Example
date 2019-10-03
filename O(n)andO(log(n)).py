## List is sorted, but then rotated.
  # Find the minimum element in less than linear time
  # return it's index

#O(n)
def find_pivot_index(input_list):
    
    for current_ele_index in range(len(input_list)):
        
        if input_list[current_ele_index] < input_list[current_ele_index - 1]:
            
            return current_ele_index 
    return 0
    
  
find_pivot_index([4,5,6,7,8,9,10,11,12,2,3])


#O(log(n))
def find_pivot_index(input_list):
    start = 0
    end = len(input_list) - 1
    min_index = 0
    
    while start < end - 1 :
        if end - start % 2 == 0:
            pivot = int((end - start)/2) + start
        else:
            pivot = int((end - start + 1)/2) + start
            
        if input_list[pivot] < input_list[min_index]:
            end = pivot
            min_index = pivot
        else:
            start = pivot
    return min_index
find_pivot_index([4,5,6,7,8,9,10,11,12,1,2,3])


