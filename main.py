import json
import os
import random
import math
import requests
from flask import Flask, request, render_template


app = Flask(__name__)


def random_number():
    return math.floor(random.random() * 99999999999999 + 1)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api")
def api():
    prompt = request.json["prompt"]
    negativePrompt = request.json["negativePrompt"]
    model = request.json["model"]

    print(prompt, negativePrompt, model)

    response = requests.post(
        f"https://api.segmind.com/v1/{model}",
        headers={
            "x-api-key": "SG_xxxxxxxxxxxxxxx",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "prompt": "A sad cat in a hat",
            "negative_prompt": "text, cropped, out of frame, worst quality",
            "samples": 1,
            "scheduler": "dpmpp_2m",
            "num_inference_steps": 25,
            "guidance_scale": 7.5,
            "img_width": 1024,
            "img_height": 1024,
            "seed": random_number(),
        }),
    )
    return response.content


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)



