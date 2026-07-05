# Setup Instructions — Laravel + Selenium + HTML Template Integration

Everything below was built and verified end-to-end in the sandbox (DB imported,
server running, login page live, Selenium script run against it, calendar page
rendering with FullCalendar). Here's how to reproduce it on your own machine.

## 1. Laravel project — take it live (Task 1)

1. Extract `main-laravel.zip` (you already have this).
2. **Missing helper files fix**: `composer.json` autoloads `app/helpers.php`
   and `app/helpers2.php`, but these files aren't present in the archive —
   Composer's autoloader fails without them. Copy the two empty placeholder
   files from `laravel-changes/app/` into your project's `app/` folder
   (or just create two empty `<?php` files with those names).
3. Copy `.env.example` to `.env` if you don't already have `.env` (this project
   actually ships with a real `.env` already, using DB name `myad` and
   `APP_URL=https://da.adlynk.in/`).
4. **Database**: `db/db.sql` is a MySQL 8 dump and uses the collation
   `utf8mb4_0900_ai_ci`. If your local server is MySQL 8, it will import as-is.
   If you're on MariaDB (or older MySQL), that collation doesn't exist and the
   import fails partway through. Use the pre-fixed dump instead:
   `laravel-changes/db/db_fixed.sql` (identical, just with the collation
   swapped to `utf8mb4_unicode_ci`). Import with:
   ```bash
   mysql -u root -e "CREATE DATABASE myad CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
   mysql -u root myad < db_fixed.sql
   ```
5. **Local domain**: routes are wrapped in `Route::domain('da.adlynk.in')`,
   so the app only responds when the request's Host header is
   `da.adlynk.in`. Point it at your machine:
   ```bash
   echo "127.0.0.1 da.adlynk.in" | sudo tee -a /etc/hosts
   ```
6. Set `APP_URL` in `.env` to match how you'll browse it, e.g.
   `APP_URL=http://da.adlynk.in:8000/` (the login/calendar views build asset
   URLs from `config('app.url')`, so this must match).
7. Run it:
   ```bash
   php artisan config:clear
   php artisan serve --host=0.0.0.0 --port=8000
   ```
8. Visit `http://da.adlynk.in:8000/login` — this is the screenshot in
   `task1_login_screenshot.png`.

## 2. Selenium script (Task 2)

File: `login_automation.py`

```bash
pip install selenium
python3 login_automation.py
```

It opens the login page, fills `#email` with a random email and `#password`
with a random password, then closes the browser. Set `LOGIN_URL` env var if
your page is at a different address. It uses Selenium's built-in driver
auto-resolution — just make sure Chrome/Chromium is installed. If you need to
pin a specific chromedriver/browser binary, set `CHROMEDRIVER_PATH` and
`CHROME_BINARY_PATH` env vars (the script reads both).

Screenshot of a successful run: `task2_selenium_filled_form_screenshot.png`.

## 3. HTML template calendar page → `/html-page` route (Task 3)

1. From `template-html.zip`, the target file is
   `html/vertical-menu-template/app-calendar.html`.
2. It only references assets via relative paths like `../../assets/...`.
   The Laravel project's `public/assets/` folder already contains the exact
   same asset set (fullcalendar, flatpickr, select2, quill, etc.) — no copying
   needed.
3. Copy the page into Laravel as a Blade view, rewriting `../../assets` to
   `/assets` (root-relative, since Laravel serves `public/` at `/`). The
   already-fixed file is at
   `laravel-changes/resources/views/pages/html-page.blade.php` — drop it into
   your project's `resources/views/pages/` folder.
4. Add the route (already added in `laravel-changes/routes/web.php`, inside
   the existing `Route::domain('da.adlynk.in')` group):
   ```php
   Route::get('html-page', function () {
       return view('pages.html-page');
   })->name('html-page');
   ```
5. `php artisan route:clear` and visit
   `http://da.adlynk.in:8000/html-page` — FullCalendar renders (42 day cells
   confirmed in the current month view). Screenshot:
   `task3_calendar_screenshot.png`.

## Notes / things worth knowing
- The `.env` in this project contains real-looking Google/Facebook OAuth
  client secrets. Treat this repo as sensitive — don't publish it publicly
  as-is.
- One 403 console warning appears on the calendar page from a Google Fonts
  preconnect request if outbound internet to `fonts.googleapis.com` is
  restricted; it's cosmetic (falls back to a system font) and doesn't affect
  functionality.
