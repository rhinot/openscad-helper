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
 - On macOS the script will automatically press F6 (render) using AppleScript
   after opening the GUI. No additional dependencies required.
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

    # Launch the OpenSCAD GUI for interactive editing/preview. Using
    # Popen allows the script to continue running without waiting for the
    # GUI process to exit.
    try:
        subprocess.Popen(["openscad", scad_file])
    except FileNotFoundError:
        print("Error: 'openscad' not found in PATH. Please install OpenSCAD.")
        return 3

    # Give the GUI a moment to create its window before attempting any
    # automation (macOS F6 press below).
    time.sleep(2)

    # On macOS, use AppleScript to activate OpenSCAD and press F6 to render.
    # This is more reliable than pyautogui and doesn't require extra dependencies.
    if platform.system() == "Darwin":
        try:
            # AppleScript to activate OpenSCAD and send F6 keystroke
            applescript = '''
                tell application "OpenSCAD" to activate
                tell application "System Events"
                    keystroke "6" using {function down}
                end tell
            '''
            subprocess.run(["osascript", "-e", applescript], check=False)
            print("Sent F6 to OpenSCAD (auto-render)")
        except Exception as e:
            print(f"Note: Could not auto-press F6: {e}")

    # If the user requested a headless build, run OpenSCAD's command line
    # exporter to create a .3mf and then attempt to open it in OrcaSlicer.
    if do_build:
        subprocess.run(["openscad", "-o", out_3mf, scad_file])

        system = platform.system()
        if system == "Darwin":
            # macOS: use the `open` utility to launch the application with the file
            subprocess.run(["open", "-a", "OrcaSlicer", out_3mf])
        elif system == "Windows":
            # Windows: `start` is a shell built-in, so run via shell=True
            subprocess.run(["start", "", "OrcaSlicer.exe", out_3mf], shell=True)
        else:
            # Linux/other: assume orca-slicer is on PATH
            subprocess.run(["orca-slicer", out_3mf])

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
