from flask import Flask
app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Football Players</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
        }

        .container {
            max-width: 800px;
            margin: 40px auto;
            text-align: center;
        }

        .player-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .player-list li {
            background-color: #fff;
            padding: 20px;
            border-bottom: 1px solid #ddd;
            margin-bottom: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .player-list li:hover {
            background-color: #f9f9f9;
        }

        .player-name {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .player-position {
            font-size: 18px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Top Football Players</h1>
        <ul class="player-list">
            <li>
                <span class="player-name">Cristiano Ronaldo</span>
                <span class="player-position">Forward</span>
            </li>
            <li>
                <span class="player-name">Lionel Messi</span>
                <span class="player-position">Forward</span>
            </li>
            <li>
                <span class="player-name">Kylian Mbappé</span>
                <span class="player-position">Forward</span>
            </li>
            <li>
                <span class="player-name">Robert Lewandowski</span>
                <span class="player-position">Striker</span>
            </li>
            <li>
                <span class="player-name">Neymar Jr.</span>
                <span class="player-position">Winger</span>
            </li>
            <li>
                <span class="player-name">Mohamed Salah</span>
                <span class="player-position">Winger</span>
            </li>
            <li>
                <span class="player-name">Kevin De Bruyne</span>
                <span class="player-position">Midfielder</span>
            </li>
        </ul>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return TEMPLATE

if __name__ == "__main__":
    app.run(debug=True)
