import cv2

def callback(pos):
    pass  # 您可以在这里添加滑块位置改变时需要执行的代码

cv2.namedWindow('color', cv2.WINDOW_NORMAL)

img = cv2.imread(r'C:\Users\19368\Desktop\13901631_1347858735837.jpg')
colorspaces = [cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2GRAY,
               cv2.COLOR_RGB2GRAY, cv2.COLOR_RGB2HSV_FULL,
               cv2.COLOR_BGR2YUV]
cv2.createTrackbar('curcolor', 'color', 0, len(colorspaces) - 1, callback)  # 注意这里的len(colorspaces) - 1
while True:
    index = cv2.getTrackbarPos('curcolor', 'color')

    # 颜色空间转换API
    cvt_img = cv2.cvtColor(img, colorspaces[index])
    cv2.imshow('color', cvt_img)  # 这里应该显示转换后的图像
    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()