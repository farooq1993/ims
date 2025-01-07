# ims

# Inventory Management System (IMS)

## Introduction
The Inventory Management System (IMS) is a web application designed to manage the stock, sales, suppliers, and stock movements of a business. This system allows administrators to track inventory levels, create sales orders, update stock levels, and manage suppliers efficiently.

## Features

- **Product Management:** Add, update, and manage products, including stock quantities, descriptions, and pricing.
- **Sales Orders:** Create and manage sales orders, which automatically update the stock quantity after a sale.
- **Stock Movements:** Track stock movement for products, including adding stock in and out.
- **Supplier Management:** Manage suppliers by adding, updating, and deleting supplier details.
- **Reporting:** View real-time data for product sales, stock movement, and more.

## Tech Stack
- **Backend:** Django (Python)
- **Database:** MongoDB (via Djongo) or any other relational database (like PostgreSQL, MySQL, or SQLite).
- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Authentication:** Django built-in authentication system


## Installation

### Requirements
- Python 3.6+
- MongoDB (or any other supported database)
- Pip (for managing Python packages)

### Steps to Set Up

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/imsproject.git
    cd imsproject
    ```

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**
    - For Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - For macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Configure the database settings:**
   - If using MongoDB, ensure `Djongo` and `pymongo` are installed. Update `DATABASES` in `settings.py` to connect to MongoDB or your chosen database.

6. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

7. **Create a superuser to access the Django admin:**
    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000` in your browser.

## Usage

- **Login**: Navigate to `/admin` to log in to the admin panel using the superuser credentials you created.
- **Managing Products**: In the admin panel, you can manage product details, stock quantity, and pricing.
- **Managing Sales Orders**: Create and view sales orders, which automatically update the stock levels based on sales.
- **Stock Movement**: Track stock in and out, updating the product stock quantity accordingly.
- **Supplier Management**: View and edit supplier details in the admin panel.

## Directory Structure

