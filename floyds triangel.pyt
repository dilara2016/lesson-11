rows = int(input("please enter total numbers of rows : "))
number = 1 #initilise by 1
print("Floyds Triangel")
for i in range( 1, rows + 1):
 for j in range( 1, i + 1):
  print(number, end = '   ')
  number = number + 1
 print()
