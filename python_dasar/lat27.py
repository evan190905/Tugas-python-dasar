import csv

data = []
with open("nilai.csv", mode="r") as f:
    for row in csv.DictReader(f):
        row["nilai"] = int(row["nilai"])  
        data.append(row)

nilai = [d["nilai"] for d in data]
rata = sum(nilai) / len(nilai)
print(f"Rata-rata: {rata:.1f}")

lulus = [d["nama"] for d in data if d["nilai"] >= 75]
print("Lulus:", lulus)

top = max(data, key=lambda d: d["nilai"])
print("Tertinggi:", top["nama"])
