def quicksort(sort_list):
  lo = 0
  hi = len(sort_list) - 1
  __quicksort(sort_list, lo, hi)
  return sort_list

def __quicksort(sort_list, lo, hi):
    if lo < hi:
      p = partition(sort_list, lo, hi)
      __quicksort(sort_list, lo, p - 1)
      __quicksort(sort_list, p+ 1, hi)

def partition(sort_list, lo, hi):
  pivot = sort_list[hi]
  i = lo
  for j in range(lo, hi):
    if sort_list[j] < pivot:
      sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
      i += 1
  sort_list[i], sort_list[hi] = sort_list[hi], sort_list[i]
  return i


to_sort = [6, 7, 3, 5, 4]
print(quicksort(to_sort))