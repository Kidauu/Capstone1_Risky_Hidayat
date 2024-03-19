from tabulate import tabulate

# Daftar produk pada toko vape store
daftarProduk = [
                ['Liquid Strawberry', 'Iceland', 20, 110000],
                ['Liquid Matcha', 'besti', 10, 110000],
                ['Pod Foom X', 'Foom', 15, 250000],
                ['Pod Oxva Slim', 'Oxva', 25, 260000],
                ['Mod Thelema', 'Lost Vape', 25, 550000],
                ['Mod R234', 'Hotcig', 15, 560000]
                ]

# Menu utama program
def menuUtama():
    print('Selamat Datang di JCDS Vape Store')
        
    print('List Menu: ')
    print('1. Menampilkan Daftar Produk')
    print('2. Menambah Produk')
    print('3. Mengubah Produk')
    print('4. Menghapus Produk')
    print('5. Membeli Produk')
    print('6. Exit Program')


keranjangBelanja = []  # Menyimpan barang yang dibeli oleh pelanggan

# Menampilkan pilihan kategori produk
def tampilkanPilihanKategori():
    print('Menu Kategori:')
    print('1. Tampilkan Semua Produk')
    print('2. Tampilkan Produk Tertentu (Liquid, Pod, Mod)')
    print('3. Cari Produk')
    print('4. Kembali ke Menu Utama')
    
# Menampilkan semua produk
def tampilkanSemuaProduk():
    data = []
    for i in range(len(daftarProduk)):
        sublist = [i, daftarProduk[i][0], daftarProduk[i][1], daftarProduk[i][2], daftarProduk[i][3]]
        data.append(sublist)
    print('\nSemua Produk:\n')
    print(tabulate(data, headers=['Index', 'Nama', 'Merk', 'Stok', 'Harga (Rp)'], tablefmt='pretty'))
    
# Menampilkan daftar produk berdasarkan kategori
def tampilkanProdukKategori(kategori):
    data = []
    for i in range(len(daftarProduk)):
        # Menggunakan indeks 0 (nama produk) untuk memeriksa kategori
        if kategori.lower() in daftarProduk[i][0].lower():  
            # .append() digunakan untuk menambahkan data produk yang sesuai dengan kategori ke dalam list data.
            data.append([i, daftarProduk[i][0], daftarProduk[i][1], daftarProduk[i][2], 'Rp. {:,.0f}'.format(daftarProduk[i][3])])
    if data:
        print(f'Daftar Produk Kategori {kategori}\n')
        print(tabulate(data, headers=['Index', 'Nama', 'Merk', 'Stok', 'Harga (Rp)'], tablefmt='pretty'))
    else:
        print(f'Tidak ada produk dalam kategori {kategori}.')
        

# Mencari produk berdasarkan nama
def cariProduk(nama):
    data = []
    for i in range(len(daftarProduk)):
        if nama.lower() in daftarProduk[i][0].lower():
            data.append([i, daftarProduk[i][0], daftarProduk[i][1], daftarProduk[i][2], 'Rp. {:,.0f}'.format(daftarProduk[i][3])])
    if not data:
        print("Produk yang Anda cari tidak ada.")
    else:
        print('\nHasil Pencarian Produk\n')
        print(tabulate(data, headers=['Index', 'Nama', 'Merk', 'Stok', 'Harga (Rp)'], tablefmt='pretty'))

# Menampilkan daftar produk
def tampilkanProduk():
    data = []
    for i in range(len(daftarProduk)):
        sublist = [i, daftarProduk[i][0], daftarProduk[i][1], daftarProduk[i][2], daftarProduk[i][3]]
        data.append(sublist)
    print('\nDaftar Produk\n')
    print(tabulate(data, headers=['Index', 'Merk', 'Nama', 'Stok', 'Harga (Rp)'], tablefmt='pretty'))

