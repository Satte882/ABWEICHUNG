#!/usr/bin/env python3
from pathlib import Path
import argparse
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import black, white
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth

TRIM_W = 5.06
TRIM_H = 7.81
BLEED = 0.125
SPINE_FACTORS = {"white": 0.002252, "cream": 0.0025}


def find_font(candidates):
    for item in candidates:
        if Path(item).exists():
            return item
    raise FileNotFoundError(f"No usable font found: {candidates}")


def build(output: Path, pages: int, paper: str):
    spine = pages * SPINE_FACTORS[paper]
    cover_w = BLEED + TRIM_W + spine + TRIM_W + BLEED
    cover_h = BLEED + TRIM_H + BLEED
    w, h = cover_w * inch, cover_h * inch

    bold = find_font([
        "/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
    ])
    regular = find_font([
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ])
    pdfmetrics.registerFont(TTFont("CoverTitle", bold))
    pdfmetrics.registerFont(TTFont("CoverSub", regular))

    spine_left = (BLEED + TRIM_W) * inch
    spine_right = (BLEED + TRIM_W + spine) * inch
    front_trim_right = (BLEED + TRIM_W + spine + TRIM_W) * inch
    front_center = (spine_right + front_trim_right) / 2

    c = canvas.Canvas(
        str(output),
        pagesize=(w, h),
        pageCompression=1,
        initialFontName="CoverTitle",
        initialFontSize=10,
    )
    c.setTitle("ABWEICHUNG - KDP Paperback Cover")
    c.setSubject(
        f"5.06 x 7.81 in; {pages} pages; B/W {paper} paper; "
        f"{cover_w:.6f} x {cover_h:.3f} in"
    )
    c.setFillColor(white)
    c.rect(0, 0, w, h, fill=1, stroke=0)
    c.setFillColor(black)
    c.setStrokeColor(black)
    c.setLineWidth(1.2)

    base_y = h * 0.515

    def heartbeat(cx, cy):
        points = [
            (-0.23, 0.00),
            (-0.14, 0.00),
            (-0.105, 0.045),
            (-0.065, -0.070),
            (0.000, 0.310),
            (0.060, -0.205),
            (0.105, 0.060),
            (0.145, 0.00),
            (0.23, 0.00),
        ]
        return [(cx + x * inch, cy + y * inch) for x, y in points]

    def stroke_poly(points):
        path = c.beginPath()
        path.moveTo(*points[0])
        for point in points[1:]:
            path.lineTo(*point)
        c.drawPath(path, stroke=1, fill=0)

    # Back cover: pure flatline, otherwise blank.
    c.line(0, base_y, spine_left, base_y)

    # Front cover: complete-width line with one pulse.
    pulse = heartbeat(front_center, base_y)
    c.line(spine_right, base_y, pulse[0][0], base_y)
    stroke_poly(pulse)
    c.line(pulse[-1][0], base_y, w, base_y)

    # Spine: same motif rotated 90 degrees, full height, no text.
    spine_center = (spine_left + spine_right) / 2
    raw = heartbeat(0, 0)
    rotated = [(spine_center - y, base_y + x) for x, y in raw]
    c.line(spine_center, 0, spine_center, rotated[0][1])
    stroke_poly(rotated)
    c.line(spine_center, rotated[-1][1], spine_center, h)

    def tracked(text, font, size, tracking, cx, y):
        widths = [stringWidth(ch, font, size) for ch in text]
        x = cx - (sum(widths) + tracking * (len(text) - 1)) / 2
        c.setFont(font, size)
        for ch, width in zip(text, widths):
            c.drawString(x, y, ch)
            x += width + tracking

    title = "ABWEICHUNG"
    title_size = 42
    tracking = 2.5
    max_title_width = (TRIM_W - 0.55) * inch
    while (
        sum(stringWidth(ch, "CoverTitle", title_size) for ch in title)
        + tracking * (len(title) - 1)
        > max_title_width
    ):
        title_size -= 0.5
    tracked(title, "CoverTitle", title_size, tracking, front_center, h * 0.675)

    c.setFont("CoverSub", 12.5)
    c.drawCentredString(front_center, h * 0.392, "Wenn die Maschine recht hat")

    c.showPage()
    c.save()
    print(
        f"pages={pages} paper={paper} spine={spine:.6f}in "
        f"cover={cover_w:.6f}x{cover_h:.3f}in"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pages", type=int, required=True)
    parser.add_argument("--paper", choices=["white", "cream"], default="white")
    parser.add_argument("--output", default="ABWEICHUNG_COVER.pdf")
    args = parser.parse_args()
    build(Path(args.output), args.pages, args.paper)


if __name__ == "__main__":
    main()
