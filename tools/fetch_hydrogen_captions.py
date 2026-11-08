#!/usr/bin/env python3
"""Fetch a limited set of public caption tracks for Hydrogen Awakening.

Requires Python 3 and yt-dlp. Downloads subtitle files only, not videos.
Requests English and Hindi tracks only to avoid excessive subtitle requests.
"""
from pathlib import Path
import shutil
import subprocess
import time

VIDEO_IDS = [
    "BP6Tg5Qj26s", "PLwHnonMi8Q", "RoYuHKwM98A", "Q5_9tvJFpFA",
    "Tm7h_QSluF8", "pQhvpUyCQPM", "o5OmQLL2z7s", "83aKDwvSO3A",
    "dYjFFxP37EQ", "fKj5ZoS1VlY",
    "sbsjaXeY7xk", "PzdDr3cjyyc", "0sI1LnTlaZI", "KPuHty0g6k0",
    "P08grJbYHj8", "FwYHa0bjYlo", "_90qRieVXTg", "gSeXwQ50sdM",
    "O-eiXhEcEnQ", "ACf7qOpfl3w",
    "5Bu4E-huwLw", "Pkg2A4ySV-Q", "jV5M2RJWY2E", "PIBzhSlxL5E",
    "be4LEz-WeQE", "ZWJGtfbZw2M", "3cCfylZWhXw", "BWJ_gDY75Jk",
    "dzVF-piY3XA", "_ygBfSfRJzw",
    "SqusmDPfp0U", "H_qVSMrB23U", "f0Jl546T1Ec", "Mn8rgM5EAVU",
    "sHiYuS20N20", "ErK-oet1PKg", "IbSkIE_oiA8", "ptHas4Yv5fQ",
    "vOpfJ41wK1s", "GAfYo4i80AU", "jJr59cGdZGU", "WqMRKDA6hVk",
]

def main():
    exe = shutil.which("yt-dlp")
    if not exe:
        print("yt-dlp is not installed. Install it with: py -m pip install -U yt-dlp")
        return 2

    out = Path("hydrogen-awakening-transcripts")
    out.mkdir(exist_ok=True)
    log_path = out / "retrieval-log.txt"
    checked = 0
    previous_files = set(out.glob("*.vtt"))
    rate_limited = False

    with log_path.open("w", encoding="utf-8") as log:
        log.write("Hydrogen Awakening public caption retrieval\n")
        log.write("English/Hindi tracks only; subtitle files only, no video downloads.\n")
        log.write("The script stops immediately if YouTube returns HTTP 429.\n\n")
        for number, video_id in enumerate(VIDEO_IDS, 1):
            url = f"https://www.youtube.com/watch?v={video_id}"
            print(f"[{number}/{len(VIDEO_IDS)}] Checking {video_id} ...")
            cmd = [
                exe, "--skip-download", "--write-subs", "--write-auto-subs",
                "--sub-langs", "en,hi,en-orig,hi-orig", "--sub-format", "vtt/best",
                "--sleep-requests", "3", "--sleep-subtitles", "8",
                "--no-warnings", "--output", str(out / "%(id)s.%(ext)s"),
                url,
            ]
            result = subprocess.run(cmd, text=True, capture_output=True)
            details = (result.stdout or "") + (result.stderr or "")
            log.write(f"\n===== {video_id} | {url} =====\n")
            log.write(details if details.strip() else f"yt-dlp exit code: {result.returncode}\n")
            checked += 1
            if "HTTP Error 429" in details or "Too Many Requests" in details:
                rate_limited = True
                print("  YouTube rate limit detected. Stopping to avoid further requests.")
                log.write("\nSTOPPED: YouTube returned HTTP 429 (Too Many Requests).\n")
                break
            if result.returncode == 0:
                print("  Check completed; verify whether a .vtt file was saved.")
            else:
                print("  Check failed; see retrieval-log.txt.")
            time.sleep(15)

    new_files = sorted(set(out.glob("*.vtt")) - previous_files)
    print(f"\nFinished. Checked {checked} videos; {len(new_files)} new caption files saved.")
    print(f"Files and log: {out.resolve()}")
    if rate_limited:
        print("YouTube rate-limited requests. Do not rerun immediately; wait before trying again.")
    print("A completed check does not guarantee captions existed; inspect the .vtt files.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
