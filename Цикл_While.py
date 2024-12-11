my_list = [42, 69, 322, 12, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
new_my_list = []
while i < len(my_list):
  if my_list[i] > 0:
    new_my_list.append(my_list[i])
  elif my_list[i] < 0:
    break
  i += 1
print(new_my_list)