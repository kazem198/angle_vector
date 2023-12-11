import cv2
import math
import numpy as np

img = cv2.imread("image/images.png")
img = cv2.resize(img, (700, 700))

pointsList = []
pointAngle = []


def gradiant(pt1, pt2):
    # print(pt1)
    return (pt2[1]-pt1[1]) / (pt2[0]-pt1[0])


def angle():
    size = len(pointsList)

    if size > 2 and size % 3 == 0:
        latesPoint = pointsList[-3:]
        # ###################################################################
        # with atan

        # m1 = gradiant(latesPoint[0], latesPoint[1])
        # m2 = gradiant(latesPoint[0], latesPoint[2])

        # tan = math.atan((m2-m1)/(1+(m1*m2)))
        # print(tan)
        # angD = round(np.degrees(tan))

        ################################################################################
        # with cos
        # firstStart = latesPoint[0]
        # firstEnd = latesPoint[1]

        # secentStart = latesPoint[0]
        # secendEnd = latesPoint[2]

        # vector1 = (firstEnd[0]-firstStart[0], firstEnd[1] - firstStart[1])
        # vector2 = (secendEnd[0]-secentStart[0], secendEnd[1] - secentStart[1])
        # dotD = vector1[0]*vector2[0]+vector1[1]*vector2[1]

        # p = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2)
        # q = math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)

        # arc = dotD/(p*q)
        # radian = math.acos(arc)

        # degree = np.degrees(radian)
################################################################################################################
# with atan2

        firstStart = latesPoint[0]
        firstEnd = latesPoint[1]

        secentStart = latesPoint[0]
        secendEnd = latesPoint[2]
        vector1 = (firstEnd[0]-firstStart[0], firstEnd[1] - firstStart[1])
        vector2 = (secendEnd[0]-secentStart[0], secendEnd[1] - secentStart[1])
        angle1 = math.atan2(vector1[1], vector1[0])
        angle2 = math.atan2(vector2[1], vector2[0])
        angle = math.degrees(angle2-angle1)
        angle = (angle+360) % 360
        degree = round(angle, 0)

        cv2.putText(img, str(degree), (latesPoint[0][0]-40, latesPoint[0][1]-20), cv2.FONT_HERSHEY_COMPLEX,
                    1.5, (0, 0, 255), 2)
        print(degree)


def clickPoint(event, x, y, flags, params):

    if event == cv2.EVENT_LBUTTONDOWN:

        size = len(pointsList)
        if size % 3 == 0:
            pointAngle.append(size)

            # print(key)
        else:
            cv2.line(img, tuple(
                pointsList[pointAngle[-1]]), (x, y), (0, 0, 255), 2)
        cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
        pointsList.append([x, y])
        angle()

#     if event == cv2.EVENT_LBUTTONDOWN:
#         size = len(pointsList)

#         # print(size, size % 3 != 0)
#         if size != 0 and size % 3 != 0:
#             cv2.line(img, tuple(
#                 pointsList[round((size-1)/3)*3]), (x, y), (0, 0, 255), 2)
#         cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)

#         pointsList.append([x, y])


while True:

    cv2.imshow("img", img)
    cv2.setMouseCallback("img", clickPoint)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
