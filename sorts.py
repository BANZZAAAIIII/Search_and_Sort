import math

mergesort_merge_count = 0
mergesort_node_count = 0


def reset_globals():
	global mergesort_merge_count
	global mergesort_node_count
	mergesort_merge_count = 0
	mergesort_node_count = 0


def mergesort(data: list[dict], compare: str) -> list[dict]:
	global mergesort_merge_count
	global mergesort_node_count
	if len(data) > 1:
		# Gets middle index as int
		m = len(data) // 2

		left = mergesort(data[:m], compare)
		right = mergesort(data[m:], compare)

		i = 0  # current index of left side
		j = 0  # current index of right side
		k = 0  # current index of list index

		l_len = 0 if left is None else len(left)
		r_len = 0 if right is None else len(right)

		mergesort_node_count += 1
		while i < l_len and j < r_len:
			mergesort_merge_count += 1
			if left[i][compare] < right[j][compare]:
				data[k] = left[i]
				i += 1
			else:
				data[k] = right[j]
				j += 1

			k += 1

		# Adds any remaining elements from left or right side to the and of the list
		while i < l_len:
			mergesort_merge_count += 1
			data[k] = left[i]
			i += 1
			k += 1

		while j < r_len:
			mergesort_merge_count += 1
			data[k] = right[j]
			j += 1
			k += 1

		return data

	else:
		return data


def mergesort_from_pos(dataset, lat, lng):
	"""
	Sorts wordlcities datasets from a given coordinate with mergesort
	using haversine formula from: https://www.movable-type.co.uk/scripts/latlong.html
	a = sin²(delta_phi/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
	c = 2 ⋅ atan2( √a, √(1−a) )
	d = R ⋅ c
	"""
	def calculateDistance(lat1, lng1):
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

	dist_from_x = calculateDistance(lat, lng)
	add_dist_to_dataset(dataset, dist_from_x)
	return mergesort(dataset, "dist")

# mergesort2(dataset)


def quicksort():
	""" Sorts worldcites dataset by latitudes with quicksort """
	raise NotImplemented


def quicksort2():
	""" Sorts wordlcities datasets latitudes and longitude with quicksort """
	raise NotImplemented
