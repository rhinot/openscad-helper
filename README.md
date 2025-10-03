# OpenSCAD Helper

Cross-platform VS Code extension to **Run** and **Build** OpenSCAD files with optional macOS auto-render and OrcaSlicer integration.

## Features

- **Run (GUI)**: Opens the current `.scad` file in OpenSCAD GUI. On macOS, the helper can automatically trigger F6 to render if the `pyautogui` package is installed and macOS Accessibility permissions are granted for your Python interpreter.
- **Build (3MF + OrcaSlicer)**: Headless export of the current `.scad` file to `.3mf` and opens OrcaSlicer ready for printing.
- Cross-platform: Works on **macOS, Windows, Linux**.
- Keyboard shortcuts: **F5** to Run, **Shift+Cmd+B** to Build (on macOS)

## Requirements

- **Python 3** installed and available in PATH.
- **OpenSCAD** installed and available in PATH (command line tool).
- **OrcaSlicer** installed (optional, for Build command).
- **macOS F6 auto-render** (optional): Install the `pyautogui` Python package and grant Accessibility permissions to the Python interpreter you use to run the helper.

```bash
pip3 install pyautogui
```

## Installation

### Option 1: Install from Source (Development)

1. **Clone or download this repository** to your local machine

2. **Install dependencies:**
   ```bash
   cd openscad-helper
   npm install
   ```

3. **Open the extension folder in VS Code:**
   ```bash
   code openscad-helper
   ```

4. **Press F5** to launch the extension in a new VS Code Extension Development Host window

### Option 2: Package and Install Locally

1. **Install vsce (VS Code Extension Manager):**
   ```bash
   npm install -g @vscode/vsce
   ```

2. **Package the extension:**
   ```bash
   cd openscad-helper
   vsce package
   ```
   This creates a `.vsix` file (e.g., `openscad-helper-0.0.1.vsix`)

3. **Install the packaged extension:**
   - In VS Code, open the Command Palette (`Cmd+Shift+P` on macOS)
   - Type "Extensions: Install from VSIX..."
   - Select the `.vsix` file you just created

## Usage

### Running OpenSCAD (Preview Mode)

1. Open a `.scad` file in VS Code
2. Press **F5** or run the command **"OpenSCAD: Run (GUI)"** from the Command Palette
3. OpenSCAD will open with your file loaded
4. On macOS (with pyautogui installed), the extension will automatically press F6 to render the preview

### Building for 3D Printing

1. Open a `.scad` file in VS Code
2. Press **Shift+Cmd+B** (macOS) or run the command **"OpenSCAD: Build (3MF + OrcaSlicer)"** from the Command Palette
3. The extension will:
   - Export your design to a `.3mf` file (saved in the same directory as your `.scad` file)
   - Open OrcaSlicer with the exported file ready for slicing

### Keyboard Shortcuts

- **F5**: Run (open in OpenSCAD GUI)
- **Shift+Cmd+B** (macOS) / **Shift+Ctrl+B** (Windows/Linux): Build to 3MF and open in OrcaSlicer

## Setup Notes

### macOS

1. **Install OpenSCAD:**
   ```bash
   brew install --cask openscad
   ```
   
2. **Ensure `openscad` command is in PATH:**
   After installing via Homebrew, the command-line tool should be available. You can verify:
   ```bash
   which openscad
   openscad --version
   ```
   
3. **For auto-render (optional):**
   - Install pyautogui: `pip3 install pyautogui`
   - Grant Accessibility permissions to your Python interpreter in **System Settings > Privacy & Security > Accessibility**

4. **Install OrcaSlicer (optional):**
   Download from [OrcaSlicer releases](https://github.com/SoftFever/OrcaSlicer/releases) and move to Applications folder

### Windows

1. Install OpenSCAD and add it to your PATH
2. Install Python 3 and add it to PATH
3. Install OrcaSlicer (optional)

### Linux

1. Install OpenSCAD: `sudo apt install openscad` (Debian/Ubuntu) or equivalent
2. Install Python 3: Usually pre-installed
3. Install OrcaSlicer: Download from [OrcaSlicer releases](https://github.com/SoftFever/OrcaSlicer/releases)

## Development

### Running Tests

```bash
npm test
```

The tests will:
- Launch a VS Code test instance
- Load the extension
- Verify commands are registered correctly

### Project Structure

```
openscad-helper/
├── extension.js       # Main extension code
├── run_scad.py       # Python helper script
├── package.json      # Extension manifest
├── test/
│   ├── extension.test.js  # Test suite
│   ├── runTest.js        # Test runner
│   └── suite/
│       └── index.js      # Mocha configuration
└── README.md
```

## Troubleshooting

### "openscad: command not found"

- Ensure OpenSCAD is installed and the command-line tool is in your PATH
- On macOS with Homebrew: `brew install --cask openscad`
- On Windows: Add OpenSCAD installation directory to PATH environment variable

### "pyautogui not installed" message

- This is normal if you haven't installed pyautogui
- The auto-F6 feature is optional; the extension will still work without it
- To enable: `pip3 install pyautogui` and grant Accessibility permissions

### Tests fail to run

- Make sure you've run `npm install` to install dependencies
- Verify VS Code version matches the engine requirement in `package.json`

## License

MIT (or your preferred license)

## Contributing

Feel free to submit issues and pull requests!
