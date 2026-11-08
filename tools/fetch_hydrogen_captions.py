#!/usr/bin/env python3
"""Fetch public caption tracks for the Hydrogen Awakening source catalogue.

Requires Python 3 and yt-dlp. This downloads subtitle files only, not videos.
Creator-uploaded and YouTube auto-generated tracks are both requested.
"""
from pathlib import Path
import shutil
import subprocess
import sys

VIDEO_IDS = [
    # Hydrogen, science and energy
    "BP6Tg5Qj26s", "PLwHnonMi8Q", "RoYuHKwM98A", "Q5_9tvJFpFA",
    "Tm7h_QSluF8", "pQhvpUyCQPM", "o5OmQLL2z7s", "83aKDwvSO3A",
    "dYjFFxP37EQ", "fKj5ZoS1VlY",
    # Vedic knowledge, philosophy and consciousness
    "sbsjaXeY7xk", "PzdDr3cjyyc", "0sI1LnTlaZI", "KPuHty0g6k0",
    "P08grJbYHj8", "FwYHa0bjYlo", "_90qRieVXTg", "gSeXwQ50sdM",
    "O-eiXhEcEnQ", "ACf7qOpfl3w",
    # Nada, sound, ragas and chakras
    "5Bu4E-huwLw", "Pkg2A4ySV-Q", "jV5M2RJWY2E", "PIBzhSlxL5E",
    "be4LEz-WeQE", "ZWJGtfbZw2M", "3cCfylZWhXw", "BWJ_gDY75Jk",
    "dzVF-piY3XA", "_ygBfSfRJzw",
    # Expanded discovery batch
    "SqusmDPfp0U", "H_qVSMrB23U", "f0Jl546T1Ec", "Mn8rgM5EAVU",
    "sHiYuS20N20", "ErK-oet1PKg", "IbSkIE_oiA8", "ptHas4Yv5fQ",
    "vOpfJ41wK1s", "GAfYo4i80AU", "jJr59cGdZGU", "WqMRKDA6hVk",
]

def main():
    exe = shutil.which("yt-dlp")
    if not exe:
        print("yt-dlp is not installed. Install it with: python -m pip install -U yt-dlp")
        return 2

    out = Path("hydrogen-awakening-transcripts")
    out.mkdir(exist_ok=True)
    log_path = out / "retrieval-log.txt"
    success = 0
    failed = 0

    with log_path.open("w", encoding="utf-8") as log:
        log.write("Hydrogen Awakening public caption retrieval\n")
        log.write("Caption tracks only; video files are not downloaded.\n\n")
        for number, video_id in enumerate(VIDEO_IDS, 1):
            url = f"https://www.youtube.com/watch?v={video_id}"
            print(f"[{number}/{len(VIDEO_IDS)}] Checking {video_id} ...")
            cmd = [
                exe, "--skip-download", "--write-subs", "--write-auto-subs",
                "--sub-langs", "all", "--sub-format", "vtt/best",
                "--no-warnings", "--output", str(out / "%(id)s.%(ext)s"),
                url,
            ]
            result = subprocess.run(cmd, text=True, capture_output=True)
            details = (result.stdout or "") + (result.stderr or "")
            log.write(f"\n===== {video_id} | {url} =====\n")
            log.write(details if details.strip() else f"yt-dlp exit code: {result.returncode}\n")
            if result.returncode == 0:
                success += 1
                print(f"  Checked (see log and saved caption files).")
            else:
                failed += 1
                print("  No captions retrieved or request failed; see retrieval-log.txt.")
    print(f"\nFinished. {success} video checks succeeded; {failed} need attention.")
    print(f"Files and log: {out.resolve()}")
    print("A successful check does not guarantee captions existed; inspect the log and .vtt files.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
