#!/usr/bin/env python3
"""make.fun entry for news-image-20261124
Generates a dense newspaper-style summary of Tuesday 24 November 2026 world news
and writes it to /output/entry.png
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import os

def get_font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSansBold.ttf" if bold else "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()

def main():
    W, H = 1600, 900
    img = Image.new("RGB", (W, H), "#0f172a")
    draw = ImageDraw.Draw(img)

    title_font = get_font(34, True)
    header_font = get_font(16, True)
    story_font = get_font(12)
    tiny_font = get_font(10)

    # Header bar
    draw.rectangle([0, 0, W, 68], fill="#1e3a5f")
    draw.text((28, 16), "THE WORLD IN ONE DAY", font=title_font, fill="#f8fafc")
    draw.text((400, 26), "·  Tuesday 24 November 2026", font=header_font, fill="#94a3b8")
    draw.text((W-270, 26), "35 stories · 9 regions", font=header_font, fill="#38bdf8")

    cols = [
        {"title": "UKRAINE / RUSSIA", "x": 18, "color": "#ef4444", "stories": [
            "Russian airstrike hits 5-storey apartment in Zaporizhzhia — 2 dead, 44 wounded",
            "Ukraine claims sea-drone strike on Russian warship near Libya base",
            "Analysis estimates >700k Russian soldiers killed since full-scale invasion",
            "Overnight Russian drones hit residential areas in Kyiv and Odesa",
        ]},
        {"title": "MIDDLE EAST", "x": 410, "color": "#f59e0b", "stories": [
            "Israel kills Hamas security chief Naeem Abu Nahel in Gaza airstrike",
            "Houthi drones strike Riyadh King Abdullah Financial District — 11 injured",
            "Saudi-led coalition strikes Hodeidah port after Riyadh attack",
            "Gaza health ministry declares meningitis alert amid access restrictions",
        ]},
        {"title": "ASIA & TECH", "x": 802, "color": "#8b5cf6", "stories": [
            "China prepares Shenzhou-24: Pakistan’s Zeeshan Ali first foreign Tiangong astronaut",
            "US jury convicts Huawei on 10 counts (fraud, sanctions, trade secrets)",
            "Bangladesh: tear gas as garment workers protest; 481 factories halt production",
            "Miss Universe 2026: Jennifer Barreto of Puerto Rico crowned in San Juan",
        ]},
    ]

    y0 = 85
    for col in cols:
        draw.rectangle([col["x"], y0, col["x"]+370, y0+26], fill=col["color"])
        draw.text((col["x"]+10, y0+4), col["title"], font=header_font, fill="#0f172a")
        y = y0 + 36
        for s in col["stories"]:
            words = s.split()
            line = ""
            for w in words:
                test = (line + " " + w).strip()
                if draw.textlength(test, font=story_font) < 350:
                    line = test
                else:
                    draw.text((col["x"]+8, y), "• " + line, font=story_font, fill="#e2e8f0")
                    y += 17
                    line = w
            if line:
                draw.text((col["x"]+8, y), "• " + line, font=story_font, fill="#e2e8f0")
                y += 20
            y += 5

    cols2 = [
        {"title": "DISASTERS & ACCIDENTS", "x": 18, "color": "#ec4899", "stories": [
            "UAE (Ras Al Khaimah): bus collides with stationary truck — 13 killed, 14 injured",
            "Vietnam (Hanoi): cooking-gas explosion at hot-pot restaurant — 7 dead, 9 hurt",
            "Turkey: Air Force training helicopter crashes in Eskişehir — 5 crew killed",
            "Indonesia candy-factory fire (weekend): at least 24 dead, dozens still missing",
        ]},
        {"title": "EUROPE & CLIMATE", "x": 410, "color": "#10b981", "stories": [
            "UK records 5,258 heat-related deaths in 2026 — highest on record (beats 2022)",
            "Belgium strike continues disrupting flights and public transport",
            "Germany becomes first country to gain access to Ukraine’s Delta battlefield system",
            "Seven EU countries push to limit Russian tourist and sports visas",
        ]},
        {"title": "AMERICAS & OTHER", "x": 802, "color": "#06b6d4", "stories": [
            "Colombia: armed men take 25 hostages in Cartagena supermarket after failed robbery",
            "Colombia car-bomb in Villavicencio injures at least 24 people",
            "Nvidia board reinstates Jensen Huang as CEO after political pressure",
            "Sheikh Hasina announces planned return to Bangladesh on 16 December (Victory Day)",
        ]},
    ]

    y0 = 470
    for col in cols2:
        draw.rectangle([col["x"], y0, col["x"]+370, y0+26], fill=col["color"])
        draw.text((col["x"]+10, y0+4), col["title"], font=header_font, fill="#0f172a")
        y = y0 + 36
        for s in col["stories"]:
            words = s.split()
            line = ""
            for w in words:
                test = (line + " " + w).strip()
                if draw.textlength(test, font=story_font) < 350:
                    line = test
                else:
                    draw.text((col["x"]+8, y), "• " + line, font=story_font, fill="#e2e8f0")
                    y += 17
                    line = w
            if line:
                draw.text((col["x"]+8, y), "• " + line, font=story_font, fill="#e2e8f0")
                y += 20
            y += 4

    # Footer
    draw.rectangle([0, H-38, W, H], fill="#1e293b")
    draw.text((28, H-26), "Sources: AP · Reuters · BBC · Al Jazeera · local agencies  ·  Dense editorial summary for make.fun", font=tiny_font, fill="#94a3b8")
    draw.text((W-200, H-26), "24 Nov 2026 UTC", font=tiny_font, fill="#64748b")

    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    img.save(dest, "PNG", optimize=True)
    print(f"Wrote {dest} ({dest.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
