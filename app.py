"""Module that creates the Flask app."""

import os

import openai
from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]


@app.route("/", methods=("GET", "POST"))
def index():
    """Main page.
    """
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(animal),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal: str) -> str:
    """Generate a prompt for the OpenAI API.

    Args:
        animal (str): The animal to generate names for.

    Returns:
        str: The prompt.
    """
    return f"""Suggest three names for an animal that is a superhero.

                Animal: Cat
                Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
                Animal: Dog
                Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
                Animal: {animal.capitalize()}
                Names:"""
