
def heap_sort(sort_list):
  __heap_sort(sort_list, len(sort_list))
  return sort_list

def __heap_sort(sort_list, count):
  __build_heap(sort_list, count)
  end = count - 1
  while end > 0:
    sort_list[end], sort_list[0] = sort_list[0], sort_list[end]
    end -= 1
    __shift_down(sort_list, 0, end)

def __build_heap(sort_list, count):
  start = (count -1) // 2
  while start > 0:
    __shift_down(sort_list, start, count - 1)
    start -= 1

def __shift_down(sort_list, start, end):
  root = start
  while 2*root + 1 <= end:
    child = 2*root + 1
    swap = root
    if sort_list[swap] < sort_list[child]:
      swap = child
    if child + 1 < end and sort_list[swap] < sort_list[child+1]:
      swap = child + 1
    if swap == root:
      return
    else:
      sort_list[root], sort_list[swap] = sort_list[swap], sort_list[root]
      root = swap


to_sort = [6, 7, 3, 5, 4]

print(heap_sort(to_sort))