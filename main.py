import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import ollama


model = "llava:7b"
ollama.pull(model)

def prompt(messages):
    stream = ollama.chat(
        model=model,
        stream=True,
        messages=messages
        # messages=[
        #     {
        #         'role': 'user',
        #         'content': 'Describe this image:',
        #         'images': ['./art.jpg']
        #     }
        # ]
    )
    return stream

def send_letter():
    global selected_images
    global message_index
    global message
    global send_id  # Declare send_id as a global variable
    if message_index < len(message):
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "User: " + message[message_index] + "\n")
        chat_box.see(tk.END)  # Scrolls chat_box to the bottom
        chat_box.config(state=tk.DISABLED)
        message_index += 1
        # Schedule sending the next letter after a delay (in milliseconds)
        send_id = root.after(delay, send_letter)
        send_button.config(state=tk.DISABLED)
        stop_button.pack(side=tk.LEFT, padx=5)  # Show stop button during sending
    else:
        stop_sending()

def stop_sending():
    global send_id  # Declare send_id as a global variable
    root.after_cancel(send_id)
    send_button.config(state=tk.NORMAL)
    stop_button.pack_forget()  # Hide stop button after sending stops

def start_sending():
    global message_index
    global message
    message = entry.get()
    if message:
        message_index = 0
        send_letter()

def clear_messages():
    chat_box.config(state=tk.NORMAL)
    chat_box.delete('1.0', tk.END)  # Delete all text from the chat box
    chat_box.config(state=tk.DISABLED)

def open_image_options():
    image_options_window = tk.Toplevel(root)
    image_options_window.title("Add an Image")

    # Set the initial size of the window
    image_options_window.geometry("260x70")

    # Get the dimensions of the root window
    root_width = root.winfo_width()
    root_height = root.winfo_height()

    # Calculate the coordinates for centering the popup window
    x_position = root.winfo_rootx() + root_width // 2 - 150  # Half of popup window width
    y_position = root.winfo_rooty() + root_height // 2 - 100  # Half of popup window height

    # Set the position of the popup window
    image_options_window.geometry(f"+{x_position}+{y_position}")

    # Prevent resizing of the window
    image_options_window.resizable(False, False)

    def take_screenshot():
        # Your code to take a screenshot goes here
        pass

    def open_saved_image():
        file_path = filedialog.askopenfilename()
        if file_path:
            selected_images.append(file_path)
            print("Selected file:", file_path)


    # Load images for buttons
    global screenshot_image, saved_image_image  # Keep references to prevent garbage collection
    screenshot_image = tk.PhotoImage(file="icons/snipping.png")
    saved_image_image = tk.PhotoImage(file="icons/search.png")

    def create_screenshot_button():
        screenshot_button = tk.Button(image_options_window, text="Screenshot", image=screenshot_image,
                                       command=take_screenshot, compound=tk.LEFT)
        screenshot_button.grid(row=0, column=0, padx=5, pady=5)

    def create_saved_image_button():
        saved_image_button = tk.Button(image_options_window, text="Saved Image", image=saved_image_image,
                                       command=open_saved_image, compound=tk.LEFT)
        saved_image_button.grid(row=0, column=1, padx=5, pady=5)

    create_screenshot_button()
    create_saved_image_button()

# Create the main application window
root = tk.Tk()
root.title("Assistant")

# Set window size and make it non-resizable
root.geometry("500x400")  # width x height
root.resizable(False, False)

# Create a Notebook (tabbed interface)
notebook = ttk.Notebook(root)

# Tab 1
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Chat')

# Frame to contain input box, send button, and stop button
chat_frame = tk.Frame(tab1)
chat_frame.pack(pady=10)

label = tk.Label(chat_frame, text="Enter Message:")
label.pack(side=tk.TOP)

entry = tk.Entry(chat_frame, width=40)
entry.pack(side=tk.TOP, pady=5)

send_button = tk.Button(chat_frame, text="Send", command=start_sending)
send_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(chat_frame, text="Clear", command=clear_messages)
clear_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(chat_frame, text="Stop", command=stop_sending)  # Initially hidden

image_button = tk.Button(chat_frame, text="Add Image", command=open_image_options)
image_button.pack(side=tk.LEFT, padx=5)

chat_box = tk.Text(tab1, width=50, height=20, state=tk.DISABLED)
chat_box.pack(pady=5)

# Tab 2
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Summarize')

label = tk.Label(tab2, text="Hello, Summarize!")
label.pack(pady=10)

button_2 = tk.Button(tab2, text="Click Me - Summarize")
button_2.pack(pady=5)

# Settings
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Settings')

label = tk.Label(tab2, text="Hello, Summarize!")
label.pack(pady=10)

button_2 = tk.Button(tab2, text="Click Me - Summarize")
button_2.pack(pady=5)

# Pack the notebook (tabbed interface) into the root window
notebook.pack(expand=True, fill='both')

# Global variables
delay = 500  # Delay between sending each letter (in milliseconds)
message_index = 0  # Index to keep track of the current letter being sent
message = ""  # Message to be sent
send_id = None  # ID for the send_letter after method

# Variable to store selected images
selected_images = []

# Start the Tkinter event loop
root.mainloop()
