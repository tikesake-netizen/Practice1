
import pygame
import os
import sys

# Запускаем Pygame и аудиомодуль
pygame.init()
pygame.mixer.init()

# Размеры окна
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

# Цвета
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GREEN = (50, 200, 100)
GRAY = (100, 100, 100)

# Шрифты
font = pygame.font.SysFont("Arial", 28)
small_font = pygame.font.SysFont("Arial", 18)

# Папка с музыкальными файлами
music_folder = "music"

# Получаем список музыкальных файлов
songs = [
    file for file in os.listdir(music_folder)
    if file.endswith((".mp3", ".wav", ".ogg"))
]

# Начальные настройки плеера
current_song = 0
is_paused = False
volume = 0.5

pygame.mixer.music.set_volume(volume)


# Функция запуска музыки
def play_song():
    global is_paused

    if songs:
        path = os.path.join(music_folder, songs[current_song])
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        is_paused = False


# Функция остановки музыки
def stop_song():
    global is_paused
    pygame.mixer.music.stop()
    is_paused = False


# Функция переключения на следующий трек
def next_song():
    global current_song
    if songs:
        current_song = (current_song + 1) % len(songs)
        play_song()


# Функция переключения на предыдущий трек
def previous_song():
    global current_song
    if songs:
        current_song = (current_song - 1) % len(songs)
        play_song()


running = True
clock = pygame.time.Clock()

# Главный цикл программы
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обрабатываем нажатия клавиш
        if event.type == pygame.KEYDOWN:

            # Воспроизведение и пауза
            if event.key == pygame.K_SPACE:
                if songs:
                    if pygame.mixer.music.get_busy() and not is_paused:
                        pygame.mixer.music.pause()
                        is_paused = True
                    elif is_paused:
                        pygame.mixer.music.unpause()
                        is_paused = False
                    else:
                        play_song()

            # Остановка музыки
            elif event.key == pygame.K_s:
                stop_song()

            # Следующий трек
            elif event.key == pygame.K_RIGHT:
                next_song()

            # Предыдущий трек
            elif event.key == pygame.K_LEFT:
                previous_song()

            # Увеличение громкости
            elif event.key == pygame.K_UP:
                volume = min(1.0, volume + 0.1)
                pygame.mixer.music.set_volume(volume)

            # Уменьшение громкости
            elif event.key == pygame.K_DOWN:
                volume = max(0.0, volume - 0.1)
                pygame.mixer.music.set_volume(volume)

    # Очищаем экран
    screen.fill(BLACK)

    # Показываем название плеера
    title = font.render("MUSIC PLAYER", True, GREEN)
    screen.blit(title, (190, 40))

    # Показываем название текущей песни
    if songs:
        song_text = small_font.render(
            "Song: " + songs[current_song], True, WHITE
        )
    else:
        song_text = small_font.render(
            "Музыкальные файлы не найдены", True, WHITE
        )

    screen.blit(song_text, (40, 120))

    # Показываем уровень громкости
    volume_text = small_font.render(
        f"Volume: {int(volume * 100)}%", True, WHITE
    )
    screen.blit(volume_text, (40, 170))

    # Показываем управление клавиатурой
    controls = [
        "SPACE - Play / Pause",
        "S - Stop",
        "LEFT - Previous song",
        "RIGHT - Next song",
        "UP / DOWN - Volume"
    ]

    for i, text in enumerate(controls):
        line = small_font.render(text, True, GRAY)
        screen.blit(line, (40, 220 + i * 30))

    # Обновляем экран
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()

