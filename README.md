# Toy Load Balancer

## Instructions to setup
1. Create a virtual environment.
2. Activate the virtual environment
3. Install the required libraries in the `requirements.txt` file using `pip`.
4. Create a .env file to instantiate the required environment variables, an example file is provided in the repo.

## Instructions to run
Open multiple terminals and run the backend_server with the command: 
```
python backend_server.py 5001 1
```
Change the port number and server number for the subsequent servers. 

Run the LB code using command: 
```
python main.py
```

## Calling the API

```
curl --location 'http://127.0.0.1:8000/hello'
```

## Calling the info API

```
curl --location 'http://127.0.0.1:8000/info'
```

