from flask import Flask, request, render_template_string

app = Flask(__name__, static_folder='.', static_url_path='')  # Serve from current directory

# Database
cards = {
    'CARD000': -5, 'CARD001': -4, 'CARD002': -3, 'CARD003': -2, 'CARD004': -1,
    'CARD005': 0, 'CARD006': 1, 'CARD007': 2, 'CARD008': 3, 'CARD009': 4, 'CARD010': 5
}
SECRET_CODE = "TREASURE2025"

# Logo configuration
LOGO_IMAGES = ["sole.png", "flavoria.png", "lions.png", "ucraft.png"]

def get_header_css():
    return """
header {
            width: 100%;
            position: fixed;
            top: 0;
            left: 0;
            display: flex;
            justify-content: center;
            padding: 15px;
            background-color: rgba(0, 0, 50, 0.8);
            box-shadow: 0 0 10px rgba(0, 0, 255, 0.6);
            z-index: 1000;
        }
        #incorrect{
            background-color: #FF0000;
            box-shadow: 0 0 10px #350808;
        }
        .logo-container {
            display: flex;
            justify-content: flex-start; /* Aligner les logos à gauche */
            width: 100%;
            max-width: 900px;
            margin-bottom:-25px;
            align-items: center;
        }
        .logo-container img {
            width: 100%;
            height: 100px;
        }
        /* Ajustement de l'espacement entre les images */
        .logo-container img:nth-child(1) {
            margin-right: 100px;
        }
        .logo-container img:nth-child(2) {
            margin-right: 100px;
        }
        .logo-container img:nth-child(3) {
            margin-right: 100px;
        }
        .logo-container img:nth-child(4) {
            margin-left: 100px;
        }
    """

@app.route("/card")
def card():
    card_id = request.args.get("id")
    if card_id not in cards:
        return "Invalid card !", 404

    return render_template_string("""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title> Trouvée</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');
                body {
                    font-family: 'Orbitron', sans-serif;
                    text-align: center;
                    background: #0b0f19;
                    color: white;
                    height: 100vh;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                }
                {{ header_css|safe }}
                .container {
                    background: rgba(30, 30, 60, 0.8);
                    padding: 30px;
                    border-radius: 15px;
                    box-shadow: 0 0 15px rgba(255, 0, 255, 0.5);
                    width: 350px;
                    margin-top: 80px;
                }
                h2 { font-size: 24px; color: #ff007f; text-shadow: 0 0 5px #ff007f; }
                input, button {
                    width: 100%;
                    padding: 10px;
                    margin: 10px 0;
                    font-size: 16px;
                    border-radius: 5px;
                    border: none;
                }
                input { background: rgba(255, 255, 255, 0.1); color: white; text-align: center; }
                button {
                    background: #ff007f;
                    color: white;
                    font-weight: bold;
                    cursor: pointer;
                    transition: all 0.3s ease-in-out;
                }
                button:hover { background: #ff00ff; box-shadow: 0 0 10px #ff00ff; }
            </style>
        </head>
        <body>
            <header>
                <div class="logo-container">
                    <img src="{{ url_for('static', filename=logos[0]) }}" style="height: 40px">
                    <img src="{{ url_for('static', filename=logos[1]) }}" >
                    <img src="{{ url_for('static', filename=logos[2]) }}" >
                    <img src="{{ url_for('static', filename=logos[3]) }}" >
                </div>
            </header>

            <div class="container">
                <h1>Welcom to squid game </h1>
                <h2>🃏 Found Card !</h2>
                <form method="post" action="/reveal">
                    <input type="hidden" name="id" value="{{ card_id }}">
                    <label>🔑 Enter the secret code :</label>
                    <input type="text" name="code" required>
                    <button type="submit">Validate</button>
                </form>
            </div>
        </body>
        </html>
    """, card_id=card_id, logos=LOGO_IMAGES, header_css=get_header_css())

