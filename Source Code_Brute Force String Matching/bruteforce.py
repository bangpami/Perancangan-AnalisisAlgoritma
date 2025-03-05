def pencocokan_bruteforce(teks, pola):
    panjang_teks = len(teks)
    panjang_pola = len(pola)
    
    for i in range(panjang_teks - panjang_pola + 1): 
        j = 0
        while j < panjang_pola and pola[j] == teks[i + j]: 
            j += 1
        
        if j == panjang_pola:
            return i
    
    return -1  


teks = "RamdhanBulanBerkah"
pola = "Bulan"
hasil = pencocokan_bruteforce(teks, pola)
print("Pola ditemukan pada indeks:", hasil)
