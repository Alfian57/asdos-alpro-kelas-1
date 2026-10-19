# Soal 3: Pembagian Permen
# Cerita: Ibu membawa 25 butir permen untuk dibagikan secara adil kepada 4 orang
# anaknya. Ibu ingin tahu berapa permen yang didapat setiap anak dan berapa butir sisa
# permen yang tidak terbagi.
# Spesifikasi:
# - Buat variabel total_permen bernilai 25 dan jumlah_anak bernilai 4.
# - Hitung permen per anak menggunakan pembagian bulat (//) ke dalam variabel
# permen_per_anak.
# - Hitung sisa permen menggunakan modulus (%) ke dalam variabel
# sisa_permen.
# - Tampilkan nilai permen_per_anak dan sisa_permen ke layar.


total_permen = 25
jumlah_anak = 4
permen_per_anak = total_permen // jumlah_anak
sisa_permen = total_permen % jumlah_anak
print(permen_per_anak)
print(sisa_permen)
