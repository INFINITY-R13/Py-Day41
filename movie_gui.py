import tkinter as tk
from tkinter import ttk

# --- 1. Create the Main Application Window ---
# This is the main container for all the other widgets.
window = tk.Tk()
window.title("My Movie Rankings") # Sets the text in the title bar
window.geometry("500x350") # Sets the initial size of the window (width x height)
window.configure(bg="#f0f0f0") # Set a light grey background color for the window

# --- 2. Create and Style the Widgets ---
# We will use Label widgets to display text.
# The 'font' option is used to control the text appearance (family, size, style).

# Main Heading (like <h1>)
# We use a larger, bold font to make it stand out.
main_heading = tk.Label(
    window,
    text="The Best Movies According to INFINITY",
    font=("Helvetica", 18, "bold"),
    bg="#f0f0f0" # Match the background color of the window
)
# The pack() method is one way to place widgets in the window.
# 'pady' adds vertical padding, and 'anchor="w"' aligns the text to the West (left).
main_heading.pack(pady=(10, 5), padx=15, anchor="w")

# Subheading (like <h2>)
sub_heading = tk.Label(
    window,
    text="My Top 3 Movies of All Time",
    font=("Helvetica", 14),
    bg="#f0f0f0"
)
sub_heading.pack(pady=(0, 10), padx=15, anchor="w")

# Separator (like <hr>)
# The ttk module provides more modern-looking widgets, including a Separator.
separator = ttk.Separator(window, orient='horizontal')
# 'fill="x"' makes the separator line span the full width of the window.
separator.pack(fill='x', padx=10, pady=5)

# --- Movie 1 ---
movie1_title = tk.Label(
    window,
    text="I Want To Eat Your Pancreas",
    font=("Helvetica", 12, "bold"),
    bg="#f0f0f0"
)
movie1_title.pack(pady=(10, 0), padx=15, anchor="w")

movie1_desc = tk.Label(
    window,
    text="The Best Anime Movie because of Sakura",
    font=("Helvetica", 11),
    bg="#f0f0f0",
    justify=tk.LEFT # Ensures multi-line text is left-aligned
)
movie1_desc.pack(pady=(2, 5), padx=15, anchor="w")

# --- Movie 2 ---
movie2_title = tk.Label(
    window,
    text="The Amazing Spider-Man 2",
    font=("Helvetica", 12, "bold"),
    bg="#f0f0f0"
)
movie2_title.pack(pady=(10, 0), padx=15, anchor="w")

movie2_desc = tk.Label(
    window,
    text="The Best Spider-Man Movie because of Gwen",
    font=("Helvetica", 11),
    bg="#f0f0f0",
    justify=tk.LEFT
)
movie2_desc.pack(pady=(2, 5), padx=15, anchor="w")

# --- Movie 3 ---
movie3_title = tk.Label(
    window,
    text="The Dark Knight",
    font=("Helvetica", 12, "bold"),
    bg="#f0f0f0"
)
movie3_title.pack(pady=(10, 0), padx=15, anchor="w")

movie3_desc = tk.Label(
    window,
    text="The Best Batman Movie because of Joker",
    font=("Helvetica", 11),
    bg="#f0f0f0",
    justify=tk.LEFT
)
movie3_desc.pack(pady=(2, 5), padx=15, anchor="w")


# --- 3. Start the Application's Main Loop ---
# This line displays the window and keeps it open, listening for events
# like button clicks or window closing. The program ends when the window is closed.
window.mainloop()
