import backend
import logger
from datetime import datetime

# ---------------- Menu & Helpers ----------------
def tampilkan_daftar(daftar):
    if not daftar:
        print("📭 Daftar belanja kosong.")
        return False
    for i, item in enumerate(daftar, start=1):
        print(f"   {i}. {item}")
    return True

def tampilkan_menu():
    sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n🕒 Waktu sekarang: {sekarang}")
    print("=== APLIKASI DAFTAR BELANJA ===")
    print("1. Tambah item")
    print("2. Lihat semua item")
    print("3. Hapus item")
    print("4. Edit item")
    print("5. Cari item")
    print("6. Keluar")

# ---------------- Handlers ----------------
def tambah_item_handler():
    item = input("Nama item: ").strip()
    if not item:
        print("⚠️ Nama item tidak boleh kosong.")
        logger.tulis_log("Peringatan: input item kosong")
        return
    pesan = backend.tambah_item(item)
    print(pesan)
    logger.tulis_log(f"Menambah item: {item}")

def lihat_item_handler():
    daftar = backend.baca_data()
    if tampilkan_daftar(daftar):
        logger.tulis_log("Melihat daftar item")
    else:
        logger.tulis_log("Melihat daftar kosong")

def hapus_item_handler():
    daftar = backend.baca_data()
    if not tampilkan_daftar(daftar):
        logger.tulis_log("Mencoba hapus saat kosong")
        return
    try:
        no = int(input("Nomor item yang akan dihapus: "))
        pesan = backend.hapus_item(no)
        print(pesan)
        logger.tulis_log(f"Menghapus item nomor {no}")
    except ValueError:
        print("⚠️ Masukkan angka.")
        logger.tulis_log("Error: input hapus bukan angka")

def edit_item_handler():
    daftar = backend.baca_data()
    if not tampilkan_daftar(daftar):
        logger.tulis_log("Mencoba edit saat kosong")
        return
    try:
        no = int(input("Nomor item yang akan diedit: "))
        nama_baru = input("Nama baru: ").strip()
        if not nama_baru:
            print("⚠️ Nama baru tidak boleh kosong.")
            logger.tulis_log("Peringatan: input edit kosong")
            return
        pesan = backend.edit_item(no, nama_baru)
        print(pesan)
        logger.tulis_log(f"Edit item nomor {no} menjadi {nama_baru}")
    except ValueError:
        print("⚠️ Masukkan angka.")
        logger.tulis_log("Error: input edit bukan angka")

def cari_item_handler():
    kata = input("Masukkan kata kunci: ").strip()
    if not kata:
        print("⚠️ Kata kunci tidak boleh kosong.")
        logger.tulis_log("Peringatan: pencarian kosong")
        return
    hasil = backend.cari_item(kata)
    if not hasil:
        print("📭 Tidak ada item yang cocok.")
        logger.tulis_log(f"Pencarian '{kata}' tidak ditemukan")
    else:
        print("\n🔍 Hasil Pencarian:")
        tampilkan_daftar(hasil)
        logger.tulis_log(f"Pencarian '{kata}' menemukan {len(hasil)} item")

# ---------------- Main ----------------
def main():
    logger.tulis_log("Program dimulai")
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == '1':
            tambah_item_handler()
        elif pilihan == '2':
            lihat_item_handler()
        elif pilihan == '3':
            hapus_item_handler()
        elif pilihan == '4':
            edit_item_handler()
        elif pilihan == '5':
            cari_item_handler()
        elif pilihan == '6':
            print("👋 Sampai jumpa!")
            logger.tulis_log("Program selesai")
            break
        else:
            print("⚠️ Pilihan tidak valid.")
            logger.tulis_log(f"Pilihan tidak valid: {pilihan}")

if __name__ == "__main__":
    main()