const path = require('path');
const { runTests } = require('@vscode/test-electron');

async function main() {
  try {
    // Path to your extension's root
    const extensionDevelopmentPath = path.resolve(__dirname, '..');

    // Path to the test runner (this is your test entry file)
    const extensionTestsPath = path.resolve(__dirname, './suite/index');

    // Download VS Code, unzip it and run the integration test
    await runTests({ extensionDevelopmentPath, extensionTestsPath });
  // eslint-disable-next-line no-unused-vars
  } catch (err) {
    console.error('Failed to run tests');
    process.exit(1);
  }
}

main();
