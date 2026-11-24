import pygame


def draw_shape(surface, tool, color, start, end, width):
    x1, y1 = start
    x2, y2 = end

    left = min(x1, x2)
    top = min(y1, y2)
    shape_width = abs(x2 - x1)
    shape_height = abs(y2 - y1)

    if tool == "Line":
        pygame.draw.line(surface, color, start, end, width)

    elif tool == "Rectangle":
        if shape_width > 0 and shape_height > 0:
            pygame.draw.rect(
                surface, color,
                (left, top, shape_width, shape_height), width
            )

    elif tool == "Square":
        side = min(shape_width, shape_height)

        if x2 < x1:
            left = x1 - side
        if y2 < y1:
            top = y1 - side

        if side > 0:
            pygame.draw.rect(
                surface, color,
                (left, top, side, side), width
            )

    elif tool == "Circle":
        radius = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)

        if radius > 0:
            pygame.draw.circle(surface, color, start, radius, width)

    elif tool == "Triangle":
        points = [
            ((x1 + x2) // 2, min(y1, y2)),
            (min(x1, x2), max(y1, y2)),
            (max(x1, x2), max(y1, y2))
        ]
        pygame.draw.polygon(surface, color, points, width)

    elif tool == "Diamond":
        points = [
            ((x1 + x2) // 2, min(y1, y2)),
            (max(x1, x2), (y1 + y2) // 2),
            ((x1 + x2) // 2, max(y1, y2)),
            (min(x1, x2), (y1 + y2) // 2)
        ]
        pygame.draw.polygon(surface, color, points, width)


def flood_fill(surface, position, new_color):
    x, y = position
    width = surface.get_width()
    height = surface.get_height()

    if not (0 <= x < width and 0 <= y < height):
        return

    target_color = surface.get_at((x, y))[:3]

    if target_color == new_color:
        return

    pixels = [(x, y)]

    while pixels:
        px, py = pixels.pop()

        if surface.get_at((px, py))[:3] != target_color:
            continue

        left = px

        while left > 0 and surface.get_at((left - 1, py))[:3] == target_color:
            left -= 1

        right = left
        above = False
        below = False

        while right < width and surface.get_at((right, py))[:3] == target_color:
            surface.set_at((right, py), new_color)

            if py > 0:
                color_above = surface.get_at((right, py - 1))[:3] == target_color

                if color_above and not above:
                    pixels.append((right, py - 1))

                above = color_above

            if py < height - 1:
                color_below = surface.get_at((right, py + 1))[:3] == target_color

                if color_below and not below:
                    pixels.append((right, py + 1))

                below = color_below

            right += 1