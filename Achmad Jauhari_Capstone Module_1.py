# CAPSTONE PROJECT MODULE 1
# Aplikasi Data Gudang Elektronik & Furnitur
# Terdiri dari Data Elektronik & Furnitur


from tabulate import tabulate

gudang = {
    "elektronik": [
        {"ID": "E001", "Nama": "TV Samsung", "Kategori": "Elektronik", "Stok": 50, "Harga": 7000000},
        {"ID": "E002", "Nama": "AC Sharp", "Kategori": "Elektronik", "Stok": 15, "Harga": 4000000},
        {"ID": "E003", "Nama": "Mesin Cuci", "Kategori": "Elektronik", "Stok": 40, "Harga": 3000000}
    ],
    "furnitur": [
        {"ID": "F001", "Nama": "Meja Kantor", "Kategori": "Furnitur", "Stok": 30, "Harga": 1200000},
        {"ID": "F002", "Nama": "Sofa", "Kategori": "Furnitur", "Stok": 20, "Harga": 3000000},
        {"ID": "F003", "Nama": "Lemari Pakaian", "Kategori": "Furnitur", "Stok": 40, "Harga": 3500000}
    ]
}
def format_and_print_items(items):
    table_data = []
    for item in items:
        table_data.append([
            item['ID'],
            item['Nama'].title(),
            item['Stok'],
            f"Rp {item['Harga']: ,}",
            item['Kategori'].capitalize()
        ])
    
    headers = ["ID", "Nama", "Stok", "Harga", "Kategori"]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

# 1. Menu Menambah Barang
def tambah_barang():
    kategori = input("\nMasukkan kategori barang (elektronik/furnitur): ").lower()
    if kategori not in gudang:
        print("Kategori tidak ditemukan.")
        return
    id_barang = input("Masukkan ID barang: ").upper()
    for item in gudang[kategori]:
        if item['ID'].upper() == id_barang:
            print(f"ID {id_barang} sudah ada dalam kategori {kategori}. Barang tidak dapat ditambahkan.")
            return
    
    nama = input("Masukkan nama barang: ")
    stok = int(input("Masukkan stok barang: "))
    harga = int(input("Masukkan harga barang: "))

    barang_baru = {'ID': id_barang, 'Nama': nama, 'Kategori': kategori.capitalize(), 'Stok': stok, 'Harga': harga}
    gudang[kategori].append(barang_baru)
    print(f"Barang {nama.title()} berhasil ditambahkan ke kategori {kategori}.")
    tampilkan_data_gudang(kategori)

# 2. Menu Menampilkan Data Gudang
def tampilkan_data_gudang(kategori_filter=None):
    if kategori_filter:
        if kategori_filter in gudang:
            barang_list = gudang[kategori_filter]
            print(f"\nMenampilkan data untuk kategori: {kategori_filter.capitalize()}")
            format_and_print_items(barang_list)
        else:
            print(f"Kategori '{kategori_filter}' tidak ditemukan.")
    else:
        for kategori, barang_list in gudang.items():
            print(f"\nMenampilkan data untuk kategori: {kategori.capitalize()}")
            format_and_print_items(barang_list)

def menu_pilihan():
    print("Pilih kategori yang ingin ditampilkan:")
    print("1. Kategori Elektronik")
    print("2. Kategori Furnitur")
    print("3. Semua Kategori")
    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == "1":
        tampilkan_data_gudang("elektronik")
    elif pilihan == "2":
        tampilkan_data_gudang("furnitur")
    elif pilihan == "3":
        tampilkan_data_gudang(kategori_filter=None)
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")


# 3. Menu Update Barang
def update_barang():
    kategori = input("\nMasukkan kategori barang yang ingin diupdate (elektronik/furnitur): ").lower()
    if kategori not in gudang:
        print("Kategori tidak ditemukan.")
        return
    
    id_barang = input("Masukkan ID barang yang ingin diupdate: ").upper()
    found = False
    for item in gudang[kategori]:
        if item['ID'] == id_barang:
            print(f"Barang yang akan diupdate: ID: {item['ID']}, Nama: {item['Nama']}, Stok: {item['Stok']}, Harga: Rp {item['Harga']: ,}")
            print("Pilih data yang ingin diupdate:")
            print("1. Nama")
            print("2. Stok")
            print("3. Harga")
            while True:
                try:
                    pilihan_update = int(input("Masukkan pilihan (1/2/3): "))
                    if pilihan_update in [1, 2, 3]:
                        break
                    else:
                        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
                except ValueError:
                    print("Input tidak valid, silakan masukkan angka 1, 2, atau 3.")
                    
            if pilihan_update == 1:
                nama_baru = input("Masukkan nama baru barang: ")
                item['Nama'] = nama_baru.title()
                print(f"Nama barang berhasil diubah menjadi {item['Nama']}.")
            elif pilihan_update == 2:
                stok_baru = int(input("Masukkan jumlah stok baru barang: "))
                item['Stok'] = stok_baru
                print(f"Stok barang berhasil diubah menjadi {item['Stok']}.")
            elif pilihan_update == 3:
                harga_baru = int(input("Masukkan harga baru barang: "))
                item['Harga'] = harga_baru
                print(f"Harga barang berhasil diubah menjadi Rp {item['Harga']: ,}.")
            else:
                print("Pilihan tidak valid.")
            
            print("\nData Barang Setelah Update:")
            tampilkan_data_gudang(kategori)
            found = True
            break
    if not found:
        print("Barang dengan ID tersebut tidak ditemukan.")

        
# 4. Menu Menghapus Barang
def hapus_barang():
    kategori = input("\nMasukkan kategori barang yang ingin dihapus (elektronik/furnitur): ").lower()
    if kategori not in gudang:
        print("Kategori tidak ditemukan.")
        return
    
    id_barang = input("Masukkan ID barang yang ingin dihapus: ").upper()
    found = False
    for item in gudang[kategori]:
        if item['ID'] == id_barang:
            harga = f"Rp {item['Harga']: ,}"
            print(f"Barang yang akan dihapus: ID: {item['ID']}, Nama: {item['Nama']}, Stok: {item['Stok']}, Harga: {harga}")
            konfirmasi = input("Apakah Anda yakin ingin menghapus barang ini? (Ya/Tidak): ").lower()
            if konfirmasi == 'ya':
                gudang[kategori].remove(item)  
                print(f"Barang {item['Nama']} dengan ID {id_barang} berhasil dihapus.")
                found = True
                break
            else:
                print("Penghapusan dibatalkan.")
                found = True
                break
    
    if not found:
        print("Barang dengan ID tersebut tidak ditemukan.")
    
    tampilkan_data_gudang(kategori)


while True:
    print("\n=== Data Gudang Purwadhika Elektronik & Furnitur ===")
    print("List Menu : ")
    print("1. Menambah Barang ")
    print("2. Menampilkan Data Gudang")
    print("3. Update Barang")
    print("4. Menghapus Barang")
    print("5. Exit Program")
    pilihan = int(input("Masukkan angka Menu yang ingin dijalankan : "))
    
    if pilihan == 1:
        tambah_barang()
    elif pilihan == 2:
        menu_pilihan()
    elif pilihan == 3:
        update_barang()
    elif pilihan == 4:
        hapus_barang()
    elif pilihan == 5:
        print("Terima kasih! Program Selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