# Menambahkan produk baru ke dalam daftar produk
def tambahProduk():
    while True:
        namaProduk = input('Masukkan Nama Produk: ').title()
        if len(namaProduk) == 0:
            print("Nama produk tidak boleh kosong.")
            continue
        elif len(namaProduk) > 20:
            print("Nama produk terlalu panjang. Harap masukkan maksimal 20 karakter.")
            continue
        # Memeriksa setiap karakter dalam namaProduk
        for char in namaProduk:
            # Jika karakter bukan huruf, angka, atau spasi
            if not (char.isalnum() or char.isspace()):
                # Cetak pesan kesalahan
                print('Input tidak valid. Harap masukkan hanya huruf dan angka.')
                # Keluar dari loop
                break
        else:
            # Jika semua karakter valid, lanjutkan dengan memeriksa apakah produk sudah ada dalam daftar
            for produk in daftarProduk:
                # Membandingkan nama produk (dalam huruf kecil) dengan nama produk dalam daftar (juga dalam huruf kecil)
                if namaProduk.lower() == produk[0].lower():
                    # Jika nama produk sudah ada dalam daftarProduk, cetak pesan dan keluar dari loop
                    print('Produk sudah ada dalam daftar. Masukkan nama produk lain.')
                    break
            else:
                # Jika nama produk tidak ada dalam daftarProduk, keluar dari loop
                break

    while True:
        merkProduk = input('Masukkan Merk Produk: ').title()
        if len(merkProduk) == 0:
            print("Merk produk tidak boleh kosong.")
            continue
        elif len(merkProduk) > 20:
            print("Merk produk terlalu panjang. Harap masukkan maksimal 20 karakter.")
            continue
        if all(char.isalnum() or char.isspace() for char in merkProduk):
            break
        else:
            print('Input tidak valid. Harap masukkan hanya huruf dan angka.')
    
    while True:
        while True:
            stokProduk = input('Masukkan Stok Produk: ')
            if stokProduk.isdigit():  
                stokProduk = int(stokProduk)
                if stokProduk > 0:
                    break
                else:
                    print('Stok harus lebih dari 0.')
            else:
                print('Input tidak valid. Harap masukkan hanya angka.')

        while True:
            hargaProduk = input('Masukkan Harga Produk: ')
            if hargaProduk.isdigit():  
                hargaProduk = int(hargaProduk)
                if hargaProduk > 0:
                    break
                else:
                    print('Harga harus lebih dari 0.')
            else:
                print('Input tidak valid. Harap masukkan hanya angka.')
    
        print('\nData Produk Baru:')
        print('Nama Produk:', namaProduk)
        print('Merk Produk:', merkProduk)
        print('Stok Produk:', stokProduk)
        print('Harga Produk:', hargaProduk)
        
        while True:
            checker = input('Apakah ingin menyimpan produk yang baru ditambahkan? (y/t): ').lower()
            if checker == 'y':
                daftarProduk.append([namaProduk, merkProduk, stokProduk, hargaProduk])
                print('Data produk disimpan.')
                break
            elif checker == 't':
                print('Data produk tidak disimpan.')
                break
            else:
                print("Input tidak valid. Silahkan masukkan 'y' untuk ya atau 't' untuk tidak.")
        tampilkanSemuaProduk()
        break  # Keluar dari loop tambahProduk setelah produk ditambahkan
    
