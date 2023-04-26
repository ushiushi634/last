import cv2
import numpy as np

# FLDテスト処理
# fileImage : 画像ファイルパス
#
def testFastLineDetector(IMG_5742):
    colorimg = cv2.imread(IMG_5742.jpg, cv2.IMREAD_COLOR)
    if colorimg is None:
        return -1
    image = cv2.cvtColor(colorimg.copy(), cv2.COLOR_BGR2GRAY)

    # FLDインスタンス生成
    length_threshold = 4 # 10
    distance_threshold = 1.41421356
    canny_th1 = 50.0
    canny_th2 = 50.0
    canny_aperture_size = 3
    do_merge = False

    # 高速ライン検出器生成
    fld = cv2.ximgproc.createFastLineDetector(length_threshold,distance_threshold,
                    canny_th1,canny_th2,canny_aperture_size,do_merge)
    #fld = cv2.createLineSegmentDetector(cv2.LSD_REFINE_STD) # LSD

    # ライン取得
    lines = fld.detect(image)
    #lines, width, prec, nfa = fld.detect(image) # LSD

    # 検出線表示
    drawnLines = np.zeros((image.shape[0],image.shape[1],3), np.uint8)
    fld.drawSegments(drawnLines, lines)
    cv2.imshow("Fast Line Detector(LINE)", drawnLines)

    # 検出線と処理画像の合成表示
    fld.drawSegments(colorimg, lines)
    cv2.imshow("Fast Line Detector", colorimg)
    cv2.waitKey()
    return 0
