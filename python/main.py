# coding: utf-8

import sys
from enum import Enum

from placement import *

availableFurniture = {
    "bed" : 0,
    "couch" : 0,
    "desk" : 0,
    "chair" : 0,
    "tv" : 0,
    "table" : 0,
    "rug" : 0,
    "shelf" : 0
}
placedFurniture = []

toEnglish = {
    "Dörr" : "door",
    "Fönster" : "window",
    "Säng" : "bed",
    "Soffa" : "couch",
    "Skrivbord" : "desk",
    "Skrivbordsstol" : "chair",
    "Vägg-TV" : "tv",
    "Soffbord" : "table",
    "Matta" : "rug",
    "Bokhylla" : "shelf"
}

# Parse input file
with open(sys.argv[1], 'r') as f:
    for line in f:
        words = line.split()
        if len(words) < 1:
            continue

        name = words[0]

        if name == "Dörr" or name == "Fönster":
            coords = words[1].split(',')
            placedFurniture.append((coords[0], coords[1], coords[2], coords[3], toEnglish[name]))
        else:
            availableFurniture[toEnglish[name]] += 1

print("Parsed input file:")
print(placedFurniture)
print(availableFurniture)

placeFuncs = [placeDesksAndChairs, placeCouchesTablesAndTv, placeBeds, placeShelves, placeRugs]
for placeFunc in placeFuncs:
    placeFunc(availableFurniture, placedFurniture)
