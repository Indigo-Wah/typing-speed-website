# Typing Speed Website

This is a very simple website that gets a quote from a list and checks it against the user input. I made it in an effort to learn JS and HTTP. And let's just say it was not easy. But it was a good first step.

Whereas I do plan on updating this in the future, I'm not sure when I will do that. I would rather expand into other projects!

## How to run

1. Clone the repo
2. Run `python3 server/server.py`
3. Run `[broswer] web/index.html`

The Python server is running on port 8080.

## How to use

**Note the nav bar is non-functional at the moment

Hit the play button to start.
This will unlock and focus the text input.
It will also send a GET request to the python server which will return a random quote.
Once the timer runs out, the server will send a POST request with the user input and the quote.
The server will then return a response with the accuracy of the user input and set that as the text on the page.

## License

MIT