# Mercury Assets Python Assessment.

- Create a Docker Compose (`docker-compose.yml`) configuration file.
	- Docker should manage two services: the flask server and nginx.
	- Each service should have its own `dockerfile`.
	- Gunicorn should be used to run the flask server.
	- nGinx should be used to reverse proxy traffic to the gunicorn/flask server.
- Please create *one* endpoint which accepts both GET and POST requests.
	- For GET requests, please return `resp = {"response": 'Success!'}`
	- For POST requests, please return 1 minute candles (OHLC) in JSON format from the POST'ed csv file in the client.
- The client POST's tick data (a `csv` file) to the server endpoint `/candle`, please modify the endpoint in `config.yaml` to work with your server endpoint.



Notes:

- You are not required to provide models or schemas within the application.
- User/Token authentication is not required.
- You are not required to include HTTPS/SSL (443).
