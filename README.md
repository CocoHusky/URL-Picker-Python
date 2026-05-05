# Browser URL Grabber (macOS)

A standalone macOS tool that collects open browser tabs from supported browsers and exports them into structured JSON grouped by browser and window.

---

## Use Options

You can use this project in two ways:

| Option | Best For | Requires Python? |
|---|---|---:|
| Download the `.app` from Releases | Normal users | No |
| Run the Python script directly | Developers / testing | Yes |

---

## Option 1 — Use the macOS App

1. Go to the repo’s **Releases** page:

```text
https://github.com/CocoHusky/browser-url-grabber/releases
```

2. Download the latest macOS release `.zip`.

Example:

```text
Browser-URL-Grabber-macOS-v0.1.1.zip
```

3. Unzip it.

4. Open:

```text
Browser URL Grabber.app
```

On first launch, macOS may block the app because it is unsigned.

Use:

```text
Right click → Open
```

Then approve the prompt.

---

## Option 2 — Run Directly With Python

Clone the repo:

```bash
git clone https://github.com/CocoHusky/browser-url-grabber.git
cd browser-url-grabber
```

Check Python:

```bash
python3 --version
```

Run the script:

```bash
python3 src/grab_browser_urls_mac.py
```

No extra Python packages are required.

---

## Requirements

| Requirement | App Release | Python Dev Run | Notes |
|---|---:|---:|---|
| macOS | Yes | Yes | Current version is macOS only |
| Python 3 | No | Yes | Only needed for direct script use |
| Browser automation permission | Yes | Yes | Required by macOS privacy settings |
| Browser extension | No | No | This does not use an extension |
| Internet access | No | No | Reads local open browser tabs only |

---

## Output Location

JSON files are saved inside:

```text
browser-url-grabber/json output/
```

Example:

```text
browser-url-grabber/json output/browser_urls_2026-05-05_14-30-10.json
```

If using the packaged `.app`, output behavior may depend on the packaged app version. Check the release notes for that version.

---

## Supported Browsers

| Browser | macOS Support | Notes |
|---|---:|---|
| Safari | Yes | Uses Safari AppleScript tab names |
| Google Chrome | Yes | Uses Chromium-style tab titles |
| Microsoft Edge | Yes | Uses Chromium-style tab titles |
| Brave | Yes | Uses Chromium-style tab titles |
| Arc | Yes | Uses Chromium-style tab titles |
| Firefox | Not yet | Planned |
| Opera | Not yet | Planned / possible later |

---

## macOS Privacy Permission

macOS may block the app, Terminal, or Python from reading browser tabs until permission is approved.

Go to:

```text
System Settings → Privacy & Security → Automation
```

Enable browser control permissions for whichever app is running Browser URL Grabber.

| Running Method | App requesting permission | Allow access to |
|---|---|---|
| `.app` release | Browser URL Grabber | Safari, Chrome, Edge, Brave, Arc |
| Terminal run | Terminal | Safari, Chrome, Edge, Brave, Arc |
| iTerm run | iTerm | Safari, Chrome, Edge, Brave, Arc |
| Python launcher | Python | Safari, Chrome, Edge, Brave, Arc |

If output is empty, incomplete, or only one browser works, check Automation permissions first.

---

## Output Format

```json
{
  "Safari": {
    "window_1": [
      {
        "tab_name": "Example Safari Tab",
        "url": "https://example.com"
      }
    ]
  },
  "Chrome": {
    "window_1": [
      {
        "tab_name": "Example Chrome Tab",
        "url": "https://github.com/"
      }
    ],
    "window_2": [
      {
        "tab_name": "Another Window",
        "url": "https://openai.com/"
      }
    ]
  }
}
```

---

## Limitations

| Limitation | Details |
|---|---|
| macOS only | Windows support is not included yet |
| Browsers must be open | Closed browsers are skipped |
| Private/incognito tabs | May not be readable depending on browser behavior |
| No network sniffing | This only reads actual browser tabs |
| No GUI yet | Current version may run silently |
| Firefox not supported yet | Planned for later |

---

## Project Structure

```text
browser-url-grabber/
├─ src/
│  └─ grab_browser_urls_mac.py
├─ json output/
├─ README.md
├─ LICENSE
├─ RELEASE.md
├─ CHANGELOG.md
└─ .gitignore
```

---

## License

MIT License
