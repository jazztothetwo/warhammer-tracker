# Warhammer Tracker

A personal piece of software to learn software dev.
A personal desktop app for tracking Warhammer armies, units, build status, painting progress, and storage boxes.

## To-do

- [x] Set up Python virtual environment
- [x] Add requirements.txt
- [x] Open a basic PySide6 window
- [ ] Create the main app window layout
- [ ] Create SQLite database tables
- [ ] Add unit form
- [ ] Save units to the database
- [ ] Display units in a table
- [ ] Add army/faction filter
- [ ] Add storage box tracking
- [ ] Build Windows exe

## Setup windows

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows PowerShell:
```bash
.\venv\Scripts\Activate.ps1
```

Install requirements:
```bash
pip install -r requirements.txt
```

Run the app:
```bash
python main.py
```

## Setup Mac

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```