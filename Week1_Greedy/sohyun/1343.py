pol = input()

pol= pol.replace('XXXX','AAAA')
pol= pol.replace('XX','BB')

if 'X' in pol:
  print(-1)
else:
  print(pol)
