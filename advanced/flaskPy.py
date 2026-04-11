from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return f'/ --> /form '

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        username = request.form["username"]
        return f'Received: {username}'
    return '''
        <form method="post">
            <input name="username">
            <input type="submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
