Q. In your opinion, what are the characteristics of high quality code? In my opinion, the characteristics of high
quality code are:

1. It is easy to read and understand.
2. It is easy to maintain.
3. It is easy to test.
4. It is easy to debug.
5. It is easy to extend.
6. It is easy to reuse.
7. It is easy to integrate.

Q. What are two of your most used design patterns? Why have you used them?

In my experience I have used the following design patterns:

1. Singleton
2. Decorator

I got the opportunity to work with Database quite often, and for creating connections usually I use Singleton pattern.
The idea behind doing so was that the thread to eaily share the global state of the connection, and it is also easy to
maintain.

Working with Python, I have used Decorator pattern to create a wrapper around the function, and it is easy to maintain
and extend the functionality of the function. This gave a level of abstraction to the function and also made the code
cleaner.

# Observations API

This is a simple API that allows you to create, and read observations.

Example Input:

```
{
    data": [
                    {
                        "monitored_id": 1,
                        "observation_name": "Heart Rate",
                        "issued": "2021-09-01T00:00:00Z",
                        "value": 80,
                        "value_type": "Number",
                        "value_unit": "BPM"
                    }
            
 }
```

APIS:

```
1. Create Observation - /observations/add_observations/
2. Get Latest Observations - /observations/get_latest_observations/
3. Get Observations - /observations/get_observations/
4. Observation Mean - /observations/observation_mean/
5. Admin: http://0.0.0.0:8000/admin/ (username: admin, password: admin1234)
```

```

To run the application:

```
docker-compose up
```
'
