DJANGO Poll App

The application functionality:
To create, edit, delete polls. It allows also to vote. 
User/admin authorization feature is coming soon.

To launch the application:
1. Clone repository
2. Change current directory
3. Create virtual environment and activate it: 
	Linux: 		create: python3 -m venv $(env_name); activate:  source env_name/bin/activate;
	Windows:	create: python -m venv $(env_name); activate: env_nam/Scripts/activate.bat;
In order to deactivate virtual environment: type 'deactivate' (for both cases).
4. Install dependencies:
	Linux: 		pip3 install -r requirements.txt
	Windows: 	pip install -r requirements.txt
	
5. Launch the application:
	Linux: 		python3 manage.py runserver
	Windows: 	python manage.py runserver
