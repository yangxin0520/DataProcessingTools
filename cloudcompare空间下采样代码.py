# cloudcompare空间下采样
import numpy as np
from math import sqrt, pow


def subSample(initData):
    initData = initData.tolist()
    ptsHold = []
    for i in range(len(initData)):
        if len(ptsHold) == 0:
            ptsHold.append(initData[i])
        else:
            flag = False
            for bjpt in ptsHold:
                L = sqrt(pow(initData[i][0] - bjpt[0], 2) + pow(initData[i][1] - bjpt[1], 2))
                if L < 0.005:
                    flag = True
                    break
                else:
                    continue
            if flag == True:
                continue
            ptsHold.append(initData[i])

    return ptsHold


if __name__ == "__main__":
    path = "File/Laplace/save5.txt"
    path1 = "File/Laplace/save6.txt"
    initData = np.loadtxt(path)
    initData1 = np.loadtxt(path1)
    initData2 = subSample(initData)
