# Is the apple ripe

Website to show people when to buy a specific apple device. 

<img src="https://i.ibb.co/YprhHSy/image.png">

## Installation

Install dependencies using npm (this will install both Python and Node.js dependencies):

```bash
npm run install:deps
```

Or install them separately:

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node.js dependencies  
npm install
cd tailwind_django/theme/static_src && npm install
```

## Usage

### Development (Unified command)

Start both Django server and Tailwind development server:

```bash
npm run dev
```

This will run both:
- Django development server on http://localhost:8000
- Tailwind CSS in watch mode for live reloading

### Alternative Development Commands

```bash
# Start only Django server
npm run django:dev

# Start only Tailwind development server
npm run tailwind:dev
```

### Production Build

Build the project for production:

```bash
npm run build
```

This will:
1. Install Python dependencies
2. Build Tailwind CSS for production
3. Collect Django static files

### Individual Commands

```bash
# Django commands
npm run django:start        # Start Django server
npm run django:migrate      # Run database migrations
npm run django:collectstatic # Collect static files

# Tailwind commands  
npm run tailwind:build      # Build Tailwind for production
npm run tailwind:dev        # Start Tailwind development server
```

### Deployment

This project is configured for deployment on Vercel. The `vercel.json` configuration file handles the build process automatically.

## Legacy Commands

For backwards compatibility, you can still use the original commands:

```bash
# run python server
python3 tailwind_django/manage.py runserver

# run tailwind server  
python3 tailwind_django/manage.py tailwind start
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
