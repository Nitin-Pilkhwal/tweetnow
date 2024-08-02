#Build the project
echo "Building the project"
python3.9 -m pip install -r requirements.txt

#run the migrations
echo "Running the migrations"
python3.9 manage.py makemigrations
python3.9 manage.py migrate

#collect the static files
echo "Collecting the static files"
python3.9 manage.py collectstatic --noinput --clear