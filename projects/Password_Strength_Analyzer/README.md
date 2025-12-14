# Password Strength Analyzer

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Security](https://img.shields.io/badge/Project-Password%20Security-success)

**Created by SIMOEEEEX**

---

## Description

**Password Strength Analyzer** is a Python-based application to **analyze and improve password security**.  

It checks password strength, provides actionable suggestions, and can generate strong random passwords. The project includes a **modern dark-themed GUI** for easy interaction.

---

## Features

- 🔐 Check password strength: Weak, Medium, Strong, Very Strong  
- 📝 Tips to improve weak passwords  
- 🎲 Generate strong random passwords  
- 🖥️ Interactive Tkinter GUI  
- 🖤 Professional dark theme  
- 📊 Optional CLI for quick testing  
- 🔻 Footer: *created by SIMOEEEEX*

---

## Password Strength Logic

- **Weak**
  - Less than 8 characters OR common password  
- **Medium**
  - Meets 2-4 security criteria (length, uppercase, lowercase, digits, special chars)  
- **Strong**
  - Meets 5 criteria  
- **Very Strong**
  - Meets all 6 criteria, including avoidance of common passwords  

**Security Criteria Checked**:  
1. Minimum length (≥8)  
2. Uppercase letters  
3. Lowercase letters  
4. Digits  
5. Special characters (`!@#$%^&*`)  
6. Not a common password  

---

## Installation

1. Make sure Python 3 is installed  
2. Open terminal in the project folder  

```bash
pip install -r requirements.txt
Usage
GUI
bash
Copy code
python gui.py
Enter a password to analyze its strength

Get tips to improve weak passwords

Generate a strong random password

CLI
bash
Copy code
python main.py
Enter passwords in terminal

Get strength evaluation and suggestions

Optionally generate strong passwords

Testing
Run tests with:

bash
Copy code
python -m unittest discover tests
Author
SIMOEEEEX
