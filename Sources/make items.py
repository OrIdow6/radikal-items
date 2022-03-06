lower = 1174655062 # Earliest item - 1 second
upper = 1646530923

ids_generation_window = 1200
num_id_items_per_date_items = 200

each_date_item_seconds = ids_generation_window * num_id_items_per_date_items

for start in range(lower, upper - each_date_item_seconds, each_date_item_seconds):
	print(f"daterange:{start}-{start + each_date_item_seconds}")
