

import socket
import tkinter as tk
from tkinter import messagebox, filedialog

HOST = '127.0.0.1' 
PORT = 5001

def download_file():
    filename = entry.get().strip()
    if not filename:
        messagebox.showwarning("Input Error", "Please enter a filename.")
        return

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        client.send(filename.encode())

        status = client.recv(1024).decode()

        if status == "FOUND":
            filesize = int(client.recv(1024).decode())


            save_path = filedialog.asksaveasfilename(
                initialfile=filename,
                title="Save File As",
                defaultextension="*.*"
            )

            if not save_path:
                client.close()
                return

            with open(save_path, 'wb') as f:
                bytes_received = 0
                while bytes_received < filesize:
                    data = client.recv(1024)
                    if not data:
                        break
                    f.write(data)
                    bytes_received += len(data)

            messagebox.showinfo("Success", f"'{filename}' downloaded successfully!\nSize: {filesize} bytes")
        else:
            messagebox.showerror("Error", f"File '{filename}' not found on server.")

        client.close()

    except ConnectionRefusedError:
        messagebox.showerror("Connection Error", "Unable to connect to the server.\nMake sure the server is running.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("File Transfer Client")
root.geometry("400x200")
root.resizable(False, False)

title_label = tk.Label(root, text="File Transfer Client", font=("Arial", 14, "bold"), fg="#333")
title_label.pack(pady=10)

tk.Label(root, text="Enter filename to download:", font=("Arial", 11)).pack(pady=5)
entry = tk.Entry(root, width=40, font=("Arial", 10))
entry.pack(pady=5)

download_btn = tk.Button(root, text="Download File", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), width=20, command=download_file)
download_btn.pack(pady=15)

status_label = tk.Label(root, text="", font=("Arial", 10), fg="gray")
status_label.pack()

root.mainloop()
