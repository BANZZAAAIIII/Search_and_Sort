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


def OBST(dataset, city_value, lat_value, prints=False):
	def optimalBinarySearchTree(keys, freq, n):
		# Based on: https://www.radford.edu/~nokie/classes/360/dp-opt-bst.html
		cost = [[0 for _ in range(n)] for _ in range(n)]
		root = [[0 for _ in range(n)] for _ in range(n)]

		# Diagonal cost
		for i in range(n):
			root[i][i] = keys[i]
			cost[i][i] = freq[i]

		for size in range(2, n + 1):
			for row in range(n - size + 2):
				col = row + size - 1
				if row >= n or col >= n:
					break

				cost[row][col] = math.inf

				# Checks cost of all nodes, from row to col, as root
				for r in range(row, col + 1):
					currentCost = 0

					# Adds cost of left subtree
					if r > row:
						currentCost += cost[row][r - 1]
					# Adds cost of right subtree
					if r < col:
						currentCost += cost[r + 1][col]

					currentCost += sum(freq[i] for i in range(row, col + 1))

					# Checks if this node has a lower cost
					if currentCost < cost[row][col]:
						root[row][col] = keys[r]
						cost[row][col] = currentCost


		return cost, root

	# keys, frequency = zip(*dataset)
	# keys = [10, 12, 20]
	# frequency = [34, 8, 50]
	# frequency = [25, 10, 20]

	keys = [10, 20, 30, 40]
	frequency = [4, 2, 6, 3]

	cost, root = optimalBinarySearchTree(keys, frequency, len(keys))
	print(f"OBST Cost: {cost[0][len(keys) - 1]}")

	if prints:
		print("nodes:")
		for d in root:
			print(f"\t{d}")

		print("Cost:")
		for d in cost:
			print(f"\t{d}")
