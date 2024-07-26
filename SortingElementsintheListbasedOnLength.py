'''Input a list and sort the elements in the list based on its length.
i/p: read the list & o/p:sort the list according to the length '''


input_list = input().split()
sorted_list = sorted(input_list, key=len)
print("Sorted list according to length: ", sorted_list)
