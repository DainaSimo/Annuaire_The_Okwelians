#!/bin/sh

echo "🛠️ Applying Django migrations..."
python manage.py migrate --noinput

echo "🔐 Creating Django superuser if needed..."
# Crée un superuser automatiquement si il n'existe pas (facultatif)
# Remplace les valeurs par tes propres identifiants
echo "from django.contrib.auth import get_user_model; User = get_user_model(); \
      User.objects.filter(username='admin').exists() or \
      User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')" \
      | python manage.py shell

echo "🚀 Starting Gunicorn server..."
exec gunicorn mon_projet.wsgi:application --bind 0.0.0.0:$PORT
