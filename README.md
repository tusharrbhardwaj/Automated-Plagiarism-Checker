# Plagiarism Report Automation Toolkit

This Python script is an all-in-one automation and file-processing solution that helps users:
- 🔀 Split large documents for free plagiarism checking
- 🔁 Automate online plagiarism checkers
- 🧾 Merge generated reports into a single professional PDF
- 🧷 Convert between `.docx`, `.txt`, and PDF formats

Built for users who need a lightweight, free way to handle plagiarism checking in large documents using publicly available online tools.



## Problems Faced and Solutions

| Problem                                                                                  |Solution Implemented                                                                 |
|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Most free plagiarism tools like Duplichecker have a **word limit (~1000)** per check     | Script splits the original `.docx` file into multiple `.txt` files containing ≤800 words to stay within the limit |
| Uploading content and downloading reports manually was **time-consuming and repetitive** | Used `Selenium` and `pynput` to automate form filling, uploading, and downloading reports |
| Each check generated a separate PDF report, which became messy                           | Used `PyPDF2` and `fpdf` to merge all individual reports into one clean, professional document |
| Copy-pasting content into the online form repeatedly was error-prone                     | Used `pyperclip` to handle clipboard operations and avoid manual errors                 |
| Files were getting disorganized                                                          | Script creates dedicated folders (`chunks/`, `reports/`) to keep files properly sorted  |

---

## Features

- **File Splitting**: Breaks large `.docx` documents into smaller chunks (~800 words each) for easier plagiarism checking.
- **Browser Automation**: Automates the process of uploading each chunk to an online tool using `Selenium`.
- **Clipboard Control**: Uses `pynput` and `pyperclip` to paste content seamlessly into web forms.
- **PDF Handling**: Merges plagiarism reports into a single, professional-looking file using `PyPDF2` and `fpdf`.
- **Auto Folder Management**: Automatically creates directories to keep things organized.

---

## Installation

### Requirements

Before running the script, make sure you have **Python 3.8+** installed.

### Required Python Libraries

You can install all required dependencies using pip:

```bash
pip install docx2txt selenium pynput pyperclip fpdf PyPDF2 webdriver-manager
```
## How It Works

###Step-by-Step Flow:

Prompt for File Name: The script asks for the name of the .docx file to split.

Conversion & Splitting: Converts .docx to .txt.

Splits the text into chunks of ~800 words.

Browser Automation: Opens Chrome browser via Selenium.

Automatically pastes content into a free plagiarism checker (e.g., Duplichecker).
Waits for results and downloads the PDF report.

File Management: Moves individual reports to a dedicated folder.
Merges all individual reports into a single PDF.

Final Output: A clean, professional PDF file named {your-file-name}-Plagiarism-Report.pdf.

## Folder Structure
```
📁 Your Folder
├── main.py
├── your_input_file.docx
├── filename/           # (Auto-created) Contains text chunks for checking
├── pdffolder/          # (Auto-created) Contains individual PDF reports
└── Duplichecker-Plagiarism-Report.pdf
```


# Use Cases

1. Academic paper checks before submission.
2. Freelancers verifying originality of content.
3. Teachers checking multiple student submissions.

# Notes & Considerations

## Browser Settings:
The current script uses a hardcoded Chrome profile path. Update the following line to your own profile path:
``` options.add_argument('user-data-dir=/Users/tushar/Library/Application Support/Google/Chrome/Default')```
Alternatively, remove this line for a new temporary Chrome profile.

Site Compatibility: Works best with tools like Duplichecker. Modify selectors if using other tools.

Error Handling: The script assumes that each upload and download succeeds. Future versions should include retry logic and exception handling.

Cross-Platform: Developed on macOS. Minor path or clipboard-related issues may occur on Windows/Linux and should be adapted accordingly.

# Future Improvements

1. Modular code structure with separate files for each task
2. Better error handling and progress reporting
3. GUI version using tkinter or PyQt
4. CLI arguments for automation and batch jobs
5. Dockerized version for isolated runs

# Author
Tushar Bharadwaj
Aspiring Cybersecurity Professional | Automation Enthusiast | Python Developer

