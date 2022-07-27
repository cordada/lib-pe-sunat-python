/*
Commitlint Configuration

Commitlint is a Git commit message linter.

- Web site: https://commitlint.js.org/
- Documentation: https://github.com/conventional-changelog/commitlint#readme
*/

module.exports = {
  extends: ["@commitlint/config-conventional"],

  /*
  Rules

  Documentation:
  https://github.com/conventional-changelog/commitlint/blob/v17.0.3/docs/reference-rules.md
  */
  rules: {
    "body-max-line-length": [1, "always", 100],
    "header-max-length": [2, "always", 72],
    "subject-case": [1, "always", ["sentence-case"]],
    "trailer-exists": [1, "always", "Ref:"],
    "type-enum": [2, "always", ["chore", "feat", "fix"]],
  },
};
