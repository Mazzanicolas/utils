import numpy as np


def split_tiles(image, height, width, overflow=''):
    h, w = image.shape[:2]
    tiles = np.array(
        [
            image[x:x+height, y:y+width]
            for x in range(0, h, height)
            for y in range(0, w, width)
        ]
    )
    return tiles

def merge_tiles(tiles, rows):
    rows = [
        np.hstack(row)
        for row in np.array_split(tiles, rows)   
    ]
    return np.vstack(rows)

if __name__=='__main__':
    import cv2 as cv

    img = cv.imread('/home/nmazza/Downloads/1589857482677.jpg')
    cv.imshow('img', img)
    cv.waitKey()
    tiles = split_tiles(img, 256, 256)
    # for tile in tiles:
    #     print(tile.shape)
    #     cv.imshow('tile',tile)
    #     cv.waitKey()
    image = merge_tiles(tiles, 4)
    cv.imshow('image', image)
    cv.waitKey()