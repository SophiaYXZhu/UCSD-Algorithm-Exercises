n = int(input())
arr = [int(i) for i in input().split()]

class CountInversions:
    def __init__(self) -> None:
        self.count = 0

    def merge(self, arr, left, right):
        local_count = 0
        i, j, k = 0, 0, 0
        mid = (len(left)+len(right))//2
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                local_count += mid-i
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return local_count

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            self.merge_sort(left)
            self.merge_sort(right)
            self.count += self.merge(arr, left, right)

my_inversion = CountInversions()
my_inversion.merge_sort(arr)
print(my_inversion.count)