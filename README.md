# Stock Information Fetcher

This Django application provides users with detailed stock information about major companies through a simple web interface, leveraging the Yahoo Finance API.

## Features
- Search for company stock information by entering the company name.
- Displays key financial metrics such as market cap, P/E ratio, enterprise value, and more.
- User-friendly interface for easy access to company data.

## Technologies Used
- **Django**: A high-level Python web framework for building web applications.
- **yfinance**: A Python library for accessing stock market data from Yahoo Finance.

## Getting Started

### Prerequisites
- Python 3.x
- Django
- yfinance library

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

3. **Install the required packages:**
   ```bash
    pip install -r requirements.txt

4. **Set up the database:**
   ```bash
   Update the settings.py file with your database configuration.
   Run migrations:
   python manage.py migrate

5. **Create a superuser (optional for accessing the admin site):**
   ```bash
   python manage.py createsuperuser

6. **Run the server:**
   ```bash
   python manage.py runserver
