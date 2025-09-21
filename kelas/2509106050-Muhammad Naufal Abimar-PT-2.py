#variabel
suhu_1 = 27 
suhu_2 = 33
suhu_3 = 46
suhu_4 = 55
suhu_5 = 67
suhu_6 = 92 

# konversi 
def  c_to_f(c):
    return (9/5) * c + 32 
def c_to_k(c):
    return c + 273.15
def c_to_r(c):
    return (4/5) * c 

# konversi sesuai ketentuan 
f1 = c_to_f(suhu_1)
f2 = c_to_f(suhu_2)

k3 = c_to_k(suhu_3)
k4 = c_to_k(suhu_4)

r5 = c_to_r(suhu_5)
r6 = c_to_r(suhu_6)

#jumlah rata rata suhu 
jumlah = f1 + f2 + k3 + k4 + r5 +r6
rata_rata = jumlah / 6 

nim = 50
bolean = nim<rata_rata

#hasil
print("hasil konversi suhu:")
print(f"Suhu 1 ({suhu_1}°C) = {f1:.2f} F")
print(f"Suhu 2 ({suhu_2}°C) = {f2:.2f} F")
print(f"Suhu 3 ({suhu_3}°C) = {k3:.2f} K")
print(f"Suhu 4 ({suhu_4}°C) = {k4:.2f} K")
print(f"Suhu 5 ({suhu_5}°C) = {r5:.2f} R")
print(f"Suhu 6 ({suhu_6}°C) = {r6:.2f} R")

print(f"Jumlah semua suhu  = {jumlah}")
print(f"Rata-rata suhu = {rata_rata}")
print(f"perbandingan variabel = {nim<rata_rata}")