# Mengubah informasi sebuah produk
def ubahProduk():
    while True:
        tampilkanSemuaProduk()
        indexProduk = input('Masukkan nomor produk yang ingin diupdate: ')
        if indexProduk.isdigit():
            indexProduk = int(indexProduk)
            if 0 <= indexProduk < len(daftarProduk):
                produk = daftarProduk[indexProduk]
                print("Produk yang akan diubah:")
                print("Nama Produk:", produk[0])
                print("Merk Produk:", produk[1])
                print("Stok Produk:", produk[2])
                print("Harga Produk:", produk[3])
                while True:
                    print('Masukkan keyword yang ingin diubah (nama/merk/stok/harga):')
                    keyword = input('Keyword: ').lower()
                    if keyword == 'nama':
                        while True:
                            value = input('Masukkan nama produk baru: ')
                            if value:
                                # Periksa duplikasi nama produk
                                # variable cek digunakan untuk merepresentasikan setiap elemen dalam daftar produk saat melakukan iterasi
                                if any(cek[0].lower() == value.lower() for cek in daftarProduk if cek != produk):
                                    print('Nama produk sudah ada. Tidak diperbolehkan adanya duplikasi.')
                                    continue
                                produk[0] = value
                                break
                            else:
                                print('Nama produk tidak boleh kosong.')
                    elif keyword == 'merk':
                        while True:
                            value = input('Masukkan merk produk baru: ')
                            if value:
                                produk[1] = value
                                break
                            else:
                                print('Merk produk tidak boleh kosong.')
                    elif keyword == 'stok':
                        while True:
                            value = input('Masukkan jumlah stok produk baru: ')
                            if value.isdigit():
                                value = int(value)
                                if value > 0:
                                    produk[2] = value
                                    break
                                else:
                                    print('Stok harus lebih dari 0.')
                            else:
                                print('Stok harus berupa bilangan bulat.')
                    elif keyword == 'harga':
                        while True:
                            value = input('Masukkan harga produk baru (Rp): ')
                            if value.isdigit():
                                value = int(value)
                                if value > 0:
                                    produk[3] = value
                                    break
                                else:
                                    print('Harga harus lebih dari 0.')
                            else:
                                print('Harga harus berupa bilangan bulat.')
                    else:
                        print('Keyword tidak valid. Harap masukkan salah satu dari: nama, merk, stok, atau harga.')
                        break
                    checker = input('Apakah ingin menyimpan perubahan? (y/t): ').lower()
                    if checker == 'y':
                        daftarProduk[indexProduk] = produk
                        print('Perubahan produk berhasil disimpan.')
                        tampilkanSemuaProduk()
                        break
                    elif checker == 't':
                        print('Perubahan produk tidak disimpan.')
                        tampilkanSemuaProduk()
                        break  
                    else:
                        print('Input tidak valid. Silahkan masukkan "y" untuk ya atau "t" untuk tidak.')
                    break
                break
            else:
                print('Nomor produk tidak valid.')
        else:
            print('Input harus berupa angka. Silahkan masukkan nomor produk yang ingin diubah.')


# Menghapus sebuah produk dari daftar produk
def hapusProduk():
    while True:
        tampilkanSemuaProduk()
        indexProduk = input("Masukkan Index Produk yang ingin dihapus: ")
        if indexProduk.isdigit():
            indexProduk = int(indexProduk)
            if 0 <= indexProduk < len(daftarProduk):
                print("Produk yang akan dihapus:")
                print("Nama Produk:", daftarProduk[indexProduk][0])
                print("Merk Produk:", daftarProduk[indexProduk][1])
                print("Stok Produk:", daftarProduk[indexProduk][2])
                print("Harga Produk:", daftarProduk[indexProduk][3])
                checker = input('Apakah Anda yakin ingin menghapus produk ini? (y/t): ').lower()
                if checker == 'y':
                    del daftarProduk[indexProduk]
                    print('Produk berhasil dihapus.')
                    tampilkanSemuaProduk()
                    break  
                elif checker == 't':
                    print('Penghapusan produk dibatalkan.')
                    tampilkanSemuaProduk()
                    break  
                else:
                    print('Input tidak valid. Silahkan masukkan "y" untuk ya atau "t" untuk tidak.')
            else:
                print('Nomor produk tidak valid.')
        else:
            print("Input tidak valid. Harap masukkan nomor produk yang sesuai.")



# Menghapus sebuah produk dari daftar produk
def hapusProduk():
    while True:
        tampilkanSemuaProduk()
        indexProduk = input("Masukkan Index Produk yang ingin dihapus: ")
        if indexProduk.isdigit():
            indexProduk = int(indexProduk)
            if 0 <= indexProduk < len(daftarProduk):
                print("Produk yang akan dihapus:")
                print("Nama Produk:", daftarProduk[indexProduk][0])
                print("Merk Produk:", daftarProduk[indexProduk][1])
                print("Stok Produk:", daftarProduk[indexProduk][2])
                print("Harga Produk:", daftarProduk[indexProduk][3])
                checker = input('Apakah Anda yakin ingin menghapus produk ini? (y/t): ').lower()
                if checker == 'y':
                    del daftarProduk[indexProduk]
                    print('Produk berhasil dihapus.')
                    tampilkanSemuaProduk()
                    break  
                elif checker == 't':
                    print('Penghapusan produk dibatalkan.')
                    tampilkanSemuaProduk()
                    break  
                else:
                    print('Input tidak valid. Silahkan masukkan "y" untuk ya atau "t" untuk tidak.')
            else:
                print('Nomor produk tidak valid.')
        else:
            print("Input tidak valid. Harap masukkan nomor produk yang sesuai.")

