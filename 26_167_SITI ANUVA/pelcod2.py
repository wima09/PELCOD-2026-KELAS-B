daftar_buku = ["audit","tata kelola","si kancil"]

print("===KOLEKSI BUKU===")
print("0",daftar_buku[0])
print("1",daftar_buku[1])
print("2",daftar_buku[2])

nama = input("Masukan nama :")
umur = int(input("Masukan umur"))
status_aktif = input("apakah kamu mahasiswa aktif? (y/n)")

pilihan1 = int(input("pilihan buku ke1:"))

syarat_umur = status_aktif and umur >=17

hari_sekarang = 0
lama_pinjam = 1
batas_pengembalian = hari_sekarang + lama_pinjam

print ("\n==hasil pinjaman==")
if not syarat_umur: 
    print("maaf {nama}, peminjaman di tolak.")
    if not status_aktif:
        print("anda bukan mahasiswa aktif")
else:
    buku_dipinjam = [daftar_buku[pilihan1]]
    print(f"selamat {nama}, peminjaman berhasil")
    print("buku yang di pinjam:", buku_dipinjam)
    print ("batas pengembalian:",{batas_pengembalian})