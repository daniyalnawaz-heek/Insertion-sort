def sort(list1):
  
  
  for i in range(1,len(list1)):
    key=list1[i]
    j=i-1
    if list1[i]<list1[j]:
      list1[j+1]=list1[j]
      j=j-1
    list1[j+1]=key  
    
    
    
list2=[35,64,85,98,35,26,86,56]  
sort(list2)
print(list2)  
    