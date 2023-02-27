# Changelog

## 1.2.2 (2023-02-27)

- (PR #44, 2023-02-08) chore: bump tox from 3.27.1 to 4.4.4
- (PR #46, 2023-02-08) chore: bump isort from 5.10.1 to 5.12.0
- (PR #45, 2023-02-08) chore: bump black from 22.12.0 to 23.1.0
- (PR #56, 2023-02-08) chore: bump cryptography from 38.0.3 to 39.0.1
- (PR #43, 2023-02-09) chore: bump flake8 from 4.0.1 to 6.0.0
- (PR #58, 2023-02-13) Improve Super-Linter GitHub Actions workflow
- (PR #59, 2023-02-13) Add Make files to cache key used for Python dependencies in CI/CD
- (PR #60, 2023-02-13) Get PyPI username from GitHub Actions variable instead of secret
- (PR #61, 2023-02-13) Fix deprecation of GitHub Actions `set-output`
- (PR #62, 2023-02-13) Pin versions of actions used in GitHub Actions workflows
- (PR #63, 2023-02-13) Remove unnecessary permissions from GitHub Actions workflows
- (PR #66, 2023-02-13) Update CI/CD information in readme
- (PR #65, 2023-02-17) chore: bump tox from 4.4.4 to 4.4.5
- (PR #67, 2023-02-19) Change cache key of release & deploy workflows to match CI workflow

## 1.2.1 (2023-02-07)

- (PR #31, 2023-01-26) chore: bump certifi from 2022.6.15 to 2022.12.7
- (PR #40, 2023-01-26) Add GitHub Dependency Review
- (PR #34, 2023-01-26) chore: bump black from 22.10.0 to 22.12.0
- (PR #41, 2023-01-26) Improve GitHub Dependency Review
- (PR #42, 2023-01-27) Update Markdownlint configuration
- (PR #39, 2023-02-03) chore: bump coverage from 6.5.0 to 7.1.0
- (PR #47, 2023-02-03) Enable Python dependency sync check for Python 3.8
- (PR #48, 2023-02-06) Refactor CI/CD workflows
- (PR #49, 2023-02-06) fix: Add missing permissions to CI/CD workflow
- (PR #50, 2023-02-07) Improve selection of deployment environment in CI/CD workflow
- (PR #51, 2023-02-07) Add missing parameter to CI/CD workflow
- (PR #52, 2023-02-07) Create GitHub release from CI/CD workflow
- (PR #53, 2023-02-07) Add GitHub environment to CI/CD workflow


## 1.2.0 (2023-01-05)

- (PR #15, 2022-08-09) chore: Improve Git commit linter
- (PR #16, 2022-08-11) chore: Add code owners
- (PR #17, 2022-08-29) Add information dashboard to readme
- (PR #18, 2022-09-06) chore: bump black from 22.6.0 to 22.8.0
- (PR #19, 2022-09-08) chore: bump coverage from 6.4.2 to 6.4.4
- (PR #22, 2022-10-19) chore: bump mypy from 0.971 to 0.981
- (PR #21, 2022-10-19) chore: bump tox from 3.25.1 to 3.26.0
- (PR #20, 2022-10-21) chore: bump coverage from 6.4.4 to 6.5.0
- (PR #23, 2022-11-02) chore: bump mypy from 0.981 to 0.982
- (PR #24, 2022-11-02) chore: bump black from 22.8.0 to 22.10.0
- (PR #25, 2022-11-02) chore: bump tox from 3.26.0 to 3.27.0
- (PR #26, 2022-11-23) fix: Fix Dependabot error pip.….Error: Constraints cannot have extras
- (PR #27, 2022-11-23) chore: bump cryptography from 37.0.4 to 38.0.3
- (PR #30, 2022-12-05) chore: bump twine from 4.0.1 to 4.0.2
- (PR #29, 2022-12-05) chore: bump mypy from 0.982 to 0.991
- (PR #28, 2022-12-06) chore: bump tox from 3.27.0 to 3.27.1
- (PR #36, 2023-01-04) chore: Add support for Python 3.10


## 1.1.0 (2022-07-28)

- (PR #12, 2022-07-28) fix: Do not ignore environment variable `TOXENV` in Makefile
- (PR #9, 2022-07-28) Add entity 'RUC' (“Registro Único de Contribuyente”)


## 1.0.0 (2022-07-28)

- (PR #1, 2022-07-27) chore: Add Editor Configuration
- (PR #3, 2022-07-27) chore: Add CI workflows
- (PR #4, 2022-07-27) chore: Add Git Ignore
- (PR #5, 2022-07-27) chore: Manage Python dependencies with Pip Tools
- (PR #2, 2022-07-27) chore: Add software license
- (PR #6, 2022-07-27) chore: Add base Make tasks
- (PR #7, 2022-07-27) fix: Add missing base Make tasks
- (PR #8, 2022-07-28) Set up base project
- (PR #10, 2022-07-28) chore: Set package version in variable `cordada.pe_sunat.__version__`
