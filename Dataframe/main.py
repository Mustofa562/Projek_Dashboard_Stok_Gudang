from Database import get_data,tambah_produk,Save_excel,tambah_stok,kurang_stok
from visualisasi import show_bar,show_pie

while True:
    print("""
============ MENU ===========
1. Lihat Data
2. Tambah Barang
3. Grafik Stok
4. Grafik Pie Nilai
5. Simpan ke Excel
6. Tambah Stok
7. Mengurangi stok
8. Keluar
""")
    
    pilihan = input('pilih menu: ')

    if pilihan == '1':
        print(get_data())
    elif pilihan == '2':
        tambah_produk()
    elif pilihan == '3':
        show_bar(get_data())
    elif pilihan == '4':
        show_pie(get_data())
    elif pilihan == '5':
        Save_excel()
    elif pilihan == '6':
        tambah_stok()
    elif pilihan == '7':
        kurang_stok()
    elif pilihan == '8':
        print("Program selesai")
        break
    
    else:
        print('pilihan tidak valid!')