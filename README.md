# "Cohen Garden" Web App

During quarantine, I bought a <a href = "https://www.raspberrypi.org/products/raspberry-pi-4-model-b/"> Raspberry Pi</a> and <a href = "https://www.amazon.com/gp/product/B07TLRYGT1/ref=ppx_yo_dt_b_asin_title_o04_s01?ie=UTF8&psc=1"> some </a> <a href = "https://www.amazon.com/gp/product/B01J9GD3DG/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1"> sensors </a> from Amazon to learn about IoT programming. After some tinkering, I thought an interesting project to learn would be to build a self-watering garden. Then, I bought some <a href = "https://www.amazon.com/gp/product/B06ZY8JGJ4/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1"> seeds </a> in an attempt to make this useful for more than my own learning to try to actually grow some herbs.

The repo for the app which manages the garden can be found <a href="https://github.com/brandonfcohen1/garden_app">here</a>.

The dashboard for the web app can be found <a href="http://cohengarden.herokuapp.com/">here</a>.

Obviously what I've done here is not the easiest, cheapest, or most effective way to grow herbs. I really just built it to use any and all sensors I could connect to the Raspberry Pi. I don't even know if the herbs will grow well here, but it was a fun project (and I've got some seedlings coming in)!

I also wanted to work on my web development skills, so I built an API to which the Pi can post the sensor readings and a front-end which will render some cool graphics. Since I built the rest of the project in Python and it is my preferred programming language, I chose <a href="https://flask.palletsprojects.com/en/1.1.x/"> Flask </a> to build the web app. I hosted the app on <a href = "https://www.heroku.com/"> Heroku </a>, since it is so simple to use and has a free "hobby" tier and used <a href = "https://www.postgresql.org/"> PostgreSQL</a> for the database which will store the readings. This is the repo for the web app/API.

This web app is really simple. There is an endpoint at which the Raspberry Pi can post the latest readings, and some logic to render a set of latest readings in a pretty simple array of charts using matplotlib and mpld3.