# Melakukan pembelian produk
def beliProduk():
    tampilkanSemuaProduk()
    while True:
        indexProdukInput = input('Masukkan Index Produk yang ingin dibeli : ')
        if indexProdukInput.isdigit():  
            indexProduk = int(indexProdukInput)
            if 0 <= indexProduk < len(daftarProduk):  
                while True:
                    qtyProduk_input = input('Masukkan jumlah yang ingin dibeli : ')
                    if qtyProduk_input.isdigit():
                        qtyProduk = int(qtyProduk_input)
                        if qtyProduk > daftarProduk[indexProduk][2]:
                            print(f'Stok tidak cukup, stok {daftarProduk[indexProduk][0]} tinggal {daftarProduk[indexProduk][2]}')
                            return
                        else:
                            keranjangBelanja.append([daftarProduk[indexProduk][0], daftarProduk[indexProduk][1], qtyProduk, daftarProduk[indexProduk][3], indexProduk])
                        break
                    else:
                        print('Inputan harus berupa angka. Silahkan coba lagi.')
                        
                print('Isi Keranjang Belanja :')
                dataKeranjang = []
                for item in keranjangBelanja:
                    # Membuat entri data untuk setiap item dalam keranjang belanja dengan format yang diinginkan
                    entry = [item[0], item[1], item[2], 'Rp. {:,.0f}'.format(item[3])]
                    # Menambahkan entri data ke dalam list dataKeranjang
                    dataKeranjang.append(entry)
                # Menampilkan data keranjang belanja menggunakan tabulate
                print(tabulate(dataKeranjang, headers=['Nama', 'Merk', 'Qty', 'Harga (Rp)'], tablefmt='pretty'))

                checker = input('Apakah ingin membeli yang lain? (y/t): ').lower()
                while checker not in ['y', 't']:  
                    print('Input tidak valid. Silahkan masukkan "y" untuk ya atau "t" untuk tidak.')
                    checker = input('Apakah ingin membeli yang lain? (y/t): ').lower()
                if checker == 't':
                    break
                elif checker == 'y':
                    tampilkanSemuaProduk()
            else:
                print('Input tidak valid. Masukkan nomor produk yang sesuai.')
        else:
            print('Inputan harus berupa angka. Silahkan coba lagi.')
            
    total_pembelian = 0
    for item in keranjangBelanja:
        # Menghitung total pembelian dengan menjumlahkan harga total setiap item dalam keranjang belanja
        total_pembelian += item[2] * item[3]

    print(f'Total Pembelian: Rp {total_pembelian:,}')


    while True:
        pembayaran = input('Masukkan jumlah pembayaran: Rp ')
        if pembayaran.isdigit():
            pembayaran = int(pembayaran)
            break
        else:
            print('Inputan harus berupa angka. Silahkan coba lagi.')
            
    kembalian = pembayaran - total_pembelian
    if kembalian >= 0:
        print(f'Pembayaran berhasil. Kembalian Anda: Rp. {kembalian:,}')
    else:
        print('Pembayaran tidak mencukupi.')
        while True:
            pembayaran = input('Uang Anda kurang. Masukkan jumlah pembayaran yang mencukupi: Rp ')
            if pembayaran.isdigit():
                pembayaran = int(pembayaran)
                if pembayaran >= total_pembelian:
                    kembalian = pembayaran - total_pembelian
                    print(f'Pembayaran berhasil. Kembalian Anda: Rp. {kembalian:,}')
                    break
                else:
                    print('Pembayaran tidak mencukupi. Masukkan jumlah yang mencukupi.')
            else:
                print('Inputan harus berupa angka. Silahkan coba lagi.')

