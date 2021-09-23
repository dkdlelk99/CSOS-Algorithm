#  2751
import sys

list_ =[]
for _ in range(int(sys.stdin.readline())):
    list_.append(int(sys.stdin.readline()))

def merge_sort(list_):
    if len(list_)<=1:
        return list_
    
    mid = len(list_)//2
    
    left = merge_sort(list_[:mid])
    right = merge_sort(list_[mid:])
    
    merged_list = []
    left_index=0
    right_index=0
    
    while left_index<len(left) and right_index<len(right):
        if left[left_index]>right[right_index]:
            merged_list.append(right[right_index])
            right_index+=1
        else:
            merged_list.append(left[left_index])
            left_index+=1
            
    if left_index != len(left):
        merged_list += left[left_index:]
    if right_index != len(right):
        merged_list += right[right_index:]
    
    return merged_list

[print(i) for i in merge_sort(list_)]
