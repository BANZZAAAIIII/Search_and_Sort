from copy import deepcopy
from random import shuffle

import filemanager as fm
import search
import sorts


def main():
	dataset = fm.get_data()

	print("1.1:")
	sorted_by_lat = sorts.mergesort(list(dataset), "lat")
	print(f"\tnumber of merges done: {sorts.mergesort_merge_count}")
	print(f"\tnumber of nodes visited: {sorts.mergesort_node_count}")
	sorts.reset_globals()

	# print("\n1.2:")
	# print("\tShuffling list")
	# shuffled_list = list(dataset)
	# shuffle(shuffled_list)
	#
	# sorted_by_lat_shuffled = sorts.mergesort(shuffled_list, "lat")
	# print(f"\tnumber of merges done: {sorts.mergesort_merge_count}")
	# print(f"\tnumber of nodes visited: {sorts.mergesort_node_count}")
	# sorts.reset_globals()
	#
	# print("\n1.3:")
	# print("Sorting by distant")
	# blarg = sorts.mergesort_from_pos(dataset, 1, 1)
	# print(f"\tnumber of merges done: {sorts.mergesort_merge_count}")
	# print(f"\tnumber of nodes visited: {sorts.mergesort_node_count}")

	print(search.binary_search(sorted_by_lat, 28.6600))



if __name__ == "__main__":
	main()
