kuadrat = lambda x: x ** 2
print(kuadrat(4))

siswa = [("Tifa", 80), ("Dani", 95)]
print(max(siswa, key=lambda s: s[1]))


x = "global"
def tes():
    global x
    x = "lokal"   # hanya di dalam tes()
    print(x)      # lokal
tes()
print(x)          #Global

