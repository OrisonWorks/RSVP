import subprocess
from pathlib import Path

BASE_URL = "https://orisonworks.github.io/RSVP/index.html?id="
OUTPUT_DIR = Path("pdf")
OUTPUT_DIR.mkdir(exist_ok=True)

CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]

browser = None
for path in CHROME_PATHS:
    if Path(path).exists():
        browser = path
        break

if not browser:
    raise SystemExit("Chrome or Edge not found. Please install one of them.")

for i in range(1, 121):
    invite_id = f"KM70-{i:03d}"
    url = f"{BASE_URL}{invite_id}"
    output_file = OUTPUT_DIR / f"{invite_id}.pdf"
    subprocess.run([
        browser,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--print-to-pdf={output_file}",
        url
    ], check=True)

print("✅ All PDFs generated in /pdf folder")
