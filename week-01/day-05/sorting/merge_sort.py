def merge_sort(sort_list):
  if len(sort_list) == 1:
    return sort_list
  mid = len(sort_list)//2
  left_list = sort_list[0:mid]
  right_list = sort_list[mid:len(sort_list)]
  
  left_list = merge_sort(left_list)
  right_list = merge_sort(right_list)

  return merge(left_list, right_list)

def merge(left_list, right_list):
  result = []
  while (len(left_list) > 0) and (len(right_list) > 0):
    if left_list[0] <= right_list[0]:
      result.append(left_list.pop(0))
    else:
      result.append(right_list.pop(0))
  
  if left_list:
    result.extend(left_list)
  if right_list:
    result.extend(right_list)
  
  return result


to_sort = [6, 7, 3, 5, 4]
print(merge_sort(to_sort))