while True:
    menuUtama()
    pilihanMenu = input('Masukkan pilihan menu: ')
    if pilihanMenu == '1':
        while True:
            tampilkanPilihanKategori()
            pilihanKategori = input('Masukkan angka kategori (1 - 4): ')
            if pilihanKategori.isdigit() and 1 <= int(pilihanKategori) <= 4:  # Menambahkan validasi input
                if pilihanKategori == '1':
                    if not daftarProduk:
                        print('Maaf, tidak ada produk yang tersedia saat ini')
                    else:
                        tampilkanSemuaProduk()
                elif pilihanKategori == '2':
                    if not daftarProduk:
                        print('Maaf, tidak ada produk yang tersedia saat ini')
                    else:
                        while True:
                            print('Pilih jenis produk:')
                            print('1. Liquid')
                            print('2. Pod')
                            print('3. Mod')
                            print('4. Kembali ke Menu Kategori')
                            jenisProduk = input('Masukkan angka jenis produk (1 - 4): ')
                            if jenisProduk == '1':
                                tampilkanProdukKategori('Liquid')
                            elif jenisProduk == '2':
                                tampilkanProdukKategori('Pod')
                            elif jenisProduk == '3':
                                tampilkanProdukKategori('Mod')
                            elif jenisProduk == '4':
                                break
                            else:
                                print('Inputan tidak valid. Harap masukkan angka antara 1 dan 4.')
                elif pilihanKategori == '3':
                    if not daftarProduk:
                        print('Maaf, tidak ada produk yang tersedia saat ini')
                    else:
                        keyword = input('Masukkan nama produk yang ingin dicari: ').lower()
                        cariProduk(keyword)
                    
                elif pilihanKategori == '4':
                    break
                else:
                    print('Inputan tidak valid. Harap masukkan angka antara 1 dan 4.')

    elif pilihanMenu == '2':
        while True:
            print("1. Tambah Produk")
            print("2. Kembali ke Menu Utama")
            subMenu = input("Pilih menu: ")
            if subMenu == '1':
                tambahProduk()
            elif subMenu == '2':
                tampilkanPilihanKategori()
                break
            else:
                print("Pilihan tidak valid. Silahkan pilih antara 1 atau 2.")

    elif pilihanMenu == '3':
        while True:
            print("1. Ubah Produk")
            print("2. Kembali ke Menu Utama")
            subMenu = input("Pilih menu: ")
            if not daftarProduk:
                print('Maaf, tidak ada produk yang tersedia saat ini')
                break 
            if subMenu == '1':
                ubahProduk()
            elif subMenu == '2':
                tampilkanPilihanKategori()
                break
            else:
                print("Pilihan tidak valid. Silakan pilih antara 1 atau 2.")
                
    elif pilihanMenu == '4':
        while True:
            print("1. Hapus Produk")
            print("2. Kembali ke Menu Utama")
            subMenu = input("Pilih menu: ")
            if not daftarProduk:
                print('Maaf, tidak ada produk yang tersedia saat ini')
                break 
            if subMenu == '1':
                hapusProduk()
            elif subMenu == '2':
                tampilkanPilihanKategori()
                break
            else:
                print("Pilihan tidak valid. Silakan pilih antara 1 atau 2.")
                
    elif pilihanMenu == '5':
        while True:
            print("1. Beli Produk")
            print("2. Kembali ke Menu Utama")
            subMenu = input("Pilih menu: ")
            if subMenu == '1':
                if not daftarProduk:
                    print('Maaf, tidak ada produk yang tersedia saat ini')
                    continue
                beliProduk()
            elif subMenu == '2':
                tampilkanPilihanKategori()
                break
            else:
                print("Pilihan tidak valid. Silahkan pilih antara 1 atau 2.")
        
    elif pilihanMenu == '6':
        print('Terima Kasih telah mengunjungi JCDS Vape Store. Sampai Jumpa Kembali!!')
        break
    else:
        print('Pilihan menu tidak valid. Masukkan angka menu antara 1 dan 6.')