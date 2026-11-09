# Free Hydrogen Awakening caption retrieval

This helper checks the original 42-video seed batch recorded in the VARTA catalogue (batches 01–02) and asks **yt-dlp** to save accessible English or Hindi creator-uploaded / auto-generated caption tracks. It does **not** download video files and does not use a paid service or API key. It does not yet include the six additional discovery leads in catalogue batch 03, and it is not a complete channel archive.

## Windows (PowerShell)

1. Install Python 3 from https://www.python.org/downloads/ (enable “Add Python to PATH”).
2. Download the latest `fetch_hydrogen_captions.py` from this repository before each new attempt; older local copies may not contain the rate-limit safeguards. Open PowerShell in the downloaded folder.
3. Install/update yt-dlp:

   ```powershell
   py -m pip install -U yt-dlp
   ```

4. Run:

   ```powershell
   py .\fetch_hydrogen_captions.py
   ```

## macOS / Linux

```bash
python3 -m pip install -U yt-dlp
python3 fetch_hydrogen_captions.py
```

## Results

The script creates `hydrogen-awakening-transcripts/` containing any returned `.vtt` caption files and a `retrieval-log.txt`. It requests English and Hindi tracks, adds delays between requests and videos, and stops immediately if YouTube returns HTTP 429 (Too Many Requests). A video may have no public captions, or YouTube may temporarily block requests. A successful yt-dlp process does not by itself prove that a caption file was saved: check for the actual files and log entries.

For reliable research, retain the video ID and URL, note the caption language and whether the track is creator-uploaded or auto-generated, and manually verify important names, Sanskrit terms, numbers and quotations against the audio. Do not treat auto-captions as an authoritative transcript.

## Important limitations

- This tool can only retrieve caption tracks YouTube makes accessible.
- It cannot recover speech when no caption track exists.
- YouTube may change its access rules; keep yt-dlp updated.
- If HTTP 429 appears, stop and do not repeatedly rerun the script. Wait at least 24 hours before a cautious retry; repeated requests can prolong a temporary rate limit.
- If the tool reports that a JavaScript runtime is required, install a supported runtime such as Deno or Node and follow the current yt-dlp documentation.
- The catalogue is a discovery sample, not a complete channel inventory.
