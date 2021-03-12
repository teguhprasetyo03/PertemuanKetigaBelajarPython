# Boolean
# Boolean adalah tipe data yang bernilai true
# or false

# Operator Perbandingan
# == ( Sama dengan sama dengan )
# != ( Tidak Sama dengan )
# > ( Lebih besar )
# < ( Lebih Kecil )
# >= ( Lebih besar sama dengan )
# <= ( LEbih kecil sama dengan )

# Operator Logika

# And = Operator and hanya akan menghasilkan True
# jika kedua operand bernilai True, selain itu
# hasilnya False.

# OR = Operator or hanya akan menghasilkan True
# jika salah satu operand bernilai True.
# Operator or hanya bernilai False jika
# kedua operand juga bernilai False.

# not -> membalikkan logika

# and
hasil = (20>10) and (10!=10)
print(hasil)

# or
a = ("nilai" == "NILAI") or (15<=3)
print(a)
print("==============")

# not
b = not(10>20)
print(b)
print("==============")

result = (25 < 20 ) and (10 == 10) or ( 1!=1)
print(result)
print("==============")

# operator assignment
# adalah operator untuk memasukkan suatu nilai ke dalam variabel.
# Operator ini sebenarnya sudah sering kita pakai sepanjang tutorial
# Python, operator assignment menggunakan tanda sama dengan (=).

angka1 = 10
angka1 += 25
print('Hasil dri angka1 adalah :',angka1)

angka2 = 20
angka2 -=25
print('Hasil dari angka2 adalah :', angka2)

angka3 = 22.7
angka3 *= 20
print('HAsil dari angka3 adalah : ', angka3)

angka4 = 765
angka4 /= 22
print('Hasil dari angka4 adalah : ', angka4)

angka5 = 25
angka5 %= 5
print('Hasil dari angka5 adalah :  ', angka5)

angka6 = 40
angka6 <<= 20
print('Hasil dari angka6 adalah : ', angka6)

angka7 = 144
angka7 ^=12

print(angka7)
# nilai = 12 < 10
# angka = 10 == 10
# print(2>=3)
# print(3!=2)
# firstname = "JONATHAN"
# lastname = "jonathan"
#
#
# print(nilai)
# print(angka)
# print(firstname == lastname)