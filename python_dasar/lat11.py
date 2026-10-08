umur, ktp = 20, True
if umur >= 17:
    if ktp:
        print("Boleh memilih")
    else:
        print("Buat KTP dulu")

umur = 16
s = "dewasa" if umur >= 17 else "anak"
print(s)  # anak


hari = "sabtu"
match hari:
    case "sabtu" | "minggu":
        print("Libur!")
    case "senin":
        print("Semangat!")
    case _:
        print("Hari kerja")