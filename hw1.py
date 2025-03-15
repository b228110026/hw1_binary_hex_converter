print('請輸入 0 ~ 255 的 整數 : ')
m = int(input())
n = m
result = 0
count = 0
while n >= 0:
  a = n // 2
  b = n % 2
  result = result + (b * 10 ** count)
  count = count + 1
  if(a):
    n = int(n / 2)
    continue
  else:
    break
print('十進位轉二進位 : ')
print(result)
n = m
result = ''
count = 0
while n >= 0:
  a = n // 16
  b = n % 16
  if(b == 10):
    b = 'A'
  elif(b == 11):
    b = 'B'
  elif(b == 12):
    b = 'C'
  elif(b == 13):
    b = 'D'
  elif(b == 14):
    b = 'E'
  elif(b == 15):
    b = 'F'
  result = str(b) + result
  count = count + 1
  if(a):
    n = int(n / 16)
    continue
  else:
    break
print('十進位轉十六進位 : ')
print(result)