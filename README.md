# Selenium Automation Project

## Project Overview

This project is a Python-based automation script using the Selenium WebDriver to perform a series of actions on a website. The script is designed to create accounts on a platform, providing the necessary information for each account from a CSV file.

## Requirements

- Python 3.x
- Selenium WebDriver
- pandas
- tkinter

## Setup

1. **Install Dependencies:**
    ```bash
    pip install selenium pandas
    ```

2. **WebDriver:**
    - Download the ChromeDriver WebDriver from [here](https://sites.google.com/chromium.org/driver/).
    - Ensure the WebDriver executable is in your system's PATH or update the `webdriver.Chrome()` call in the script with the path to the executable.

3. **CSV Files:**
    - Prepare two CSV files:
        - `self_information.csv`: Contains the information required for account creation.
        - `accounts.csv`: Contains the list of accounts and their corresponding verification links.

## Running the Script

1. **Run the Script:**
    ```bash
    python script.py
    ```
    The script will launch a GUI window with a "Start" button.

2. **Start the Automation:**
    - Click the "Start" button to initiate the account creation process.

3. **Monitor Progress:**
    - The script will loop through the accounts, providing real-time updates on the console.

4. **Completion:**
    - Once all accounts have been processed, the script will print "End."

## Troubleshooting

- If the script encounters any issues during execution, error messages will be printed to the console, providing details about the problem.

## Notes

- The script uses the Chrome browser by default. Ensure compatibility if using a different browser.

- The script is designed for educational purposes and should be used responsibly and in compliance with the terms of service of the target website.
