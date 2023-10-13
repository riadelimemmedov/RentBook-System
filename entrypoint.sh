APP_NAMES=("author" "book" "customer" "publisher" "rental" "cart" "account")

for APP_NAME in "${APP_NAMES[@]}"; do
    #Run makemigrations for specific apps
    echo "$APP_NAME"
    python3 manage.py makemigrations $APP_NAME
done

#Run makemigrations and migrate without specifying a particular app
python3 manage.py makemigrations
python3 manage.py migrate #If you dont wont show migrations status for each migrate use => --noinput after migrate command
python3 manage.py runserver


#Execute any additional commands passed to the script
exec "$@"
