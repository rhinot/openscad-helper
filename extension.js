// VS Code extension entry point for the OpenSCAD helper.
// This file registers two commands with VS Code:
//  - openscad.run  -> Open the current .scad file in the OpenSCAD GUI
//  - openscad.build -> Run a headless build that exports a .3mf and opens OrcaSlicer
// The heavy lifting is delegated to the bundled Python helper script `run_scad.py`.

const vscode = require("vscode");
const { execFile } = require("child_process");
const path = require("path");

// activate is called when the extension is first used. We register commands here
function activate(context) {
    // Path to the helper Python script that does the OpenSCAD launching/building
    const scriptPath = path.join(context.extensionPath, "run_scad.py");

    // Register the "Run" command which opens OpenSCAD GUI for the active file.
    // It shows a warning if no editor/file is active.
    let runCmd = vscode.commands.registerCommand("openscad.run", () => {
        console.log("[OpenSCAD Helper] RUN command triggered");
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showWarningMessage("No active SCAD file to run.");
            return;
        }
        const file = editor.document.fileName;

        // Spawn the helper script with python3 and the current file path.
        // execFile is used to avoid spawning a shell.
        execFile("python3", [scriptPath, file]);

        // Notify the user that the GUI was launched (and macOS automation will run
        // if pyautogui is available on the user's Python environment).
        vscode.window.showInformationMessage(
            "OpenSCAD GUI launched. macOS auto-render if pyautogui is installed."
        );
    });

    // Register the "Build" command which runs the helper script with --build.
    // This performs a headless export to .3mf and then tries to open OrcaSlicer.
    let buildCmd = vscode.commands.registerCommand("openscad.build", () => {
        console.log("[OpenSCAD Helper] BUILD command triggered");
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            vscode.window.showWarningMessage("No active SCAD file to build.");
            return;
        }
        const file = editor.document.fileName;

        // Run the helper script in build mode.
        execFile("python3", [scriptPath, file, "--build"]);
        vscode.window.showInformationMessage(
            "Build started: 3MF export + OrcaSlicer."
        );
    });

    // Add registered disposables to the extension context so they are cleaned up
    // when the extension is deactivated/unloaded.
    context.subscriptions.push(runCmd, buildCmd);
}

// Optional deactivate hook - left intentionally empty as there is no cleanup
// required beyond the command disposables above.
function deactivate() {}

module.exports = {
    activate,
    deactivate,
};
