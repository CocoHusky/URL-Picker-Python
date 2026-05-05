# Browser URL Grabber

Browser URL Grabber is a local Python utility for macOS that collects open browser tabs from Safari, Chrome, Edge, Brave, and Arc.

It exports the results as JSON organized by browser, window, tab name, and URL.

## Purpose

This tool is designed for quickly collecting browser context for research, job applications, AI workflows, tab cleanup, documentation, and personal archiving.

## Current Features

- Collects open tabs from supported macOS browsers
- Supports Safari, Chrome, Edge, Brave, and Arc
- Groups URLs by browser
- Groups tabs by browser window
- Uses simple window labels such as `a`, `b`, `c`, `aa`, `ab`
- Exports JSON only
- Runs locally
- No browser extension required
- No cloud service required

## Example Output

```json
{
  "Safari": {
    "a": [
      {
        "tab_name": "Apple",
        "url": "https://www.apple.com/"
      }
    ]
  },
  "Chrome": {
    "a": [
      {
        "tab_name": "GitHub",
        "url": "https://github.com/"
      }
    ],
    "b": [
      {
        "tab_name": "OpenAI",
        "url": "https://openai.com/"
      }
    ]
  }
}