from graph import *
import math

windowSize(455, 300)
brushColor("#9febf5")
rectangle(0, 0, 455, 300)

penColor("#059420")
rectangle(455, 300, 0, 150)

brushColor("#059420")
rectangle(0, 150, 455, 300)

brushColor("#946b06")
penColor("#084e0d")
rectangle(69, 202, 185, 126)

penColor("#a36821")
brushColor("#059492")
rectangle(109, 178, 144, 150)

penColor("#000000")
brushColor("#ec2b42")
p =  [[69, 125], [126, 68], [184, 125]]
polygon(p)

brushColor("#000000")
rectangle(328, 189, 338, 137)

brushColor("#065206")
penColor("#022b02")
circle(336, 80, 19)
circle(314, 100, 19)
circle(359, 100, 19)
circle(336, 113, 19)
circle(316, 125, 19)
circle(351, 125, 19)

penColor("black")
brushColor("white")
circle(224, 54, 19)
circle(243, 54, 19)
circle(263, 54, 19)
circle(286, 54, 19)
circle(265, 38, 19)
circle(243, 38, 19)

penColor("pink")
brushColor("pink")
a = []
for i in range(20):
    a.append((395 + 21 * math.sin(math.pi / 10 * i),
              46 + 21 * math.cos(math.pi / 10 * i)))
    a.append((395 + 23 * math.sin(math.pi / 10 * i + math.pi / 20),
              46 + 23 * math.cos(math.pi / 10 * i + math.pi / 20)))
polygon(a)

run()
