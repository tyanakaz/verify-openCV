# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 漫画化フィルタ
def manga_filter(src, screen1, screen2, th1=60, th2=150):
    
    # グレースケール変換
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    screen1 = cv2.cvtColor(screen1, cv2.COLOR_BGR2GRAY)
    screen2 = cv2.cvtColor(screen2, cv2.COLOR_BGR2GRAY)

    # スクリーントーン画像を入力画像と同じ大きさにリサイズ
    screen1 = cv2.resize(screen1,(gray.shape[1],gray.shape[0]))
    screen2 = cv2.resize(screen2,(gray.shape[1],gray.shape[0]))

    # Cannyアルゴリズムで輪郭検出し、色反転
    edge = 255 - cv2.Canny(gray, 80, 120)

    # 三値化
    gray[gray <= th1] = 0
    gray[gray >= th2] = 255
    gray[ np.where((gray > th1) & (gray < th2)) ] = screen1[ np.where((gray > th1)&(gray < th2)) ]
    gray[ np.where((gray > th1) & (gray < th2)) ] = screen2[ np.where((gray > th1)&(gray < th2)) ]

    # 三値画像と輪郭画像を合成
    return cv2.bitwise_and(gray, edge)


def main():

    # 入力画像とスクリーントーン画像を取得
    img = cv2.imread("main.jpg") 
    screen1 = cv2.imread("screen.jpg")
    screen2 = cv2.imread("screen2.jpg")

    # 画像の漫画化
    manga = manga_filter(img, screen1, screen2, 60, 150)
    
    # 結果を出力
    cv2.imwrite("output.jpg", manga)


if __name__ == '__main__':
    main()