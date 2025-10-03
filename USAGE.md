# Quick Start Guide - OpenSCAD Helper Extension

## Installation Steps

### Method 1: Run in Development Mode (Quickest)

1. Open the extension folder in VS Code:
   ```bash
   cd /Users/ryan/projects/vscode/openscad-helper
   code .
   ```

2. Press **F5** in VS Code
   - This launches a new "Extension Development Host" window with your extension loaded

3. In the new window, open or create a `.scad` file to test

### Method 2: Package and Install

1. Install the packaging tool (if not already installed):
   ```bash
   npm install -g @vscode/vsce
   ```

2. Package the extension:
   ```bash
   cd /Users/ryan/projects/vscode/openscad-helper
   vsce package
   ```
   This creates `openscad-helper-0.0.1.vsix`

3. Install the extension:
   - Open VS Code Command Palette: `Cmd+Shift+P`
   - Type: "Extensions: Install from VSIX..."
   - Select the `.vsix` file

## Using the Extension

### Test with a Sample File

Create a test file `test.scad`:

```openscad
// Simple cube example
cube([10, 10, 10]);
```

### Command 1: Run (Preview in OpenSCAD)

**Keyboard Shortcut:** Press **F5** while editing a `.scad` file

**Or via Command Palette:**
1. `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)
2. Type: "OpenSCAD: Run (GUI)"
3. Press Enter

**What happens:**
- OpenSCAD application opens with your file
- On macOS (if pyautogui is installed), F6 is automatically pressed to render

### Command 2: Build (Export to 3MF)

**Keyboard Shortcut:** Press **Shift+Cmd+B** (macOS)

**Or via Command Palette:**
1. `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)
2. Type: "OpenSCAD: Build (3MF + OrcaSlicer)"
3. Press Enter

**What happens:**
- OpenSCAD runs headless export to create `test.3mf` (same directory as `.scad` file)
- OrcaSlicer opens with the 3MF file loaded (if installed)

## Verifying Setup

### Check OpenSCAD Installation

```bash
openscad --version
```

Expected output: Something like `OpenSCAD version 2021.01` or newer

If not found:
- **macOS:** `brew install --cask openscad`
- **Windows:** Download from openscad.org and add to PATH
- **Linux:** `sudo apt install openscad`

### Check Python Installation

```bash
python3 --version
```

Expected output: `Python 3.x.x`

### Optional: Install pyautogui (for macOS auto-render)

```bash
pip3 install pyautogui
```

Then grant Accessibility permissions:
- System Settings > Privacy & Security > Accessibility
- Add your Python interpreter

## Troubleshooting

### Extension doesn't appear in Development Host

1. Check the Debug Console in the main VS Code window for errors
2. Verify `package.json` is valid JSON
3. Try running: `npm install` in the extension directory

### "openscad: command not found"

- The OpenSCAD command-line tool is not in your PATH
- Install OpenSCAD and ensure the CLI tool is accessible

### Commands don't execute

- Make sure you have a `.scad` file open and focused
- Check Output panel in VS Code (View > Output) for error messages

### Tests fail

```bash
npm test
```

If tests fail:
1. Ensure dependencies are installed: `npm install`
2. Check that VS Code version is compatible (1.104.0+)

## Next Steps

- Edit your `.scad` files in VS Code
- Use F5 to quickly preview changes in OpenSCAD
- Use Shift+Cmd+B to export and prepare for 3D printing
- Optionally install the OpenSCAD syntax highlighting extension for better code editing

Enjoy your streamlined OpenSCAD workflow! 🎉
