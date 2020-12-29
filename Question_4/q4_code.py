
# Question 4

def populate_matrix(file_name):
	'''populate a matrix from the given file'''
	res = []
	f = open(file_name, "r")
	for line in f:
		l = []
		for number in line:
			if number.isdigit():
				l.append(int(number))
		res.append(l)
	f.close()

	return res

def initialize_matrix(matrix):
	'''replace all 1 by -1, we need this step to mark all the unexplored aera.'''
	for row in matrix:
		for i in range(len(row)):
			if row[i] == 1:
				row[i] = -1

	return matrix

#4-connectivity	
def find_cc(matrix):
	'''mark all the 4-connectivity component'''	
	cc = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == -1:
				cc += 1
				dfs(matrix, i, j, cc)

	print("There are total " + str(cc) + " connected components.")
	return matrix


def dfs(matrix, i, j, cc):
	'''run dfs starting from the (i, j) cell'''
	dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

	matrix[i][j] = cc
	for dir in dirs:
		x = i + dir[0]
		y = j + dir[1]
		if 0 <= x <= len(matrix)-1 and 0 <= y <= len(matrix[0])-1:
			if matrix[x][y] == -1:
				dfs(matrix, x, y, cc)

def save(matrix, file_name):
	'''save matrix to a file'''
	with open(file_name,'w') as f:
		for line in matrix:
			s = [str(num) for num in line]
			f.write(" ".join(s) + '\n')

def main(input_file_name, output_file_name):
	matrix = populate_matrix(input_file_name)
	matrix = initialize_matrix(matrix)
	res = find_cc(matrix)
	save(res, output_file_name)
	
main("input_question_4", "output_question_4")