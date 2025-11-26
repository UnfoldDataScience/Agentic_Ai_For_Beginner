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

### Part A: Generate Your OpenAI API Key

1.  **Create an Account:**
    * Go to the **[OpenAI Platform website](https://platform.openai.com/)** and sign up or log in. You may need to verify your phone number.
2.  **Navigate to API Keys:**
    * Once logged in, click on your profile icon (or the navigation menu) and select **"View API keys"** or go to the **[API Keys page](https://platform.openai.com/api-keys)**.
3.  **Create a New Key:**
    * Click the **"+ Create new secret key"** button. 
    * Give your key a descriptive name (e.g., `course-project-key`).
4.  **Copy and Save Immediately:**
    * Click **"Create secret key"**. Your key will be displayed **only once**.
    * **Immediately copy and paste this key** into a temporary, secure document. You will use it in the next step. If you lose it, you must generate a new one.
5.  **Add Billing (Required for Usage):**
    * The key will not work until you have a payment method on file (even for small amounts of usage). Navigate to the **Billing** section to add a payment method and set a usage limit (recommended for safety).

### Part B: Setup the `.env` File

1.  **Create the `.env` File:**
    * Open the main folder for this course repository on your computer.(Or any other folder if you wish to)
    * Inside this main folder, create a **new file** and name it **`.env`** (it must have **no extension** like `.txt`).

2.  **Add Your API Key:**
    * Open the newly created **`.env`** file with a text editor.
    * Store your key using the `KEY=VALUE` format. Paste the key you copied in the previous step:

    ```
    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    ```
    * **Crucial:** Do not use quotes around the key value. Save and close the file.

3.  **Accessing the Key in Code:**
    * The Python code in this course will automatically read the key from the `.env` file for secure use (Just ensure you give the right path)
  
The video, [OpenAI: How To Generate API Keys](https://www.youtube.com/watch?v=Lj43aSwNpog), provides a visual walkthrough of the process for generating, saving, and managing your OpenAI API keys.

## 3. Final Setup Test: Running Code and Checking Keys

This test ensures that your Jupyter environment is working and that the API key is being loaded correctly from your `.env` file.

1.  **Launch Jupyter:**
    * Open **Anaconda Navigator** and launch **Jupyter Notebook**. (Alternative via command prompt)

2.  **Open or Create a Notebook:**
    * Click **New** in the top-right corner and select **Python 3** (or the kernel you installed) to create a new notebook.

3.  **Run the Test Code:**
    * Open your terminal or Anaconda Prompt and run the following command:
    pip install python-dotenv

    *Now, In the first code cell of Jupyter notebbok, paste the following Python code:

    ```python
    import os
    from dotenv import load_dotenv 

    # This command loads the variables from the .env file
    load_dotenv() 

    # We now try to get the API key
    api_key = os.getenv("OPENAI_API_KEY")

    if api_key:
        print("Success! Your OpenAI API key was loaded correctly.")
        print(f"Key starts with: {api_key[:5]}...")
    else:
        print("Failure! The key was NOT loaded. Please check your .env file.")
        print("Make sure you are running the notebook from the same directory as the .env file.")
    ```

    * Click the **Run** button (or press `Shift + Enter`) to execute the code.

5.  **Verify the Output:**
    * **Success** will look like this (you should see the first 5 characters of your key):
        ```
        Success! Your OpenAI API key was loaded correctly.
        Key starts with: sk-xx...
        ```
    * **Failure** means you need to re-check the spelling of the file (`.env`), the variable name (`OPENAI_API_KEY`), and that the notebook is running in the correct location.

Congratulations! If you see the **Success** message, your environment is ready for the course!
