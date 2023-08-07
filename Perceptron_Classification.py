def perceptron_classifier(data_train, data_test):
	
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 8

	weight = [[0,0] for x in range(10)]

	def helper():
		count = 0

		for i in range(len(data_train)):
			data = data_train[i]
			dot_array = [0 for x in range(10)]
			for n in range(10):
				dot_array[n] = dot_product(data, weight[n])
			max_dot = max(dot_array)
			max_index = dot_array.index(max_dot)
			if not max_index == data[2]:
				count += 1
				weight[max_index][0] = weight[max_index][0] - data[0]
				weight[max_index][1] = weight[max_index][1] - data[1]

				weight[int(data[2])][0] = weight[int(data[2])][0] + data[0]
				weight[int(data[2])][1] = weight[int(data[2])][1] + data[1]

		return count

	flag = 51
	while flag > 20:
		flag = helper()
	
	for i in range(len(data_test)):
		data = data_test[i]
		dot_array = [0 for x in range(10)]
		for n in range(10):
			dot_array[n] = dot_product(data, weight[n])
		max_index = dot_array.index(max(dot_array))

		data_test[i][2] = max_index

	return


# function to calculate dot product 
def dot_product(a, b):
	sum = 0
	for i in range(len(b)):
		if i < 2: sum += a[i] * b[i]
		if i == 2: sum += 1 * b[i]
	return sum

