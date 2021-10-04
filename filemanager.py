import csv


def get_data(norway=False) -> list[dict]:
	dataset = []

	with open("data/worldcities.csv", encoding='utf-8') as csv_file:
		reader = csv.DictReader(csv_file)
		for row in reader:
			if norway and row["country"] == "Norway":
				dataset.append({"city": row["city"], "lat": float(row["lat"]), "lng": float(row["lng"])})
			elif not norway:
				dataset.append({"city": row["city"], "lat": float(row["lat"]), "lng": float(row["lng"])})

	return dataset
