# Setup Guide

Follow these steps to set up the HSA Digital Shoebox project on your local machine.

## Step 1: Clone the Repository to Your Computer

Instead of creating a new folder, you will link your local machine to your GitHub account.

- Open VS Code.
- Press Ctrl + Shift + P to open the Command Palette.
- Type "Git: Clone" and paste your repository URL: https://github.com/haitaow2009/HSA-Digital-Shoebox.git.
- Choose a folder on your computer to save it and click Open when prompted.

## Step 2: Set Up an Isolated Development Environment

Professional projects use Virtual Environments to keep dependencies clean and version-controlled.

- Open the VS Code terminal (Terminal > New Terminal).
- Create the environment:
  - Windows: `python -m venv .venv`
  - Mac/Linux: `python3 -m venv .venv`
- Activate it:
  - Windows: `.venv\Scripts\activate`
  - Mac/Linux: `source .venv/bin/activate`
- Select Interpreter: Press Ctrl + Shift + P, type "Python: Select Interpreter", and choose the one labeled with (.venv).

## Step 3: Create Professional Project Files

To make your repository stand out to interviewers, you need a clean structure.

- `main.py`: The entry point for your code.
- `hsa_data.csv`: Your "Digital Shoe-box" database file (created automatically by your code later).
- `.gitignore`: This is crucial. Create this file and add the text `.venv/` inside it. This prevents your local environment files from being uploaded to GitHub.
- `requirements.txt`: A file to list your project's libraries.

## Step 4: Write Your Initial Code Logic

## Step 5: Push Your Changes to GitHub

- Sync your local work with your online repository.
- Click the Source Control icon (on the left sidebar).
- Click the + icon next to your files to "Stage" them.
- Type a commit message like `feat: initial HSA logging logic`.
- Click Commit, then click Sync Changes to upload your work to GitHub.
