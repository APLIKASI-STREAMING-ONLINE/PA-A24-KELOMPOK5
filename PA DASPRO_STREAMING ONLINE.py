import os
import csv
import pwinput
from prettytable import PrettyTable
import time

film_path = r"Tugas/Semester 1/Praktikum Daspro/PA/data_film.csv"
pengguna = r"Tugas/Semester 1/Praktikum Daspro/PA/data_pengguna.csv"
langganan = r"Tugas/Semester 1/Praktikum Daspro/PA/data_langganan.csv"
saldo_path = r"Tugas/Semester 1/Praktikum Daspro/PA/data_saldo.csv"

def load_user_data():
    try:
        data = {}
        with open(pengguna, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    data[row[0]] = row[1]
        return data
    except FileNotFoundError:
        # Default pengguna jika file tidak ditemukan
        data = {"admin": "admin123", "Rama": "123"}
        save_user_data(data)
        return data

def save_user_data(data):
    with open(pengguna, "w", newline="") as file:
        writer = csv.writer(file)
        for username, password in data.items():
            writer.writerow([username, password])

def load_langganan_data():
    try:
        data = {}
        with open(langganan, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    data[row[0]] = row[1]
        return data
    except FileNotFoundError:
        data = {"admin": "1", "Rama": "0"}
        save_user_data(data)
        return data

def save_langganan_data(data):    
    with open(langganan, "w", newline="") as file:
        writer = csv.writer(file)
        for username, status in data.items():
            writer.writerow([username, status])

def load_saldo_data():
    saldo = {}
    try:
        with open(saldo_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    saldo[row[0]] = float(row[1])
    except FileNotFoundError:
        # Default saldo jika file tidak ditemukan
        saldo = {"admin": 50000, "Rama": 50000}
        save_saldo_data(saldo)
    return saldo

def save_saldo_data(saldo):
    with open(saldo_path, "w", newline="") as file:
        writer = csv.writer(file)
        for username, saldo_amount in saldo.items():
            writer.writerow([username, saldo_amount])

def load_film_data():
    try:
        with open(film_path, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_film_data(films):
    with open(film_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=films[0].keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerows(films)

def tambah_film():
    print("\n======== TAMBAH FILM BARU ========")
    try:
        existing_films = []
        try:
            with open(film_path, mode="r") as file:
                reader = csv.DictReader(file)
                existing_films = [film["judul"].lower() for film in reader]
        except FileNotFoundError:
            with open(film_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(['judul', 'tahun', 'kategori', 'sutradara', 'durasi', 'kategori_usia', 'pemeran_utama'])

        while True:
            try:
                judul = input("Judul film: ").strip()
                if not judul:
                    print("Judul film tidak boleh kosong!")
                    continue
                if judul.lower() in existing_films:
                    print("Film dengan judul tersebut sudah ada!")
                    continue
                break
            except KeyboardInterrupt:
                print("Jangan tekan ctrl+c, Program terganggu.")
                try:
                    input("Tekan enter untuk melanjutkan...")
                except KeyboardInterrupt:
                    pass
                os.system("cls")

        while True:
            try:
                tahun = input("Tahun rilis: ").strip()
                if not tahun.isdigit() or len(tahun) != 4:
                    raise ValueError("Tahun harus berupa 4 digit angka!")
                break
            except ValueError as e:
                print(e)
            except KeyboardInterrupt:
                print("Jangan tekan ctrl+c, Program terganggu.")
                try:
                    input("Tekan enter untuk melanjutkan...")
                except KeyboardInterrupt:
                    pass
                os.system("cls")

        while True:
            try:
                kategori = input("Kategori film: ").strip()
                sutradara = input("Sutradara: ").strip()
                break
            except KeyboardInterrupt:
                print("Jangan tekan ctrl+c, Program terganggu.")
                try:
                    input("Tekan enter untuk melanjutkan...")
                except KeyboardInterrupt:
                    pass
                os.system("cls")

        while True:
            try:
                durasi = input("Durasi (dalam menit): ").strip()
                if not durasi.isdigit():
                    print("Durasi harus berupa angka!")
                    continue
                break
            except KeyboardInterrupt:
                print("Jangan tekan ctrl+c, Program terganggu.")
                try:
                    input("Tekan enter untuk melanjutkan...")
                except KeyboardInterrupt:
                    pass
                os.system("cls")

        while True:
            try:
                kategori_usia = input("Kategori usia (SU/13+/17+/21+): ").strip().upper()
                if kategori_usia not in ["SU", "13+", "17+", "21+"]:
                    print("Kategori usia tidak valid! Pilih: SU/13+/17+/21+")
                    continue
                break
            except KeyboardInterrupt:
                print("Jangan tekan ctrl+c, Program terganggu.")
                try:
                    input("Tekan enter untuk melanjutkan...")
                except KeyboardInterrupt:
                    pass
                os.system("cls")

        while True:
            try:
                pemeran_utama = input("Pemeran utama: ").strip()
                break
            except KeyboardInterrupt:
                print("Jangan tekan ctrl+c, Program terganggu.")
                try:
                    input("Tekan enter untuk melanjutkan...")
                except KeyboardInterrupt:
                    pass
                os.system("cls")

        film_baru = {
            'judul': judul,
            'tahun': tahun,
            'kategori': kategori,
            'sutradara': sutradara,
            'durasi': durasi,
            'kategori_usia': kategori_usia,
            'pemeran_utama': pemeran_utama
        }

        with open(film_path, mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=film_baru.keys())
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(film_baru)

        print("\nFilm berhasil ditambahkan!")

    except Exception as e:
        print(f"\nTerjadi kesalahan: {str(e)}")

    input("\nTekan enter untuk melanjutkan...")
    os.system("cls")

def hapus_film():
    films = lihat_semua_film()
    if not films:
        input("Tekan enter untuk melanjutkan...")
        return
    
    try:
        nomor_film = int(input("\nMasukkan nomor film yang ingin dihapus: "))
        if nomor_film < 1 or nomor_film > len(films):
            print("Nomor film tidak valid!")
            input("Tekan enter untuk melanjutkan...")
            return
        
        film = films[nomor_film - 1]
        judul = film["judul"]
        
        with open(film_path, mode="r") as file:
            reader = csv.DictReader(file)
            films = list(reader)
        
        films.pop(nomor_film - 1)
        
        with open(film_path, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=films[0].keys())
            writer.writeheader()
            writer.writerows(films)
        
        print(f"\nFilm '{judul}' berhasil dihapus!")
        
    except ValueError:
        print("Nomor film harus berupa angka!")
    except KeyboardInterrupt:
        print("Jangan tekan ctrl+c, Program terganggu.")
        try:
            input("Tekan enter untuk melanjutkan...")
        except KeyboardInterrupt:
            pass
        os.system("cls")
    
    input("Tekan enter untuk melanjutkan...")
    os.system("cls")

def lihat_semua_film():
    table = PrettyTable()
    table.field_names = ["No", "Judul", "Tahun", "Kategori", "Sutradara", "Durasi", "Kategori Usia", "Pemeran Utama"]

    try:
        with open(film_path, mode="r") as file:
            reader = csv.DictReader(file)
            films = list(reader)
            for idx, film in enumerate(films, 1):
                table.add_row([idx, film["judul"], film["tahun"], film["kategori"], film["sutradara"], film["durasi"], film["kategori_usia"], film["pemeran_utama"]])
        
            print("+------------------------------------------+")
            print("         🎬    DAFTAR SEMUA FILM           ")
            print("+------------------------------------------+")           
            print(table)
            return films

    except FileNotFoundError:
        print("File data film tidak ditemukan.")
        return []
    input("Tekan enter untuk melanjutkan...")
    os.system("cls")

def update_film():
    films = lihat_semua_film()
    if not films:
        input("Tekan enter untuk melanjutkan...")
        
    try:
        nomor_film = int(input("\nMasukkan nomor film yang ingin diupdate: "))
        if nomor_film < 1 or nomor_film > len(films):
            print("Nomor film tidak valid!")
            input("Tekan enter untuk melanjutkan...")
            return
        
        film = films[nomor_film - 1]
        
        while True:
            print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
            judul_baru = input(f"Judul ({film['judul']}): ").strip()

            while True:
                tahun_baru = input(f"Tahun ({film['tahun']}): ").strip()
                if tahun_baru == "":
                    break
                elif not tahun_baru.isdigit() or len(tahun_baru) != 4:
                    print("Tahun harus berupa angka 4 digit!")
                    continue
                else:
                    break
            kategori_baru = input(f"Kategori ({film['kategori']}): ").strip()

            sutradara_baru = input(f"Sutradara ({film['sutradara']}): ").strip()

            while True:
                durasi_baru = input(f"Durasi ({film['durasi']}): ").strip()
                if durasi_baru == "":
                    break
                elif not durasi_baru.isdigit():
                        print("Durasi harus berupa angka!")
                        continue
                else:
                    break

            while True:
                kategori_usia_baru = input(f"Kategori Usia ({film['kategori_usia']}) (SU/13+/17+/21+): ").strip()
                if kategori_usia_baru == "":
                    break
                elif kategori_usia_baru not in ["SU", "13+", "17+", "21+"]:
                    print("Kategori usia tidak valid! Pilih: SU/13+/17+/21+")
                    continue
                else:
                    break

            pemeran_baru = input(f"Pemeran Utama ({film['pemeran_utama']}): ").strip()
            break
        
        films[nomor_film - 1].update({
            'judul': judul_baru if judul_baru else film['judul'],
            'tahun': tahun_baru if tahun_baru else film['tahun'],
            'kategori': kategori_baru if kategori_baru else film['kategori'],
            'sutradara': sutradara_baru if sutradara_baru else film['sutradara'],
            'durasi': durasi_baru if durasi_baru else film['durasi'],
            'kategori_usia': kategori_usia_baru if kategori_usia_baru else film['kategori_usia'],
            'pemeran_utama': pemeran_baru if pemeran_baru else film['pemeran_utama']
        })
        
        fieldnames = ['judul', 'tahun', 'kategori', 'sutradara', 'durasi', 'kategori_usia', 'pemeran_utama']
        with open(film_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(films)
        
        print("\nData film berhasil diupdate!")
        os.system("cls")
        
    except ValueError:
        print("Input tidak valid!")
    except KeyboardInterrupt:
        print("Jangan tekan ctrl+c, Program terganggu.")
        try:
            input("Tekan enter untuk melanjutkan...")
        except KeyboardInterrupt:
            pass
        os.system("cls")

    input("Tekan enter untuk melanjutkan...")


def tampilkan_invoice(username, paket, harga, saldo_terakhir):
    # Membuat table invoice
    table = PrettyTable()
    table.title = "INVOICE"
    table.field_names = ["Deskripsi", "Detail"]
    
    # Menambahkan data ke dalam table
    table.add_row(["Nama Pengguna", username])
    table.add_row(["Paket", paket])
    table.add_row(["Harga", f"Rp {harga:,}"])
    table.add_row(["Saldo Setelah Transaksi", f"Rp {saldo_terakhir:,.2f}"])
    
    # Menampilkan invoice
    print(table)
    print("====================")
    input("\nTekan enter untuk melanjutkan...")

def beli_paket(username):
    os.system("cls")
    saldo = load_saldo_data()
    langganan = load_langganan_data()
    
    if username not in saldo:
        print("Pengguna tidak ditemukan!")
        return
    
    # Jika pengguna sudah memiliki paket langganan
    if username in langganan and langganan[username] != '0':
        print("Anda sudah memiliki paket langganan!")
        print("Paket langganan Anda saat ini:", langganan[username])

        # Memberikan opsi upgrade paket jika sudah berlangganan
        while True:
            try:
                print("\nPilih paket yang ingin Anda upgrade:")
                if langganan[username] == "Paket Basic":
                    print("1. Upgrade ke Paket Standard - Rp 100.000")
                    print("2. Upgrade ke Paket Premium - Rp 200.000")
                elif langganan[username] == "Paket Standard":
                    print("1. Upgrade ke Paket Premium - Rp 200.000")
                else:
                    print("Anda sudah berada pada paket Premium, tidak bisa upgrade lebih lanjut.")

                if langganan[username] == "Paket Basic":
                    pilihan = int(input("\nMasukkan pilihan (1/2/0 Untuk keluar): "))
                    if pilihan == 0:
                        break
                    elif pilihan == 1:
                        if langganan[username] == "Paket Basic":
                            beli_paket_upgrade(username, 100000, "Paket Standard")
                            break
                        elif langganan[username] == "Paket Standard":
                            beli_paket_upgrade(username, 200000, "Paket Premium")
                            break
                        os.system("cls")
                    elif pilihan == 2:
                        if langganan[username] == "Paket Basic":
                            beli_paket_upgrade(username, 200000, "Paket Premium")
                            break
                        elif langganan[username] == "Paket Standard":
                            beli_paket_upgrade(username, 200000, "Paket Premium")
                            break
                        os.system("cls")
                    else:
                        print("Pilihan tidak valid! Harap pilih 1,2, atau 0 untuk keluar.")
                        input("Tekan enter untuk melanjutkan...")
                        os.system("cls")
                elif langganan[username] == "Paket Standard":
                    pilihan = int(input("\nMasukkan pilihan (1/0 Untuk keluar): "))
                    if pilihan == 0:
                        break
                    elif pilihan == 1:
                        beli_paket_upgrade(username, 200000, "Paket Premium")
                        break
                    else:
                        print("Pilihan tidak valid! Harap pilih 1 atau 0 untuk keluar.")
                        input("Tekan enter untuk melanjutkan...")
                        os.system("cls")
                elif langganan[username] == "Paket Premium":
                    pilihan = int(input("\nMasukkan pilihan (0 Untuk keluar): "))
                    if pilihan == 0:
                        break
                    else:
                        print("Pilihan tidak valid! Harap pilih 0 untuk keluar.")
                        input("Tekan enter untuk melanjutkan...")
                        os.system("cls")
                else:
                    print("Pilihan tidak valid! Harap pilih 1 atau 2.")
                    input("Tekan enter untuk melanjutkan...")
                    os.system("cls")
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
                input("Tekan enter untuk melanjutkan...")
                os.system("cls")
            except KeyboardInterrupt:
                print("Jangan tekan ctrl+c, Program terganggu.")
                try:
                    input("Tekan enter untuk melanjutkan...")
                except KeyboardInterrupt:
                    pass
                os.system("cls")

    else:
        os.system("cls")
        print(f"\nSaldo Anda saat ini: Rp{saldo[username]:,.2f}")
    
        while True:
            try:
                pilihan = int(input("Pilih paket langganan\n1. Paket Basic - Rp 50.000\n2. Paket Standard - Rp 100.000\n3. Paket Premium - Rp 200.000\n4. Exit\nMasukkan pilihan: "))
                if pilihan not in [1, 2, 3, 4]:
                    print("Pilihan tidak valid! Harap pilih 1, 2, 3, atau 4.")
                    input("Tekan enter untuk melanjutkan...")
                    os.system("cls")
                    continue 
                break
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
                input("Tekan enter untuk melanjutkan...")
                os.system("cls")
            except KeyboardInterrupt:
                print("Jangan tekan ctrl+c, Program terganggu.")
                try:
                    input("Tekan enter untuk melanjutkan...")
                except KeyboardInterrupt:
                    pass
                os.system("cls")

        # Proses pembelian paket berdasarkan pilihan
        if pilihan == 1 and saldo[username] >= 50000:
            saldo[username] -= 50000
            langganan[username] = "Paket Basic"
            save_langganan_data(langganan)
            save_saldo_data(saldo)
            tampilkan_invoice(username, "Paket Basic", 50000, saldo[username])
            os.system("cls")
        elif pilihan == 2 and saldo[username] >= 100000:
            saldo[username] -= 100000
            langganan[username] = "Paket Standard"
            save_langganan_data(langganan)
            save_saldo_data(saldo)
            tampilkan_invoice(username, "Paket Standard", 100000, saldo[username])
            os.system("cls")
        elif pilihan == 3 and saldo[username] >= 200000:
            saldo[username] -= 200000
            langganan[username] = "Paket Premium"
            save_langganan_data(langganan)
            save_saldo_data(saldo)
            tampilkan_invoice(username, "Paket Premium", 200000, saldo[username])
            os.system("cls")
        elif pilihan == 4:
            return
        else:
            print("Saldo tidak cukup untuk membeli paket ini atau pilihan tidak valid!")
            print("Apakah anda ingin top up saldo?")
            while True:
                try:
                    pilihan = int(input("1. Ya\n2. Tidak\nMasukkan pilihan(1/2): "))
                    if pilihan == 1:
                        top_up_saldo(username)
                        beli_paket(username)
                        break
                    elif pilihan == 2:
                        break
                    else:
                        print("Pilihan tidak valid! Harap pilih 1 atau 2.")
                        input("Tekan enter untuk melanjutkan...")
                        os.system("cls")
                except ValueError:
                    print("Input tidak valid! Harap masukkan angka.")
                    input("Tekan enter untuk melanjutkan...")
                    os.system("cls")
                except KeyboardInterrupt:
                    print("Jangan tekan ctrl+c, Program terganggu.")
                    try:
                        input("Tekan enter untuk melanjutkan...")
                    except KeyboardInterrupt:
                        pass
                    os.system("cls")
    
def beli_paket_upgrade(username, harga, paket_baru):
    saldo = load_saldo_data()
    langganan = load_langganan_data()
    
    if saldo[username] >= harga:
        saldo[username] -= harga
        langganan[username] = paket_baru
        save_langganan_data(langganan)
        save_saldo_data(saldo)
        tampilkan_invoice(username, paket_baru, harga, saldo[username])
    else:
        print("Saldo tidak cukup untuk upgrade paket.")
        print("Apakah anda ingin top up saldo?")
        while True:
                try:
                    pilihan = int(input("1. Ya\n2. Tidak\nMasukkan pilihan(1/2): "))
                    if pilihan == 1:
                        top_up_saldo(username)
                        beli_paket(username)
                        break
                    elif pilihan == 2:
                        break
                    else:
                        print("Pilihan tidak valid! Harap pilih 1 atau 2.")
                        input("Tekan enter untuk melanjutkan...")
                        os.system("cls")
                except ValueError:
                    print("Input tidak valid! Harap masukkan angka.")
                    input("Tekan enter untuk melanjutkan...")
                    os.system("cls")
                except KeyboardInterrupt:
                    print("Jangan tekan ctrl+c, Program terganggu.")
                    try:
                        input("Tekan enter untuk melanjutkan...")
                    except KeyboardInterrupt:
                        pass
                    os.system("cls")

def tonton_film(username):
    film_path = load_film_data()  # Memuat data film
    langganan = load_langganan_data()  # Memuat data langganan pengguna
    films = lihat_semua_film()  # Menampilkan semua film

    print("\n____ 📺 TONTON FILM ____")
    
    # Memeriksa apakah pengguna sudah memiliki paket langganan
    if username not in langganan or langganan[username] == '0':
        print("\nAnda belum memiliki paket langganan!")
        while True:
            try:
                pilihan = int(input("Apakah anda ingin membeli paket langganan? \n1. Ya\n2. Tidak\nMasukkan pilihan (1/2): "))
                if pilihan == 1:
                    beli_paket(username)  # Pengguna membeli paket
                    # Setelah membeli paket, lanjutkan menonton film
                    tonton_film(username)
                    break  # Keluar dari loop setelah membeli paket
                elif pilihan == 2:
                    print("Anda tidak dapat menonton film tanpa paket langganan.")
                    break  # Keluar dari loop jika tidak membeli paket
                else:
                    print("Pilihan tidak valid! Harap pilih 1 atau 2.")
                    input("Tekan enter untuk melanjutkan...")
                    os.system("cls")
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
                input("Tekan enter untuk melanjutkan...")
                os.system("cls")
            except KeyboardInterrupt:
                print("Jangan tekan ctrl+c, Program terganggu.")
                try:
                    input("Tekan enter untuk melanjutkan...")
                except KeyboardInterrupt:
                    pass
                os.system("cls")
    else:
        # Jika pengguna sudah memiliki paket langganan
        paket = langganan[username]
        
        print(f"\nPaket langganan Anda: {paket}")
        
        # Menentukan batas kualitas berdasarkan paket
        if paket == 'Paket Basic':
            kualitas_terbatas = '720p'
        elif paket == 'Paket Standard':
            kualitas_terbatas = '1080p'
        elif paket == 'Paket Premium':
            kualitas_terbatas = '4K'
        else:
            print("Paket langganan tidak valid.")
            return

        # Menampilkan daftar film yang dapat Anda tonton berdasarkan kualitas paket
        print("\nDaftar film yang dapat Anda tonton berdasarkan kualitas paket:")
        film_tersedia = []
        for i, film in enumerate(films, 1):
            print(f"{i}. {film['judul']} - Kualitas {kualitas_terbatas}")  # Menampilkan kualitas berdasarkan paket
            film_tersedia.append(film)

        # Memilih film atau keluar
        while True:
            try:
                print("\nMasukkan '0' untuk kembali ke menu sebelumnya.")
                pilihan_film = int(input("\nPilih film yang ingin Anda tonton (Masukkan nomor film): "))
                
                if pilihan_film == 0:
                    print("Kembali ke menu sebelumnya.")
                    break  # Kembali ke menu sebelumnya tanpa menonton film
                    
                # Memeriksa apakah pilihan film valid
                if 1 <= pilihan_film <= len(film_tersedia):
                    film_terpilih = film_tersedia[pilihan_film - 1]
                    print(f"\nMemutar film {film_terpilih['judul']} dengan kualitas {kualitas_terbatas}...")
                    print("____________________________________")
                    print("|                                  |")
                    print("|                                  |")
                    countdown = 5
                    for i in range(countdown, 0, -1):
                        print(f"\r|                ({i})               |", end="") 
                        time.sleep(1)

                    print("\n|     ↻    ◁     ||     ▷    ↺     |")
                    print("|                                  |")
                    print("|      Film selesai diputar        |")
                    print("|                                  |")
                    print("|__________________________________|")
                    input("Tekan enter untuk melanjutkan...")
                    break
                else:
                    print("Nomor film tidak valid! Silakan coba lagi.")
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
                input("Tekan enter untuk melanjutkan...")
                os.system("cls")
            except KeyboardInterrupt:
                print("Jangan tekan ctrl+c, Program terganggu.")
                try:
                    input("Tekan enter untuk melanjutkan...")
                except KeyboardInterrupt:
                    pass
                os.system("cls")

    os.system("cls")

def cari_film():
    os.system("cls")
    films = lihat_semua_film()
    while True:
        try:
            judul_film = input("Masukkan judul film yang ingin dicari: ").lower().strip()
            if not judul_film:
                print("Input tidak boleh kosong")
                continue
            break
        except KeyboardInterrupt:
            print("Jangan tekan ctrl+c, Program terganggu.")
            try:
                input("Tekan enter untuk melanjutkan...")
            except KeyboardInterrupt:
                pass
            os.system("cls")
    film_ditemukan = False

    for film in films:
        if judul_film.lower() in film["judul"].lower():
            print(f"Judul Film: {film['judul']}")
            print(f"Kategori: {film['kategori']}")
            print(f"Tahun Rilis: {film['tahun']}")
            print(f"Sutradara: {film['sutradara']}")
            print(f"Durasi: {film['durasi']}")
            print(f"Kategori Usia: {film['kategori_usia']}")
            print(f"Pemeran Utama: {film['pemeran_utama']}")
            film_ditemukan = True
            break

    if not film_ditemukan:
        print("Film yang Anda cari tidak ditemukan.")
        input("Tekan enter untuk melanjutkan...")
        os.system("cls")
        cari_film()

    input("Tekan enter untuk melanjutkan...")
    os.system("cls")

def top_up_saldo(username):
    saldo = load_saldo_data()  # Memuat data saldo
    if username not in saldo:
        print("Pengguna tidak ditemukan!")
        return

    while True:
        try:
            # Meminta input jumlah top-up dari pengguna
            jumlah_top_up = int(input("Masukkan jumlah saldo yang ingin ditambahkan: Rp "))
            if jumlah_top_up <= 0:
                print("Jumlah saldo yang ditambahkan harus lebih besar dari nol!")
                continue
            break  # Keluar dari loop jika input valid
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
        except KeyboardInterrupt:
            print("Jangan tekan ctrl+c, Program terganggu.")
            try:
                input("Tekan enter untuk melanjutkan...")
            except KeyboardInterrupt:
                pass
            os.system("cls")

    saldo[username] += jumlah_top_up 
    save_saldo_data(saldo)  
    print(f"Saldo Anda berhasil ditambahkan! Saldo saat ini: Rp {saldo[username]:.2f}")

    input("Tekan enter untuk melanjutkan...")  
    os.system("cls")

def login():
    username_admin = load_user_data()
    while True:
        try:
            username = input("Username : ")
            password = pwinput.pwinput("Password : ")
            break
        except KeyboardInterrupt:
            print("Jangan tekan ctrl+c, Program terganggu.")
            try:
                input("Tekan enter untuk melanjutkan...")
            except KeyboardInterrupt:
                pass
    if username in username_admin and username_admin[username] == password:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Selamat datang, {'Admin' if username == 'admin' else username}")
        return username
    else:
        print("\nUsername atau kata sandi yang Anda masukkan salah!")
        input("Tekan enter untuk melanjutkan...")
        return None

def register():
    username_admin = load_user_data()
    while True:
        try:
            username = input("Username : ").strip()
            if not username: 
                print("Username tidak boleh kosong!")
                continue
            if username in username_admin:
                print("Username telah digunakan")
                continue
        except KeyboardInterrupt:
            print("Jangan tekan ctrl+c, Program terganggu.")
            try:
                input("Tekan enter untuk melanjutkan...")
            except KeyboardInterrupt:
                pass
        
        while True:
            try:
                password = pwinput.pwinput("Password : ").strip()
                if not password: 
                    print("Password tidak boleh kosong!")
                    continue
                break
            except KeyboardInterrupt:
                print("Jangan tekan ctrl+c, Program terganggu.")
                try:
                    input("Tekan enter untuk melanjutkan...")
                except KeyboardInterrupt:
                    pass
                os.system("cls")

        username_admin[username] = password
        save_user_data(username_admin)

        saldo = load_saldo_data()
        saldo[username] = 50000  
        save_saldo_data(saldo)
        langganan = load_langganan_data()
        langganan[username] = 0
        save_langganan_data(langganan)
        
        print("Akun Anda telah terdaftar dengan saldo 50.000")
        input("Tekan enter untuk melanjutkan...")
        break

def admin():
    os.system("cls")
    while True:
        try:
            print("\n+-----------------------------------+")
            print("|            MENU ADMIN             |")
            print("+-----------------------------------+")
            print("|         1. Tambah Film            |")
            print("|         2. Hapus Film             |")
            print("|         3. Update film            |")
            print("|         4. Lihat semua film       |")
            print("|         5. Exit                   |")
            print("+-----------------------------------+")
            pilihan_admin = input("\nMasukkan pilihan: ")
            
            if pilihan_admin == "1":
                tambah_film()
            elif pilihan_admin == "2":
                hapus_film()
            elif pilihan_admin == "3":
                update_film()
            elif pilihan_admin == "4":
                lihat_semua_film()
                input("Tekan enter untuk melanjutkan...")
                os.system("cls")
            elif pilihan_admin == "5":
                break
            else:
                print("Pilihan tidak tersedia")
                input("Tekan enter untuk melanjutkan...")
        except KeyboardInterrupt:
            print("Jangan tekan ctrl+c, Program terganggu.")
            try:
                input("Tekan enter untuk melanjutkan...")
            except KeyboardInterrupt:
                pass
            os.system("cls")

def user(username):
    while True:
        try:
            saldo = load_saldo_data()
            print(f"\nSaldo Anda saat ini: Rp{saldo[username]:.2f}")
            langganan = load_langganan_data()
            print(f"Status langganan Anda: {langganan[username]}")
            print("\n+-----------------------------------+")
            print("|             MENU USER             |")
            print("+-----------------------------------+")
            print("|          1. Tonton Film           |")
            print("|          2. Cari Film             |")
            print("|          3. Beli Paket            |")
            print("|          4. Top up saldo          |")
            print("|          5. Exit                  |")
            print("+-----------------------------------+")
            pilihan_user = input("\nMasukkan pilihan: ")
            
            if pilihan_user == "1":
                tonton_film(username)
            elif pilihan_user == "2":
                cari_film()
            elif pilihan_user == "3":
                beli_paket(username)
            elif pilihan_user == "4":
                top_up_saldo(username)
            elif pilihan_user == "5":
                print("Exit")
                break
            else:
                print("Pilihan tidak tersedia")
                input("Tekan enter untuk melanjutkan...")
        except KeyboardInterrupt:
            print("Jangan tekan ctrl+c, Program terganggu.")
            try:
                input("Tekan enter untuk melanjutkan...")
            except KeyboardInterrupt:
                pass


def main():
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n+---------------------------------+")
            print("🎬   ✧˖ WELCOME TO NETFLIX!   ˖✧ 🎬")
            print("+---------------------------------+")
            print("\n+---------------------------------+")
            print("|            MENU UTAMA           |")
            print("+---------------------------------+")
            print("|           1. Login              |")
            print("|           2. Register           |")
            print("|           3. Exit               |")
            print("+---------------------------------+")
            pilihan_user = input("\nMasukkan pilihan : ")
            
            if pilihan_user == '1':
                username = login()
                if username:
                    if username == "admin":
                        admin()
                    else:
                        user(username)
            elif pilihan_user == '2':
                register()
            elif pilihan_user == '3':
                break
            else:
                print("Pilihan tidak tersedia")
                input("Tekan enter untuk melanjutkan...")
        except KeyboardInterrupt:
            print("Jangan tekan ctrl+c, Program terganggu.")
            try:
                input("Tekan enter untuk melanjutkan...")
            except KeyboardInterrupt:
                pass
            os.system("cls")

main()