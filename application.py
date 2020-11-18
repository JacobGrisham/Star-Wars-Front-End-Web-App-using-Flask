import os
from flask import Flask, render_template

# Configure application
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def deathStar():
  return render_template("death-star.html")

@app.route("/millennium-falcon-model")
def millenniumFalconModel():
  return render_template("millennium-falcon/millennium-falcon-model.html")

@app.route("/millennium-falcon-blueprint")
def millenniumFalconBlueprint():
  return render_template("millennium-falcon/millennium-falcon-blueprint.html")

@app.route("/star-destroyer-model")
def starDestroyerModel():
  return render_template("star-destroyer/star-destroyer-model.html")

@app.route("/star-destroyer-blueprint")
def starDestroyerBlueprint():
  return render_template("star-destroyer/star-destroyer-blueprint.html")

@app.route("/tie-fighter-model")
def tieFighterModel():
  return render_template("tie-fighter/tie-fighter-model.html")

@app.route("/tie-fighter-blueprint")
def tieFighterBlueprint():
  return render_template("tie-fighter/tie-fighter-blueprint.html")

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('404.html'), 404

# Run Server
if __name__ == '__main__':
    app.run(debug = True)
# Run the following in the command line: python application.py