# import folium
# import csv


# for s1, s2, s3, s4, s5, s6 in csv:
#    (lat, lon)= s6.split(",")
   
#    m = folium.Map(location=[lat, lon], zoom_start=13)
#    m.save("map.html")
   
#    webbrowser.open("map.html")
   
   

# # Koordinatları al
# lat = input("Enlem girin: ")
# lon = input("Boylam girin: ")

# # Haritayı oluştur
# m = folium.Map(location=[lat, lon], zoom_start=13)

# # Koordinatları pin'le
# folium.Marker(location=[lat, lon]).add_to(m)

# # Haritayı kaydet
# m.save("map.html")

# # Haritayı aç
# webbrowser.open("map.html")



import pandas as pd
import folium

# CSV dosyasını oku
df = pd.read_csv('veriler.csv')

# Harita üzerindeki başlangıç konumu, verilerin ortalaması olarak belirlenir
center_lat = df['GPS'].apply(lambda x: float(x.split(',')[0])).mean()
center_lon = df['GPS'].apply(lambda x: float(x.split(',')[1])).mean()

# Folium harita nesnesi oluştur
m = folium.Map(location=[center_lat, center_lon], zoom_start=13)

# CSV dosyasındaki her satır için bir işaretçi oluştur
for index, row in df.iterrows():
    gps = row['GPS']
    lat = float(gps.split(',')[0])
    lon = float(gps.split(',')[1])
    marker = folium.Marker([lat, lon])
    marker.add_to(m)

# Haritayı görüntüle
m
