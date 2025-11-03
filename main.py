import matplotlib.pyplot as plt

sizes = [10, 15, 20, 25, 30, 35, 40, 45, 50, 
 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 
 105, 110, 115, 120, 250, 500, 750, 1000, 1500, 2000]
bubble_comparisons = []
selection_comparisons = []
merge_comparisons = []

# put your code here

plt.plot(sizes, bubble_comparisons, label="bubble sort")
plt.plot(sizes, selection_comparisons, label="selection sort")
plt.plot(sizes, merge_comparisons, label="merge sort")
plt.legend()
plt.show()
