import csv


def save_data_to_csv(data, filename):
   
   # dictionary listák mentése CSV-be

    if not data:
        print("No data to save.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"Data saved to {filename}.")
