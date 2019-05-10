def insert_sort(sort_list):
  for i in range(len(sort_list)):
    j = i
    for j in range(i, 0, -1):
      if sort_list[j] < sort_list[j-1]:
        sort_list[j], sort_list[j-1] = sort_list[j-1], sort_list[j]
    
  return sort_list

to_sort = [6, 7, 3, 5, 4]

print(insert_sort(to_sort))
