
def generateMatrix(COUNT):
	for line in range(1, (ROW + COL)):
		start_col = max(0, line - ROW)
		count = min(line, (COL - start_col), ROW)

		for j in range(0, count):
			matrix[min(ROW, line) - j - 1][start_col + j] = COUNT
			COUNT += 1

def printMatrix():
	print("\n")
	for i in range(0, ROW):
		for j in range(0, COL):
			print(matrix[i][j], end="\t")
		print()



while True:
	ROW = int(input("\nEnter the number of Rows : "))
	COL = int(input("Enter the number of Columns : "))
	matrix = [[0 for i in range(COL)] for j in range(ROW)]
	COUNT = 1
	
	generateMatrix(COUNT)
	printMatrix()
	
	choice = input("\nDo you wish to continue ? (y/n) : ")
	if choice == 'n' or choice == 'N':
		break
	elif choice == 'y' or choice == 'Y':
		continue
	else:
		print("\nInvalid Choice : Terminating Program...")
		break