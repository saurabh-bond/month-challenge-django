# Month Challenge App (Django)

A beginner-friendly Django application that displays motivational or fun challenges for each month. The goal is to practice Django fundamentals including views, URL routing, and templates.

https://github.com/user-attachments/assets/1e1755c8-d12e-4b65-8822-025db8e0fadf


---

## Table of Contents

- [Features](#-features)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Example Output](#-example-output)
- [Tech Stack](#-tech-stack)
- [Learning Goals](#-learning-goals)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [License](#-license)

---

## Features

- Homepage shows all 12 months
- Click on any month to view its specific challenge
- URL routing using month name or number (`/challenges/january/` or `/challenges/1/`)
- Basic HTML templates with context data rendering
- Simple and clean app structure for Django beginners

---

## Getting Started

Follow these steps to run the project locally on your machine.

### Prerequisites

- Python installed (recommended version ≥ 3.8)
- Internet connection (to install Django)

Check Python version:

```
python --version
``` 
```
git clone https://github.com/saurabh-bond/month-challenge-django.git
cd month-challenge-django
```

Installing Django Globally 
```
python -m pip install Django
```

Verify by running 

``` 
django-admin 
```
we should see available subcommands list 

Create new project (not required in this case)
```
django-admin startproject month_challenge
```

To Run locally 

Switch to dev branch to get the complete running code
```
cd month_challenge
git checkout dev
git pull origin dev
```

```
python manage.py runserver
```

For making the html code compatible with django (tags, filters, {{}}, {% %} ) 
install django extension in vs code 
django -- by Baptiste Darthenay

Once we install django, we are no longer able to use the html features (like type h1 and clicking on tab should generate the html element)
for making that work, lets add these settings. 
settings.json file 
"files.associations": {
  "*.html": "django-html"
},
"emmet.includeLanguages": {
  "django-html": "html"
}

How to open settings.json file 
1. Press Cmd + Shift + P to open the Command Palette.
2. Type "Preferences: Open Settings (JSON)" and press Enter.
This opens the settings.json file where you can add custom configurations.

