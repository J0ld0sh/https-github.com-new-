from graph import *
import math

windowSize(700, 450)
canvasSize(700, 450)
penColor("#9febf5")
brushColor("#9febf5")
rectangle(0, 0, 700, 225)
penColor("#059420")
brushColor("#059420")
rectangle(0, 225, 700, 450)

brushColor("#946b06")
penColor("#084e0d")
rectangle(75, 360, 245, 245)
penColor("#a36821")
brushColor("#059492")
rectangle(130, 325, 185, 280)
penColor("#000000")
brushColor("#ec2b42")
p = [(75, 245), (155, 160), (245, 245)]
polygon(p)

brushColor("#946b06")
penColor("#084e0d")
rectangle(400, 310, 510, 240)
penColor("#a36821")
brushColor("#059492")
rectangle(440, 290, 470, 260)
penColor("#000000")
brushColor("#ec2b42")
p = [(400, 240), (455, 185), (510, 240)]
polygon(p)

brushColor("#000000")
rectangle(300, 270, 320, 350)
brushColor("#065206")
penColor("#022b02")
circle(310, 180, 30)
circle(280, 210, 30)
circle(350, 210, 30)
circle(310, 230, 30)
circle(285, 250, 30)
circle(340, 260, 30)

brushColor("#000000")
rectangle(550, 245, 565, 305)
brushColor("#065206")
penColor("#022b02")
circle(560, 185, 20)
circle(535, 205, 20)
circle(585, 205, 20)
circle(560, 220, 20)
circle(540, 235, 20)
circle(580, 240, 20)

penColor("black")
brushColor("white")
circle(130, 75, 25)
circle(157, 75, 25)
circle(183, 75, 25)
circle(210, 75, 25)
circle(188, 55, 25)
circle(155, 55, 25)

circle(350, 105, 20)
circle(370, 105, 20)
circle(390, 105, 20)
circle(410, 105, 20)
circle(390, 90, 20)
circle(370, 90, 20)

circle(560, 95, 25)
circle(587, 95, 25)
circle(613, 95, 25)
circle(640, 95, 25)
circle(618, 75, 25)
circle(585, 75, 25)

penColor("#74777b")
brushColor("pink")
a = []
for i in range(20):
    a.append((50 + 30 * math.sin(math.pi / 10 * i),
              45 + 30 * math.cos(math.pi / 10 * i)))
    a.append((50 + 35 * math.sin(math.pi / 10 * i + math.pi / 20),
              45 + 35 * math.cos(math.pi / 10 * i + math.pi / 20)))
polygon(a)

run()
