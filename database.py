import json
import os

FILE_DATA = "data_belanja.json"

def baca_data():
    try:
        if os.path.exists(FILE_DATA):
            with open(FILE_DATA, "r") as file:
                return json.load(file)
        return[] 
    except json.J50NDecodeError:
        print(" File data rusak. Membuat file baru")
        return[]
    except Exception as e:
        print(f" Error tak terduga saat membaca: {e}")
        return[]

def tulis_data(data):
    try:
        with open(FILE_DATA, "w") as file:
             json.dump(data, file, indent=4)
    except Exception as e:
        print(f" Gagal menyimpan data: {e}")