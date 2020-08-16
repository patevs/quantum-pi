# Python Template

> Template repository for `Python` projects.

---

## Links & Resources

* [`pyscaffold`](https://github.com/pyscaffold/pyscaffold) Python project template generator with batteries included.
  * [`pyscaffold-markdown`](https://github.com/pyscaffold/pyscaffoldext-markdown) PyScaffold extension which replaces reStructuredText by Markdown.
  * [`pyscaffold-pyproject`](https://github.com/pyscaffold/pyscaffoldext-pyproject) Simple PyScaffold extension adding a pyproject.toml file.

[](.)

* [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) CLI utility that creates projects from cookiecutters.
  * [`cookiecutter-pypackage`](https://github.com/audreyfeldroy/cookiecutter-pypackage) Cookiecutter template for a Python package.

---

## Pyscaffold

```bash
# Install pyscaffold
pip install pyscaffold
# Install extensions
pip install pyscaffoldext-markdown
pip install pyscaffoldext-pyproject
# Generate new project
putup my_project
cd my_project
# Setup project
python setup.py develop
# Create project with extensions
putup my_project --pyproject --markdown
```

## Cookiecutter

```bash
# Install cookiecutter
pip install --user cookiecutter
# Create project from the cookiecutter-pypackage.git repo template
# You'll be prompted to enter values.
# Then it'll create your Python package in the current working directory,
# based on those values.
$ cookiecutter https://github.com/audreyr/cookiecutter-pypackage
# For the sake of brevity, repos on GitHub can just use the 'gh' prefix
$ cookiecutter gh:audreyr/cookiecutter-pypackage
# Create project in the current working directory, from the local
# cookiecutter-pypackage/ template
$ cookiecutter cookiecutter-pypackage/
```

---

## Project Structure

```md
.
├── .commitlintrc.json
├── .editorconfig
├── .gitignore
├── .huskyrc
├── .np-config.json
├── LICENSE
├── package.json
└── README.md
```

---
