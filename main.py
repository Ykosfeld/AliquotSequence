import cmath
from turtle import *
from aliquot import aliquot
import numpy as np

def calc_points(n: int, radius: float) -> list[tuple[float, float]]:
    points = dict()
    theta = (2 * cmath.pi) / n
    for k in range(n+1):
        polar = cmath.rect(radius, k * theta)
        points[k] = (polar.real, polar.imag)

    return points


def gradient_colors(start_color, end_color, num_colors):
    # Converte as cores de hexadecimal para RGB
    start_rgb = [int(start_color[i:i+2], 16) / 255.0 for i in (1, 3, 5)]
    end_rgb = [int(end_color[i:i+2], 16) / 255.0 for i in (1, 3, 5)]

    # Gera os valores de RGB para o gradiente
    gradient = np.linspace(start_rgb, end_rgb, num_colors)
    
    # Converte de volta para hexadecimal
    hex_colors = ['#{:02x}{:02x}{:02x}'.format(int(r * 255), int(g * 255), int(b * 255)) for r, g, b in gradient]

    return hex_colors

# Exemplo de uso
start_color = "#00ff00"  # Vermelho
end_color = "#ff0000"    # Azul
num_colors = 10           # Número de cores no gradiente

colors = gradient_colors(start_color, end_color, 100)


points = calc_points(100, 500)

t = Turtle()
tracer(False)
# t.circle(100)

for color, n in zip(colors, range(101)):

    sequence = aliquot.aliquot_sequence_until_repeat(n)
    t.color(color)
    t.teleport(*points[n])
    for k in sequence:
        t.goto(points[k % 100])

update()
done()

