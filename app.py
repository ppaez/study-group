from data import download
from data import extract
from process import load
from pathlib import Path


url = (
    "https://fenixservices.fao.org/faostat/static/bulkdownloads/"
    "Production_Crops_Livestock_E_All_Data.zip"
)
zip_file = "production_data.zip"
csv_folder = Path("csv")
csv_file = csv_folder / "Production_Crops_Livestock_E_All_Data.csv"

print("Explore 'Crops and livestock products' data from the FAO of the UN.")
download(url, zip_file)
extract(zip_file, csv_folder)
rows = load(csv_file)

items = []
areas = []
for row in rows:
    item = row["Item"]
    area = row["Area"]
    if item not in items:
        items.append(item)
    if area not in areas:
        areas.append(area)

print(f"{len(rows):,} rows")
print(len(items), "items")
print(len(areas), "areas")
