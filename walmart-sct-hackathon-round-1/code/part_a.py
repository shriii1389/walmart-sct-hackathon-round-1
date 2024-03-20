import csv
import numpy as np
"""
    Procedure I used:
    1. Read csv file
    2. Take each column values and add it on to a a list of dictionaries dictionary for ease of life. 
    3. Now just implement travelling salesman algorithem. A direct question on this concep
"""
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    a = np.sin(delta_phi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
    res = R * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 2)

inputFiles=[r"C:\Users\shrih\OneDrive\Desktop\walmart-sct-hackathon-round-1\input_datasets\part_a\part_a_input_dataset_1.csv",
            r"C:\Users\shrih\OneDrive\Desktop\walmart-sct-hackathon-round-1\input_datasets\part_a\part_a_input_dataset_2.csv",
            r"C:\Users\shrih\OneDrive\Desktop\walmart-sct-hackathon-round-1\input_datasets\part_a\part_a_input_dataset_3.csv",
            r"C:\Users\shrih\OneDrive\Desktop\walmart-sct-hackathon-round-1\input_datasets\part_a\part_a_input_dataset_4.csv",
            r"C:\Users\shrih\OneDrive\Desktop\walmart-sct-hackathon-round-1\input_datasets\part_a\part_a_input_dataset_5.csv"]
orders = []

for dataset in inputFiles:
    with open(dataset, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            orders.append({
                'order_id': row['order_id'],
                'latitude': float(row['lat']),  # Update column names as per your CSV file
                'longitude': float(row['lng']),
                'depot_latitude': float(row['depot_lat']),
                'depot_longitude': float(row['depot_lng'])
            })

    for order in orders:
        order['distance'] = haversine_distance(order['depot_latitude'], order['depot_longitude'],
                                               order['latitude'], order['longitude'])

    orders.sort(key=lambda x: x['distance'])

    total_distance = 0
    current_latitude = orders[0]['depot_latitude']
    current_longitude = orders[0]['depot_longitude']
    path = ["depot"]

    for order in orders:
        distance = haversine_distance(current_latitude, current_longitude, order['latitude'], order['longitude'])
        total_distance += distance
        current_latitude = order['latitude']
        current_longitude = order['longitude']
        path.append(order['order_id'])

    last_order = orders[-1]
    distance_to_depot = haversine_distance(last_order['latitude'], last_order['longitude'],
                                           last_order['depot_latitude'], last_order['depot_longitude'])
    total_distance += distance_to_depot
    path.append("depot")

    print(f"{' -> '.join(path)}")
    print(f"{total_distance:.2f} km")
    writer.writerow({'Dataset': dataset, 'Best Route Distance': f"{total_distance:.2f} km"})
