import math


def binary_search(dataset, city_value, lat_value):
	def search(data, left_index, right_index):
		if right_index > 1:
			middle = (left_index + right_index) // 2
			if math.isclose(data[middle]["lat"], lat_value) and data[middle]["city"] == city_value:
				return data[middle]

			if data[middle]["lat"] > lat_value:
				return search(data, left_index, middle - 1)
			else:
				return search(data, middle + 1, right_index)
		else:
			return None

	return search(dataset, 0, len(dataset) - 1)
