# 说明

## 成绩
    无道具，平均800M；最好可过1M，最差会陷入死循环（运行70s后固定跳出）
    死循环原因： 过快，导致同时移动两个能拼成3个一列（一行）也会被计入，实际上不会消除，就会不停地连动这两个

## 局限性
    因为识别颜色是固定范围，所以最好调低效果，否则快速消除期间以及各种特殊宝石会使得识别率下降。
    最好可以加些手动，防止死循环。
    不会自动吃加倍
    记得全屏 或者给定游戏区域（左上右下的像素坐标）哦 否则会乱点
