import math


def binary_search(dataset, city_value, lat_value):
	def search(data, left_index, right_index):
		if right_index > 1:
			middle = (left_index + right_index) // 2
			# Is using isclose a good idea? 41.728_ has a lot of cities
			if math.isclose(data[middle]["lat"], lat_value) and data[middle]["city"] == city_value:
				return data[middle]

			if data[middle]["lat"] > lat_value:
				return search(data, left_index, middle - 1)
			else:
				return search(data, middle + 1, right_index)
		else:
			return None

	return search(dataset, 0, len(dataset) - 1)


def OBST(dataset, city_value, lat_value):
	INT_MAX = 2147483647

	def optimalSearchTree(keys, freq, n):

		""" Create an auxiliary 2D matrix to store
			results of subproblems """
		cost = [[0 for x in range(n)] for y in range(n)]

		""" cost[i][j] = Optimal cost of binary search
		tree that can be formed from keys[i] to keys[j].
		cost[0][n-1] will store the resultant cost """

		# For a single key, cost is equal to
		# frequency of the key
		for i in range(n):
			cost[i][i] = freq[i]

		# Now we need to consider chains of
		# length 2, 3, ... . L is chain length.
		for L in range(2, n + 1):

			# i is row number in cost
			for i in range(n - L + 2):

				# Get column number j from row number
				# i and chain length L
				j = i + L - 1
				if i >= n or j >= n:
					break
				cost[i][j] = INT_MAX

				# Try making all keys in interval
				# keys[i..j] as root
				for r in range(i, j + 1):

					# c = cost when keys[r] becomes root
					# of this subtree
					c = 0
					if (r > i):
						c += cost[i][r - 1]
					if (r < j):
						c += cost[r + 1][j]
					c += sum(freq, i, j)
					if (c < cost[i][j]):
						cost[i][j] = c
		return cost[0][n - 1]

	# A utility function to get sum of
	# array elements freq[i] to freq[j]
	def sum(freq, i, j):

		s = 0
		for k in range(i, j + 1):
			s += freq[k]
		return s

	# Driver Code

	keys = [10, 12, 20]
	freq = [34, 8, 50]
	n = len(keys)
	print("Cost of Optimal BST is ", optimalSearchTree(keys, freq, n))