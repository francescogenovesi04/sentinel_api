### SentinelAPI
AI-Powered Breaking Change Monitor

SentinelAPI is an intelligent monitoring system designed to oversee external APIs in real time. Leveraging the integration of Django and OpenAI, the system automatically detects any changes in OpenAPI/Swagger documentation, translating complex technical shifts into simple explanations and promptly flagging breaking changes.

## Key Features

   -Asynchronous Monitoring: Efficient management of heavy background tasks using Celery and Redis.

   -Semantic AI Analysis: Leverages GPT-4o/mini to interpret the technical significance of changes, moving beyond simple textual differences.

   -Modern Dashboard: Responsive interface built with Tailwind CSS and HTMX for instant updates without page reloads.

   -Granular Control: Centralized target management via Admin Panel, with the ability to enable or disable monitoring for each individual resource.


## Installation and Setup

Development Environment Note:

**This setup guide is optimized for Linux Mint. However, the steps are fully compatible with Ubuntu, Debian, and most Linux-based distributions using the apt package manager.**

0. Install Redis (if you haven't already)
 
 ```
 sudo apt update
 sudo apt install redis-server
 ```
   
1. Project Cloning

```
git clone <tuo-link-github>
cd sentinel_api
```

2. Virtual environment

```
python -m venv venv
source venv/bin/activate 
```

3. Dependency Installation

```pip install -r requirements.txt```

4. Environment Variable Configuration

Create a .env file in the root of the project

```
OPENAI_API_KEY=la_tua_chiave_qui
SECRET_KEY=tua_secret_key
DEBUG=True
```

5. Database installation
   
```
python manage.py migrate
python manage.py createsuperuser
```

## Workflow & Daily Routine

To ensure SentinelAPI is fully operational, you must start the following services in three separate terminals:

-Terminal A (Web Server): 

```python manage.py runserver```

-Terminal B (Celery Worker):

```celery -A core worker --loglevel=info```

-Terminal C (Celery Beat) (Manages scheduled automatic scanning, e.g., every 5 minutes):

```celery -A core beat --loglevel=info```
    
## How It Works

-Add Target: Enter the URL of a Swagger/OpenAPI JSON in the Django Admin Panel.

-Monitoring: - Manual: Click "Analyze Now" on the dashboard for an instant check.

-Automatic: If the toggle is set to ON, Celery Beat runs the check periodically.

-AI Comparison: The system downloads the live documentation, compares it with the last saved version, and generates a detailed report via GPT-4o, highlighting whether the changes will require updates to your code.
