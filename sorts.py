
def mergesort(data: list[dict]):
	""" Sorts worldcites dataset by latitudes with mergesort """
	if len(data) > 1:
		# Gets middle index as int
		m = len(data) // 2

		left = data[:m]
		right = data[m:]

		# pass by reference
		mergesort(left)
		mergesort(right)

		i = 0  # current index of left side
		j = 0  # current index of right side
		k = 0  # current index of list index

		l_len = len(left)
		r_len = len(right)

		while i < l_len and j < r_len:
			if left[i]["lat"] < right[j]["lat"]:
				data[k] = left[i]
				i += 1
			else:
				data[k] = right[j]
				j += 1

			k += 1

		# Adds any remaining elements from left or right side to the and of the list
		while i < l_len:
			data[k] = left[i]
			i += 1
			k += 1

		while j < r_len:
			data[k] = right[j]
			j += 1
			k += 1


def mergesort2():
	""" Sorts wordlcities datasets latitudes and longitude with mergesort """
	raise NotImplemented


def quicksort():
	""" Sorts worldcites dataset by latitudes with quicksort """
	raise NotImplemented


def quicksort2():
	""" Sorts wordlcities datasets latitudes and longitude with quicksort """
	raise NotImplemented
