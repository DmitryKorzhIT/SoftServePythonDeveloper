from flask import Flask, render_template
import random
app = Flask(__name__)

#list of snake images
images = [
          "https://www.generatormix.com/images/snakes/taipan.jpg",
          "https://www.generatormix.com/images/snakes/boa.jpg",
          "https://www.generatormix.com/images/snakes/ahaetulla-prasina.jpg",
          "https://www.generatormix.com/images/snakes/flying-snake.jpg",
          "https://www.generatormix.com/images/snakes/inland-taipan.jpg",
          "https://www.generatormix.com/images/snakes/black-racer.jpg",
          "https://www.generatormix.com/images/snakes/tiger-keelback.jpg",
          "https://www.generatormix.com/images/snakes/golden-lancehead.jpg",
          "https://www.generatormix.com/images/snakes/long-nosed-vine-snake.jpg"
]
@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__=="__main__":
    app.run(host="0.0.0.0")
