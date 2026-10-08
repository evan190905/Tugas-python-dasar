siswa = {"nama": "Tifa", "umur": 19}
siswa["kota"] = "Bekasi"
siswa["umur"] = 20
print(siswa["nama"])
print(siswa.get("hobi", "-"))

for k, v in siswa.items():
    print(f"{k}: {v}")