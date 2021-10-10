import math
from typing import List


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


def OBST_search(dataset: List[dict], city_value, lat_value, printy=False):
	def optimalBinarySearchTree(data, n):
		# Based on: https://www.radford.edu/~nokie/classes/360/dp-opt-bst.html
		cost = [[0 for _ in range(n)] for _ in range(n)]
		root = [[0 for _ in range(n)] for _ in range(n)]
		node = [[0 for _ in range(n)] for _ in range(n)]

		# Diagonal cost
		for i in range(n):
			root[i][i] = data[i]["lat"]
			cost[i][i] = data[i]["freq"]

		for size in range(2, n + 1):
			for row in range(n - size + 2):
				col = row + size - 1

				if row >= n or col >= n:
					break

				cost[row][col] = math.inf

				# Checks cost of all nodes, from row to col, as root
				for r in range(row, col + 1):
					# Cost of current node
					currentCost = sum(data[i]["freq"] for i in range(row, col + 1))

					# Adds cost of left subtree
					if r != row:
						currentCost += cost[row][r - 1]
					# Adds cost of right subtree
					if r != col:
						currentCost += cost[r + 1][col]

					# Checks if this node has a lower cost
					if currentCost < cost[row][col]:
						root[row][col] = data[r]["lat"] # Updates root
						node[row][col] = r				# updates index
						cost[row][col] = currentCost	# Updates cost

		return root, node, cost

	# dataset = [{"lat": 10, "freq": 4}, {"lat": 20, "freq": 2}, {"lat": 30, "freq": 6}, {"lat": 40, "freq": 3}]
	root, node, cost = optimalBinarySearchTree(dataset, len(dataset))

	print(f"\tOBST Cost: {cost[0][len(dataset) - 1]}")
	print(f"\tRoot node: {root[0][len(dataset) - 1]}")
	print(f"\tNode node: {dataset[node[0][len(dataset) - 1]]}")
	if printy:
		print("\tRoot:")
		for d in root:
			print(f"\t\t{d}")

		print("\tNode:")
		for d in node:
			print(f"\t\t{d}")

		print("\tCost:")
		for d in cost:
			print(f"\t\t{d}")

	def search():
		for i, row in enumerate(root):
			for j, col in enumerate(row):
				if col == lat_value:
					if dataset[i]["city"] == city_value:
						return dataset[i]
		return None
	print(f"\tSearch result: {search()}")

	return root, node, cost
