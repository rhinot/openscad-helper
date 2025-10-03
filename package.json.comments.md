This file documents `package.json` entries for developers.

- name, displayName, description, version: Basic extension metadata.
- engines: VS Code engine compatibility.
- main: Path to the extension bundle that VS Code loads.
- contributes: Declares commands and keybindings exposed to VS Code.
- scripts: Helpful npm scripts used during development/publish.
- devDependencies: Packages required for building and testing the extension.

Note: JSON files do not support comments. Keep this sidecar near package.json
when you want to explain fields.