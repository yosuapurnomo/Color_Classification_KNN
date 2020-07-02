import cv2 as cv
import sys
import keyboard
import Kmean

Cropp_Img = False
ix, iy, ix_end, iy_end = 0, 0, 0, 0

def Mouse_Crop(event, x, y, flags, param):
    global ix, iy, ix_end, iy_end, Cropp_Img

    if event == cv.EVENT_LBUTTONDOWN:
        print("cv.EVENT_LBUTTONDOWN")
        ix, iy, ix_end, iy_end = x, y, x, y
        Cropp_Img = True
        print("ix = ", ix, "iy = ", iy, "\nix_end = ", ix_end, "iy_end = ", iy_end)

    elif event == cv.EVENT_MOUSEMOVE:
        # print("cv.EVENT_MOUSEMOVE")
        if Cropp_Img == True:
            ix_end, iy_end = x, y

    elif event == cv.EVENT_LBUTTONUP:
        print("cv.EVENT_LBUTTONUP")
        ix_end, iy_end = x, y
        Cropp_Img = False
        print("ix = ", ix, "iy = ", iy, "\nix_end = ", ix_end, "iy_end = ", iy_end)
        refPoint = [(ix, iy), (ix_end, iy_end)]

        if len(refPoint) == 2:
            img2 = img[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            clear = cv.fastNlMeansDenoisingColored(img2)

            show_clear = cv
            show_clear.imshow("Image Clear ", clear)
            show_clear.moveWindow("Image Clear", 100, 500)
            # print("Image Clear = \n", clear)
            c1 = int(cv.mean(clear)[0])
            c2 = int(cv.mean(clear)[1])
            c3 = int(cv.mean(clear)[2])
            # print(cv.mean(clear))
            print("\nMean 1 = \n", c1)
            print("\nMean 2 = \n", c2)
            print("\nMean 3 = \n", c3)

            final = Kmean.kmean(c3, c2, c1)
            print(f"RGB {c3, c2, c1} Termasuk dalam Kategori Warna : ", final.check())


img = cv.imread('img/View.jpg')
img_copy = img.copy()

cv.namedWindow("image")
cv.setMouseCallback("image", Mouse_Crop)

while True:
    i = img.copy()

    if not Cropp_Img:
        cv.imshow("image", img)

    elif Cropp_Img:
        cv.rectangle(i, (ix, iy), (ix_end, iy_end), (255, 0, 0), 2)
        cv.imshow("image", i)

    if keyboard.is_pressed('Esc'):
        print("Exit")
        sys.exit(0)
    cv.waitKey(1)

cv2.destroyAllWindows()

