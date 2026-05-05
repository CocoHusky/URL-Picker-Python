
## RELEASE.md

```md
# Release Notes

## v1.0.0 — macOS App with Enhanced JSON Output

### Added

- Packaged as macOS `.app` bundle (Browser URL Grabber.app)
- JSON summary section at the top with:
  - Total number of browsers detected
  - Tab count for each browser
  - Total URLs across all browsers
  - Generation timestamp
- Window naming now uses `window_1`, `window_2`, etc. (instead of `a`, `b`, `c`)

### Changed

- Output location: JSON files now save to `~/Documents/Browser URL Grabber/json output/`
- Window labels updated for better readability and consistency

### Notes

This is the first stable release with a packaged macOS application.

## v0.1.0 — Initial macOS Test Release

### Added

- Initial macOS Python script
- Safari tab collection
- Chrome tab collection
- Edge tab collection
- Brave tab collection
- Arc tab collection
- JSON export grouped by browser and window
- Window labels using `a`, `b`, `c`, `aa`, `ab`, etc.
- Desktop output file generation

### Notes

This is an early test release intended to validate local browser tab collection on macOS.

### Known Limitations

- macOS only
- Requires Automation permission
- No GUI yet
- No packaged `.app` yet
- No Windows `.exe` yet
- Firefox is not supported yet