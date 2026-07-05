# Laravel Internship Assignment

This repository contains the solution for the Laravel Internship Assignment.

## Tasks Completed

### Task 1: Laravel Project Setup
- Set up the Laravel project on a local development environment.
- Configured the application using the provided `.env` file.
- Imported the provided MySQL database (`db.sql`).
- Successfully ran the application locally.
- Verified the login page.

### Task 2: Selenium Automation
- Created a Python Selenium automation script.
- The script:
  - Opens the Laravel login page.
  - Generates random email and password values.
  - Enters the values into the login form.
  - Closes the browser automatically.

### Task 3: HTML Template Integration
- Integrated the provided HTML Calendar template into the Laravel project.
- Converted the HTML page into a Laravel Blade view.
- Copied all required assets (CSS, JS, fonts, images) into the Laravel `public` directory.
- Added a new Laravel route:

```
/html-page
```

which displays the calendar page.

---

## Tech Stack

- Laravel
- PHP
- MySQL
- Blade Templates
- HTML5
- CSS3
- JavaScript
- Python
- Selenium WebDriver

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### Install Dependencies

```bash
composer install
npm install
```

### Configure Environment

Copy the environment file.

```bash
cp .env.example .env
```

Generate the application key.

```bash
php artisan key:generate
```

Update the database credentials inside `.env`.

Example:

```env
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=laravel_assignment
DB_USERNAME=root
DB_PASSWORD=
```

### Import Database

Import the provided `db.sql` file into MySQL.

### Start the Application

```bash
php artisan serve
```

In another terminal:

```bash
npm run dev
```

Visit:

```
http://127.0.0.1:8000
```

---

## Selenium Script

Install dependencies:

```bash
pip install selenium webdriver-manager
```

Run:

```bash
python selenium.py
```

---

## Project Structure

```
├── app
├── bootstrap
├── config
├── database
├── public
│   └── assets
├── resources
│   └── views
│       └── calendar.blade.php
├── routes
│   └── web.php
├── selenium.py
└── README.md
```

---

## Features

- Laravel Authentication
- Database Integration
- Selenium Login Automation
- HTML Template Integration
- Blade Template Rendering
- Responsive Calendar Page

---

## Author

**Mohammad Shiyabuddeen**

GitHub: https://github.com/mohdshiyab

