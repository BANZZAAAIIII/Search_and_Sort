
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


def mergesort2():
	""" Sorts wordlcities datasets latitudes and longitude with mergesort """
	raise NotImplemented


def quicksort():
	""" Sorts worldcites dataset by latitudes with quicksort """
	raise NotImplemented


def quicksort2():
	""" Sorts wordlcities datasets latitudes and longitude with quicksort """
	raise NotImplemented
