import cv2

vc = cv2.VideoCapture(r'F:\master1\数学建模\2017D\附件2-典型视频\附件2-典型视频\不带晃动-动态背景\waterSurface\input\input.avi')  # 读入视频文件，命名cv
n = 1  # 计数

if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
else:
    rval = False

timeF = 1  # 视频帧计数间隔频率

i = 0
while rval:  # 循环读取视频帧
    rval, frame = vc.read()
    if (n % timeF == 0):  # 每隔timeF帧进行存储操作
        i += 1
        print(i)
        cv2.imshow("", frame)
        cv2.waitKey(200)
        cv2.imwrite(r'C:\Users\99025\Desktop\1/{}.jpg'.format(i), frame)  # 存储为图像
    n = n + 1
    cv2.waitKey(1)
vc.release()
