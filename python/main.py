# coding: utf-8

import sys
from enum import Enum

import placement
from furnitureList import *

import warnArea
import constants

warnAreas = []
placedFurniture = []

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

def toSwedish(word):
    for key in toEnglish:
        if toEnglish[key] == word:
            return key

# Parse input file
with open(sys.argv[1], 'r') as f:
    for line in f:
        words = line.split()
        if len(words) < 1:
            continue

        name = words[0]

        if name == "Dörr" or name == "Fönster":
            coords = list(map(int, words[1].split(',')))
            placement.addPlacedFurniture(
                    placedFurniture, 
                    (coords[0], coords[1], coords[2], coords[3], toEnglish[name]),
                    warnAreas
                )
        else:
            availableFurniture[toEnglish[name]] += 1


#Place furniture
done = False
while( not done ):
    if(availableFurniture["tv"] != 0):
        scores = placement.assessScore("tv", warnArea)

        bestSpot = scores[0]
        bestScore = scores[0][2]
        for s in scores:
            if s[2] > bestScore:
                bestScore = s[2]
                bestSpot = s

        placement.placeFurnitureInSpan("tv", [s[0], s[1]], placedFurniture)


        
        

print("Parsed input file:")
print(placedFurniture)
print(availableFurniture)

# Calculate optimal furniture placement
#placeFuncs = [placeCouchesTablesAndTv, placeDesksAndChairs, placeBeds, placeShelves, placeRugs]
#for placeFunc in placeFuncs:
#    placeFunc(availableFurniture, placedFurniture)

placement.placeFurniture(placedFurniture, availableFurniture, warnAreas);

placement.addPlacedFurniture(placedFurniture, (10,0,100,200,"bed"), warnAreas)
placement.addPlacedFurniture(placedFurniture, (200,150,250,330,"couch"), warnAreas)

# Write output files
# Write data to be displayed on web page
graphicData = open('data/furnitureData.js', 'w')
graphicData.write('furnitures = [')
isfirst = True
for furniture in placedFurniture:
    center = getCenter(furniture)
    if not isfirst:
        graphicData.write(',')
    graphicData.write('["{1}",{0[0]},{0[1]},{2}]'.format(center, getType(furniture), getAngle(furniture)))
    isfirst = False
graphicData.write('];\n')
graphicData.close()

# Write Configura data
configuraData = open('output.txt', 'w')
for furniture in placedFurniture:
    type = getType(furniture)
    if type != "door" and type != "window":
        configuraData.write("{}\t{},{},{},{}\n".format(toSwedish(type), getX1(furniture), getY1(furniture), getX2(furniture), getY2(furniture)))
configuraData.close()
