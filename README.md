# Is the apple ripe

Website to show people when to buy a specific apple device. 

<img src="https://i.ibb.co/YprhHSy/image.png">

## Installation

Install both Python and Node.js dependencies:

```bash
# Install Python dependencies
pip install django django-tailwind django-browser-reload beautifulsoup4 requests

# Install Node.js dependencies
npm install
```

## Usage

### Quick Start (Recommended)

Run both the Django server and Tailwind development server with a single command:

```bash
npm start
```

This will start both servers concurrently:
- Django development server at http://localhost:8000
- Tailwind CSS development server (auto-recompiling styles)

### Manual Commands (Alternative)

You can also run the servers separately if needed:

```bash
# Run Django server
cd tailwind_django && python3 manage.py runserver

# Run Tailwind development server (in another terminal)
cd tailwind_django && python3 manage.py tailwind start
```

### Available Scripts

- `npm start` or `npm run dev` - Runs both servers concurrently
- `npm run server` - Runs only the Django server
- `npm run frontend` - Runs only the Tailwind development server

Then proceed to open your browser at the page http://localhost:8000

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