@app.route("/reveal", methods=["POST"])
def reveal():
    card_id = request.form.get("id")
    code = request.form.get("code")

    if card_id not in cards:
        return "Invalid cart !", 404
        
    if code != SECRET_CODE:
        return render_template_string("""
            <!DOCTYPE html>
            <html lang="fr">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Code Incorrect</title>
                <style>
                    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');
                    body {
                        font-family: 'Orbitron', sans-serif;
                        text-align: center;
                        background: #190000;
                        color: white;
                        height: 100vh;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        flex-direction: column;
                        animation: glitch-bg 0.1s infinite alternate;
                    }
                    {{ header_css|safe }}
                    @keyframes glitch-bg { 0% { background: #300000; } 100% { background: #190000; } }
                    .container {
                        background: rgba(60, 10, 10, 0.8);
                        padding: 30px;
                        border-radius: 15px;
                        box-shadow: 0 0 15px rgba(255, 0, 0, 0.5);
                        width: 350px;
                        border: 3px solid red;
                        animation: shake 0.3s infinite alternate;
                    }
                    @keyframes shake { 0% { transform: translateX(-2px); } 100% { transform: translateX(2px); } }
                    h2 { font-size: 28px; color: #ff0000; text-shadow: 0 0 10px #ff0000; }
                    .alert { font-size: 20px; color: white; background: red; padding: 10px; border-radius: 5px; margin: 15px 0; }
                    .return-btn {
                        background: #ff0000;
                        color: white;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        font-size: 16px;
                        cursor: pointer;
                        transition: all 0.3s ease-in-out;
                    }
                    .return-btn:hover { background: #ff5555; box-shadow: 0 0 10px #ff5555; }
                </style>
            </head>
            <body>
                <header id="incorrect">
                    <div class="logo-container">
                        <img src="{{ url_for('static', filename=logos[0]) }}" style="height: 40px">
                        <img src="{{ url_for('static', filename=logos[1]) }}" >
                        <img src="{{ url_for('static', filename=logos[2]) }}">
                        <img src="{{ url_for('static', filename=logos[3]) }}">
                    </div>
                </header>
                <audio autoplay>
                    <source src="https://www.soundjay.com/button/beep-07.wav" type="audio/wav">
                </audio>
                <div class="container">
                    <h2>🚨 ACCESS DENIED 🚨</h2>
                    <p class="alert">Incorrect password !</p>
                    <button class="return-btn" onclick="window.location.href='/card?id={{ card_id }}'">🔄 Retry</button>
                </div>
            </body>
            </html>
        """, card_id=card_id, logos=LOGO_IMAGES, header_css=get_header_css())

    # Correct code handling
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Valeur de la Carte</title>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap');
                body {
                    font-family: 'Orbitron', sans-serif;
                    text-align: center;
                    background: #0b0f19;
                    color: white;
                    height: 100vh;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    flex-direction: column;
                }
                {{ header_css|safe }}
                .container {
                    background: rgba(30, 30, 60, 0.8);
                    padding: 30px;
                    border-radius: 15px;
                    box-shadow: 0 0 15px rgba(255, 0, 255, 0.5);
                    width: 350px;
                    animation: fadeIn 1s ease-in-out;
                }
                @keyframes fadeIn { from { opacity: 0; transform: scale(0.8); } to { opacity: 1; transform: scale(1); } }
                h2 { font-size: 27px; color: #ff007f; text-shadow: 0 0 5px #ff007f; }
                h1 { font-size: 27px; color: #00ff00; text-shadow: 0 0 5px #00ff00;text-transform:uppercase; }
                .value { font-size: 36px; font-weight: bold; color: #00ffff; text-shadow: 0 0 10px #00ffff; margin: 20px 0; }
                .return-btn {
                    background: #ff007f;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    font-size: 16px;
                    cursor: pointer;
                    transition: all 0.3s ease-in-out;
                }
                .return-btn:hover { background: #ff00ff; box-shadow: 0 0 10px #ff00ff; }
            </style>
        </head>
        <body>
            <header>
                <div class="logo-container">
                    <img src="{{ url_for('static', filename=logos[0]) }}" style="height: 40px">
                    <img src="{{ url_for('static', filename=logos[1]) }}" >
                    <img src="{{ url_for('static', filename=logos[2]) }}" >
                    <img src="{{ url_for('static', filename=logos[3]) }}" >
                </div>
            </header>
     <h1>Welcom to squid game </h1>
            <div class="container">
                <h1>Welcom to squid game </h1>
                <h2>🎴 Card Value :</h2>
                <p class="value">{{ value }}</p>
                <button class="return-btn" onclick="window.location.href='/card?id={{ card_id }}'">🔄 Retry</button>
            </div>
        </body>
        </html>
    """, card_id=card_id, value=cards[card_id], logos=LOGO_IMAGES, header_css=get_header_css())

if __name__ == "__main__":
    app.run(debug=True)
