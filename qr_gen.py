import qrcode
import os

# Définir le dossier où enregistrer les QR codes
output_folder = "static"

# Créer le dossier s'il n'existe pas
os.makedirs(output_folder, exist_ok=True)

# Générer les cartes avec toutes les valeurs de -5 à 5 (exactement une fois chacune)
values = list(range(-5, 6))  # Liste des valeurs de -5 à 5
cards = {}

for i, value in enumerate(values):  # 11 cartes correspondant aux 11 valeurs
    card_id = f"CARD{i:03}"  # Ex: CARD000, CARD001...
    cards[card_id] = value

# Générer et sauvegarder les QR codes
for card_id, value in cards.items():
    url = f"http://yourdomain.com/card?id={card_id}"
    qr = qrcode.make(url)
    qr.save(os.path.join(output_folder, f"{card_id}.png"))
    print(f"QR Code généré pour {card_id}: {url}, Valeur = {value}")

# Afficher la liste des cartes générées
print("\nListe des cartes et leurs valeurs :")
for card, value in cards.items():
    print(f"{card}: {value}")
