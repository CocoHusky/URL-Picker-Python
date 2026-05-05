#!/usr/bin/env python3
import subprocess
import json
from datetime import datetime
from pathlib import Path

BROWSERS = {
    "Safari": "Safari",
    "Chrome": "Google Chrome",
    "Edge": "Microsoft Edge",
    "Brave": "Brave Browser",
    "Arc": "Arc",
}


def run_osa(script: str):
    return subprocess.run(
        ["osascript", "-e", script],
        capture_output=True,
        text=True
    )


def app_running(app_name: str) -> bool:
    script = f'tell application "System Events" to (name of processes) contains "{app_name}"'
    result = run_osa(script)
    return result.stdout.strip().lower() == "true"


def window_label(index: int) -> str:
    letters = "abcdefghijklmnopqrstuvwxyz"
    label = ""

    index += 1
    while index > 0:
        index -= 1
        label = letters[index % 26] + label
        index //= 26

    return label


def grab_tabs(browser_label: str, app_name: str):
    title_prop = "name" if browser_label == "Safari" else "title"

    script = f'''
    tell application "{app_name}"
        set out to ""
        set windowIndex to 0

        repeat with w in windows
            set windowIndex to windowIndex + 1
            repeat with t in tabs of w
                try
                    set tabTitle to {title_prop} of t
                    set tabURL to URL of t

                    if tabURL is not missing value and tabURL is not "" then
                        set out to out & windowIndex & " ||| " & tabTitle & " ||| " & tabURL & linefeed
                    end if
                end try
            end repeat
        end repeat

        return out
    end tell
    '''

    result = run_osa(script)
    return result.stdout.strip(), result.stderr.strip()


def main():
    output_data = {}

    for browser_label, app_name in BROWSERS.items():
        if not app_running(app_name):
            continue

        raw_output, error = grab_tabs(browser_label, app_name)

        if error:
            print(f"[WARN] {browser_label}: {error}")

        browser_data = {}

        for line in raw_output.splitlines():
            parts = line.split(" ||| ", 2)
            if len(parts) != 3:
                continue

            window_number_raw, tab_title, tab_url = parts

            if not tab_url.startswith(("http://", "https://")):
                continue

            try:
                window_index = int(window_number_raw) - 1
            except ValueError:
                continue

            win_label = window_label(window_index)

            if win_label not in browser_data:
                browser_data[win_label] = []

            browser_data[win_label].append({
                "tab_name": tab_title.strip(),
                "url": tab_url.strip()
            })

        if browser_data:
            output_data[browser_label] = browser_data

    stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    repo_root = Path(__file__).resolve().parents[1]
    out_dir = Path.home() / "Documents" / "Browser URL Grabber" / "json output"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"browser_urls_{stamp}.json"

    out_path.write_text(
        json.dumps(output_data, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"Saved to: {out_path}")


if __name__ == "__main__":
    main()