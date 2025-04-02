# 🛍️ Vani - E-commerce Website for Product Sales

**Vani** is a **Django-based e-commerce web application** that allows users to browse, search, and purchase products online.  
The platform offers a seamless shopping experience with features like user authentication, product categorization, and a shopping cart system.

---

## 🚀 Live Website ✅

The application is live and can be accessed at:  
[https://vani-6hcu.onrender.com](https://vani-6hcu.onrender.com)

---

## 🛠 Features ✅

- ✅ **User Authentication**: Secure user registration and login system.
- ✅ **Product Listings**: Browse products organized by categories.
- ✅ **Product Search**: Search functionality to find products quickly.
- ✅ **Shopping Cart**: Add products to the cart and manage quantities.
- ✅ **Checkout Process**: Seamless checkout experience for users.
- ✅ **Responsive Design**: Optimized for both desktop and mobile devices.
- ✅ **Payment Integration**: (Stripe, Razorpay, or PayPal - specify if applicable)

---

## 🔧 Installation & Setup ✅

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vaibhav-singh05/Vani.git
   cd Vani
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   ```
   - **Activate the Virtual Environment**:
     - **Windows**: `venv\Scripts\activate`
     - **Mac/Linux**: `source venv/bin/activate`

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Database Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```
   - Provide a **username**, **email**, and **password** when prompted.

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   - The application will be available at **http://127.0.0.1:8000/**.

---

## 🏗 Project Structure ✅

```
Vani/
├── authcart/                   # Authentication and Cart management
│   ├── migrations/             # Database migrations
│   ├── templates/authcart/     # Templates specific to auth and cart
│   ├── __init__.py
│   ├── admin.py                # Admin configurations
│   ├── apps.py                 # App configuration
│   ├── forms.py                # Forms for user authentication and cart
│   ├── models.py               # Database models
│   ├── tests.py                # Test cases
│   ├── urls.py                 # URL routing
│   └── views.py                # Views for authentication and cart
│
├── ecommerce/                  # Root Django project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Root URL configurations
│   └── wsgi.py
│
├── ecommerceapp/               # Main e-commerce application
│   ├── migrations/             # Database migrations
│   ├── templates/ecommerceapp/ # Templates specific to e-commerce
│   ├── __init__.py
│   ├── admin.py                # Admin configurations
│   ├── apps.py                 # App configuration
│   ├── forms.py                # Forms for product management
│   ├── models.py               # Database models
│   ├── tests.py                # Test cases
│   ├── urls.py                 # URL routing
│   └── views.py                # Views for product management
│
├── media/                      # Media files (e.g., product images)
│   └── images/                 # Directory for image files
│
├── static/                     # Static files (CSS, JavaScript, Images)
│   ├── css/                    # CSS files
│   ├── js/                     # JavaScript files
│   └── images/                 # Static image files
│
├── templates/                  # Global templates
│   ├── base.html               # Base template
│   └── ...                     # Other global templates
│
├── db.sqlite3                  # SQLite database file
├── manage.py                   # Django's CLI management script
├── requirements.txt            # List of dependencies
└── README.md                   # Project documentation
```

---

## 🖼 Screenshots ✅

(Add screenshots here to showcase UI and features.)

---

## 💡 Tech Stack ✅

- **Backend**: Django, Django REST Framework
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite / PostgreSQL (mention whichever is used)
- **Payment Gateway**: Stripe / Razorpay / PayPal (if integrated)
- **Hosting**: Render (or mention where it's deployed)

---

## 🤝 Contributing ✅

Contributions are welcome! To contribute:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bug fix.
3. **Commit your changes** with descriptive messages.
4. **Push to your fork** and submit a **Pull Request**.

---

## 📝 License ✅

This project is licensed under the **MIT License**. (Specify actual license if different.)

---

## 📬 Contact ✅

For any inquiries or support, please contact:

- **Author**: Vaibhav Singh
- **Email**: [vaibhavsingh273010@gmail.com](mailto:vaibhavsingh273010@gmail.com)
- **LinkedIn**: [https://www.linkedin.com/in/vaibhav-singh-2a5991229/](https://www.linkedin.com/in/vaibhav-singh-2a5991229/)

---

**Happy Coding!** 🚀
