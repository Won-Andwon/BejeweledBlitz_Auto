from PIL import ImageGrab
from pymouse import PyMouse
import time


def move_mouse(o1, o2):
    mouse = PyMouse()
    mouse.click(o1[0], o1[1])
    mouse.click(o2[0], o2[1])


# 屏幕上的游戏区域位置
bbox = (523, 348, 843, 668)
time1 = time.time()
con = 1
A_image = ImageGrab.grab(bbox)

while con:
    image_slices = [A_image.crop((x * 40, y * 40, (x + 1) * 40, (y + 1) * 40)) for x in range(8) for y in range(8)]

    color_slices = []
    x = 0
    for i in image_slices:
        validcount = 1
        validcolor = [0, 0, 0]
        for count, color in i.getcolors(1600):
            if color[0] < 50 and color[1] < 50 and color[2] < 50:
                continue
            validcount += count
            for each in range(3):
                validcolor[each] += (count * color[each])

        validcolor = [validcolor[i] / validcount for i in range(3)]

        if 190 < validcolor[0] < 220 and 15 < validcolor[1] < 25 and 35 < validcolor[2] < 45:
            color_slices.append("red")
        elif 180 < validcolor[0] < 205 and 185 < validcolor[1] < 205 and 185 < validcolor[2] < 205:
            color_slices.append("white")
        elif 205 < validcolor[0] < 230 and 110 < validcolor[1] < 125 and 35 < validcolor[2] < 45:
            color_slices.append("orange")
        elif 215 < validcolor[0] < 235 and 185 < validcolor[1] < 200 and 20 < validcolor[2] < 30:
            color_slices.append("yellow")
        elif 25 < validcolor[0] < 35 and 185 < validcolor[1] < 210 and 55 < validcolor[2] < 65:
            color_slices.append("green")
        elif 10 < validcolor[0] < 20 and 115 < validcolor[1] < 125 and 200 < validcolor[2] < 220:
            color_slices.append("blue")
        elif 180 < validcolor[0] < 200 and 20 < validcolor[1] < 30 and 170 < validcolor[2] < 200:
            color_slices.append("purple")
        else:
            color_slices.append("other")
        x += 1


    def judge_three(p1, p2, p3):
        # 判界
        if p1[0] < 0 or p1[1] < 0 \
                or p2[0] < 0 or p2[1] < 0 \
                or p3[0] < 0 or p3[1] < 0 \
                or p1[0] > 7 or p1[1] > 7 \
                or p2[0] > 7 or p2[1] > 7 \
                or p3[0] > 7 or p3[1] > 7:
            return 0
        if color_slices[p1[0] + p1[1] * 8] == "other" \
                or color_slices[p2[0] + p2[1] * 8] == "other" \
                or color_slices[p3[0] + p3[1] * 8] == "other":
            return 0
        if color_slices[p1[0] + p1[1] * 8] == color_slices[p3[0] + p3[1] * 8] == color_slices[p2[0] + p2[1] * 8]:
            return 1
        else:
            return 0

    for i in range(8):
        for j in range(8):
            # 坐标换算方式 i+j*8
            # 尝试向上交换
            if judge_three((i - 3, j), (i - 2, j), (i, j)) or \
                    judge_three((i - 1, j - 2), (i - 1, j - 1), (i, j)) or \
                    judge_three((i - 1, j - 1), (i - 1, j + 1), (i, j)) or \
                    judge_three((i - 1, j + 1), (i - 1, j + 2), (i, j)) or \
                    judge_three((i, j - 2), (i, j - 1), (i - 1, j)) or \
                    judge_three((i, j - 1), (i, j + 1), (i - 1, j)) or \
                    judge_three((i, j + 1), (i, j + 2), (i - 1, j)) or \
                    judge_three((i + 2, j), (i + 1, j), (i - 1, j)):
                # print((i, j), (i - 1, j))
                o1 = (bbox[0] + 40 * j + 20, bbox[1] + 40 * i + 20)
                o2 = (bbox[0] + 40 * j + 20, bbox[1] + 40 * (i - 1) + 20)
                move_mouse(o1, o2)
                time.sleep(0.1)

                continue
            # 尝试向左交换
            if judge_three((i, j - 3), (i, j - 2), (i, j)) or \
                    judge_three((i - 2, j - 1), (i - 1, j - 1), (i, j)) or \
                    judge_three((i - 1, j - 1), (i + 1, j - 1), (i, j)) or \
                    judge_three((i + 1, j - 1), (i + 2, j - 1), (i, j)) or \
                    judge_three((i - 2, j), (i - 1, j), (i, j - 1)) or \
                    judge_three((i - 1, j), (i + 1, j), (i, j - 1)) or \
                    judge_three((i + 1, j), (i + 2, j), (i, j - 1)) or \
                    judge_three((i, j + 2), (i, j + 1), (i, j - 1)):
                # print((i, j), (i, j - 1))
                o1 = (bbox[0] + 40 * j + 20, bbox[1] + 40 * i + 20)
                o2 = (bbox[0] + 40 * (j - 1) + 20, bbox[1] + 40 * i + 20)
                move_mouse(o1, o2)
                time.sleep(0.1)

                continue
    A_image = ImageGrab.grab(bbox)

    time2 = time.time()
    if (time2 - time1) > 70:
        con = 0
