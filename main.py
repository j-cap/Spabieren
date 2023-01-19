"""
Main playground for testing the code

Author: WeberJ
Date: 2023-01-19
"""

import geopandas as gpd
import matplotlib.pyplot as plt

from io import BytesIO
from PIL import Image

import requests
import math

TILE_SIZE = 256
URL = "https://tile.openstreetmap.org/{z}/{x}/{y}.png".format

def point_to_pixels(lon, lat, zoom):
    """convert gps coordinates into web meractor pixel coordinates"""
    r = math.pow(2, zoom) * TILE_SIZE
    lat = math.radians(lat)

    x = int((lon + 180) / 360 * r)
    y = int((1 - math.log(math.tan(lat) + (1 / math.cos(lat))) / math.pi) / 2 * r)
    return x, y

def main():
    """Main function"""
    print("Hello from Spabieren!")

    zoom = 16
    x, y = point_to_pixels(-90.064279, 29.95863, zoom)    
    
    x_tiles, y_tiles = int(x / TILE_SIZE), int(y / TILE_SIZE)

    # format the url
    url = URL(z=zoom, x=x_tiles, y=y_tiles)

    # make the request
    with requests.get(url) as response:
        # response.raise_for_status()
        img = Image.open(BytesIO(response.content))

    plt.imshow(img)
    plt.show()
    # # Read the shapefile
    # # map_df = gpd.read_file("data/FMZKVERKEHR1OGDPolygon.shp")
    # map_df = gpd.read_file("data/xn604qt2854.shp")
    # # Show data format
    # map_df.head()

    # # Set image properties
    # fig, ax = plt.subplots(1, figsize=(10, 10))
    # map_df.plot(cmap='Wistia', ax=ax)
    # ax.axis('off')
    # ax.set_aspect('equal')
    # plt.show()

    return 0

if __name__ == "__main__":
    main()