# coding: utf-8

import sys
from enum import Enum

from placement import *
from furnitureList import *

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
            coords = list(map(int, words[1].split(',')))
            placedFurniture.append((coords[0], coords[1], coords[2], coords[3], toEnglish[name]))
        else:
            availableFurniture[toEnglish[name]] += 1

print("Parsed input file:")
print(placedFurniture)
print(availableFurniture)

# Calculate optimal furniture placement
placeFuncs = [placeCouchesTablesAndTv, placeDesksAndChairs, placeBeds, placeShelves, placeRugs]
for placeFunc in placeFuncs:
    placeFunc(availableFurniture, placedFurniture)

# Write output files
# Write data to be displayed on web page
graphicData = open('data/furnitureData.js', 'w')
graphicData.write('furnitures = [')
isfirst = True
for furniture in placedFurniture:
    center = getCenter(furniture)
    if not isfirst:
        graphicData.write(',')
    graphicData.write('["{1}",{0[0]},{0[1]}]'.format(center, getType(furniture)))
    isfirst = False
graphicData.write(']\n')
