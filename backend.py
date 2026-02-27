import database  # Wajib ada agar backend bisa akses database

def tambah_item(nama):
    # Gunakan database.baca_data() bukan baca_data() saja
    daftar = database.baca_data() 
    daftar.append(nama)
    database.tulis_data(daftar)
    return f"✅ '{nama}' berhasil ditambahkan."

def semua_item():
    return database.baca_data()

def hapus_item(no):
    daftar = database.baca_data()
    if 1 <= no <= len(daftar):
        item = daftar.pop(no - 1)
        database.tulis_data(daftar)
        return f"❌ '{item}' dihapus."
    else:
        return "⚠️ Nomor tidak valid."
        
def edit_item(no, nama_baru):
    """Mengedit item pada nomor urut tertentu."""
    daftar = database.baca_data()
    if 1 <= no <= len(daftar):
        item_lama = daftar[no - 1]
        daftar[no - 1] = nama_baru
        database.tulis_data(daftar)
        return f" '{item_lama}' di ubah menjadi '{nama_baru}'"
    else:
        return " Nomor tidak valid."
        
def cari_item(kata_kunci):
    
    """mengembalikan daftar item yang mengandung kata kunci"""
    daftar = database.baca_data()
    hasil = [item for item in daftar if kata_kunci.lower()in item.lower()]
    return hasil