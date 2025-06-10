import drawsvg as draw
import random


def generate_svg():
    svg_width = 1012
    svg_height = 350
    num_vert_rectangles = 500
    num_stops = 10
    d = draw.Drawing(svg_width, svg_height, origin="top-left")

    for i in range(num_vert_rectangles):
        g = draw.LinearGradient(0.5, 0, 0.5, svg_height)
        for j in range(num_stops):
            color = "black" if random.randint(0, 1) == 1 else "transparent"
            offset = j / (num_stops - 1)
            s = g.add_stop(
                offset,
                color,
                1,
            )
            values = f"{offset};{offset + offset};{0};{offset}"
            dur = f"{random.uniform(10, 30)}s"
            s.append_anim(
                draw.Animate(
                    "offset",
                    dur,
                    values,
                    repeatCount="indefinite",
                )
            )

        x = i * svg_width // num_vert_rectangles
        y = 0
        xw = svg_width // num_vert_rectangles
        rect = draw.Rectangle(x, y, xw, svg_height, fill=g)
        d.append(rect)

    d.save_svg("gr.svg")


if __name__ == "__main__":
    generate_svg()
    print("SVG file created")
