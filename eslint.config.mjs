// ESLint configuration used by the project. This file sets up a minimal set
// of warnings instead of errors so the extension development experience is
// forgiving during early development while still surfacing common problems.

import globals from "globals";

export default [{
    // Apply to all JavaScript files in the workspace
    files: ["**/*.js"],
    languageOptions: {
        // Provide common global variables used by Node, CommonJS and Mocha tests
        globals: {
            ...globals.commonjs,
            ...globals.node,
            ...globals.mocha,
        },

        // Modern JS features are allowed (ES2022)
        ecmaVersion: 2022,
        sourceType: "module",
    },

    // A small rule-set configured as warnings to guide developers without
    // failing builds during development.
    rules: {
        "no-const-assign": "warn",
        "no-this-before-super": "warn",
        "no-undef": "warn",
        "no-unreachable": "warn",
        "no-unused-vars": "warn",
        "constructor-super": "warn",
        "valid-typeof": "warn",
    },
}];