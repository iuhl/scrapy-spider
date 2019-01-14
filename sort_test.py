import random


class sort:

    pass


# 插入排序
class all_sort:
    def insertion_sort(self, arr, length):
        for num in range(1, length):
            tmp = arr[num]
            num2 = 0
            for num1 in range(1, num)[::-1]:
                if arr[num1 - 1] > tmp:
                    arr[num1] = arr[num1 - 1]
                    num2=num1
                else:
                    break
            arr[num2] = tmp
        print(arr)
    pass


arr = []
for num in range(0, 1000):
    arr.append(random.randint(0, 1000))

print(arr)

x=all_sort()
print(x.insertion_sort(arr, 1000))
