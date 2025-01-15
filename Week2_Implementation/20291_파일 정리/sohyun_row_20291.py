N= int(input())

files = [list(map(str, input().split('.'))) for _ in range(N)]

print(files)

print(files[0][1])

file_type= [['txt',0],['spc',0],['icpc',0],['world',0]]

print(file_type[0][0])


for i in range(N):
  files[i][1] == file_type[i][0]
  file_type[i][1]+=1


file_type[0].sort()

print(file_type)