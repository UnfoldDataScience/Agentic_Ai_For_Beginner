## Securely Managing API Keys with a `.env` File

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
    ```python
    import os
    from dotenv import load_dotenv 

    # This command loads the variables from the .env file (Given .env is present in same folder)
    env_path = r'.env full path here'
    load_dotenv(env_path)

    #sample code for above step(commented intentionally - please note, you need to give full path if .env is not present in same folder from where you are running this code)
    #env_path = r'E:\YTReusable\.env'
    #load_dotenv(env_path)

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
