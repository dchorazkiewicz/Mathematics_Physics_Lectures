# ChatGPT working memory for this repository

This file records the working conventions that ChatGPT should follow when assisting with this repository.

## Default repository

Use this repository by default for all GitHub work:

```text
dchorazkiewicz/Lectures_notes_old_school
```

Do not use `dchorazkiewicz/Mathematics_Physics_Lectures` or any other repository unless the user explicitly asks for a different repository.

## Default branch

Use:

```text
main
```

unless the user explicitly asks for another branch.

## Path handling

The user will often provide paths relative to the repository root. Treat such paths as paths inside `dchorazkiewicz/Lectures_notes_old_school`.

For example, if the user provides:

```text
Phys/chapters/kinematics/velocity.tex
```

then the corresponding GitHub URL is:

```text
https://github.com/dchorazkiewicz/Lectures_notes_old_school/blob/main/Phys/chapters/kinematics/velocity.tex
```

For write operations use:

```text
repository_full_name: dchorazkiewicz/Lectures_notes_old_school
path: <relative path from repository root>
branch: main
```

## Repository tree

Before tasks that depend on locating files or understanding the repository structure, read:

```text
https://github.com/dchorazkiewicz/Lectures_notes_old_school/blob/main/tree.txt
```

The file is named `tree.txt`. If a `tree.md` file is later added and the user explicitly points to it, use that instead.

## Standard workflow before editing files

1. Read `tree.txt` from the repository root.
2. Resolve any user-provided relative path against the root of `dchorazkiewicz/Lectures_notes_old_school`.
3. Fetch the target file using the full GitHub URL when helpful.
4. Modify only the requested file or requested section.
5. Commit to `main` unless the user says otherwise.
6. Do not switch repositories unless the user explicitly instructs it.
