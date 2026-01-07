# Cookiecutter Basic Jupyter Template

[Cookiecutter Basic Jupyter](https://github.com/mpmansell/cookiecutter-basic-jupyter) template for a generic Jupyter Python workflow environment.

* GitHub repo:
* Free software: MIT license

## See TODO.md

- 'TODO.md` has a list of items to be done to improve this package

## Features

* Create working environment for a Jupyter Notebook (Python).
* Uses Poetry for environment management
* Provides Makefile to help access features.

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet:

```bash
pip install -U cookiecutter
```

### Step 1: Generate a Jupyter Python project:

```bash
cookiecutter https://github.com/mpmansell/cookiecutter-basic-jupyter.git
```

Follow the on screen prompts to configure the project per your specifications.

### Step 2: Install the Poetry environment

```bash
make install
```

### Step 3: Activate the virtual environment

Run the following command to get instructions for activating the newly created virtual environment:

```bash
make venv-activate
```

* For Windows this will be:

```powershell
Invoke-Expression (poetry env activate)
```

* For Bash in a Posix environment (Linux, Mac, Unix, etc):   (NOT for Git Bash - See below)

```bash
source `poetry env info --path`/bin/activate
```

* Git Bash is not supported since, when the OS is probed, it will identify as Windows

### Step 4: Check to see if the Virtual Environment is active

To ensure the virtual environmnet has actually be activated (and that you are not using the system default, which could be 'damaged' if you install modules), use the following command:

```bash
make show-env
```

This will show the path to the currently active Python executable and allow you to check that the default interpreter is not active. If it is, then the virtual environmnet has not been successfully activated.

### Step 5: Initialise the Git repository

To initialise the Git repo for this project, use:

```bash
make git-init
```

This will create and initialise the local repo, as well as adding all the freshly created files and making the initial commit.

Follow the Git documentation, or you GUI/development environment's instructions for creating a remote copy, and synchronising with it

### Step 6: Start Visual Studio Code with the default notebook:

Enter the following:

```bash
make run-notebook
```

## Makefile options

To see what options the `Makefile` provides, type the following:

```bash
make help
```

## This Template Isn't  Exactly What You Want?

Don't worry, you have options:

### Fork This / Create Your Own

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

### Or Submit a Pull Request

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.
