# Twilio Bot
This is a Twilio bot.


## Requirements
This project uses Docker and Docker Compose. Please install them before continuing.
Also, you must have a Twilio account set up in order to use this program.


## Setup
First, create a ```.env``` file inside the ```twilio_bot``` directory.
Then, add the required environment variables, as shown below:
```
ACCOUNT_SID=[SID goes here]
AUTH_TOKEN=[token goes here]

TO_NUMBER=[phone number goes here]
FROM_NUMBER=[Twilio phone number goes here]
```

Then, run ```docker-compose up -d --build``` to build the image and run the container.


## How to Use
Once the container is running, watch the app message away!
