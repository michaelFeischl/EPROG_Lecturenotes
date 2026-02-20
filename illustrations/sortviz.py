import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation
from math import sin, pi


fig, ax = plt.subplots(1,1)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            ax.clear()
            ax.bar(range(n), arr, color='lightblue')
            plt.pause(0.01)

n=40        
data = [random.random() for _ in range(n)]
bubble_sort(data)

# def bubble_sort(arr, k):
#     n = len(arr)
#     counter = 0
#     for i in range(n):
#         for j in range(0, n-i-1):
#             counter += 1
#             if counter == k:
#                 return
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
    
# n=40        
# data = [random.random() for _ in range(n)]


# fig, ax = plt.subplots()

# x = [i for i in range(n)] 
# bars = ax.bar(x, data, color='lightblue')

# def animate(i):
#     tmp = data.copy()
#     bubble_sort(tmp, i)
#     for bar, height in zip(bars, tmp):
#         bar.set_height(height)
#     return bars,

# ani = animation.FuncAnimation(
#     fig, animate, interval=20, frames=int(n*(n+1)/2)+1)
# ani.save('sort.gif', writer='pillow')
# #plt.show()