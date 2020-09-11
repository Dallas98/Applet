import cv2
import numpy as np

# 轮廓检测时，对象必须是白色的，背景是黑色的。
img = cv2.imread(r'C:\Users\99025\Desktop\2\23.jpg.jpg',0)

thres_label = 5000
new_label = np.zeros(img.shape, np.uint8)
_, contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
n = len(contours)  # 轮廓的个数
for i in range(n):
    temp = np.zeros(img.shape, np.uint8)
    temp[img == i] = i
    for num, values in enumerate(contours):
        if cv2.contourArea(values) < thres_label:
            cv2.drawContours(temp, contours, num, 0, thickness=-1)
    new_label += temp
img1 = new_label
cv2.imwrite('005.jpg', img1)

# thres_label = 100
# new_label = np.zeros(img.shape, np.uint8)
# _, contours, _ = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# n = len(contours)  # 轮廓的个数
# for i in range(n):
#     temp = np.zeros(img.shape, np.uint8)
#     temp[img == i] = i
#     for num, values in enumerate(contours):
#         if cv2.contourArea(values) < thres_label:
#             cv2.drawContours(temp, contours, num, 0, thickness=-1)
#     new_label += temp
# img1 = new_label
# cv2.imwrite('out.jpg', img1)
# print("sss")
