import requests

# Endpoint dan parameter
url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Samarinda",  # Nama kota
    "appid": "6b0023afabd6da75d4e39872b7c08cda",  # Ganti dengan API key kamu
    "units": "metric"  # Satuan suhu (Celsius)
}

# Kirim request GET
response = requests.get(url, params=params)

# Periksa status response
if response.status_code == 200:
    data = response.json()
    print(f"Cuaca di {data['name']}: {data['weather'][0]['description']}")
    print(f"Suhu: {data['main']['temp']}°C")
else:
    print(f"Error: {response.status_code}")
    print(response.text)  # Tambahkan ini untuk melihat pesan kesalahan
