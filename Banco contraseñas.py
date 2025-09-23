
import os
import json
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import simpledialog, messagebox


DATA_FILE = 'passwords.json'
KEY_FILE = 'key.key'

def generate_key():
	key = Fernet.generate_key()
	with open(KEY_FILE, 'wb') as f:
		f.write(key)
	return key

def load_key():
	if not os.path.exists(KEY_FILE):
		return generate_key()
	with open(KEY_FILE, 'rb') as f:
		return f.read()

def encrypt_data(data, key):
	f = Fernet(key)
	return f.encrypt(json.dumps(data).encode())

def decrypt_data(token, key):
	f = Fernet(key)
	return json.loads(f.decrypt(token).decode())

def save_passwords(passwords, key):
	encrypted = encrypt_data(passwords, key)
	with open(DATA_FILE, 'wb') as f:
		f.write(encrypted)

def load_passwords(key):
	if not os.path.exists(DATA_FILE):
		return {}
	with open(DATA_FILE, 'rb') as f:
		encrypted = f.read()
	return decrypt_data(encrypted, key)

def add_password(site, username, password, key):
	passwords = load_passwords(key)
	passwords[site] = {'username': username, 'password': password}
	save_passwords(passwords, key)

def get_password(site, key):
	passwords = load_passwords(key)
	return passwords.get(site)

def delete_password(site, key):
	passwords = load_passwords(key)
	if site in passwords:
		del passwords[site]
		save_passwords(passwords, key)

def list_sites(key):
	passwords = load_passwords(key)
	return list(passwords.keys())



class PasswordManagerGUI:
	def __init__(self, master):
		self.master = master
		master.title("Banco de contraseñas")
		self.key = load_key()

		self.frame = tk.Frame(master)
		self.frame.pack(padx=10, pady=10)

		self.add_btn = tk.Button(self.frame, text="Añadir contraseña", command=self.add_password)
		self.add_btn.grid(row=0, column=0, padx=5, pady=5)

		self.get_btn = tk.Button(self.frame, text="Obtener contraseña", command=self.get_password)
		self.get_btn.grid(row=0, column=1, padx=5, pady=5)

		self.delete_btn = tk.Button(self.frame, text="Eliminar contraseña", command=self.delete_password)
		self.delete_btn.grid(row=0, column=2, padx=5, pady=5)

		self.list_btn = tk.Button(self.frame, text="Lista de sitios", command=self.list_sites)
		self.list_btn.grid(row=0, column=3, padx=5, pady=5)

		self.output = tk.Text(self.frame, height=10, width=50)
		self.output.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
		self.output.config(state=tk.DISABLED)

	def add_password(self):
		site = simpledialog.askstring("Sitio", "Ingresar nombre del sitio:")
		if not site:
			return
		username = simpledialog.askstring("Usuario", "Ingresar usuario:")
		if not username:
			return
		password = simpledialog.askstring("Contraseña", "Ingresar contraseña:", show='*')
		if not password:
			return
		add_password(site, username, password, self.key)
		messagebox.showinfo("Hecho", "Contraseña añadida.")

	def get_password(self):
		site = simpledialog.askstring("Sitio", "Ingresar nombre del sitio:")
		if not site:
			return
		entry = get_password(site, self.key)
		self.output.config(state=tk.NORMAL)
		self.output.delete(1.0, tk.END)
		if entry:
			self.output.insert(tk.END, f"Sitio: {site}\nUsuario: {entry['username']}\nContraseña: {entry['password']}\n")
		else:
			self.output.insert(tk.END, "Ninguna entrada encontrada.\n")
		self.output.config(state=tk.DISABLED)

	def delete_password(self):
		site = simpledialog.askstring("Sitio", "Entra el nombre del sitio para eliminar:")
		if not site:
			return
		delete_password(site, self.key)
		messagebox.showinfo("Eliminado", "Eliminado si existia.")

	def list_sites(self):
		sites = list_sites(self.key)
		self.output.config(state=tk.NORMAL)
		self.output.delete(1.0, tk.END)
		if sites:
			self.output.insert(tk.END, "Sitios:\n" + '\n'.join(sites))
		else:
			self.output.insert(tk.END, "Ningun sitio encontrado.")
		self.output.config(state=tk.DISABLED)

def main():
	root = tk.Tk()
	app = PasswordManagerGUI(root)
	root.mainloop()

if __name__ == "__main__":
	main()

