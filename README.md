
# Flask Apps🌐

A collection of Flask web applications showcasing different concepts and features of the Flask framework. These projects demonstrate practical implementations of web development patterns using Python and Flask.

## 🚀 Projects

### 1. Blog Website
**Location:** `blog_website/`

A complete blog application with user authentication and post management.

**Features:**
- User registration and login system
- Session management
- SQLite database integration with SQLAlchemy
- User and Post models with relationships
- Template inheritance with Jinja2
- Flash messaging for user feedback
- Responsive design with custom CSS

**Key Files:**
- `app.py` - Main application with routes and models
- `templates/` - HTML templates (base, index, login, register, post)
- `static/` - CSS and static assets

### 2. Weather Dashboard
**Location:** `weather-dashboard/`

An interactive weather application with API integration and data persistence.

**Features:**
- Real-time weather data from OpenWeatherMap API
- Save favorite locations
- Weather search history
- RESTful API endpoints
- AJAX-powered frontend
- SQLite database for storing favorites and history
- Responsive dashboard interface

**Key Files:**
- `app.py` - Flask app with API routes
- `templates/index.html` - Dashboard interface
- `static/script.js` - Frontend JavaScript
- `requirements.txt` - Python dependencies

**API Endpoints:**
- `POST /get_weather` - Get weather data for a location
- `POST /save_favorite` - Save location as favorite
- `GET /favorites` - Retrieve favorite locations
- `GET /weather_history` - Get weather search history

## 🛠️ Tech Stack

- **Backend:** Flask, SQLAlchemy
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Template Engine:** Jinja2
- **External APIs:** OpenWeatherMap API
- **HTTP Client:** Requests library

## 📋 Requirements

- Python 3.7+
- Flask 3.0.3
- Flask-SQLAlchemy 3.1.1
- Requests 2.32.3
- SQLAlchemy 2.0.36

See `weather-dashboard/requirements.txt` for complete dependency list.

## 🚀 Getting Started

### Clone the Repository
```bash
git clone https://github.com/sashankL-01/Flask_apps.git
cd Flask_apps
```

### Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
# For weather dashboard
cd weather-dashboard
pip install -r requirements.txt

# For blog website (install Flask and Flask-SQLAlchemy)
pip install Flask Flask-SQLAlchemy
```

### Configuration

#### Blog Website
1. Navigate to `blog_website/`
2. Update the secret key in `app.py`
3. Run the application:
   ```bash
   python app.py
   ```

#### Weather Dashboard
1. Navigate to `weather-dashboard/`
2. Get an API key from [OpenWeatherMap](https://openweathermap.org/api)
3. Replace `"your api key"` in `app.py` with your actual API key
4. Run the application:
   ```bash
   python app.py
   ```

## 🌟 Features Demonstrated

### Database Operations
- SQLAlchemy ORM models
- Database relationships (One-to-Many)
- CRUD operations
- Database migrations

### Web Development Patterns
- MVC architecture
- Template inheritance
- Static file serving
- Form handling
- Session management
- Flash messaging

### API Development
- RESTful API design
- JSON response handling
- External API integration
- AJAX requests
- Error handling

### Frontend Technologies
- Responsive design
- JavaScript DOM manipulation
- Form validation
- Dynamic content loading

## 📱 Usage

### Blog Website
1. Register a new account or login
2. View all posts on the homepage
3. Click on individual posts to read them
4. Logout when finished

### Weather Dashboard
1. Enter a city name to get current weather
2. Save frequently checked locations as favorites
3. View your search history
4. Load favorite locations for quick access

## 🔧 Development Notes

### Security Considerations
- The blog website stores passwords in plain text (for demo purposes only)
- In production, implement proper password hashing
- Use environment variables for sensitive data like API keys

### Database
- Both apps use SQLite databases
- Databases are created automatically on first run
- Located in respective project directories

## 🤝 Contributing

Feel free to:
- Add new Flask applications
- Improve existing features
- Fix bugs or security issues
- Enhance documentation
- Add tests

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

**Sashank L** - [@sashankL-01](https://github.com/sashankL-01)

---

*Happy coding with Flask! 🐍*
=======
# Flask_apps

This repository contains a collection of Flask-based web applications developed for learning, experimentation, and demonstration purposes. Each project showcases different features and capabilities of the Flask framework, ranging from simple apps to more complex, full-featured web services.

## Projects Overview

Below is a brief description of the main projects included in this repository:

### 1. Basic Flask App
A starter application illustrating the basic structure of a Flask project. It demonstrates routing, template rendering, and handling HTTP requests.

### 2. RESTful API Example
A simple REST API built with Flask. This project covers API endpoint creation, JSON responses, and basic CRUD operations.

### 3. Authentication Demo
An app demonstrating user registration, login, and session management using Flask and Flask-Login. It also touches on password hashing for security.

### 4. Database Integration Example
A sample web app showing integration with a database using SQLAlchemy. It includes model definitions, database migrations, and querying.

### 5. File Upload App
A project that allows users to upload files securely to the server. Demonstrates handling file uploads, validation, and storage.

### 6. Template Inheritance & Static Files
A mini-project showcasing Jinja2 template inheritance, inclusion of static assets (CSS, JS), and the use of Flask’s static file handling.

### 7. Custom Error Pages
This project handles custom error pages for 404, 500, and other HTTP errors, improving user experience.

---

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sashankL-01/Flask_apps.git
   cd Flask_apps
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run a project:**
   Each project is usually in its own directory. Navigate into a project folder and run:
   ```bash
   flask run
   ```

---

## Requirements

- Python 3.7+
- Flask
- Other dependencies listed in `requirements.txt`

---

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues for suggestions and improvements.

---

## License

This repository is licensed under the MIT License.

---

**Happy coding with Flask!**

