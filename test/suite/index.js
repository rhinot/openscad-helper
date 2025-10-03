// test/suite/index.js
const path = require('path');
const Mocha = require('mocha');

function run() {
  const mocha = new Mocha({ ui: 'tdd', color: true }); // TDD -> suite/test

  // Directly load your single test file
  const testFile = path.resolve(__dirname, '../extension.test.js');
  mocha.addFile(testFile);

  return new Promise((resolve, reject) => {
    try {
      mocha.run(failures => {
        if (failures > 0) {
          reject(new Error(`${failures} tests failed.`));
        } else {
          resolve();
        }
      });
    } catch (err) {
      reject(err);
    }
  });
}

module.exports = { run };
