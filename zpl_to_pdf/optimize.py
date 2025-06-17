import os
import re
from zpl_to_pdf.logger import logger

LABEL_WIDTH_DOTS = 4 * 300
LABEL_HEIGHT_DOTS = 6 * 300

def _scale_value(value: int, scale: float) -> int:
    return int(round(value * scale))


def optimize_zpl(zpl_data: str, original_file_path: str | None = None) -> str:
    """Optimize ZPL code to fit a 4x6 label.

    This function rescales coordinates found in ``^FO`` and ``^FT`` commands so
    that all elements stay within the printable area of a 4x6 inch label at
    300 DPI. If the optional ``original_file_path`` is provided, the optimized
    ZPL is saved alongside the original file with ``_optimized`` appended to its
    name.
    """
    pattern_coords = re.compile(r"\^(FO|FT)(-?\d+),(\-?\d+)")
    coords = [(int(m.group(2)), int(m.group(3))) for m in pattern_coords.finditer(zpl_data)]

    max_x = max((x for x, _ in coords), default=0)
    max_y = max((y for _, y in coords), default=0)

    scale_x = LABEL_WIDTH_DOTS / max_x if max_x > LABEL_WIDTH_DOTS else 1.0
    scale_y = LABEL_HEIGHT_DOTS / max_y if max_y > LABEL_HEIGHT_DOTS else 1.0
    scale = min(scale_x, scale_y, 1.0)

    def repl_coords(match: re.Match) -> str:
        cmd = match.group(1)
        x = int(match.group(2))
        y = int(match.group(3))
        if scale < 1.0:
            x = _scale_value(x, scale)
            y = _scale_value(y, scale)
        x = max(0, min(x, LABEL_WIDTH_DOTS))
        y = max(0, min(y, LABEL_HEIGHT_DOTS))
        return f"^{cmd}{x},{y}"

    optimized_zpl = pattern_coords.sub(repl_coords, zpl_data)

    pattern_gb = re.compile(r"\^GB(-?\d+),(-?\d+)((?:,[^\^]*)?)")

    def repl_gb(match: re.Match) -> str:
        width = int(match.group(1))
        height = int(match.group(2))
        rest = match.group(3) or ""
        if scale < 1.0:
            width = _scale_value(width, scale)
            height = _scale_value(height, scale)
        width = max(0, min(width, LABEL_WIDTH_DOTS))
        height = max(0, min(height, LABEL_HEIGHT_DOTS))
        return f"^GB{width},{height}{rest}"

    optimized_zpl = pattern_gb.sub(repl_gb, optimized_zpl)

    if original_file_path:
        base, ext = os.path.splitext(original_file_path)
        if not ext:
            ext = ".txt"
        optimized_path = f"{base}_optimized{ext}"
        try:
            with open(optimized_path, "w") as f:
                f.write(optimized_zpl)
            logger.info(f"ZPL optimizado guardado en: {optimized_path}")
        except OSError as e:
            logger.error(f"No se pudo guardar el ZPL optimizado: {e}")
    return optimized_zpl
