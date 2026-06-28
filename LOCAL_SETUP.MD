# Local Development Environment Setup

This guide explains how to set up a local Python environment for all coding projects in this course.

> **Recommended Python Version:** Python 3.12.x

**Last Updated:** June 2026

---

# Quick Start

Follow these steps to get your local environment ready:

1. Install Python 3.12.x
2. Install Visual Studio Code (VS Code)
3. Install the Python extension for VS Code
4. Download the resources for the current course section
5. Create a virtual environment
6. Install the section-specific `requirements.txt`
7. Open the notebook and start coding

---

# Course Structure

Each coding section in this course is designed as an **independent project**.

Every section includes its own:

* Notebook(s)
* Python script(s) (where applicable)
* `requirements.txt`
* Supporting resources

Before starting a new coding section, simply repeat the environment setup using that section's `requirements.txt`.

This approach minimizes dependency conflicts and makes the course easier to maintain as AI libraries evolve.

---

# Step 1 - Install Python

Download Python from the official website:

https://www.python.org/downloads/

During installation:

* ✅ Check **Add Python to PATH**
* ✅ Click **Install Now**

---

# Step 2 - Verify Python Installation

Open Command Prompt (Windows) or Terminal (macOS/Linux).

Run:

```bash
python --version
```

or

```bash
python3 --version
```

Expected output:

```text
Python 3.12.x
```

If Python is not recognized, restart your terminal or computer.

If the issue persists, reinstall Python and ensure **Add Python to PATH** was selected during installation.

---

# Step 3 - Install Visual Studio Code

Download Visual Studio Code from:

https://code.visualstudio.com/

Install it using the default settings.

---

# Step 4 - Install the Python Extension

Open VS Code.

Go to:

**Extensions** (`Ctrl + Shift + X`)

Search for:

```text
Python
```

Install the official **Python** extension published by Microsoft.

This extension provides:

* Python support
* Jupyter Notebook support
* Debugging
* IntelliSense
* Environment management

---

# Step 5 - Download the Course Resources

Download the resources for the current course section from Udemy.

Extract the ZIP file.

Open the section folder in VS Code.

You should see files similar to:

* Notebook(s)
* Python script(s)
* `requirements.txt`
* README.md
* Supporting resources

---

# Step 6 - Open the Integrated Terminal

In VS Code, open:

**Terminal → New Terminal**

All remaining commands will be executed from this terminal.

---

# Step 7 - Create a Virtual Environment

Run:

```bash
python -m venv .venv
```

This creates an isolated Python environment for the current section.

---

# Step 8 - Activate the Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Once activated, you should see the virtual environment name (typically `.venv`) displayed at the beginning of your terminal prompt.

---

# Step 9 - Install the Required Packages

Install the dependencies for the current section.

```bash
pip install -r requirements.txt
```

This installs all Python packages required for that section.

Because each coding section is maintained independently, always install the `requirements.txt` included with the current section.

The installation may take a few minutes depending on your internet connection.

---

# Step 10 - Select the Python Interpreter

In VS Code:

1. Press **Ctrl + Shift + P**
2. Search for **Python: Select Interpreter**
3. Select the interpreter from the `.venv` folder you just created.

You should now see the selected interpreter displayed in the bottom-right corner of VS Code.

---

# Step 11 - Open the Notebook

Open the notebook included with the current section.

When prompted, select the kernel associated with your virtual environment.

Run the notebook cells sequentially from top to bottom.

If the first few cells execute successfully, your environment is ready.

---

# Troubleshooting

## Python is not recognized

Try:

```bash
python3 --version
```

If the issue persists:

* Restart your terminal or computer.
* Reinstall Python.
* Ensure **Add Python to PATH** was selected during installation.

---

## Package installation fails

Ensure that:

* Your virtual environment is activated.
* You are running the command from the correct project folder.

Then run:

```bash
pip install -r requirements.txt
```

---

## Wrong Python Interpreter

If VS Code selects the wrong interpreter:

1. Press **Ctrl + Shift + P**
2. Search for **Python: Select Interpreter**
3. Select the interpreter from the `.venv` folder.

---

# Frequently Asked Questions

### Can I use PyCharm instead of VS Code?

Yes. Any Python IDE can be used.

---

### Can I use Jupyter Notebook?

Yes. The notebooks are standard Jupyter notebooks.

---

### Can I use Anaconda?

Yes. However, the examples in this course use standard Python virtual environments.

---

### Do I need to create a new virtual environment for every section?

Yes, this is recommended.

Each coding section is maintained independently and includes its own `requirements.txt`. Using a separate virtual environment for each section helps avoid dependency conflicts and ensures the projects run as tested.

---

# Next Steps

Your local development environment is now ready.

For every new coding section:

1. Open the section folder.
2. Create (or activate) its virtual environment.
3. Install the section's `requirements.txt`.
4. Run the notebook or Python scripts.

Happy Learning!
