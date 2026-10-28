"""@brief Render a command and its output as a terminal-style PNG screenshot.

The screenshots of the README and the wiki are made with this script, so no
desktop is captured. Needs Pillow (`pip install -e ".[dev]"`).
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BACKGROUND = (30, 30, 30)
TITLE_BAR = (50, 50, 50)
TEXT = (212, 212, 212)
PROMPT = (96, 200, 96)
FONT_SIZE = 16
PADDING = 16
BAR_HEIGHT = 30
MAX_COLUMNS = 110
MAX_LINES = 40
FONT_FILES = (
    "consola.ttf",
    "DejaVuSansMono.ttf",
    "LiberationMono-Regular.ttf",
    "Menlo.ttc",
)


def _load_font() -> ImageFont.ImageFont | ImageFont.FreeTypeFont:
    for name in FONT_FILES:
        try:
            return ImageFont.truetype(name, FONT_SIZE)
        except OSError:
            continue
    return ImageFont.load_default()


def _fit(lines: list[str]) -> list[str]:
    fitted = [
        line if len(line) <= MAX_COLUMNS else line[: MAX_COLUMNS - 3] + "..."
        for line in lines
    ]
    if len(fitted) > MAX_LINES:
        fitted = fitted[:MAX_LINES] + ["..."]
    return fitted


def render(command: str, output: str, target: Path) -> None:
    """@brief Draw the command and its output and save the PNG.

    @param command The command line shown after the prompt.
    @param output The text the command printed.
    @param target The PNG file to write.
    """
    font = _load_font()
    lines = _fit(output.rstrip().splitlines())
    prompt = "$ "
    columns = max([len(prompt + command), *(len(line) for line in lines)])
    char_width = font.getlength("M")
    line_height = FONT_SIZE + 6
    width = int(columns * char_width) + 2 * PADDING
    height = BAR_HEIGHT + 2 * PADDING + line_height * (len(lines) + 1)
    image = Image.new("RGB", (max(width, 480), height), BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, image.width, BAR_HEIGHT), fill=TITLE_BAR)
    for index, color in enumerate(((255, 95, 86), (255, 189, 46), (39, 201, 63))):
        x = PADDING + index * 22
        draw.ellipse((x, 9, x + 12, 21), fill=color)
    y = BAR_HEIGHT + PADDING
    draw.text((PADDING, y), prompt, font=font, fill=PROMPT)
    draw.text((PADDING + font.getlength(prompt), y), command, font=font, fill=TEXT)
    for line in lines:
        y += line_height
        draw.text((PADDING, y), line, font=font, fill=TEXT)
    target.parent.mkdir(parents=True, exist_ok=True)
    image.save(target)
