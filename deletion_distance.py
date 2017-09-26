def deletion_distance(str1, str2):
  a = []
  if not len(str1) or not len(str2):
    return len(str1) or len(str2)

  for i in range(len(str1)+1):
    a.append([0 for _ in range(len(str2)+1)])
  for i in range(len(str1)+1):
    for j in range(len(str2)+1):
      if i == 0:
        a[i][j] = j
      if j == 0:
        a[i][j] = i
      elif str1[i-1] == str2[j-1]:
        a[i][j] = a[i-1][j-1]
      else:
        a[i][j] = 1 + min(a[i-1][j], a[i][j-1])
  print(a)
        
  return a[-1][-1]
  
str1 = ""
str2 = "hit"

print(deletion_distance(str1, str2))