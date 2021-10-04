from operator import itemgetter
from itertools import groupby
from random import shuffle

import filemanager
import filemanager as fm
import search
import sorts


def main():
	# dataset = fm.get_data()

	# print("1.1:")
	# sorted_by_lat = sorts.mergesort(list(dataset), "lat")
	# print(f"\tnumber of merges done: {sorts.merge_count}")
	# print(f"\tnumber of nodes visited: {sorts.node_count}")
	# sorts.reset_globals()
	#
	# print("\n1.2:")
	# print("\tShuffling list")
	# shuffled_list = list(dataset)
	# shuffle(shuffled_list)
	#
	# sorted_by_lat_shuffled = sorts.mergesort(shuffled_list, "lat")
	# print(f"\tnumber of merges done: {sorts.merge_count}")
	# print(f"\tnumber of nodes visited: {sorts.node_count}")
	# sorts.reset_globals()
	#
	# print("\n1.3:")
	# print("Sorting by distant")
	# sorted_from_pos = sorts.mergesort_from_pos(list(dataset), 1, 1)
	# print(f"\tnumber of merges done: {sorts.merge_count}")
	# print(f"\tnumber of nodes visited: {sorts.node_count}")
	#
	#
	# print("\n2.1:")
	# sorted_by_lat = sorts.quicksort(list(dataset), "lat")
	# print(f"\tnumber of merges done: {sorts.merge_count}")
	# print(f"\tnumber of nodes visited: {sorts.node_count}")
	# sorts.reset_globals()
	#
	#
	# print("\n2.2:")
	# print("\tShuffling list")
	# shuffled_list = list(dataset)
	# shuffle(shuffled_list)
	#
	# sorted_by_lat_shuffled = sorts.quicksort(shuffled_list, "lat")
	# print(f"\tnumber of merges done: {sorts.merge_count}")
	# print(f"\tnumber of nodes visited: {sorts.node_count}")
	# sorts.reset_globals()
	#
	#
	# print("\n2.3:")
	# print("Sorting by distant")
	# sorted_from_pos = sorts.quicksort_from_pos(list(dataset), 1, 1)
	# print(f"\tnumber of merges done: {sorts.merge_count}")
	# print(f"\tnumber of nodes visited: {sorts.node_count}")
	#
	#
	# print("\n3.1 search")
	# print("\t" + str(search.binary_search(sorted_by_lat, "Catas Altas", -20.0750)))
	# print("\t" + str(search.binary_search(sorted_by_lat, "Itaúna", -20.0750)))

	dataset = filemanager.get_data()

	counter = sorts.quicksort(dataset, "lat")
	# for d in sorted(dataset, key=itemgetter("lat")):
	# 	print(d)

	# results = groupby(counter, key=itemgetter("lat"))
	# for key, valuesiter in results:
	# 	print(key, [v["city"] for v in valuesiter])


	search.OBST(dataset, 1, "a")

if __name__ == "__main__":
	main()
