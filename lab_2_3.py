import string
import os
import threading


def merge_sort(array):
    n = len(array)
    if n < 2:
        return array

    left = merge_sort(array[0:n//2])
    right = merge_sort(array[n//2:n])

    i = j = 0
    sort_array = []
    while (i < len(left)) or (j < len(right)):
        if i >= len(left):
            sort_array.append(right[j])
            j += 1
        elif j >= len(right):
            sort_array.append(left[i])
            i += 1
        elif left[i] < right[j]:
            sort_array.append(left[i])
            i += 1
        else:
            sort_array.append(right[j])
            j += 1

    return sort_array

def thread_fun(x, y, fun):
    if fun == 'sort':
        for _ in range(x, y):
            string[_] = string[_].split()
            string[_] = merge_sort(string[_])
    if fun == 'join':
        for _ in range(x,y):
            string[_] = ' '.join(string[_])
    if fun == 'write':
        file = open('additional/sorted.txt','w')
        for _ in string:
            file.write(_ + '\n')
        file.close()



file = open('additional/text.txt','r')
string = file.read().split('\n')
file.close()
length = len(string)


thread1 = threading.Thread(target=thread_fun, args=(0, length//2, 'sort'))
thread2 = threading.Thread(target=thread_fun, args=(length//2, length, 'sort'))

thread1.start(); thread2.start()
thread1.join(); thread2.join()

string = merge_sort(string)

thread3 = threading.Thread(target=thread_fun, args=(0, length//2, 'join'))
thread4 = threading.Thread(target=thread_fun, args=(length//2, length, 'join'))

thread3.start(); thread4.start()
thread3.join(); thread4.join()

thread_fun(0,0,'write')
