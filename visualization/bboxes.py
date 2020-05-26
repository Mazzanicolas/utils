import numpy as np
import cv2 as cv

def bbox(image, points, ptype='corners', border_alpha=0.8, fill_alpha=0.2,
         fill=False, background_color=(0,0,255), border_color=(50,225,50),
         border_thickness=5):
    overlay, original = image.copy(), image.copy()
    if ptype=='corners':
        vertex_1, vertex_2 = points
        if fill:
            filled = cv.rectangle(overlay, vertex_1, vertex_2, background_color, -1)
            overlay = cv.addWeighted(overlay, fill_alpha, original, 1-fill_alpha, 0, original)
        cv.rectangle(overlay, vertex_1, vertex_2, border_color, border_thickness)
    else:
        raise NotImplementedError
    image = cv.addWeighted(overlay, border_alpha, image, 1-border_alpha, 0, image)
    return image

if __name__ == '__main__':
    img = cv.imread('../../Downloads/image-3.jpg')
    image = bbox(img, [(900,500),(1500,700)], fill=True)
    cv.imshow('bbox', image)
    cv.waitKey()

    img = cv.imread('../../Downloads/1589639098952.jpg')
    image = bbox(img, [(900,500),(1500,700)], fill=True)
    cv.imshow('bbox', image)
    cv.waitKey()