import math

mergesort_merge_count = 0
mergesort_node_count = 0


def reset_globals():
	global mergesort_merge_count
	global mergesort_node_count
	mergesort_merge_count = 0
	mergesort_node_count = 0


def mergesort(data: list[dict]) -> list[dict]:
	""" Sorts worldcites dataset by latitudes with mergesort """
	global mergesort_merge_count
	global mergesort_node_count
	if len(data) > 1:
		# Gets middle index as int
		m = len(data) // 2

		left = mergesort(data[:m])
		right = mergesort(data[m:])

		i = 0  # current index of left side
		j = 0  # current index of right side
		k = 0  # current index of list index

		l_len = 0 if left is None else len(left)
		r_len = 0 if right is None else len(right)

		mergesort_node_count += 1
		while i < l_len and j < r_len:
			mergesort_merge_count += 1
			if left[i]["lat"] < right[j]["lat"]:
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
	d = R ⋅ c """

	def calculateDistance(lat1, lng1):
		def inner(lat2, lng2):
			def toRad(x): return x * (math.pi / 180)
			R = 6371e3  # earths radius in m
			phi1 = toRad(lat1)
			lambda1 = toRad(lng1)
			phi2 = toRad(lat2)
			lambda2 = toRad(lng2)

			delta_phi = phi2 - phi1
			delta_lambda = lambda2 - lambda1

			a = (math.sin(delta_phi / 2) * math.sin(delta_phi / 2) +
				 math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) * math.sin(delta_lambda / 2))
			c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
			return R * c

		return inner

	def mergesort2(data):
		global mergesort_merge_count
		global mergesort_node_count
		if len(data) > 1:
			# Gets middle index as int
			m = len(data) // 2

			left = mergesort2(data[:m])
			right = mergesort2(data[m:])

			i = 0  # current index of left side
			j = 0  # current index of right side
			k = 0  # current index of list index

			l_len = 0 if left is None else len(left)
			r_len = 0 if right is None else len(right)

			mergesort_node_count += 1
			while i < l_len and j < r_len:
				mergesort_merge_count += 1

				if dist_from_x(left[i]["lat"], left[i]["lng"]) < dist_from_x(right[j]["lat"], right[j]["lng"]):
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

	dist_from_x = calculateDistance(35.6897, 139.6922)
	print(dist_from_x(-6.2146, 106.8451))


# mergesort2(dataset)


def quicksort():
	""" Sorts worldcites dataset by latitudes with quicksort """
	raise NotImplemented


def quicksort2():
	""" Sorts wordlcities datasets latitudes and longitude with quicksort """
	raise NotImplemented
