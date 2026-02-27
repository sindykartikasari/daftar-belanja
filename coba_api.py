import urllib.request
import json

urls = [
    "http://api.open-notify.org/astros.json",
    "http://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts"
]

for url in urls:
    try:
        print(f"Mencoba {url}...")
        response = urllib.request.urlopen(url, timeout=5)
        data_json = response.read().decode('utf-8')
        data= json.loads(data_json)
        print("✅ Berhasill\n")

        # Tampilkan data sesuai URL
        if "astros" in url:
            print(f"Astronaut di ISS: {data['number']} orang")
            for astronaut in data['people']:
                print(f" - {astronaut['name']}")
        elif "httpbin" in url:
            print(f"Origin IP: {data['origin']}")

        elif "jsonplaceholder" in url:
            print("Contoh judul:", data[0]["title"])
        break  # Keluar dari loop jika berhasil
    except Exception as e:
        print(f"Gagal: {e}\n")

else:
    # Jika semua URL gagal
    print("❌ Semua URL gagal. Gunakan data lokal.")
    data = [{"title": "Belajar API"}, {"title": "Error Handling"}, {"title": "Logging"}]
    print("\nData lokal:")
    for i, post in enumerate(data, start=1):
        print(f"{i}. {post['title']}")
            