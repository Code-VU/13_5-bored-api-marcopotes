# Query Parameters
Today we're going to play with the [Bored API!](https://www.boredapi.com/)

When we look at a website we can use `query parameters` to get different responses.

For instance, to just get a random JSON response from the Bored API, we can visit:

https://www.boredapi.com/api/activity/

This returns a json with a random activity like:

```json
{"activity":"Play a game of tennis with a friend","type":"social","participants":2,"price":0.1,"link":"","key":"1093640","accessibility":0.4}
```

We can then pass in parameters like a function by adding `?` at the end and then passing a key/value pair like `key=value`

https://www.boredapi.com/api/activity?participants=1

Here we are getting a response that matches the partcipant being 0!

```json
{"activity":"Prepare a 72-hour kit","type":"busywork","participants":1,"price":0.5,"link":"https://www.ready.gov/kit","key":"4266522","accessibility":0.5}
```

This will return something from the API that matches 1 participant!

We can pass in multiple parameters by using the `&`:

https://www.boredapi.com/api/activity?participants=1&price=0

This returns something like:

```json
{"activity":"Make a bucket list","type":"busywork","participants":1,"price":0,"link":"","key":"2735499","accessibility":0}
```

# Assignment
Now that we know about the bored API, and we can use query parameters, write a program so we can ask the user what kind of activity they might want.


### Ask the user for the following parameters:
1. A query parameter
2. The value

Send the request while passing in the parameters and have your program list just the received activities.
Then print out just the activities

### Sample Output:
```
***Activity Generator *** 
What is your query parameter? key     
What is the value? 5585829
Recommended Activity: Go to an escape room
```

```
***Activity Generator *** 
What is your query parameter? participants    
What is the value? 8
Recommended Activity: Have a football scrimmage with some friends
```

### BONUS:
As a bonus exercise, try doing these requests in the browser or on Postman. You can also try to add in extra parameters! You can even try looking up your own API to write Python code for!
