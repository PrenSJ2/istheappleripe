# Is The Apple Ripe

Django web application that helps users determine when to buy Apple devices by showing product status recommendations based on release cycles.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

- **CRITICAL SETUP**: Bootstrap, build, and test the repository:
  ```bash
  # Install Python dependencies
  pip3 install django django-tailwind django-browser-reload beautifulsoup4 requests
  
  # Install Node.js dependencies for Tailwind CSS
  cd tailwind_django/theme/static_src
  npm install  # Takes ~4 seconds. NEVER CANCEL.
  
  # Build Tailwind CSS
  cd ../../
  python3 manage.py tailwind build  # Takes ~2 seconds. NEVER CANCEL.
  
  # Check Django configuration
  python3 manage.py check  # Should show no issues
  ```

- **NETWORK ACCESS LIMITATION**: The application calls `import_data()` in `app1/views.py` which fetches data from `buyersguide.macrumors.com`. This will fail in firewall-restricted environments. For testing:
  ```bash
  # Temporarily comment out the import_data() call in app1/views.py home view
  # The database already contains sample data for testing
  ```

- **Run the application**:
  ```bash
  cd tailwind_django
  python3 manage.py runserver  # Takes ~2 seconds to start. NEVER CANCEL.
  # Open browser to http://localhost:8000
  ```

- **Run Tailwind CSS in watch mode** (for development):
  ```bash
  # In a separate terminal
  cd tailwind_django
  python3 manage.py tailwind start  # Takes ~2 seconds to start. NEVER CANCEL.
  ```

## Validation

- **ALWAYS test complete user scenarios after making changes**:
  1. **Search functionality**: Navigate to http://localhost:8000, type "iPhone" in search box
  2. **Product display**: Verify results show with color-coded status (green=Buy Now, yellow=Caution, red=Don't Buy)
  3. **Database content**: Check that 23+ Apple products exist with `python3 manage.py shell -c "from app1.models import Products; print(Products.objects.count())"`

- **Manual validation scenarios**:
  - Test search with "iPhone", "iPad", "Mac" queries
  - Verify AJAX search returns HTML with styled product cards
  - Check that product images load (may be blocked in restricted environments)
  - Confirm status colors match recommendations

- **No tests exist** - the project has no test suite. Create tests if modifying core functionality.

## Project Structure

- **Django Project**: `tailwind_django/` - Main Django application
- **Main App**: `app1/` - Contains models, views, and templates for Apple product recommendations
- **Database**: `db.sqlite3` - SQLite database with 23+ Apple products already populated
- **Tailwind Theme**: `theme/static_src/` - Node.js project for Tailwind CSS compilation
- **Static Files**: Built CSS is output to `theme/static/css/dist/styles.css`

## Common Tasks

### Repository Structure
```
.
├── README.md
├── tailwind_django/
│   ├── manage.py
│   ├── db.sqlite3                    # Pre-populated with Apple product data
│   ├── app1/                         # Main application
│   │   ├── models.py                 # Products model
│   │   ├── views.py                  # IMPORTANT: Contains external API call
│   │   ├── urls.py
│   │   ├── utils.py                  # Web scraping functions
│   │   ├── templates/
│   │   └── static/myJS.js            # AJAX search functionality
│   ├── tailwind_django/              # Django settings
│   └── theme/                        # Tailwind CSS integration
│       ├── static_src/
│       │   ├── package.json          # Node.js dependencies
│       │   └── src/styles.css        # Tailwind source
│       └── static/css/dist/styles.css # Built CSS
```

### Key Files and Their Purpose

- **`app1/utils.py`**: Contains `import_data()` function that scrapes buyersguide.macrumors.com
- **`app1/views.py`**: `home()` view calls `import_data()` - **will fail in restricted networks**
- **`app1/models.py`**: `Products` model stores Apple device data (name, status, color, etc.)
- **`app1/static/myJS.js`**: Handles real-time search with AJAX calls to `/search/<query>`
- **`theme/static_src/package.json`**: Tailwind CSS build configuration

### Dependencies

**Python packages** (install with pip3):
- `django` - Web framework
- `django-tailwind` - Tailwind CSS integration for Django
- `django-browser-reload` - Hot reload during development
- `beautifulsoup4` - HTML parsing for web scraping
- `requests` - HTTP requests for external API calls

**Node.js packages** (install with npm in `theme/static_src/`):
- `tailwindcss` - CSS framework
- `cross-env` - Cross-platform environment variables
- Various Tailwind plugins (@tailwindcss/forms, @tailwindcss/typography, etc.)

### Timing and Performance

- **npm install**: ~4 seconds
- **Tailwind build**: ~2 seconds
- **Tailwind watch startup**: ~2 seconds
- **Django server startup**: ~2 seconds
- **Django migrations**: Pre-applied (no migration needed)
- **Database queries**: Fast (SQLite with 23 records)

### Troubleshooting

**Network Access Issues**:
- `ConnectionError` on startup = `import_data()` trying to fetch external data
- Comment out `import_data()` call in `app1/views.py` for testing
- Database already contains sample data for validation

**Build Issues**:
- Missing Tailwind CSS = Run `python3 manage.py tailwind build`
- JavaScript errors = Check `app1/static/myJS.js` is loading
- Style issues = Verify `theme/static/css/dist/styles.css` exists

**Search Not Working**:
- Check AJAX endpoint at `/search/<query>` returns HTML
- Verify database has products with `Products.objects.all()`
- Test search function directly: `/search/iPhone`

## Development Workflow

1. **Start development servers**:
   ```bash
   # Terminal 1: Django
   cd tailwind_django && python3 manage.py runserver
   
   # Terminal 2: Tailwind watch (optional)
   cd tailwind_django && python3 manage.py tailwind start
   ```

2. **Make code changes** - Both servers auto-reload on file changes

3. **Test changes**:
   - Navigate to http://localhost:8000
   - Test search functionality with various Apple product names
   - Verify styling and responsiveness

4. **Before committing**:
   - Build production CSS: `python3 manage.py tailwind build`
   - Test that search returns properly styled results
   - Verify no JavaScript console errors

## Important Notes

- **External Dependency**: Application requires internet access to fetch fresh Apple product data
- **Database State**: Pre-populated with 23 Apple products for testing
- **Responsive Design**: Uses Tailwind CSS with mobile-first approach
- **AJAX Search**: Real-time search without page refreshes
- **Color Coding**: Green (Buy Now), Yellow (Caution), Red (Don't Buy), Gray (Neutral)