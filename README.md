# fullthrottle-test
This a Django application with User and ActivityPeriod models.
Created a custom management command to populate the database with some random data.
All the data can be viewed with a REST API in json format.

## Usage
Start by cloning the reposirtory.
<pre>git clone https://github.com/hritik7080/fullthrottle-test.git</pre>
Change your working directory.
<pre>cd fullthrottle-test</pre>
Then intsall all the required libraries with following command.
<pre>pip install -r requirements.txt</pre>
Now you have all the dependencies intalled in you system for this projet.<br>
By default the database may be empty. So you can add some dummy data with a custom management command.<br>
<pre>python manage.py populate_database 10</pre>
This will add 10 values in the Users model. For each user program will create 3 values in ActivityPeriod for start_time and end_time. That means, when you create 10 values for Users model the program will create 30 values for ActivityPeriod model. Start time and end time may not be meaningful as they were generated randomly.
#### The above command deletes all the previous data and added new data to the database.
To append the new data in the database. Use this command:
<pre>python manage.py populate_database 10 --append</pre>
This will not delete the previously added data.<br><br>
### For Localhost
To get all the data stored in the Database in the json, use following API with get request.
<pre>http://127.0.0.1:8000/data/getdata/</pre>
You can open this link directly on browser or use postman o check the api.

### Check my hosted app
<pre>https://fullthrottl-test.herokuapp.com/data/getdata/</pre>
Just open this link on browser or postman to check my hosted django appliation.<br>
On postman use get request only.





