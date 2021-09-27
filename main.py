import filemanager as fm
import sorts


def main():
	dataset = fm.get_data()

	sorts.mergesort(dataset)
	for d in dataset:
		print(d)


if __name__ == "__main__":
	main()
