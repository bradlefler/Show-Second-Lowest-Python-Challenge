def quicksort(grades, low, high):
    if low < high:
        pi = partition(grades, low, high)
        quicksort(grades, low, pi - 1)
        quicksort(grades, pi + 1, high)

def partition(grades, low, high):
    pivot = grades[high][1]
    i = (low - 1)
    for j in range(low, high):
        if grades[j][1] < pivot:
            i = i + 1
            temp = grades[j]
            grades[j] = grades[i]
            grades[i] = temp
    temp = grades[i + 1]
    grades[i + 1] = grades[high]
    grades[high] = temp
    return i + 1

N = int(input())
grades = []
for i in range(N):
    name = input()
    grade = float(input())
    temp = [name, grade]
    grades.append(temp)
quicksort(grades, 0, N - 1)

second_lowest = 1
size = len(grades)
while second_lowest < size and grades[second_lowest][1] == grades[second_lowest - 1][1]:
    second_lowest = second_lowest + 1

names = []
names.append(grades[second_lowest][0])
while second_lowest + 1 < size and grades[second_lowest][1] == grades[second_lowest + 1][1]:
    second_lowest = second_lowest + 1
    names.append(grades[second_lowest][0])
names.sort()

for i in range(len(names)):
    print(names[i])