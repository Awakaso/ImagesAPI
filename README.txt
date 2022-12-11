
#######################################
Python3 Django REST API
#######################################

Certify to have Python3 installed
Certify to have PostgreSQL installed and to set instance forwarding to default port.


Follow this steps to run the program:
1- Create a virtual environment and execute it
2- Execute the following command to install all the packages that have been used in development (file inside ImagesAPI/images):
	'pip install -r requirements.txt'
3- Execute the following commands to create and populate postgreSQL database. Make sure you are in the same folder as 'manage.py'.
	'manage.py makemigrations'
	'manage.py migrate'
	
4- Run 'manage.py runserver' to start. Make sure you are in the same folder as 'manage.py'.


From now on API is available on localhost.
Open your browser on:
   - To list registers from db, go to:
		http://127.0.0.1:8000/images/

   - To create a new register in db, go to:
		http://127.0.0.1:8000/images/create

	Enter in content valid information in a valid format. Example:
		{
        	  "id": 24,
        	  "title": "new Item 24",
                  "image_url": "",
                  "description": "Description 24"
                }
	Then press "POST".

   - To select and view specific register from db, choose an item and respective ID from the list, go to:
		http://127.0.0.1:8000/images/"ID"

	In here it is posible to Modify or Delete that register.

	- To Modify:
		Enter in content valid information in a valid format. Example for http://127.0.0.1:8000/images/23

		{
        	  "title": "Change title in id 23",
                }

		Then press "PUT".

	- To Delete:
		Press on "DELETE".

	 	 