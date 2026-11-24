import pygame
import sys
import os
from datetime import datetime
from tools import draw_shape, flood_fill

pygame.init()

WIDTH = 1000
HEIGHT = 700
TOOLBAR_HEIGHT = 130

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

font = pygame.font.SysFont("Arial", 20)
small_font = pygame.font.SysFont("Arial", 16)

canvas = pygame.Surface((WIDTH, HEIGHT - TOOLBAR_HEIGHT))
canvas.fill(WHITE)

colors = [BLACK, RED, GREEN, BLUE, YELLOW]
selected_color = BLACK

tools = [
    "Pencil",
    "Line",
    "Rectangle",
    "Circle",
    "Square",
    "Triangle",
    "Diamond",
    "Eraser",
    "Fill",
    "Text"
]

selected_tool = "Pencil"

brush_sizes = [2, 5, 10]
brush_size = 5

drawing = False
last_pos = None
start_pos = None
preview_pos = None

text_active = False
text_input = ""
text_position = None

status_message = ""
status_time = 0

clock = pygame.time.Clock()
running = True


def draw_text(text, x, y, color=BLACK):
    surface = small_font.render(text, True, color)
    screen.blit(surface, (x, y))


def save_canvas():
    global status_message, status_time

    folder = os.path.dirname(os.path.abspath(__file__))
    filename = datetime.now().strftime("painting_%Y%m%d_%H%M%S_%f.png")
    filepath = os.path.join(folder, filename)

    try:
        pygame.image.save(canvas, filepath)

        status_message = "Saved: " + filename
        print("Canvas saved successfully!")
        print("File location:", filepath)

    except (pygame.error, OSError) as error:
        status_message = "Save error: " + str(error)
        print("Save error:", error)

    status_time = pygame.time.get_ticks()


while running:
    screen.fill(GRAY)
    screen.blit(canvas, (0, TOOLBAR_HEIGHT))

    pygame.draw.rect(
        screen, (180, 180, 180),
        (0, 0, WIDTH, TOOLBAR_HEIGHT)
    )

    for i, tool in enumerate(tools):
        x = 5 + i * 98
        button = pygame.Rect(x, 10, 93, 35)

        button_color = BLUE if selected_tool == tool else WHITE
        pygame.draw.rect(screen, button_color, button)
        pygame.draw.rect(screen, BLACK, button, 2)

        label = small_font.render(tool, True, BLACK)
        screen.blit(label, (x + 5, 18))

    for i, color in enumerate(colors):
        x = 15 + i * 50
        pygame.draw.rect(screen, color, (x, 60, 35, 30))

        if color == selected_color:
            pygame.draw.rect(screen, BLACK, (x, 60, 35, 30), 3)

    draw_text("Brush size:", 300, 65)

    for i, size in enumerate(brush_sizes):
        x = 400 + i * 55
        button = pygame.Rect(x, 60, 45, 30)

        button_color = BLUE if brush_size == size else WHITE
        pygame.draw.rect(screen, button_color, button)
        pygame.draw.rect(screen, BLACK, button, 2)

        label = small_font.render(str(size), True, BLACK)
        screen.blit(label, (x + 15, 67))

    draw_text("1 = 2px | 2 = 5px | 3 = 10px | Ctrl+S = Save", 600, 65)

    if status_message and pygame.time.get_ticks() - status_time < 4000:
        draw_text(status_message, 15, 105, GREEN)

    if drawing and start_pos and preview_pos:
        if selected_tool not in ["Pencil", "Eraser"]:
            preview_canvas = canvas.copy()

            draw_shape(
                preview_canvas,
                selected_tool,
                selected_color,
                start_pos,
                preview_pos,
                brush_size
            )

            screen.blit(preview_canvas, (0, TOOLBAR_HEIGHT))

    if text_active and text_position:
        preview = font.render(text_input + "|", True, selected_color)
        screen.blit(
            preview,
            (text_position[0], text_position[1] + TOOLBAR_HEIGHT)
        )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if text_active:
                if event.key == pygame.K_RETURN:
                    text_surface = font.render(text_input, True, selected_color)
                    canvas.blit(text_surface, text_position)

                    text_active = False
                    text_input = ""
                    text_position = None

                elif event.key == pygame.K_ESCAPE:
                    text_active = False
                    text_input = ""
                    text_position = None

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]

                elif event.unicode.isprintable():
                    text_input += event.unicode

            else:
                if event.key == pygame.K_1:
                    brush_size = 2

                elif event.key == pygame.K_2:
                    brush_size = 5

                elif event.key == pygame.K_3:
                    brush_size = 10

                elif event.key == pygame.K_s and event.mod & pygame.KMOD_CTRL:
                    save_canvas()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos

            if mouse_y < TOOLBAR_HEIGHT:
                for i, tool in enumerate(tools):
                    x = 5 + i * 98
                    button = pygame.Rect(x, 10, 93, 35)

                    if button.collidepoint(event.pos):
                        selected_tool = tool

                for i, color in enumerate(colors):
                    x = 15 + i * 50

                    if pygame.Rect(x, 60, 35, 30).collidepoint(event.pos):
                        selected_color = color

                for i, size in enumerate(brush_sizes):
                    x = 400 + i * 55
                    button = pygame.Rect(x, 60, 45, 30)

                    if button.collidepoint(event.pos):
                        brush_size = size

            else:
                canvas_pos = (
                    mouse_x,
                    mouse_y - TOOLBAR_HEIGHT
                )

                if selected_tool == "Fill":
                    flood_fill(canvas, canvas_pos, selected_color)

                elif selected_tool == "Text":
                    text_active = True
                    text_input = ""
                    text_position = canvas_pos

                elif selected_tool in ["Pencil", "Eraser"]:
                    drawing = True
                    last_pos = canvas_pos

                    draw_color = WHITE if selected_tool == "Eraser" else selected_color

                    pygame.draw.circle(
                        canvas,
                        draw_color,
                        canvas_pos,
                        max(1, brush_size // 2)
                    )

                else:
                    drawing = True
                    start_pos = canvas_pos
                    preview_pos = canvas_pos

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                current_pos = (
                    event.pos[0],
                    event.pos[1] - TOOLBAR_HEIGHT
                )

                if 0 <= current_pos[1] < canvas.get_height():
                    if selected_tool in ["Pencil", "Eraser"]:
                        draw_color = WHITE if selected_tool == "Eraser" else selected_color

                        pygame.draw.line(
                            canvas, draw_color,
                            last_pos, current_pos, brush_size
                        )

                        pygame.draw.circle(
                            canvas, draw_color,
                            current_pos, max(1, brush_size // 2)
                        )

                        last_pos = current_pos

                    else:
                        preview_pos = current_pos

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if drawing:
                if selected_tool not in ["Pencil", "Eraser"]:
                    end_pos = (
                        event.pos[0],
                        event.pos[1] - TOOLBAR_HEIGHT
                    )

                    if 0 <= end_pos[1] < canvas.get_height():
                        draw_shape(
                            canvas,
                            selected_tool,
                            selected_color,
                            start_pos,
                            end_pos,
                            brush_size
                        )

                drawing = False
                last_pos = None
                start_pos = None
                preview_pos = None

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()