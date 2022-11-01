import cv2
import numpy as np

path1 = "Milan"  # 文件夹名
path2 = "M_fu"  # 文件名字前半部分
nums = 49  # 文件数量


sumL = []
for i in range(1, nums + 1):
    img = cv2.imread(path1 + "/" + path2 + str(i) + ".tif", -1)
    sum = 0
    for ii in img:
        for j in ii:
            if j < -10000000:
                j = 0
            else:
                sum += j
    # name = "M_fu/" + str(i)
    sumL.append(sum)

np.savetxt("result.txt", sumL)
