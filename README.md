# Social Dots

A Django web application with a beautiful UI built using Tailwind CSS and Django Jet Admin.

## Features

- Modern UI with Tailwind CSS
- Enhanced admin interface with Django Jet
- Fully responsive design
- PostgreSQL database integration
- Ready for Vercel deployment

## Local Development

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file based on `.env.example`
6. Run migrations: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Start the development server: `python manage.py runserver`

## Deployment to Vercel

### Prerequisites

1. A Vercel account
2. The Vercel CLI installed: `npm i -g vercel`
3. A PostgreSQL database (e.g., Neon, Supabase, etc.)

### Deployment Steps

1. Login to Vercel CLI: `vercel login`
2. Navigate to your project directory
3. Deploy to Vercel: `vercel`
4. Follow the prompts to configure your project
5. Set the required environment variables in the Vercel dashboard:
   - `SECRET_KEY`
   - `DEBUG` (set to False for production)
   - `DATABASE_URL`

### Important Notes

- The `build_files.sh` script handles the build process on Vercel
- Static files are served using WhiteNoise
- The Django admin panel is enhanced with Django Jet

## Admin Panel

Access the enhanced admin panel at `/admin` with your superuser credentials. The admin interface is powered by Django Jet, providing a modern and user-friendly experience.

## License

MIT