import tkinter as tk
from PIL import Image, ImageTk  # Nouvelle boîte à outils pour les images

def faire_le_calcul():
    texte_t = case_tension.get()
    texte_c = case_courant.get()
    texte_r = case_resistance.get()
    
    try:
        if texte_t == "" and texte_c != "" and texte_r != "":
            resultat = float(texte_c) * float(texte_r)
            etiquette_resultat.config(text=f"Tension = {resultat:.2f} V", fg="#4CAF50")
            
        elif texte_c == "" and texte_t != "" and texte_r != "":
            resultat = float(texte_t) / float(texte_r)
            etiquette_resultat.config(text=f"Courant = {resultat:.2f} A", fg="#4CAF50")
            
        elif texte_r == "" and texte_t != "" and texte_c != "":
            resultat = float(texte_t) / float(texte_c)
            etiquette_resultat.config(text=f"Résistance = {resultat:.2f} Ohms", fg="#4CAF50")
            
        else:
            etiquette_resultat.config(text="Erreur : Laisse 1 seule case vide !", fg="#F44336")
            
    except ValueError:
        etiquette_resultat.config(text="Erreur : Chiffres uniquement !", fg="#F44336")

# --- Création de la fenêtre ---
fenetre = tk.Tk()
fenetre.title("Calculateur Ohm")
fenetre.geometry("350x480") 

# --- 1. Ajout de l'image de fond ---
# On ouvre l'image, on la redimensionne à la taille de la fenêtre, et on l'affiche
image_fond_originale = Image.open("fond.jpg").resize((350, 480))
image_fond = ImageTk.PhotoImage(image_fond_originale)

label_fond = tk.Label(fenetre, image=image_fond)
label_fond.place(x=0, y=0, relwidth=1, relheight=1) # Place l'image sur tout l'arrière-plan

# --- 2. Chargement des petites icônes ---
# On redimensionne les icônes à 30x30 pixels pour qu'elles soient discrètes
img_batterie = ImageTk.PhotoImage(Image.open("batterie.jpg").resize((30, 30)))
img_eclair = ImageTk.PhotoImage(Image.open("eclair.jpg").resize((30, 30)))
img_resistance = ImageTk.PhotoImage(Image.open("resistance.jpg").resize((30, 30)))

police_texte = ("Arial", 12, "bold")

# --- Interface par-dessus le fond ---
# Tension
tk.Label(fenetre, text=" Tension (V) :", image=img_batterie, compound="left", bg="#282C34", fg="white", font=police_texte).pack(pady=(20, 5))
case_tension = tk.Entry(fenetre, font=("Arial", 14), justify="center")
case_tension.pack()

# Courant
tk.Label(fenetre, text=" Courant (A) :", image=img_eclair, compound="left", bg="#282C34", fg="white", font=police_texte).pack(pady=(15, 5))
case_courant = tk.Entry(fenetre, font=("Arial", 14), justify="center")
case_courant.pack()

# Résistance
tk.Label(fenetre, text=" Résistance (Ohms) :", image=img_resistance, compound="left", bg="#282C34", fg="white", font=police_texte).pack(pady=(15, 5))
case_resistance = tk.Entry(fenetre, font=("Arial", 14), justify="center")
case_resistance.pack()

# Bouton
bouton = tk.Button(fenetre, text="Calculer", command=faire_le_calcul, font=("Arial", 14, "bold"), bg="#61AFEF", fg="black")
bouton.pack(pady=25)

# Résultat
etiquette_resultat = tk.Label(fenetre, text="Laisse la case à calculer vide", bg="#282C34", fg="#E5C07B", font=("Arial", 12, "bold"))
etiquette_resultat.pack()

fenetre.mainloop()