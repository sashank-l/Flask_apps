
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
