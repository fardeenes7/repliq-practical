### This repository was created for a practical task for the role of Junior Django Developer for Repliq

## Installation

1. Clone the repository
2. Create a virtual environment
3. Install requirements
4. Run the server

```bash
git clone
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations company asset api && python manage.py migrate
python manage.py loaddata data.json
python manage.py runserver
```

## Usage

1. Go to http://127.0.0.1:8000/docs
2. Play with the API in the Swagger UI

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Author

MD Fardeen Ehsan Shawon
[Facebook](https://www.facebook.com/fardeen.es7/)
[LinkedIn](https://www.linkedin.com/in/fardeenes7/)
[GitHub](https://www.github.com/fardeenes7)
[Email](mailto:fardeen.es7@gmail.com)
