from flask import Flask, render_template_string
import utils
app = Flask(__name__)

def get_score_from_file():
    try:    
        with open(utils.SCORES_FILE_NAME, 'r') as scores_file:
            saved_score = scores_file.read().strip()
            if len(saved_score) == 0:
                saved_score = 0
            else:
                saved_score = int(saved_score)
            return saved_score, None
    except Exception as e:
        return None, str(e)

@app.route("/")

def score_server():
    score, error = get_score_from_file()
    if score:
        return render_template_string("""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>The score is:</h1>
                <div id="score">{{ score }}</div>
            </body>
        </html>
        """, score=score)
    else:
        return render_template_string("""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>ERROR:</h1>
                <div id="score" style="color:red">{{ error }}</div>
            </body>
        </html>
        """, error=error)
    
if __name__ == "__main__":
    app.run(port=5000)