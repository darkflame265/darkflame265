"""Build static profile graphics from typography and actual service screenshots."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def font(size, bold=False):
    return ImageFont.truetype(
        "C:/Windows/Fonts/malgunbd.ttf" if bold else "C:/Windows/Fonts/malgun.ttf", size
    )


banner = Image.new("RGB", (1600, 420), "#111720")
d = ImageDraw.Draw(banner)
d.rectangle((1120, 0, 1600, 420), fill="#2549E8")
d.text((68, 37), "KIM KIHEE / WEB UI & DEVELOPMENT", font=font(20, True), fill="#70D9CC")
d.line((68, 88, 1060, 88), fill="#36404F", width=2)
d.text((65, 111), "웹 UI를 설계하고,", font=font(68, True), fill="white")
d.text((65, 207), "서비스로 연결합니다.", font=font(68, True), fill="white")
d.text((69, 346), "김기희  /  darkflame265", font=font(23), fill="#B4C0CE")
d.text((1170, 57), "DESIGN", font=font(40, True), fill="white")
d.text((1170, 119), "BUILD", font=font(40, True), fill="white")
d.text((1170, 181), "SHIP", font=font(40, True), fill="#A0F0D1")
d.line((1170, 285, 1530, 285), fill="#6F88F2", width=2)
d.text((1170, 318), "Web / UI / Interaction", font=font(22), fill="white")
banner.save(ASSETS / "profile-banner.png", optimize=True)

shot = Image.open(ASSETS / "pathclash-desktop.png").convert("RGB")
game = shot.crop((420, 0, 1020, 900)).resize((552, 828), Image.Resampling.LANCZOS)
preview = Image.new("RGB", (1600, 900), "#10191D")
preview.paste(game, (48, 36))
d = ImageDraw.Draw(preview)
d.text((674, 137), "WEB GAME / GOOGLE PLAY", font=font(22, True), fill="#65DCD0")
d.text((668, 220), "PathClash", font=font(95, True), fill="#F2F7FC")
d.text((674, 373), "실시간 1:1 전략 게임", font=font(37, True), fill="#D4E4EC")
d.text((674, 461), "반응형 UI · 실시간 상호작용", font=font(26), fill="#A1B5C2")
d.text((674, 510), "웹과 Android에서 이어지는 플레이", font=font(26), fill="#A1B5C2")
d.line((674, 631, 1490, 631), fill="#304650", width=2)
d.text((674, 683), "PLAN / BUILD / LAUNCH / OPERATE", font=font(21, True), fill="#65DCD0")
d.text((674, 739), "pathclash.com", font=font(30), fill="white")
preview.save(ASSETS / "pathclash-preview.webp", quality=90, method=6)
Image.open(ASSETS / "portfolio-desktop.png").convert("RGB").save(
    ASSETS / "portfolio-preview.webp", quality=90, method=6
)
print("Profile banner and two project previews created.")
