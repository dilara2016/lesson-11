#take input
print("half pyramid pattern of stars (*):")
n = int(input("enter the numbers of rows: "))
#outer loop to handil numbers of rows
for i in range (n):
    #inner loops to handil numbers of colums
 for j in range(i+1):
    #display result
    print("* ", end =   "")
 print()