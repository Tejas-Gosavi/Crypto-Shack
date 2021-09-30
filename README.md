### About Project 
CryptoShack - Live crypto currency tracker web app.
After some specific regular interval, clienside data will be updated. <br/>
Used Coin Gecko api to get realtime data.<br/>
Added search field to search by name and symbol.<br/>
Added light/dark theme.<br/>
More features coming soon.<br/>

### Run project in your system
open 4 command prompts, traverse to project dir. and run following commands respectively. <br/>
* In 1st - py manage.py runserver <br/>
* In 2nd - celery -A crypto beat -l INFO <br/>
* In 3rd - celery -A crypto worker -l INFO <br/>
* In 4th - redis-server <br/>

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