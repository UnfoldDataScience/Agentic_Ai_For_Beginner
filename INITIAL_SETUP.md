## 🚀 Initial Course Environment Setup

This guide will walk you through the two essential steps needed to start working with this course repository: **setting up your Python environment using Anaconda/Jupyter** and **securely managing your API keys**.

---

## 1. Setting up Python and Jupyter with Anaconda

We will use **Anaconda**, a popular distribution for data science, which includes **Python** and the **Jupyter Notebook** environment we'll use for coding.

### Step-by-Step Installation

1.  **Download Anaconda:**
    * Go to the official **[Anaconda Distribution website](https://www.anaconda.com/download)**.
    * Find the installer for your operating system (Windows, macOS, or Linux). Ensure you select the **latest Python version** (e.g., Python 3.11 or newer).
    * Download the installer file.

2.  **Run the Installer:**
    * Locate the downloaded file and run it.
    * Follow the prompts. For most steps, the **default settings are fine**.
    * On the **Advanced Installation Options** screen, it's generally recommended to **leave the "Add Anaconda to your PATH environment variable" unchecked** unless you are an advanced user.

3.  **Verify the Installation:**
    * Once complete, search for and open the **Anaconda Navigator** program.
    * Inside the Navigator, find the **Jupyter Notebook** tile.
    * Click the **"Launch"** button under **Jupyter Notebook**. This should open a new tab in your web browser.
    * Alternatively you can enter command **jupyter notebook** in command prompt to launch Jupyter notebook

4.  **Close Jupyter:**
    * Close the browser tab. To completely stop the server, close the **command line/terminal window** that opened when you launched Jupyter.

You are now ready to run Python code and use Jupyter Notebooks!

---

## 2. Securely Managing API Keys with a `.env` File

It is crucial **never to save your secret API key directly in your code files**. We use a special file called **`.env`** (for "environment") to securely store these keys.

### Step-by-Step `.env` Setup

1.  **Create the `.env` File:**
    * Open the main folder for this course repository on your computer. (You can use any other folder as well)
    * Inside this main folder, create a **new file** and name it **`.env`** (it must have **no extension** like `.txt`).

2.  **Add Your API Key:**
    * Open the newly created **`.env`** file with a text editor.
    * Store your key using the `KEY=VALUE` format. For an OpenAI key, it should look like this (replace the placeholder):

    ```
    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ```
    * **Crucial:** Do not use quotes around the key value. Save and close the file.

3.  **Accessing the Key in Code:**
    * The Python code in this course will automatically read the key from the `.env` file for secure use. (Ensure to give right path)

