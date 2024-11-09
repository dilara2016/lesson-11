# take input from user
rows = int(input("please enter total numbers of rows : "))
number = 1 #initilise by 1
print("Floyds Triangel")
#outer loops for numbers of rows
for i in range( 1, rows + 1):
# inner loops for numbers of colums
 for j in range( 1, i + 1):
#display results
  print(number, end = '   ')
  number = number + 1
 print()