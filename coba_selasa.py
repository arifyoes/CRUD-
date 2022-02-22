

Karyawan = [{'NIK' : '001JKT', 'Nama' : 'Hassan', 'Jenis Kelamin' : 'Pria', 'Domisili' : 'Jakarta', 'Jabatan' : 'Data Science'},
{'NIK' : '002JKT', 'Nama' : 'Umar', 'Jenis Kelamin' : 'Pria', 'Domisili' : 'Jakarta', 'Jabatan' : 'Data Science'}]


#Menu Pertama
def Read_Data ():
    read = True 
    while read != '3':
        print("\n++++++++++Report Data Karyawan+++++++++\n")
        print("1. Report Seluruh Data")
        print("2. Report Data Tertentu")
        print("3. Kembali Ke Menu Utama")
        read = input("Silahkan Pilih Sub Menu Read Data [1-3] : ")
        if read == '1':
            if len(Karyawan) != 0 :
                print('Daftar Karyawan : ')
                for j, i in enumerate(Karyawan):
                    print(f"{j+1}, NIK : {i['NIK']}, Nama : {i['Nama']}, Jenis Kelamin : {i['Jenis Kelamin']}, Domisili : {i['Domisili']}, Jabatan : {i['Jabatan']}") 
            else:
                print('\n****Tidak Ada Data Karyawan****')
            continue
        elif read == '2' :
            if len(Karyawan) != 0:
                kry = input ('Masukkan NIK : ').upper()
                print(f"Data Karyawan Dengan NIK : {kry}")
                for j, i in enumerate(Karyawan):
                    if i['NIK'] == kry:
                        print(f"{j+1}. NIK : {i['NIK']}, Nama : {i['Nama']}, Jenis Kelamin : {i['Jenis Kelamin']}, Domisili : {i['Domisili']}, Jabatan : {i['Jabatan']}")
                        break
                else :
                    print('\n****Tidak Ada Data Karyawan****')
            else :
                print('\n****Karyawan Tidak Terdaftar****')
        elif read =='3' :
            print(pilihanMenu)
            break
        else:
            print('\n****Pilihan Menu Tidak Ada****')
    return

#Menu Kedua
def Create_Data ():
    
    create = True 
    while create != '2':
        print("\n++++++++++Report Data Karyawan+++++++++\n")
        print("1. Tambah Data Karyawan")
        print("2. Kembali Ke Menu Utama")
        create_karyawan = input("Silahkan Pilih Sub Menu Read Data [1-2] : ")
        if create_karyawan == '1':
             if len(Karyawan) != 0 :
                nikKaryawan = input ('Masukkan NIK : ').upper()
                for j, i in enumerate(Karyawan):
                    if nikKaryawan  == i['NIK']:
                        print('data sudah ada')
                        break
                    else :
                        NamaKaryawan = input('Masukkan Nama : ')
                        jkKaryawan = input('Masukkan Jenis Kelamin L/P: ').upper()
                        domisilikKaryawan = input('Masukkan Domisili : ')
                        jabatanKaryawan = input('Masukkan Jabatan : ')
                        if len(Karyawan) != 0:
                                kry = input ('Simpan data atau tidak Y/N : ').upper()
                                while True:
                                    if kry == 'Y':
                                        Karyawan.append({"NIK":nikKaryawan,"Nama":NamaKaryawan,"Jenis Kelamin":jkKaryawan,"Domisili":domisilikKaryawan,"Jabatan":jabatanKaryawan})
                                        print('Data disimpan')
                                        break
                                    elif kry == 'N':
                                      break 
                                    else :
                                        print('Hanya Ada Pilihan (Y/N) ')     
                                break
                        else :
                            print('\n****Tidak Ada Menu****')
        elif create_karyawan =='2' :
            print(pilihanMenu)
            break
        else :
            print('\n****Pilihan Menu Tidak Ada****')
    # return
                

