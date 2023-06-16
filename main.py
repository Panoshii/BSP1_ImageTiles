import cv2
import numpy as np
import random

def shuffleimage(image):
    height, width,  = image.shape
    tile_height = height // 3
    tile_width = width // 3

    tiles = []
    for i in range(3):
        for j in range(3):
            tile = image[i * tile_height:(i + 1) * tile_height, j * tile_width:(j + 1) * tile_width]
            tiles.append(tile)

    random.shuffle(tiles)

    shuffled_image = np.vstack([np.hstack(tiles[:3]), np.hstack(tiles[3:6]), np.hstack(tiles[6:])])
    return shuffled_image


cv2.namedWindow("Shuffled Image", cv2.WINDOW_NORMAL)


cv2.namedWindow("Live Camera", cv2.WINDOW_NORMAL)


cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()


    shuffled_frame = shuffle_image(frame)


    cv2.imshow("Shuffled Image", shuffled_frame)


    cv2.imshow("Live Camera", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()