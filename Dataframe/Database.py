
#### Database ####

import pandas as pd

df = pd.DataFrame({
    'Produk': ['Ram','Monitor','VGA','Casing','Processor','SSD','PSU','Motherboard'],
    'Harga' : [500000,1500000,4000000,500000,2000000,1000000,700000,1500000],
    'Stok'  : [20,12,30,8,21,50,30,28] 
})

df['Total Nilai'] = df['Harga']*df['Stok']


#fungsi input 

def tambah_produk():
    global df  #mengubah dataframe utama

    nama = input("Masukkan nama produk: ")
    harga = int(input("Masukkan harga produk: "))
    stok = int(input("Masukkan stok produk: "))

    df.loc[len(df)] = [nama, stok, harga, stok * harga]
    print(f"\n {nama} berhasil ditambahkan!\n")

def get_data():
    return df

def Save_excel():
    df.to_excel('Stok Gudang.xlsx',index=False)
    print('File sudah dibuat')


# fungsi tambah stok
def tambah_stok():
    global df

    while True:
        print(df['Produk'])

        user = input('pilih salah satu produk yg ingin di tambah stok dg nama barang: ') 

        if user in df['Produk'].values:
            jumlah = int(input('Masukan jumlah stok yang ingin ditambahkan: '))

            #index produk
            idx = df.index[df['Produk'] == user][0]

            #update stok
            df.loc[idx,'Stok']+= jumlah
            print(f'Stok {user} berhasil ditambahkan')
        else:
            print('produk tidak ditemukan')

        exit = input('apakah ingin mengakhiri program (y/n): ')
        if exit == 'y':
            print('program selesai')
            break

#Funsi mengurangi stok

def kurang_stok():
    global df

    while True:

        print(df['Produk'])

        user = input('pilih salah satu produk yg ingin di kurangi stoknya dg nama barang: ') 

        if user in df['Produk'].values:
            jumlah = int(input('Masukan angka yang anda ingin kurangi: '))

            #index produk
            idx = df.index[df['Produk'] == user][0]

            #update stok
            df.loc[idx,'Stok']-= jumlah
            print(f'Stok {user} berhasil dikurangkan')
        else:
            print('produk tidak ditemukan')

        exit = input('apakah ingin mengakhiri program (y/n): ')
        if exit == 'y':
            print('program selesai')
            break



