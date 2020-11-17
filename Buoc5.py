import math
import os

#Các thống số đã cho trong bài :
Bg = 4                      # Em nhận Bg với 10 đơn xoá dấu ","
N = 10
lg = 1*0.001                # phải đổi đơn vị (mm) sáng (m)
Ac = Ag = 600*10**(-6)
mu0 = 4 * math.pi * 10 ** (-7)
F = 250

while F <= 350:
    print("Lực hút điên từ : F =", F, "(N)")
    # Hc đo được từ bảng B-H
    Hc = [32, 35, 38, 42, 46, 50, 54, 58, 64, 70, 75, 82, 94, 112, 125, 140, 178, 185, 250, 300, 330, 700, 1100, 2000, 3000]
    j = 0
    Bg = 4
    while Bg <= 16:
        print("Từ cảm khe hở và lõi thép  : Bg = Bc =", Bg/10,"(T)")    # Em chia Bg với 10 để được số cũ trong bài
        Bc = Bg
        lc = ((F * mu0) - (Bg * lg))/(mu0 * Hc[j])
        I = 2 * ((Hc[j] * lc * mu0) + lg * Bc)/(N * Bc) * math.sqrt(F/(mu0 * Ac))
        print("Dòng điện cấp vào cuộn dây : I =", format(I,".3"), "(A)")
        print("\n")
        j += 1
        Bg += 0.5
    F += 10

os.system("pause")