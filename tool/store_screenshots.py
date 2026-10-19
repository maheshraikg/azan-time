"""Play Store screenshots (1080x1920) with a caption, from docs/screenshots.

    flutter test tool/screenshots/screenshot_test.dart   # app screenshots
    python3 tool/store_screenshots.py                    # framed store set

Writes docs/store/screenshots/. Needs Pillow and the Flutter SDK's Roboto.
"""
import os
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(os.environ.get('FLUTTER_ROOT', '/opt/flutter'),
                     'bin/cache/artifacts/material_fonts')
ITEMS = [
    ('en_1_today', 'Exact Azan & Namaz times', 'Live countdown under a living sky'),
    ('en_12_share', 'Share prayer times', 'As a poster, in 12 languages'),
    ('en_2b_calendar', 'Hijri calendar', 'Islamic dates and occasions'),
    ('en_13_duas', 'Duas & Azkar', 'Arabic, meaning and a tap counter'),
    ('en_14_ramadan', 'Ramadan timetable', 'Suhoor and Iftar countdown'),
    ('en_3_qibla', 'Qibla compass', 'Glows when you face the Kaaba'),
    ('en_5_alerts', 'Your Azan, your way', 'Recorded Azan, Iqama and auto-silent'),
]
W, H = 1080, 1920
TOP, BOTTOM = (7, 15, 43), (11, 77, 70)
GOLD = (226, 184, 75)


def main():
    title = ImageFont.truetype(os.path.join(FONTS, 'Roboto-Black.ttf'), 76)
    sub = ImageFont.truetype(os.path.join(FONTS, 'Roboto-Medium.ttf'), 42)
    out = os.path.join(ROOT, 'docs/store/screenshots')
    os.makedirs(out, exist_ok=True)
    for n, (name, head, line) in enumerate(ITEMS, 1):
        img = Image.new('RGB', (W, H))
        d = ImageDraw.Draw(img)
        for y in range(H):
            t = y / H
            d.line([(0, y), (W, y)],
                   fill=tuple(int(TOP[i] + (BOTTOM[i] - TOP[i]) * t) for i in range(3)))
        r = random.Random(n)
        for _ in range(90):
            x, y = r.random() * W, r.random() * 300
            s, a = r.random() * 2 + 0.6, int(110 + r.random() * 120)
            d.ellipse([x - s, y - s, x + s, y + s], fill=(a, a, a))
        for y, text, font, fill in [(90, head, title, GOLD), (192, line, sub, (235, 240, 238))]:
            d.text(((W - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)
        shot = Image.open(os.path.join(ROOT, 'docs/screenshots', name + '.png')).convert('RGB')
        h = H - 300 - 70
        w = int(shot.width * h / shot.height)
        shot = shot.resize((w, h), Image.LANCZOS)
        x0, y0 = (W - w) // 2, 300
        shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(shadow).rounded_rectangle(
            [x0, y0 + 12, x0 + w, y0 + h + 12], radius=44, fill=(0, 0, 0, 150))
        img = Image.alpha_composite(
            img.convert('RGBA'), shadow.filter(ImageFilter.GaussianBlur(18))).convert('RGB')
        mask = Image.new('L', (w, h), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=255)
        img.paste(shot, (x0, y0), mask)
        ImageDraw.Draw(img).rounded_rectangle(
            [x0 - 1, y0 - 1, x0 + w, y0 + h], radius=41, outline=GOLD, width=3)
        img.save(os.path.join(out, f'{n}_{name[3:]}.png'), optimize=True)


if __name__ == '__main__':
    main()
