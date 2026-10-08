import csv

data = []
with open("nilai.csv", mode="r") as f:
    for row in csv.DictReader(f):
        row["nilai"] = int(row["nilai"])  
        data.append(row)

rekap = {}
for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'kelas':<6}{'jumlah':>8}{'Rata-rata':>8}")
for k, v in sorted(rekap.items()):
    rata = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata:>8.1f}")