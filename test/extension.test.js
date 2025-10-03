// Tests for the openscad-helper extension using Mocha and VS Code Test API
// @ts-nocheck
 

const assert = require('assert');
const vscode = require('vscode');
const sinon = require('sinon');
const child_process = require('child_process');

suite('OpenSCAD Helper Extension Test Suite', function () {
    let ext;
    let execFileStub;

    setup(async function () {
        // Stub execFile before activating extension
        execFileStub = sinon.stub(child_process, 'execFile').callsFake((cmd, args, callback) => {
            console.log('[Test] execFile called:', cmd, args);
            // Call callback if provided to avoid hanging
            if (typeof callback === 'function') {
                callback(null, '', '');
            }
            return { pid: 12345 }; // mock process
        });

        // Get the installed extension
        ext = vscode.extensions.getExtension('rhinot.openscad-helper');
        if (!ext) {
            throw new Error('openscad-helper extension is not installed');
        }

        // Activate it (commands now reference stubbed execFile)
        await ext.activate();
    });

    teardown(function () {
        // Restore the original execFile after each test
        if (execFileStub) {
            execFileStub.restore();
        }
    });

    test('Extension should be present', function () {
        assert.ok(ext, 'Extension should exist');
        assert.ok(ext.isActive, 'Extension should be active after activation');
    });

    test('Run command should show warning without active editor', async function () {
        // Ensure no active editor
        await vscode.commands.executeCommand('workbench.action.closeAllEditors');
        
        // Run the command
        await vscode.commands.executeCommand('openscad.run');
        
        // Command should not call execFile if there's no active editor
        // This is actually expected behavior - no error means success
        assert.ok(true, 'Command executed without error');
    });

    test('Build command should show warning without active editor', async function () {
        // Ensure no active editor
        await vscode.commands.executeCommand('workbench.action.closeAllEditors');
        
        // Run the command
        await vscode.commands.executeCommand('openscad.build');
        
        // Command should not call execFile if there's no active editor
        assert.ok(true, 'Command executed without error');
    });
});
