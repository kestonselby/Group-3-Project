# Contributions

This file records **what each member personally contributed**: the slice they own, and the
commit that proves they did each topic at each milestone. It is how your team proves the
per-student topic rule in [`MILESTONES.md`](MILESTONES.md), and it is what the TA reads at
every checkpoint.

Update it **before every checkpoint** (Weeks 4, 8, 12). Keep every milestone table in this
one file - do not delete the earlier ones; the history matters.

Use each member's full name as it appears in the team table in [`README.md`](README.md),
which is where GitHub usernames are recorded.

---

## Slices

Each member owns **one comparable feature**, built end to end across the term; every
milestone adds its new topics to *each* slice. Agree on these at Milestone 0 and fill them
in - the rest of this file is one row per member, per milestone, against their slice.

| Student | Slice (the feature they own) |
|---------|------------------------------|
| <name>  | <feature>                    |
| <name>  | <feature>                    |
| <name>  | <feature>                    |
| <name>  | <feature>                    |
| <name>  | <feature>                    |

<!-- Teams of four: delete the fifth row, here and in the tables below. -->

---

## How to fill in the milestone tables

In each cell, put a **commit hash** (e.g. `a1b2c3d`) - or, if your team is using them, a
**merged pull request** (e.g. `#14`) - **authored by that student** that demonstrates that
topic **in their own slice**.

- One commit or PR can fill two cells if it genuinely covers both topics (a function that
  also holds the feature's state, say).
- A **blank cell** means that student did not demonstrate that topic for that milestone,
  and loses **those individual marks** only - it does not drag down the rest of the team.
- Get a commit hash with `git log --oneline`, and check what a hash actually contains with
  `git show a1b2c3d`. The TA will.

Worked example:

| Student | Planning | Control flow | Collections | Functions |
|---------|----------|--------------|-------------|-----------|
| Alice   | a1b2c3d  | e4f5a6b      | e4f5a6b     | 9f8e7d6   |
| Bob     | b2c3d4e  | 1c2d3e4      | 1c2d3e4     | 7a6b5c4   |

---

## Milestone 1 - Core Prototype (Units 01-02)

| Student | Planning | Control flow | Collections | Functions |
|---------|----------|--------------|-------------|-----------|
| <name>  |          |              |             |           |
| <name>  |          |              |             |           |
| <name>  |          |              |             |           |
| <name>  |          |              |             |           |
| <name>  |          |              |             |           |

<!-- Optional but recommended: a line per member saying which function or file to look at. -->

## Milestone 2 - Practical Application (Unit 03)

| Student | OOP | File I/O | Recursion | Command-line args | Interface (TUI/GUI) |
|---------|-----|----------|-----------|-------------------|---------------------|
| <name>  |     |          |           |                   |                     |
| <name>  |     |          |           |                   |                     |
| <name>  |     |          |           |                   |                     |
| <name>  |     |          |           |                   |                     |
| <name>  |     |          |           |                   |                     |

## Milestone 3 - Final Product (Units 04-05)

| Student | Data structure | Algorithm strategy | Sockets | Concurrency |
|---------|----------------|--------------------|---------|-------------|
| <name>  |                |                    |         |             |
| <name>  |                |                    |         |             |
| <name>  |                |                    |         |             |
| <name>  |                |                    |         |             |
| <name>  |                |                    |         |             |
