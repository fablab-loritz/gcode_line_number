import tkinter as tk
from tkinter import filedialog, messagebox

def add_line_numbers(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        with open(output_file, 'w') as file:
            line_number = 10
            for line in lines:
                stripped_line = line.strip()
                if stripped_line:  # Ajoute un numéro de ligne seulement si la ligne n'est pas vide
                    file.write(f"N{line_number} {line}")
                    line_number += 10
                else:
                    file.write(line)  # Lignes vides conservées telles quelles
        return True
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors du traitement : {e}")
        return False

def process_file():
    input_file = filedialog.askopenfilename(
        title="Sélectionner un fichier G-code",
        filetypes=[("Fichiers PRG", "*.PRG"), ("Tous les fichiers", "*.*")]
    )
    if not input_file:
        return  # L'utilisateur a annulé la sélection
    
    output_file = filedialog.asksaveasfilename(
        title="Enregistrer le fichier modifié",
        defaultextension=".PRG",
        filetypes=[("Fichiers PRG", "*.PRG"), ("Tous les fichiers", "*.*")]
    )
    if not output_file:
        return  # L'utilisateur a annulé la sauvegarde

    if add_line_numbers(input_file, output_file):
        messagebox.showinfo("Succès", "Le fichier a été traité avec succès.")

# Interface Tkinter
root = tk.Tk()
root.title("Ajout de numéros de ligne au G-code")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Ajouter des numéros de ligne au fichier G-code")
label.pack(pady=10)

process_button = tk.Button(frame, text="Sélectionner et traiter le fichier", command=process_file)
process_button.pack(pady=10)

exit_button = tk.Button(frame, text="Quitter", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
