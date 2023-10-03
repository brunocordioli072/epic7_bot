# Epic7 Bot Contributing Guide

Hi! We're really excited that you're interested in contributing to Epic7 Bot! Before submitting your contribution, please read through the following.

## Repo Setup

To develop locally, fork the Epic7 Bot repository and clone it in your local machine.

To develop and test the Epic7 Bot:

1. Run `npm run install` in Epic7 Bot root folder.

2. Run `npm run build:app:watch` in Epic7 Bot root folder.

3. Run `npm run dev:core` in in Epic7 Bot root folder on separate terminal.

## Pull Request Guidelines

- Checkout a topic branch from a base branch (e.g. `development`), and merge back against that branch.

- If adding a new feature:

  - Add accompanying test case.
  - Provide a convincing reason to add this feature. Ideally, you should open a suggestion issue first, and have it approved before working on it.

- If fixing a bug:

  - If you are resolving a special issue, add `(fix #xxxx[,#xxxx])` (#xxxx is the issue id) in your PR title for a better release log (e.g. `fix: update entities encoding/decoding (fix #3899)`).
  - Provide a detailed description of the bug in the PR. Live demo preferred.

- It's OK to have multiple small commits as you work on the PR. GitHub can automatically squash them before merging.