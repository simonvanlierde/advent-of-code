# Security

## Report a vulnerability

Report it privately, through
[a GitHub security advisory](https://github.com/simonvanlierde/advent-of-code/security/advisories/new)
or by email to <90462640+simonvanlierde@users.noreply.github.com>. Don't open a public issue or pull request for it:
anyone can read those before there is a fix.

Please include:

- What the problem is and where it is: a file, a function or a dependency.
- Steps to reproduce it, or a proof of concept.
- The impact you expect, and the version or commit you saw it in.

I acknowledge a report within 14 days, then tell you whether I can reproduce it and when I
expect a fix.

## Fixes and disclosure

A fix lands on `main`. When it is in, I publish the GitHub security advisory for it and
credit you unless you'd rather not be named.

## Scope

In scope:

- The code in `src/` and the notebooks, including how they read the `AOC_SESSION`
  cookie from `.env`.
- The CI workflow in `.github/workflows`.
- The dependencies in `uv.lock`, when the problem affects this project.

Out of scope:

- A problem in a dependency that doesn't affect this project. Report it upstream.
