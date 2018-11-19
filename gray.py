import cv2
img = cv2.imread("main.jpg")
# グレイスケールに変換
gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
xyz = cv2.cvtColor(img, cv2.COLOR_BGR2XYZ)
# ファイルに保存
cv2.imwrite("./main-gray.jpg", gry)
cv2.imwrite("./main-ycrcb.jpg", ycrcb)
cv2.imwrite("./main-hsv.jpg", hsv)
cv2.imwrite("./main-xyz.jpg", xyz)

