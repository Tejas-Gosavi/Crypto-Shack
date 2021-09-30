### About Project 
CryptoShack - Live crypto currency tracker web app.
After some specific regular interval, clienside data will be updated.
Used Coin Gecko api to get realtime data.
Added search field to search by name and symbol.
Added light/dark theme.
More features coming soon.

### Run project in your system
open 4 command prompts, traverse to project dir. and run following commands respectively.
In 1st - py manage.py runserver
In 2nd - celery -A crypto beat -l INFO
In 3rd - celery -A crypto worker -l INFO
In 4th - redis-server

### Built with
* Fronted - HTML, CSS, Javascript, Bootstrap5, Vue.js.
* Backend - Django
    * Websockets - Django Channels
    * Background Tasks - Celery
    * Task queue - Redis
* Database - SQLite

### Project images
![ ](https://github.com/Tejas-Gosavi/CryptoShack/blob/master/Screenshot-1.png)
<hr />

![ ](https://github.com/Tejas-Gosavi/CryptoShack/blob/master/Screenshot-2.png)
<hr />

![ ](https://github.com/Tejas-Gosavi/CryptoShack/blob/master/Screenshot-3.png)
<hr />

![ ](https://github.com/Tejas-Gosavi/CryptoShack/blob/master/Screenshot-4.png)
<hr />

![ ](https://github.com/Tejas-Gosavi/CryptoShack/blob/master/Screenshot-5.png)
<hr />