from flask import Flask, render_template,request
import requests

app= Flask(__name__)

@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():

    api_url = "https://api.chucknorris.io/jokes/random"

    response = requests.get(api_url).json()
    img_url = "<img src=" + response['icon_url'] + ">"

    return "Random joke from chuck norris: " + response['value'] + img_url


if __name__=='__main__':
    app.run(debug=True)
