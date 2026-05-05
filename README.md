# Browser URL Grabber (macOS)

A standalone Python tool that collects open browser tabs from supported macOS browsers and exports them into structured JSON grouped by browser and window.

---

## Quick Start

```bash
git clone https://github.com/CocoHusky/browser-url-grabber.git
cd browser-url-grabber
python3 src/grab_browser_urls_mac.py
```

---

## Requirements

| Requirement | Needed? | Notes |
|---|---:|---|
| macOS | Yes | Current version is macOS only |
| Python 3 | Yes | No extra Python packages required |
| Terminal | Yes | Used to run the script |
| Browser automation permission | Yes | Required by macOS privacy settings |
| Browser extension | No | This does not use an extension |
| Internet access | No | The script reads local open browser tabs |

---

## Check Python

```bash
python3 --version
```

If Python 3 is installed, you should see:

```text
Python 3.x.x
```

---

## Install Python If Missing

Download from:

```text
https://www.python.org/downloads/
```

Or install with Homebrew:

```bash
brew install python
```

---

## How to Run

From the project root:

```bash
python3 src/grab_browser_urls_mac.py
```

Optional executable mode:

```bash
chmod +x src/grab_browser_urls_mac.py
./src/grab_browser_urls_mac.py
```

---

## Output Location

JSON files are saved inside the repo:

```text
browser-url-grabber/json output/
```

Example:

```text
browser-url-grabber/json output/browser_urls_2026-05-05_14-30-10.json
```

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

macOS may block Terminal or Python from reading browser tabs until permission is approved.

Go to:

```text
System Settings → Privacy & Security → Automation
```

Enable browser control permissions for the app running the script.

| App requesting permission | Allow access to |
|---|---|
| Terminal | Safari, Chrome, Edge, Brave, Arc |
| iTerm | Safari, Chrome, Edge, Brave, Arc |
| Python | Safari, Chrome, Edge, Brave, Arc |

If output is empty, incomplete, or only one browser works, check Automation permissions first.

---

## Output Format

```json
{
  "Safari": {
    "a": [
      {
        "tab_name": "Example Safari Tab",
        "url": "https://example.com"
      }
    ]
  },
  "Chrome": {
    "a": [
      {
        "tab_name": "Example Chrome Tab",
        "url": "https://github.com/"
      }
    ],
    "b": [
      {
        "tab_name": "Another Window",
        "url": "https://openai.com/"
      }
    ]
  }
}
```

---

## Window Labels

Browser windows are labeled alphabetically.

| Window Number | Label |
|---:|---|
| 1 | `a` |
| 2 | `b` |
| 3 | `c` |
| 26 | `z` |
| 27 | `aa` |
| 28 | `ab` |
| 29 | `ac` |

---

## Limitations

| Limitation | Details |
|---|---|
| macOS only | Windows support is not included yet |
| Browsers must be open | Closed browsers are skipped |
| Private/incognito tabs | May not be readable depending on browser behavior |
| No network sniffing | This only reads actual browser tabs |
| No GUI yet | Current version runs from Terminal |
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
