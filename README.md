# PontoMais Bot
Well, I recently joined a company that insists that employees sign a digital point. Well, as I'm forgotten, I decided to automate this process with Python and Selenium. It keeps running and checks if the current time is time to sign the point, if it is, it opens the browser and does the whole process for me. Now all I have to do is leave the script running and that's it!
[PontoMais website](https://pontomais.com.br/).


## How to Use
```
$ git clone git@github.com:sammarxz/pontomais-bot.git
$ cd pontomais-bot
$ pip install -r requirements.txt
$ python app.py
```

### REQUIRED!
You will need the [chromedriver](https://sites.google.com/chromium.org/driver/) for this works. Download the latest version and install it in your PC (move to `/usr/local/bin`).

---

#### TODO:
* [ ] - Make it more random so it doesn't look like a robot
