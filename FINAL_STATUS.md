# OpenSCAD Helper Extension - Final Status (v0.0.6)

## ✅ Installation Complete

**Current Version:** 0.0.6  
**GitHub Repository:** https://github.com/rhinot/openscad-helper  
**Package:** `openscad-helper-0.0.6.vsix` (10.3 KB)

---

## 🎯 What Works

### Commands Available
1. **OpenSCAD: Run (GUI)** - Opens file in OpenSCAD with auto-render (F6)
2. **OpenSCAD: Build (3MF + OrcaSlicer)** - Exports to 3MF and opens slicer

### How to Access
- **F5 key** - Run command (when .scad file is open)
- **Shift+Cmd+B** - Build command (when .scad file is open)
- **Editor title buttons** - Play icon (Run) and Package icon (Build) at top-right
- **Right-click menu** - Both commands in context menu
- **Command Palette** - Cmd+Shift+P → type "OpenSCAD"

---

## 🔧 Auto-Render Feature (macOS)

The extension automatically presses F6 in OpenSCAD to render your design.

### Requirements
✅ **Accessibility Permission for VS Code**  
You've already granted this! VS Code can now control OpenSCAD.

### How It Works
1. Opens OpenSCAD with your file
2. Waits 2 seconds for window to appear
3. Uses AppleScript to activate OpenSCAD and press F6
4. Your design renders automatically

### If It Doesn't Work
- **Reload VS Code**: Cmd+Shift+P → "Developer: Reload Window"
- **Check permissions**: System Settings > Privacy & Security > Accessibility > VS Code should be enabled
- **Try manually**: If auto-render fails, just press F6 manually in OpenSCAD

---

## 📁 Files in This Extension

```
openscad-helper/
├── extension.js       # VS Code extension code
├── run_scad.py       # Python helper (handles OpenSCAD launching)
├── package.json      # Extension manifest
├── LICENSE           # Attribution-NonCommercial license
├── README.md         # Full documentation
├── USAGE.md          # Quick-start guide
└── test/             # Test suite (all passing)
```

---

## 🚀 Quick Test

1. **Open or create a .scad file** in VS Code:
   ```openscad
   cube([20, 20, 20]);
   ```

2. **Press F5** (or click the Play button at top-right)

3. **What should happen:**
   - OpenSCAD opens with your file
   - After ~2 seconds, it automatically renders (F6)
   - You see: "OpenSCAD launched with auto-render (F6)."

4. **Test Build** with **Shift+Cmd+B**:
   - Creates `filename.3mf` in same directory
   - Opens OrcaSlicer (if installed)

---

## 📝 License

**Attribution-NonCommercial**
- ✅ Free for personal/non-commercial use
- ✅ Requires attribution (credit to rhinot)
- ✅ Allows modifications (Share-Alike)
- ❌ No commercial use without permission

---

## 🐛 Troubleshooting

### F5 doesn't work
- Ensure the file has `.scad` extension
- Try clicking the Play button instead
- Reload window: Cmd+Shift+P → "Developer: Reload Window"

### Auto-render (F6) doesn't trigger
- Verify VS Code has Accessibility permission
- System Settings > Privacy & Security > Accessibility
- Toggle VS Code off and on again
- Restart VS Code

### "openscad: command not found"
```bash
brew install --cask openscad
```

### Can't see context menu items
- Right-click inside the editor (not on file in sidebar)
- Ensure file has .scad extension
- Reload window if just installed

---

## 📊 Version History

- **v0.0.6** - Reduced delay to 2s, fixed F5 keybinding, added permission prompt
- **v0.0.5** - Fixed AppleScript F6 automation with helpful error messages
- **v0.0.4** - Fixed notification messages and added error logging
- **v0.0.3** - Added AppleScript for F6 automation
- **v0.0.2** - Added context menus and editor title buttons
- **v0.0.1** - Initial release

---

## 🎉 Summary

Your OpenSCAD Helper extension is **fully functional and ready to use**!

✅ Tests passing  
✅ Code on GitHub  
✅ Extension installed  
✅ Auto-render working (with permissions)  
✅ Keyboard shortcuts active  
✅ Context menus working  
✅ Comprehensive documentation  

**Repository:** https://github.com/rhinot/openscad-helper

Enjoy your streamlined OpenSCAD workflow! 🚀
