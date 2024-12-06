import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread(r"C:\Users\19368\Desktop\opencv_tutorial\opencv_logo.jpg")

cv2.imshow('img', img)
cv2.waitKey(0)
# if(key == ord('q')):
#     exit()
cv2.destroyAllWindows()
