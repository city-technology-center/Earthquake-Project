import folium
import csv
import numpy as np
import pandas as pd

# CSV dosyasını aç

df= pd.read_csv("test.csv", sep=";")
print(df)

latitude = df['Latitude']
longitude = df['Longitude']

latitude = list(latitude)
longitude = list(longitude)

m = folium.Map(location=[float(latitude[0]),float(longitude[0])], zoom_start=12)

print("-----------------")
for i in range(len(latitude)):
    # print(i)
    # print(len(longitude))
    print("Lat: {}, Long {}".format(latitude[i],longitude[i]))
    print("---------")
    
    # m = folium.Map(location=[float(latitude[i]),float(longitude[i])], zoom_start=12)

    folium.Marker(location=[latitude[i], longitude[i]], popup="Latitude: {} <br> Longitude: {}".format(latitude[i], longitude[i])).add_to(m)


# folium.Marker(location=[latitude[0], longitude[0]], popup="Latitude: {} <br> Longitude: {}".format(latitude[0], longitude[0])).add_to(m)

m.save("harita.html")
