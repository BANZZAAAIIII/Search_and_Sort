import math
import random

merge_count = 0
node_count = 0


def reset_globals():
	global merge_count
	global node_count
	merge_count = 0
	node_count = 0


def calculateDistance(lat1, lng1):
	""""
	uses haversine formula from: https://www.movable-type.co.uk/scripts/latlong.html
	a = sin²(delta_phi/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
	c = 2 ⋅ atan2( √a, √(1−a) )
	d = R ⋅ c
	"""
	def inner(lat2, lng2):
		R = 6371  # earths radius in m
		phi1 = math.radians(lat1)
		lambda1 = math.radians(lng1)
		phi2 = math.radians(lat2)
		lambda2 = math.radians(lng2)

		delta_phi = phi2 - phi1
		delta_lambda = lambda2 - lambda1

		a = (math.sin(delta_phi / 2) * math.sin(delta_phi / 2) +
			 math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) * math.sin(delta_lambda / 2))
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
		return R * c

	return inner


def add_dist_to_dataset(data, dist_from):
	for d in data:
		d["dist"] = dist_from(d["lat"], d["lng"])


def mergesort(data: list[dict], compare: str) -> list[dict]:
	global merge_count
	global node_count
	node_count += 1
	if len(data) > 1:
		# Gets middle index as int
		m = len(data) // 2

		left = mergesort(data[:m], compare)
		right = mergesort(data[m:], compare)

		Left_index = 0  # current index of left side
		right_index = 0  # current index of right side
		current_index = 0  # current index of list index

		l_len = len(left) if left is not None else 0
		r_len = len(right) if right is not None else 0

		while Left_index < l_len and right_index < r_len:
			merge_count += 1
			if left[Left_index][compare] < right[right_index][compare]:
				data[current_index] = left[Left_index]
				Left_index += 1
			else:
				data[current_index] = right[right_index]
				right_index += 1

			current_index += 1

		# Adds any remaining elements from left or right side to the and of the list
		while Left_index < l_len:
			merge_count += 1
			data[current_index] = left[Left_index]
			Left_index += 1
			current_index += 1

		while right_index < r_len:
			merge_count += 1
			data[current_index] = right[right_index]
			right_index += 1
			current_index += 1

		return data

	else:
		return data


def mergesort_from_pos(dataset, lat, lng):
	"""	Sorts wordlcities datasets with distance from given coordinate with mergesort """
	dist_from_x = calculateDistance(lat, lng)
	add_dist_to_dataset(dataset, dist_from_x)
	return mergesort(dataset, "dist")


def quicksort(dataset: list[dict], compare: str) -> list[dict]:
	""" Sorts worldcites dataset by latitudes with quicksort """

	def sort(data: list[dict], left_index: int, right_index: int):
		global node_count
		node_count += 1
		if left_index <= right_index:
			p = partition(data, left_index, right_index)

			sort(data, left_index, p - 1)
			sort(data, p + 1, right_index)
		else:
			return

		return data

	def partition(data: list[dict], left_index: int, right_index: int) -> int:
		global merge_count
		# pivot_index = random.randrange(left_index, right_index + 1)
		# data[pivot_index], data[right_index] = data[right_index], data[pivot_index]
		pivot_index = right_index
		pivot = data[pivot_index][compare]
		i = left_index - 1
		for j in range(left_index, pivot_index):
			if data[j][compare] < pivot:
				i += 1
				data[i], data[j] = data[j], data[i]
				merge_count += 1

		data[i + 1], data[pivot_index] = data[pivot_index], data[i + 1]
		return i + 1

	return sort(dataset, 0, len(dataset) - 1)


def quicksort_from_pos(dataset, lat, lng):
	""" Sorts wordlcities datasets with distance from given coordinate quicksort """
	dist_from_x = calculateDistance(lat, lng)
	add_dist_to_dataset(dataset, dist_from_x)
	return quicksort(dataset, "dist")
