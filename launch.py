import tkinter as tk
import subprocess
import webbrowser


    
def show_error(error):
    bootpage = tk.Tk()
    bootpage.title("Launch")

    # Set window size and make it non-resizable
    bootpage.geometry("500x400")  # width x height
    bootpage.resizable(False, False)

    def run_ollama():
        if ollama_erorr == "missing ollama":
            # If there's an error, display a message and a link
            error_label.config(text="Error: Make sure you have 'Ollama' installed\n")
            link_label.config(text="Click here to install 'Ollama'", cursor="hand2")
            link_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://ollama.com"))
        else:
            # If there's an error, display a message and a link
            error_label.config(text="Error: " + str(ollama_erorr))
            

    # Button to launch ollama
    launch_button = tk.Button(bootpage, text="Launch Ollama", command=run_ollama, pady=10)

    launch_button.pack()

    # Label to display error message
    error_label = tk.Label(bootpage, text="", fg="red", font=("Arial", 14))
    error_label.pack()

    # Label for the link
    link_label = tk.Label(bootpage, text="", fg="blue", cursor="", font=("Arial", 14))
    link_label.pack()

    bootpage.mainloop()




ollama_erorr = None
try:
    # Run the shell command
    subprocess.run(["ollama serve"], check=True)
    subprocess.run(["pip install -r requirements.txt"], check=True)
except Exception as error:
    if error == FileNotFoundError:
        show_error("missing ollama")
    else:
        print(error)
