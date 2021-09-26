import csv


def get_data() -> list[dict]:
	dataset = []

	with open("data/worldcities.csv", encoding='utf-8') as csv_file:
		reader = csv.DictReader(csv_file)
		for row in reader:
			dataset.append({"city": row["city"], "lat": row["lat"], "lng": row["lng"]})

	return dataset
