# ChatGPT GitHub connector setup for this repository

This document describes the configuration and working rules required for ChatGPT to reliably read and write files in this repository.

## Repository to use

The default repository for this project is:

```text
dchorazkiewicz/Lectures_notes_old_school
```

ChatGPT must not use `dchorazkiewicz/Mathematics_Physics_Lectures` or any other repository unless the user explicitly requests that.

The default branch is:

```text
main
```

## Required GitHub App configuration

The ChatGPT Codex Connector / GitHub App must be installed for the GitHub account:

```text
dchorazkiewicz
```

The repository access setting should be configured as:

```text
All repositories
```

This setting is important. In this setup, selecting only `dchorazkiewicz/Lectures_notes_old_school` may allow reading but can still cause write operations such as `create_file` or `update_file` to fail with:

```text
403 Resource not accessible by integration
```

With `All repositories` enabled, write access was confirmed by successfully creating a file in `dchorazkiewicz/Lectures_notes_old_school`.

## Required permissions

The GitHub App must have:

```text
Read and write access to code
```

This permission is required for operations that modify repository contents, including:

- creating files,
- updating files,
- deleting files,
- committing changes through the connector.

The app may also show read/write access to actions, issues, pull requests, and workflows. For ordinary file edits, the critical permission is write access to code / contents.

## Path handling rules

The user often provides paths relative to the repository root. These paths must be resolved against:

```text
dchorazkiewicz/Lectures_notes_old_school
```

For example, if the user provides:

```text
Phys/chapters/kinematics/velocity.tex
```

then the full GitHub URL is:

```text
https://github.com/dchorazkiewicz/Lectures_notes_old_school/blob/main/Phys/chapters/kinematics/velocity.tex
```

For write operations, use:

```text
repository_full_name: dchorazkiewicz/Lectures_notes_old_school
path: Phys/chapters/kinematics/velocity.tex
branch: main
```

Do not prefix paths with another repository name. Do not switch to another repository unless explicitly instructed.

## Repository tree file

Before tasks that depend on locating files, understanding the project layout, or resolving relative paths, read:

```text
https://github.com/dchorazkiewicz/Lectures_notes_old_school/blob/main/tree.txt
```

The repository tree file is currently named:

```text
tree.txt
```

If a `tree.md` file is later added and the user explicitly points to it, use that file instead.

## Standard working procedure

Before editing or locating files:

1. Read `tree.txt` from the repository root.
2. Treat user-provided file paths as relative to the root of `dchorazkiewicz/Lectures_notes_old_school`.
3. Build full GitHub URLs using `https://github.com/dchorazkiewicz/Lectures_notes_old_school/blob/main/` plus the relative path.
4. Fetch the target file before editing.
5. Modify only the requested file or requested section.
6. Commit to `main` unless the user explicitly requests another branch.
7. Avoid unrelated changes.
8. Do not use other repositories unless explicitly requested.

## Write-access verification

A simple write test can be done by creating a small temporary file in the repository root, for example:

```text
tmp_write_check.md
```

using:

```text
repository_full_name: dchorazkiewicz/Lectures_notes_old_school
branch: main
```

If this returns:

```text
403 Resource not accessible by integration
```

then the GitHub App configuration should be checked. The known working configuration is:

```text
Repository access: All repositories
Permissions: Read and write access to code
```

After the test, temporary test files should be removed unless the user wants to keep them.
