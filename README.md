# Ice Cream Parlor Web App

A basic web app built with Flask to view ice cream flavors, add them to the cart, and give suggestions.

---

## Steps to Run the App

1. **Clone the repo:**

   git clone git@github.com:EdisonS45/ice_cream_parlor_app.git 
   
   cd ice_cream_parlor_app

2. **Create a Virtual Environment:**

   For Windows:
   python -m venv venv

   For macOS/Linux:
   python3 -m venv venv

3. **Activate the Virtual Environment:**

   For Windows:
   .\venv\bin\activate

   For macOS/Linux:
   source venv/bin/activate

4. **Install Dependencies:**

   pip install -r requirements.txt

5. **Run the App:**

   Set environment to development:
   export FLASK_ENV=development # macOS/Linux
   set FLASK_ENV=development # Windows

   Then run:
   flask run

6. Open a browser and go to `http://127.0.0.1:5000`

## Features

- View ice cream flavors
- Add/remove flavors from cart
- View user suggestions
