from copy import deepcopy
from random import shuffle

import filemanager as fm
import sorts

def print_dataset_simple(dataset):
	for d in dataset:
		print(d["lat"])

def main():
	dataset = fm.get_data()
	#
	# sorted_by_lat = sorts.mergesort(list(dataset))
	# print(f"number of merges done: {sorts.mergesort_merge_count}")
	# print(f"number of nodes visited: {sorts.mergesort_node_count}")
	# sorts.reset_globals()
	#
	# print("\nShuffling list")
	# shuffled_list = list(dataset)
	# shuffle(shuffled_list)
	#
	# sorted_by_lat_shuffled = sorts.mergesort(shuffled_list)
	# print(f"number of merges done: {sorts.mergesort_merge_count}")
	# print(f"number of nodes visited: {sorts.mergesort_node_count}")
	#

	blarg = sorts.mergesort_from_pos(dataset, 1, 1)

	for b in blarg:
		print(b)



if __name__ == "__main__":
	main()