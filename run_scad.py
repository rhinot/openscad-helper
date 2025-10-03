#!/usr/bin/env python3
"""run_scad.py

Small helper script used by the VS Code extension to open or build an
OpenSCAD file. Designed to be cross-platform and intentionally lightweight.

Usage:
    python run_scad.py <file.scad> [--build]

Behavior:
 - Without --build: launches the OpenSCAD GUI for the provided file.
 - With --build: runs a headless export to <file>.3mf and then attempts to
   open the result in OrcaSlicer.

Notes:
 - Auto-render (F6) support:
   * macOS: Uses AppleScript (requires Accessibility permissions)
   * Windows: Uses pyautogui or pywinauto (install with: pip install pyautogui)
   * Linux: Uses xdotool or pyautogui (install xdotool recommended)
 - This script keeps error handling minimal because it is intended as a
   development helper. Expand error handling if you rely on it in CI.
"""

import subprocess
import time
import platform
import sys
import os


def main(argv):
    # Simple argument check
    if len(argv) < 2:
        print("Usage: python run_scad.py <file.scad> [--build]")
        return 2

    scad_file = argv[1]
    do_build = "--build" in argv
    out_3mf = os.path.splitext(scad_file)[0] + ".3mf"

    # If the user requested a headless build, run OpenSCAD's command line
    # exporter to create a .3mf and then attempt to open it in OrcaSlicer.
    if do_build:
        print(f"Building 3MF: {out_3mf}")
        result = subprocess.run(["openscad", "-o", out_3mf, scad_file],
                               capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✓ Successfully created: {out_3mf}")
            
            # Open the 3MF in OrcaSlicer if available
            system = platform.system()
            if system == "Darwin":
                # macOS: use the `open` utility to launch the application with the file
                subprocess.run(["open", "-a", "OrcaSlicer", out_3mf], 
                             capture_output=True, check=False)
                print("✓ Opened in OrcaSlicer")
            elif system == "Windows":
                # Windows: `start` is a shell built-in, so run via shell=True
                subprocess.run(["start", "", "OrcaSlicer.exe", out_3mf], shell=True)
            else:
                # Linux/other: assume orca-slicer is on PATH
                subprocess.run(["orca-slicer", out_3mf])
        else:
            print(f"Error creating 3MF: {result.stderr}")
            return 4
    else:
        # Run mode: Launch the OpenSCAD GUI for interactive editing/preview.
        # Using Popen allows the script to continue running without waiting for the
        # GUI process to exit.
        try:
            subprocess.Popen(["openscad", scad_file])
        except FileNotFoundError:
            print("Error: 'openscad' not found in PATH. Please install OpenSCAD.")
            return 3

        # Give the GUI a moment to create its window before attempting automation.
        time.sleep(0.5)

        # Cross-platform auto-render: Send F6 keystroke to OpenSCAD
        system = platform.system()
        
        if system == "Darwin":
            # macOS: Use AppleScript to send F6
            # NOTE: Requires Accessibility permissions for VS Code
            try:
                applescript = '''
                    tell application "OpenSCAD" to activate
                    delay 0.5
                    tell application "System Events"
                        key code 97
                    end tell
                '''
                result = subprocess.run(["osascript", "-e", applescript], 
                                       capture_output=True, text=True, check=False)
                if result.returncode == 0:
                    print("✓ Sent F6 to OpenSCAD (auto-render)")
                elif "1002" in result.stderr:
                    print("\n⚠️  Auto-render failed: Accessibility permission needed")
                    print("To enable: System Settings > Privacy & Security > Accessibility")
                    print("Add Visual Studio Code.app, then restart VS Code.\n")
                else:
                    print(f"Note: Could not auto-press F6: {result.stderr}")
            except Exception as e:
                print(f"Note: Could not auto-press F6: {e}")
                
        elif system == "Windows":
            # Windows: Use pyautogui if available, otherwise try pywinauto
            try:
                import pyautogui
                time.sleep(0.5)  # Extra wait for window focus
                pyautogui.press('f6')
                print("✓ Sent F6 to OpenSCAD (auto-render)")
            except ImportError:
                try:
                    # Try pywinauto as fallback
                    from pywinauto import Application
                    time.sleep(1)
                    app = Application(backend="uia").connect(title_re=".*OpenSCAD.*")
                    app.top_window().set_focus()
                    app.top_window().type_keys("{F6}")
                    print("✓ Sent F6 to OpenSCAD (auto-render)")
                except:
                    print("Note: Auto-render requires 'pyautogui' or 'pywinauto'")
                    print("Install with: pip install pyautogui")
                    
        elif system == "Linux":
            # Linux: Use xdotool (most reliable) or pyautogui as fallback
            try:
                # Try xdotool first (most reliable on Linux)
                result = subprocess.run(["xdotool", "search", "--name", "OpenSCAD", 
                                       "windowactivate", "key", "F6"],
                                      capture_output=True, text=True, check=False)
                if result.returncode == 0:
                    print("✓ Sent F6 to OpenSCAD (auto-render)")
                else:
                    raise Exception("xdotool not available")
            except:
                try:
                    # Fallback to pyautogui
                    import pyautogui
                    time.sleep(0.5)
                    pyautogui.press('f6')
                    print("✓ Sent F6 to OpenSCAD (auto-render)")
                except ImportError:
                    print("Note: Auto-render requires 'xdotool' or 'pyautogui'")
                    print("Install with: sudo apt install xdotool  (or)  pip install pyautogui")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
