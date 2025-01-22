computer_num= int(input())

direct_connection = int(input())

array = []
count=0
tmp=0

virus_computer= []

for _ in range(direct_connection):
    
    connection = list(map(int, input().split()))
    array.append(connection)  

for i in range(direct_connection):
    if array[i][0] == 1:
      tmp = array[i][1]
      if tmp in virus_computer:
         break
      else:
         virus_computer.append(tmp)
      



print(array)