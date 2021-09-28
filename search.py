import math


def binary_search(dataset, value):
	def search(data, left_index, right_index, val):
		if right_index >= 1:
			middle = (left_index + right_index) // 2
			if math.isclose(data[middle]["lat"], val):
				return data[middle]

			if data[middle]["lat"] > val:
				return search(data, left_index, middle - 1, val)
			else:
				return search(data, middle + 1, right_index, val)
		else:
			return None

	return search(dataset, 0, len(dataset) - 1, value)
