APP_NAMES=("author" "book" "customer" "publisher" "rental" "cart" "account")

for APP_NAME in "${APP_NAMES[@]}"; do
    #Run makemigrations for specific apps
    python manage.py makemigrations $APP_NAME
done

#Run makemigrations and migrate without specifying a particular app
python manage.py makemigrations
python manage.py migrate

#Execute any additional commands passed to the script
exec "$@"
