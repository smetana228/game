from un import *

text_map = [
    'WWWWWWWWWWWWWW',
    'W............W',
    'W...WWWWW....W',
    'W...W........W',
    'W...W........W',
    'W...W...W....W',
    'W.......W....W',
    'W.......W....W',
    'W...WWWWW....W',
    'W............W',
    'WWWWWWWWWWWWWW'
]

world_map = set()
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i*TILE, j*TILE))
