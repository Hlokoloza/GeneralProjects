def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if not swapped:
            break
    return arr

user_input=input('Enter numbers seperated by b: ')
mylist=[int(i) for i in user_input.split('b')]
interger_list=[int(j) for j in mylist]
print('Here is a list of string values',mylist)
print(f'Here is a list of integer values {interger_list}')
print('Here is the bubble sorted list',bubble_sort(interger_list))
