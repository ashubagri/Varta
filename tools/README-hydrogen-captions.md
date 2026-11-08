# Free Hydrogen Awakening caption retrieval

This helper checks the 42 video discovery leads in the VARTA Hydrogen Awakening catalogue and asks **yt-dlp** to save any available creator-uploaded or YouTube auto-generated caption tracks. It does **not** download video files and does not use a paid service or API key.

## Windows (PowerShell)

1. Install Python 3 from https://www.python.org/downloads/ (enable “Add Python to PATH”).
2. Open PowerShell in the downloaded folder.
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

The script creates `hydrogen-awakening-transcripts/` containing any returned `.vtt` caption files and a `retrieval-log.txt`. A video may have no public captions, or YouTube may temporarily block requests. A successful yt-dlp process does not by itself prove that a caption file was saved: check for the actual files and log entries.

For reliable research, retain the video ID and URL, note the caption language and whether the track is creator-uploaded or auto-generated, and manually verify important names, Sanskrit terms, numbers and quotations against the audio. Do not treat auto-captions as an authoritative transcript.

## Important limitations

- This tool can only retrieve caption tracks YouTube makes accessible.
- It cannot recover speech when no caption track exists.
- YouTube may change its access rules; keep yt-dlp updated.
- If the tool reports that a JavaScript runtime is required, install a supported runtime such as Deno or Node and follow the current yt-dlp documentation.
- The catalogue is a discovery sample, not a complete channel inventory.
