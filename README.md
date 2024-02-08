# Python Patcher Updates

## Description

This repo contains html which is displayed in the installer, so we can update the installer html without building a new installer release.

The html files are compiled into a single `updates.json` file which is used by the installer - the installer does not use the `.html` files directly.

## Notes

- `.html` is used instead of markdown so I can be lazy and embed colors or other stuff which markdown doesn't support
- I don't think you can reference vue variables etc. in the `html` here.

## How to update install status

**NOTE: Currently this 'load mod status from github' is only enabled for Hou Plus, as a test.**

- Find or create the `.html` file matching the chapter you want to edit (currently only supported for Hou Plus). The name must match the name in the `installData.json` file exactly (in the other `python-patcher` repo).
    - You may need to cross reference where the html appears in the installer to edit it properly, (drojf: TODO, make it easier to find where html is appears in the installer)
- Edit the `.html` file and push to `main` branch
- A new release will be created automatically. The installer will download the the generated `updates.json` and display it in the installer.

