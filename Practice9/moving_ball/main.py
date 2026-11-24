

import pygame
import sys

# Запускаем Pygame
pygame.init()

# Размеры игрового окна
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# Цвета
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
BLACK = (0, 0, 0)

# Начальные координаты мяча
ball_x = WIDTH // 2
ball_y = HEIGHT // 2

# Радиус мяча
ball_radius = 25

# Скорость движения по горизонтали и вертикали
speed_x = 5
speed_y = 4

clock = pygame.time.Clock()
running = True

# Главный игровой цикл
while running:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Изменяем координаты мяча
    ball_x += speed_x
    ball_y += speed_y

    # Проверяем столкновение с левой и правой границами
    if ball_x + ball_radius >= WIDTH or ball_x - ball_radius <= 0:
        speed_x = -speed_x

    # Проверяем столкновение с верхней и нижней границами
    if ball_y + ball_radius >= HEIGHT or ball_y - ball_radius <= 0:
        speed_y = -speed_y

    # Очищаем экран
    screen.fill(WHITE)

    # Рисуем мяч
    pygame.draw.circle(
        screen,
        BLUE,
        (ball_x, ball_y),
        ball_radius
    )

    # Обновляем экран
    pygame.display.flip()

    # Ограничиваем частоту кадров до 60
    clock.tick(60)

pygame.quit()
sys.exit()
