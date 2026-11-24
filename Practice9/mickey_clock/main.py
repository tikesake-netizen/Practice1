
import pygame
import math
import sys
from datetime import datetime

# Запускаем Pygame
pygame.init()

# Размеры окна
WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")

# Загружаем изображение часов
clock_image = pygame.image.load("images/clock.jpg").convert()
clock_image = pygame.transform.scale(clock_image, (400, 400))

# Определяем центр часов
center_x = WIDTH // 2
center_y = HEIGHT // 2

running = True
fps = pygame.time.Clock()

# Главный игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполняем фон
    screen.fill((240, 240, 240))

    # Отображаем изображение часов
    screen.blit(clock_image, (center_x - 200, center_y - 200))

    # Получаем текущее время
    now = datetime.now()

    seconds = now.second
    minutes = now.minute + seconds / 60
    hours = (now.hour % 12) + minutes / 60

    # Рассчитываем углы поворота стрелок
    second_angle = seconds * 6
    minute_angle = minutes * 6
    hour_angle = hours * 30

    # Функция для рисования стрелки
    def draw_hand(angle, length, color, width):
        radians = math.radians(angle - 90)

        # Вычисляем конечную точку стрелки
        end_x = center_x + length * math.cos(radians)
        end_y = center_y + length * math.sin(radians)

        pygame.draw.line(
            screen,
            color,
            (center_x, center_y),
            (end_x, end_y),
            width
        )

    # Рисуем часовую, минутную и секундную стрелки
    draw_hand(hour_angle, 90, (0, 0, 0), 8)
    draw_hand(minute_angle, 130, (0, 0, 0), 5)
    draw_hand(second_angle, 150, (255, 0, 0), 2)

    # Рисуем центральную точку часов
    pygame.draw.circle(screen, (0, 0, 0), (center_x, center_y), 7)

    # Обновляем экран
    pygame.display.flip()

    # Ограничиваем частоту кадров до 60
    fps.tick(60)

pygame.quit()
sys.exit()


