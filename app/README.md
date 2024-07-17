# How does this app works?

Is a simple Python's flask app that will try to connect to a redis database.
It exposes three endpoints:
- `/`: GET request Will return a simple message.
- `/set`: POST request that will set a key-value pair in the redis database
- `/get`: GET request that will return the value of the key provided in the request.
- `/error`: GET request that will return an error.

# Simply build the image
Remember to change `your-dockerhub-username` to your dockerhub username and change the reference in manifests 
```bash
docker build -t your-dockerhub-username/conn-to-redis:latest .
````