#Menu Ketiga 
def Update_Data():
    Update = True
    while Update != '2':
        print("\n++++++++++Update Data Karyawan+++++++++\n")
        print("1. Update Data Karyawan")
        print("2. Kembali Ke Menu Utama")
        Update_karyawan = input("Silahkan Pilih Sub Menu Update Data [1-2] : ")
        if Update_karyawan == '1':

            updateNIK = input('Masukkan NIK: ')
            if len(Karyawan) != 0 :
                for j, i in enumerate(Karyawan):
                    if updateNIK == i['NIK']:
                        print(f"{j+1}, NIK : {i['NIK']}, Nama : {i['Nama']}, Jenis Kelamin : {i['Jenis Kelamin']}, Domisili : {i['Domisili']}, Jabatan : {i['Jabatan']}")
                        while True:
                            rubahAwal = input('\nAnda Yakin ingin Update Data (Y/N) : ').upper()
                            if rubahAwal == 'Y':
                                inputUpdate = input('\nMasukkan Data yang ingin di ganti (Nama, Jenis Kelamin, Domisili atau Jabatan) : ')
                                if inputUpdate == 'Nama' :
                                        gantiNama = input ('Masukkan Nama Baru: ')
                                        for j, i in enumerate(Karyawan):
                                            if gantiNama == i['Nama']:
                                                print('Nama sudah ada')
                                            else:
                                                i["Nama"] = gantiNama
                                            print('berhasil di update')
                                            break
                                        break
                                elif inputUpdate == 'Jenis Kelamin' :
                                        gantiJK = input ('Masukkan Jenis Kelamin Baru: ')
                                        for j, i in enumerate(Karyawan):
                                            if gantiJK == i['Jenis Kelamin']:
                                                print('Jenis Kelamin sudah ada')
                                            else:
                                                i["Jenis Kelamin"] = gantiJK
                                            print('berhasil di update')
                                            break
                                        break
                                elif inputUpdate == 'Domisili' :
                                        gantiDo = input ('Masukkan Domisili Baru: ')
                                        for j, i in enumerate(Karyawan):
                                            if gantiDo == i['Domisili']:
                                                print('Domisili sudah ada')
                                            else:
                                                i["Domisili"] = gantiDo
                                            print('berhasil di update')
                                            break
                                        break
                                elif inputUpdate == 'Jabatan' :
                                        gantiJ = input ('Jabatan Baru: ')
                                        for j, i in enumerate(Karyawan):
                                            if gantiJ == i['Jabatan']:
                                                print('Jabatan sudah ada')
                                            else:
                                                i["Jabatan"] = gantiJ
                                            print('berhasil di update')
                                            break
                                        break
                                else:
                                    print('\nInput Hanya boleh NIK, Nama, Jenis Kelamin, Domisili atau Jabatan')
                            elif rubahAwal == 'N':
                                break
        elif Update_karyawan =='2' :
            print(pilihanMenu)
            break
        else :
            print('\n****Pilihan Menu Tidak Ada****')
# return



# Menu KeEmpat
def Delete_Data ():
    delete = True 
    while delete != '2':
        print("\n++++++++++Menu Hapus Data Karyawan+++++++++\n")
        print("1. Delete Data Karyawan")
        print("2. Kembali Ke Menu Utama")
        delete_karyawan = input("Silahkan Pilih Sub Menu Delete Data [1-2] : ")
        if delete_karyawan == '1':
            hapusNIk = input('Masukkan NIK : ')
            if len(Karyawan) != 0 :
                for j, i in enumerate(Karyawan):
                    if hapusNIk == i['NIK']:
                        print(f"{j+1}, NIK : {i['NIK']}, Nama : {i['Nama']}, Jenis Kelamin : {i['Jenis Kelamin']}, Domisili : {i['Domisili']}, Jabatan : {i['Jabatan']}")
                        while True:
                            inputHapus = input('Apakan Anda Yakin Menghapus Data Karyawan? (Y/N) : ').upper()
                            if inputHapus == 'Y':
                                for i in range(len(Karyawan)):
                                    if Karyawan[i]['NIK'] == hapusNIk:
                                        del Karyawan[i]
                                        print('\n-----Data Karyawan Berhasil Di Hapus-----')
                                        break
                                    else:
                                        break
                                break
                            elif inputHapus == 'N':
                                print('Data Karyawan Tidak Disimpan')
                                break
                            else :
                                print('Hanya Ada Pilihan (Y/N) ')
                    else:
                        break
            else:
                print('----NIK Karyawan Tidak Terdaftar----')
        elif delete_karyawan =='2' :
            print(pilihanMenu)
            break
    return


while True:
    pilihanMenu = input('''
        Selamat Datang di Database Karyawan
    
        list Menu:
    
        1. Report Data Karyawan
        2. Menambah Data Karyawan
        3. Mengubah Data Karyawan
        4. Menghapus Data Karyawan
        5. Exit Program
        
        Silahkan Pilih Sub Menu Read Data [1-5] : ''')
    
    if(pilihanMenu == '1') :
        Read_Data ()
    elif(pilihanMenu == '2') :
        Create_Data ()
    elif(pilihanMenu == '3') :
        Update_Data()
    elif(pilihanMenu == '4') :
        Delete_Data ()
    else :
        print('\n****Pilihan Menu Tidak Ada****')
        break

