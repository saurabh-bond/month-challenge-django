# Month Challenge App (Django)

A beginner-friendly Django application that displays motivational or fun challenges for each month. The goal is to practice Django fundamentals including views, URL routing, and templates.

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
```
cd month_challenge
python manage.py runserver
```
