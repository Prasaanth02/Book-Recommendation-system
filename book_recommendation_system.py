import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import json
import os

class BookRecommendationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Recommendation System")
        self.root.geometry("900x600")  # Increased size to fit all books
        self.root.configure(bg="#f0f0f0")
        
        # Define mood colors for a more colorful interface
        self.mood_colors = {
            "Happy 😊": {"primary": "#FFD700", "secondary": "#FFEB99", "text": "#8B4513"},  # Gold/Yellow
            "Sad 😢": {"primary": "#6495ED", "secondary": "#B0C4DE", "text": "#00008B"},    # Blue
            "Excited 🤩": {"primary": "#FF4500", "secondary": "#FFA07A", "text": "#8B0000"}, # Orange/Red
            "Relaxed 😌": {"primary": "#98FB98", "secondary": "#DCFCDC", "text": "#006400"}, # Light Green
            "Curious 🧐": {"primary": "#9370DB", "secondary": "#D8BFD8", "text": "#4B0082"}, # Purple
            "Adventurous 🧗": {"primary": "#20B2AA", "secondary": "#AFEEEE", "text": "#008080"}, # Teal
            "Inspired ✨": {"primary": "#FF69B4", "secondary": "#FFC0CB", "text": "#8B008B"}  # Pink
        }
        
        # Track the currently selected mood button for highlighting
        self.selected_mood_btn = None
        
        # User data file path
        self.user_data_file = os.path.join(os.path.expanduser("~"), "book_recommendations_data.json")
        
        # Settings file path
        self.settings_file = os.path.join(os.path.expanduser("~"), ".book_rec_settings.json")
        
        # Load settings and check for custom data location
        self.settings = self.load_settings()
        if "data_location" in self.settings:
            self.user_data_file = self.settings["data_location"]
        
        # Load user data (saved books and ratings)
        self.user_data = self.load_user_data()
        
        # Book database organized by mood with emojis
        self.moods_with_emojis = {
            "Happy 😊": [
                {"title": "The Alchemist", "author": "Paulo Coelho", "description": "A magical story about following your dreams."},
                {"title": "A Man Called Ove", "author": "Fredrik Backman", "description": "A heartwarming tale about the transformative power of friendship."},
                {"title": "The House in the Cerulean Sea", "author": "TJ Klune", "description": "A charming fantasy novel full of joy and found family."},
                {"title": "Where the Crawdads Sing", "author": "Delia Owens", "description": "A beautiful coming-of-age story set in the marshes of North Carolina."},
                {"title": "Project Hail Mary", "author": "Andy Weir", "description": "An uplifting sci-fi adventure about saving humanity."}
            ],
            "Sad 😢": [
                {"title": "A Little Life", "author": "Hanya Yanagihara", "description": "A profound exploration of trauma, friendship, and healing."},
                {"title": "The Road", "author": "Cormac McCarthy", "description": "A post-apocalyptic tale of a father and son's journey."},
                {"title": "Never Let Me Go", "author": "Kazuo Ishiguro", "description": "A melancholic story about love and what it means to be human."},
                {"title": "Norwegian Wood", "author": "Haruki Murakami", "description": "A nostalgic story of loss and growing up."},
                {"title": "The Book Thief", "author": "Markus Zusak", "description": "A poignant tale set during World War II, narrated by Death."}
            ],
            "Excited 🤩": [
                {"title": "Ready Player One", "author": "Ernest Cline", "description": "A thrilling adventure in a virtual reality world."},
                {"title": "The Hunger Games", "author": "Suzanne Collins", "description": "A fast-paced dystopian adventure of survival."},
                {"title": "Jurassic Park", "author": "Michael Crichton", "description": "A thrilling sci-fi adventure with dinosaurs."},
                {"title": "The Da Vinci Code", "author": "Dan Brown", "description": "A page-turning mystery filled with codes and conspiracies."},
                {"title": "Artemis Fowl", "author": "Eoin Colfer", "description": "An exciting tale of a young criminal mastermind."}
            ],
            "Relaxed 😌": [
                {"title": "The Thursday Murder Club", "author": "Richard Osman", "description": "A cozy mystery solved by retirement home residents."},
                {"title": "Under the Tuscan Sun", "author": "Frances Mayes", "description": "A memoir about renovating a villa in Tuscany."},
                {"title": "The No. 1 Ladies' Detective Agency", "author": "Alexander McCall Smith", "description": "Gentle mysteries set in Botswana."},
                {"title": "A Year in Provence", "author": "Peter Mayle", "description": "A charming account of life in the French countryside."},
                {"title": "The Secret Garden", "author": "Frances Hodgson Burnett", "description": "A classic tale of renewal and growth."}
            ],
            "Curious 🧐": [
                {"title": "Sapiens", "author": "Yuval Noah Harari", "description": "A brief history of humankind."},
                {"title": "Freakonomics", "author": "Steven D. Levitt & Stephen J. Dubner", "description": "Exploring the hidden side of everything."},
                {"title": "Cosmos", "author": "Carl Sagan", "description": "A journey through the universe."},
                {"title": "The Code Breaker", "author": "Walter Isaacson", "description": "The story of CRISPR and gene editing."},
                {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "description": "An exploration of the two systems that drive the way we think."}
            ],
            "Adventurous 🧗": [
                {"title": "Into Thin Air", "author": "Jon Krakauer", "description": "A personal account of the Mt. Everest disaster."},
                {"title": "The Lost City of Z", "author": "David Grann", "description": "A tale of deadly obsession in the Amazon."},
                {"title": "Endurance", "author": "Alfred Lansing", "description": "Shackleton's incredible voyage in Antarctica."},
                {"title": "Wild", "author": "Cheryl Strayed", "description": "A woman's journey of self-discovery on the Pacific Crest Trail."},
                {"title": "The Hobbit", "author": "J.R.R. Tolkien", "description": "A classic adventure of a hobbit's unexpected journey."}
            ],
            "Inspired ✨": [
                {"title": "Educated", "author": "Tara Westover", "description": "A memoir about the transformative power of education."},
                {"title": "Becoming", "author": "Michelle Obama", "description": "The former First Lady's inspiring journey."},
                {"title": "Atomic Habits", "author": "James Clear", "description": "Building good habits and breaking bad ones."},
                {"title": "Man's Search for Meaning", "author": "Viktor E. Frankl", "description": "Finding purpose and meaning in difficult circumstances."},
                {"title": "The Power of Now", "author": "Eckhart Tolle", "description": "A guide to spiritual enlightenment."}
            ]
        }
        
        # Current view mode (recommendations or saved books)
        self.current_view = "recommendations"
        
        self.create_widgets()
        
    def load_user_data(self):
        """Load user data from JSON file"""
        if os.path.exists(self.user_data_file):
            try:
                with open(self.user_data_file, 'r') as f:
                    return json.load(f)
            except:
                return {"saved_books": []}
        else:
            return {"saved_books": []}
    
    def save_user_data(self):
        """Save user data to JSON file"""
        # Ensure directory exists
        os.makedirs(os.path.dirname(self.user_data_file), exist_ok=True)
        with open(self.user_data_file, 'w') as f:
            json.dump(self.user_data, f)
            
    def load_settings(self):
        """Load application settings"""
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        else:
            return {}
        
    def save_settings(self):
        """Save application settings"""
        os.makedirs(os.path.dirname(self.settings_file), exist_ok=True)
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f)
            
    def choose_data_location(self):
        """Let user choose where to save their data"""
        # Get directory from user
        directory = filedialog.askdirectory(
            title="Choose where to save your book recommendations data",
            initialdir=os.path.dirname(self.user_data_file)
        )
        
        if directory:  # If user didn't cancel
            # Create the new file path
            new_file_path = os.path.join(directory, "book_recommendations_data.json")
            
            # If we already have data and the file location is changing
            if os.path.exists(self.user_data_file) and self.user_data_file != new_file_path:
                # Copy existing data to new location
                try:
                    with open(self.user_data_file, 'r') as src:
                        data = json.load(src)
                    with open(new_file_path, 'w') as dst:
                        json.dump(data, dst)
                    messagebox.showinfo("Success", f"Your data has been moved to:\n{new_file_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"Could not move your data: {str(e)}")
                    return
            
            # Update the file path
            self.user_data_file = new_file_path
            
            # Save the new location in settings
            self.settings["data_location"] = new_file_path
            self.save_settings()
            
            # Reload data from the new location
            self.user_data = self.load_user_data()
            
    def show_settings(self):
        """Show settings dialog"""
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("400x300")
        settings_window.configure(bg="#f0f0f0")
        settings_window.resizable(False, False)
        
        # Make it modal
        settings_window.transient(self.root)
        settings_window.grab_set()
        
        # Header
        header_label = tk.Label(
            settings_window,
            text="Settings",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            pady=10
        )
        header_label.pack(fill=tk.X)
        
        # Data location section
        location_frame = tk.LabelFrame(
            settings_window,
            text="Data Storage Location",
            font=("Arial", 12),
            bg="#f0f0f0",
            padx=20,
            pady=15
        )
        location_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Current location
        current_location_label = tk.Label(
            location_frame,
            text="Current location:",
            font=("Arial", 10),
            bg="#f0f0f0",
            anchor="w"
        )
        current_location_label.pack(fill=tk.X)
        
        location_text = tk.Text(
            location_frame,
            height=2,
            width=40,
            font=("Arial", 9),
            wrap=tk.WORD,
            bg="#ffffff",
            relief=tk.SUNKEN,
            state=tk.DISABLED
        )
        location_text.pack(fill=tk.X, pady=5)
        
        # Enable, insert text, then disable again
        location_text.configure(state=tk.NORMAL)
        location_text.insert(tk.END, self.user_data_file)
        location_text.configure(state=tk.DISABLED)
        
        # Change location button
        change_btn = tk.Button(
            location_frame,
            text="Change Location",
            command=lambda: [self.choose_data_location(), settings_window.destroy()],
            font=("Arial", 10),
            bg="#4a7abc",
            fg="white",
            padx=10,
            pady=5
        )
        change_btn.pack(pady=10)
        
        # Close button
        close_btn = tk.Button(
            settings_window,
            text="Close",
            command=settings_window.destroy,
            font=("Arial", 10),
            bg="#f0f0f0",
            padx=20,
            pady=5
        )
        close_btn.pack(side=tk.BOTTOM, pady=20)
        
        # Center the window
        settings_window.update_idletasks()
        width = settings_window.winfo_width()
        height = settings_window.winfo_height()
        x = (self.root.winfo_width() // 2) - (width // 2) + self.root.winfo_x()
        y = (self.root.winfo_height() // 2) - (height // 2) + self.root.winfo_y()
        settings_window.geometry(f"{width}x{height}+{x}+{y}")
        
    def create_widgets(self):
        # Header with gradient effect
        header_frame = tk.Frame(self.root, bg="#4a7abc")
        header_frame.pack(fill=tk.X)
        
        # Create a canvas for the gradient header
        header_canvas = tk.Canvas(header_frame, height=70, bg="#4a7abc", highlightthickness=0)
        header_canvas.pack(fill=tk.X)
        
        # Create gradient effect
        for i in range(70):
            # Gradient from darker blue to lighter blue
            r = int(74 + (i/70) * 50)  # 74 to 124
            g = int(122 + (i/70) * 50)  # 122 to 172
            b = int(188 + (i/70) * 30)  # 188 to 218
            color = f'#{r:02x}{g:02x}{b:02x}'
            header_canvas.create_line(0, i, 900, i, fill=color)
        
        header_label = tk.Label(
            header_canvas, 
            text="📚 Book Recommendation System 📚", 
            font=("Arial", 24, "bold"), 
            bg="#4a7abc", 
            fg="white",
            pady=10
        )
        header_canvas.create_window(450, 35, window=header_label)
        
        # Navigation buttons at the top right
        nav_frame = tk.Frame(header_frame, bg="#4a7abc")
        nav_frame.pack(anchor="ne", padx=20, pady=(0, 10))
        
        # Settings button
        settings_btn = tk.Button(
            nav_frame,
            text="⚙️ Settings",
            command=self.show_settings,
            font=("Arial", 11),
            bg="#f0f0f0",
            fg="#4a7abc",
            padx=10,
            pady=5,
            relief=tk.RAISED,
            bd=1,
            cursor="hand2"
        )
        settings_btn.pack(side=tk.LEFT, padx=10)
        
        # Add hover effect to settings button
        def on_settings_enter(e):
            settings_btn['bg'] = '#e6e6e6'
            settings_btn['fg'] = '#2a5a9c'
        
        def on_settings_leave(e):
            settings_btn['bg'] = '#f0f0f0'
            settings_btn['fg'] = '#4a7abc'
            
        settings_btn.bind("<Enter>", on_settings_enter)
        settings_btn.bind("<Leave>", on_settings_leave)
        
        # Enhanced "My Saved Books" button with hover effect
        saved_btn = tk.Button(
            nav_frame,
            text="My Saved Books 🔖",
            command=self.show_saved_books_view,
            font=("Arial", 11, "bold"),
            bg="#f0f0f0",
            fg="#4a7abc",
            padx=15,
            pady=8,
            relief=tk.RAISED,
            bd=2,
            cursor="hand2"
        )
        saved_btn.pack(side=tk.RIGHT)
        
        # Add hover effect to the button
        def on_enter(e):
            saved_btn['bg'] = '#e6e6e6'
            saved_btn['fg'] = '#2a5a9c'
        
        def on_leave(e):
            saved_btn['bg'] = '#f0f0f0'
            saved_btn['fg'] = '#4a7abc'
            
        saved_btn.bind("<Enter>", on_enter)
        saved_btn.bind("<Leave>", on_leave)
        
        # Main content
        content_frame = tk.Frame(self.root, bg="#f0f0f0")
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Mood selection frame with enhanced styling - centered at the top
        self.mood_selection_frame = tk.Frame(content_frame, bg="#f0f0f0")
        self.mood_selection_frame.pack(fill=tk.X)
        
        # Center container for mood selection
        center_frame = tk.Frame(self.mood_selection_frame, bg="#f0f0f0")
        center_frame.pack(pady=10, fill=tk.X)
        
        mood_frame = tk.LabelFrame(
            center_frame, 
            text="How are you feeling today? 🤔", 
            font=("Arial", 16, "bold"), 
            bg="#f0f0f0", 
            fg="#333333",
            padx=20, 
            pady=15,
            relief=tk.GROOVE,
            bd=2
        )
        mood_frame.pack(pady=5, padx=20, anchor="center")
        
        self.mood_var = tk.StringVar()
        moods = list(self.moods_with_emojis.keys())
        self.mood_buttons = {}  # Store references to mood buttons
        
        # Create a grid layout for mood buttons - all in one row
        mood_buttons_frame = tk.Frame(mood_frame, bg="#f0f0f0")
        mood_buttons_frame.pack(pady=10)
        
        for i, mood in enumerate(moods):
            # Use the mood-specific colors
            color = self.mood_colors[mood]["primary"]
            secondary_color = self.mood_colors[mood]["secondary"]
            text_color = self.mood_colors[mood]["text"]
            
            # Create a frame for each mood button for better styling
            btn_frame = tk.Frame(mood_buttons_frame, bg="#f0f0f0", padx=3, pady=3)
            btn_frame.grid(row=0, column=i, padx=3, pady=3)
            
            # Create the mood button with custom styling - larger and more prominent
            mood_btn = tk.Button(
                btn_frame, 
                text=mood, 
                font=("Arial", 12, "bold"),
                bg=color,
                fg=text_color,
                activebackground=secondary_color,
                activeforeground=text_color,
                padx=8,
                pady=10,
                relief=tk.RAISED,
                bd=2,
                width=10,
                height=2,
                cursor="hand2"
            )
            mood_btn.pack(fill=tk.BOTH, expand=True)
            
            # Store reference to the button
            self.mood_buttons[mood] = mood_btn
            
            # Configure button click
            mood_btn.configure(command=lambda m=mood, btn=mood_btn: self.select_mood(m, btn))
            
            # Add hover effect
            mood_btn.bind("<Enter>", lambda e, btn=mood_btn, c=secondary_color: self.on_mood_enter(btn, c))
            mood_btn.bind("<Leave>", lambda e, btn=mood_btn, m=mood: self.on_mood_leave(btn, m))
        
        # Results frame with scrollbar
        self.results_container = tk.Frame(content_frame, bg="#f0f0f0")
        self.results_container.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Add scrollbar
        self.canvas = tk.Canvas(self.results_container, bg="#f0f0f0", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.results_container, orient="vertical", command=self.canvas.yview)
        self.results_frame = tk.Frame(self.canvas, bg="#f0f0f0")
        
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.results_frame, anchor="nw")
        
        # Configure scrolling with mouse wheel
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)  # For Windows
        self.canvas.bind_all("<Button-4>", self._on_mousewheel)    # For Linux (scroll up)
        self.canvas.bind_all("<Button-5>", self._on_mousewheel)    # For Linux (scroll down)
        
        self.results_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        
        # Initial message
        self.initial_msg = tk.Label(
            self.results_frame,
            text="Select your mood to get book recommendations! 📚",
            font=("Arial", 12, "italic"),
            bg="#f0f0f0",
            wraplength=800,
            justify=tk.CENTER
        )
        self.initial_msg.pack(pady=30)
        
        # Footer
        footer_frame = tk.Frame(self.root, bg="#4a7abc", height=30)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        footer_label = tk.Label(
            footer_frame,
            text="© 2023 Book Recommendation System 📚",
            font=("Arial", 8),
            bg="#4a7abc",
            fg="white",
            pady=5
        )
        footer_label.pack()
    
    def _on_mousewheel(self, event):
        """Handle mouse wheel scrolling"""
        # Different event handling for different platforms
        if event.num == 4:  # Linux scroll up
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:  # Linux scroll down
            self.canvas.yview_scroll(1, "units")
        else:  # Windows
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
    def on_frame_configure(self, event):
        """Reset the scroll region to encompass the inner frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def on_canvas_configure(self, event):
        """When the canvas changes size, resize the window within it"""
        width = event.width
        self.canvas.itemconfig(self.canvas_frame, width=width)
    
    def show_recommendations_view(self):
        """Switch to recommendations view with animation effect"""
        self.current_view = "recommendations"
        self.mood_selection_frame.pack(fill=tk.X)
        self.clear_results()
        
        # Create a more visually appealing welcome screen
        welcome_frame = tk.Frame(self.results_frame, bg="#f0f0f0")
        welcome_frame.pack(fill=tk.BOTH, expand=True)
        
        # Welcome emoji with animation effect
        emoji_label = tk.Label(
            welcome_frame,
            text="📚",
            font=("Arial", 48),
            bg="#f0f0f0",
            fg="#4a7abc"
        )
        emoji_label.pack(pady=(50, 10))
        
        # Animate the emoji
        def animate_emoji():
            current_size = int(emoji_label.cget("font").split()[1])
            if current_size < 60:
                emoji_label.config(font=("Arial", current_size + 1))
                self.root.after(50, animate_emoji)
            else:
                # Shrink back
                shrink_emoji()
                
        def shrink_emoji():
            current_size = int(emoji_label.cget("font").split()[1])
            if current_size > 48:
                emoji_label.config(font=("Arial", current_size - 1))
                self.root.after(50, shrink_emoji)
        
        # Start animation
        self.root.after(100, animate_emoji)
        
        # Welcome message
        welcome_label = tk.Label(
            welcome_frame,
            text="Welcome to Book Recommendations!",
            font=("Arial", 18, "bold"),
            bg="#f0f0f0",
            fg="#4a7abc"
        )
        welcome_label.pack()
        
        # Instructions
        self.initial_msg = tk.Label(
            welcome_frame,
            text="Select your mood above to discover books tailored to how you feel today.",
            font=("Arial", 12, "italic"),
            bg="#f0f0f0",
            wraplength=800,
            justify=tk.CENTER
        )
        self.initial_msg.pack(pady=10)
        
        # Add a decorative element
        separator = ttk.Separator(welcome_frame, orient="horizontal")
        separator.pack(fill=tk.X, padx=150, pady=20)
    
    def show_saved_books_view(self):
        """Switch to saved books view"""
        self.current_view = "saved_books"
        self.mood_selection_frame.pack_forget()
        self.display_saved_books()
    
    def clear_results(self):
        """Clear the results frame"""
        for widget in self.results_frame.winfo_children():
            widget.destroy()
    
    def save_book(self, book, mood):
        """Save a book to user data"""
        # Check if book is already saved
        for saved_book in self.user_data["saved_books"]:
            if saved_book["title"] == book["title"] and saved_book["author"] == book["author"]:
                messagebox.showinfo("Already Saved", f"'{book['title']}' is already in your saved books!")
                return
        
        # Add book to saved books
        saved_book = book.copy()
        saved_book["mood"] = mood
        saved_book["rating"] = 0  # Default rating
        self.user_data["saved_books"].append(saved_book)
        self.save_user_data()
        messagebox.showinfo("Book Saved", f"'{book['title']}' has been added to your saved books!")
    
    def rate_book(self, book_title, rating):
        """Rate a saved book"""
        for book in self.user_data["saved_books"]:
            if book["title"] == book_title:
                book["rating"] = rating
                self.save_user_data()
                messagebox.showinfo("Rating Saved", f"You rated '{book_title}' {rating}/5 stars!")
                # Refresh the saved books view if currently viewing it
                if self.current_view == "saved_books":
                    self.display_saved_books()
                return
    
    def remove_saved_book(self, book_title):
        """Remove a book from saved books"""
        for i, book in enumerate(self.user_data["saved_books"]):
            if book["title"] == book_title:
                del self.user_data["saved_books"][i]
                self.save_user_data()
                messagebox.showinfo("Book Removed", f"'{book_title}' has been removed from your saved books.")
                # Refresh the saved books view
                self.display_saved_books()
                return
    
    def display_saved_books(self):
        """Display all saved books"""
        self.clear_results()
        
        if not self.user_data["saved_books"]:
            # Create a visually appealing empty state
            empty_frame = tk.Frame(self.results_frame, bg="#f0f0f0", pady=30)
            empty_frame.pack(fill=tk.BOTH, expand=True)
            
            # Empty state icon
            empty_label = tk.Label(
                empty_frame,
                text="📚",
                font=("Arial", 48),
                bg="#f0f0f0"
            )
            empty_label.pack(pady=(50, 10))
            
            # Empty state message
            no_books_label = tk.Label(
                empty_frame,
                text="You haven't saved any books yet!",
                font=("Arial", 16, "bold"),
                bg="#f0f0f0",
                wraplength=800,
                justify=tk.CENTER
            )
            no_books_label.pack()
            
            # Empty state instruction
            instruction_label = tk.Label(
                empty_frame,
                text="Select a mood to get recommendations and save books you like.",
                font=("Arial", 12, "italic"),
                bg="#f0f0f0",
                wraplength=800,
                justify=tk.CENTER
            )
            instruction_label.pack(pady=10)
            
            # Back to recommendations button
            back_btn = tk.Button(
                empty_frame,
                text="Get Recommendations 📖",
                command=self.show_recommendations_view,
                font=("Arial", 12, "bold"),
                bg="#4a7abc",
                fg="white",
                padx=15,
                pady=8,
                relief=tk.RAISED,
                cursor="hand2"
            )
            back_btn.pack(pady=20)
            
            # Add hover effect
            def on_back_enter(e):
                back_btn['bg'] = '#3a5a8c'
            
            def on_back_leave(e):
                back_btn['bg'] = '#4a7abc'
                
            back_btn.bind("<Enter>", on_back_enter)
            back_btn.bind("<Leave>", on_back_leave)
            
            return
        
        # Enhanced header for saved books with gradient effect
        header_frame = tk.Frame(self.results_frame, bg="#4a7abc", padx=15, pady=15, relief=tk.GROOVE)
        header_frame.pack(fill=tk.X, pady=(10, 20))
        
        # Create gradient effect for header
        header_canvas = tk.Canvas(header_frame, height=60, bg="#4a7abc", highlightthickness=0)
        header_canvas.pack(fill=tk.X)
        
        for i in range(60):
            # Gradient from darker purple to lighter purple
            r = int(74 + (i/60) * 50)
            g = int(122 + (i/60) * 50)
            b = int(188 + (i/60) * 30)
            color = f'#{r:02x}{g:02x}{b:02x}'
            header_canvas.create_line(0, i, 900, i, fill=color)
        
        saved_header = tk.Label(
            header_canvas,
            text="📚 Your Saved Books 📚",
            font=("Arial", 18, "bold"),
            bg="#4a7abc",
            fg="white",
            pady=10
        )
        header_canvas.create_window(450, 30, window=saved_header)
        
        # Create a frame for all books
        books_container = tk.Frame(self.results_frame, bg="#f0f0f0")
        books_container.pack(fill=tk.BOTH, expand=True)
        
        # Display all saved books
        for i, book in enumerate(self.user_data["saved_books"]):
            # Create a frame for each book
            book_frame = tk.Frame(books_container, bg="#f0f0f0", padx=10, pady=10, relief=tk.RIDGE, bd=1)
            book_frame.pack(fill=tk.X, pady=10, padx=20)
            
            # Top row with book number and mood
            top_row = tk.Frame(book_frame, bg="#f0f0f0")
            top_row.pack(fill=tk.X)
            
            # Book number
            number_label = tk.Label(
                top_row,
                text=f"Book {i+1}",
                font=("Arial", 10, "bold"),
                bg="#a0c8e2",
                fg="white",
                padx=5,
                pady=2
            )
            number_label.pack(side=tk.LEFT)
            
            # Mood label
            if "mood" in book:
                mood_name = book["mood"].split()[0]
                mood_label = tk.Label(
                    top_row,
                    text=f"Mood: {mood_name}",
                    font=("Arial", 10),
                    bg="#e6e6e6",
                    padx=5,
                    pady=2
                )
                mood_label.pack(side=tk.LEFT, padx=(10, 0))
            
            # Book title
            title_label = tk.Label(
                book_frame,
                text=f"📕 {book['title']}",
                font=("Arial", 14, "bold"),
                bg="#f0f0f0",
                fg="#4a7abc"
            )
            title_label.pack(pady=(5, 0))
            
            # Author
            author_label = tk.Label(
                book_frame,
                text=f"by {book['author']} ✍️",
                font=("Arial", 11, "italic"),
                bg="#f0f0f0"
            )
            author_label.pack(pady=(0, 5))
            
            # Description
            desc_frame = tk.Frame(book_frame, bg="#e6e6e6", padx=10, pady=10)
            desc_frame.pack(fill=tk.X, pady=5)
            
            desc_label = tk.Label(
                desc_frame,
                text=f"💬 {book['description']}",
                font=("Arial", 10),
                bg="#e6e6e6",
                wraplength=700,
                justify=tk.LEFT
            )
            desc_label.pack(anchor="w")
            
            # Rating and remove buttons frame
            action_frame = tk.Frame(book_frame, bg="#f0f0f0", pady=5)
            action_frame.pack(fill=tk.X)
            
            # Rating label
            rating_label = tk.Label(
                action_frame,
                text="Rate this book:",
                font=("Arial", 10),
                bg="#f0f0f0"
            )
            rating_label.pack(side=tk.LEFT, padx=(0, 5))
            
            # Rating buttons with enhanced interactive styling
            current_rating = book.get("rating", 0)
            star_frame = tk.Frame(action_frame, bg="#ffffff")
            star_frame.pack(side=tk.LEFT)
            
            for star in range(1, 6):
                is_filled = star <= current_rating
                
                star_btn = tk.Button(
                    star_frame,
                    text="★",
                    font=("Arial", 16),
                    bg="#ffffff",
                    fg="#ffcc00" if is_filled else "#dddddd",
                    activeforeground="#ffaa00",
                    bd=0,
                    padx=2,
                    cursor="hand2",
                    command=lambda b=book["title"], r=star: self.rate_book(b, r)
                )
                star_btn.pack(side=tk.LEFT)
                
                # Add hover effects for stars
                def on_star_enter(e, btn=star_btn, r=star, cr=current_rating):
                    # Highlight stars up to this one
                    for i, widget in enumerate(star_frame.winfo_children()):
                        if i < r:
                            widget.config(fg="#ffaa00")  # Brighter gold
                        else:
                            widget.config(fg="#dddddd")  # Light gray
                
                def on_star_leave(e, cr=current_rating):
                    # Restore original state
                    for i, widget in enumerate(star_frame.winfo_children()):
                        if i < cr:
                            widget.config(fg="#ffcc00")  # Gold
                        else:
                            widget.config(fg="#dddddd")  # Light gray
                
                star_btn.bind("<Enter>", on_star_enter)
                star_btn.bind("<Leave>", on_star_leave)
            
            # Remove button
            remove_btn = tk.Button(
                action_frame,
                text="🗑️ Remove",
                font=("Arial", 9),
                bg="#ff6b6b",
                fg="white",
                padx=5,
                pady=2,
                command=lambda b=book["title"]: self.remove_saved_book(b)
            )
            remove_btn.pack(side=tk.RIGHT)
        
        # Reset scroll position to top
        self.canvas.yview_moveto(0)
    
    def on_mood_enter(self, button, color):
        """Handle mouse enter event for mood buttons"""
        if button != self.selected_mood_btn:
            button.config(bg=color)
    
    def on_mood_leave(self, button, mood):
        """Handle mouse leave event for mood buttons"""
        if button != self.selected_mood_btn:
            button.config(bg=self.mood_colors[mood]["primary"])
    
    def select_mood(self, mood, button):
        """Handle mood selection with visual feedback"""
        # Reset previous selection if any
        if self.selected_mood_btn:
            prev_mood = self.mood_var.get()
            self.selected_mood_btn.config(
                bg=self.mood_colors[prev_mood]["primary"],
                relief=tk.RAISED
            )
        
        # Set the new selection
        self.mood_var.set(mood)
        self.selected_mood_btn = button
        
        # Highlight the selected button
        button.config(
            bg=self.mood_colors[mood]["secondary"],
            relief=tk.SUNKEN
        )
        
        # Show recommendations
        self.recommend_book()
    
    def recommend_book(self):
        """Display book recommendations based on selected mood"""
        if self.current_view != "recommendations":
            self.show_recommendations_view()
            return
            
        # Clear previous results
        self.clear_results()
        
        mood = self.mood_var.get()
        
        if not mood:
            messagebox.showinfo("Selection Required", "Please select your mood first! 🙂")
            self.initial_msg = tk.Label(
                self.results_frame,
                text="Select your mood to get book recommendations! 📚",
                font=("Arial", 12, "italic"),
                bg="#f0f0f0",
                wraplength=800,
                justify=tk.CENTER
            )
            self.initial_msg.pack(pady=30)
            return
        
        # Extract mood name without emoji for display
        mood_name = mood.split()[0]
        
        # Get mood-specific colors
        mood_color = self.mood_colors[mood]["primary"]
        mood_secondary = self.mood_colors[mood]["secondary"]
        mood_text = self.mood_colors[mood]["text"]
        
        # Create a themed header with the mood color
        header_frame = tk.Frame(self.results_frame, bg=mood_secondary, padx=15, pady=15, relief=tk.GROOVE, bd=2)
        header_frame.pack(fill=tk.X, pady=(10, 20))
        
        # Display header for recommendations with mood-specific styling
        mood_label = tk.Label(
            header_frame,
            text=f"📚 Based on your {mood_name.lower()} mood, we recommend these books: 📚",
            font=("Arial", 16, "bold"),
            bg=mood_secondary,
            fg=mood_text,
            pady=10
        )
        mood_label.pack()
        
        # Create a frame for all books with a subtle background color
        books_container = tk.Frame(self.results_frame, bg="#f0f0f0")
        books_container.pack(fill=tk.BOTH, expand=True)
        
        # Display all 5 books for the selected mood in a vertical list
        books = self.moods_with_emojis[mood]
        
        for i, book in enumerate(books):
            # Create a frame for each book with mood-themed styling
            book_frame = tk.Frame(
                books_container, 
                bg="#ffffff", 
                padx=15, 
                pady=15, 
                relief=tk.RIDGE, 
                bd=2,
                highlightbackground=mood_color,
                highlightthickness=2
            )
            book_frame.pack(fill=tk.X, pady=12, padx=20)
            
            # Add a subtle color bar on the left side
            color_bar = tk.Frame(book_frame, bg=mood_color, width=8)
            color_bar.pack(side=tk.LEFT, fill=tk.Y)
            
            # Content frame for the book details
            content_frame = tk.Frame(book_frame, bg="#ffffff", padx=10)
            content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            
            # Book number with mood color
            number_label = tk.Label(
                content_frame,
                text=f"Book {i+1}",
                font=("Arial", 10, "bold"),
                bg=mood_color,
                fg="white",
                padx=8,
                pady=3
            )
            number_label.pack(anchor="nw")
            
            # Book title with mood-specific color
            title_label = tk.Label(
                content_frame,
                text=f"📕 {book['title']}",
                font=("Arial", 16, "bold"),
                bg="#ffffff",
                fg=mood_text
            )
            title_label.pack(pady=(5, 0), anchor="w")
            
            # Author
            author_label = tk.Label(
                content_frame,
                text=f"by {book['author']} ✍️",
                font=("Arial", 12, "italic"),
                bg="#ffffff"
            )
            author_label.pack(pady=(0, 8), anchor="w")
            
            # Description with styled frame
            desc_frame = tk.Frame(content_frame, bg=mood_secondary, padx=12, pady=12, relief=tk.FLAT)
            desc_frame.pack(fill=tk.X, pady=8)
            
            desc_label = tk.Label(
                desc_frame,
                text=f"💬 {book['description']}",
                font=("Arial", 11),
                bg=mood_secondary,
                fg=mood_text,
                wraplength=700,
                justify=tk.LEFT
            )
            desc_label.pack(anchor="w")
            
            # Action buttons frame
            action_frame = tk.Frame(content_frame, bg="#ffffff", pady=8)
            action_frame.pack(fill=tk.X)
            
            # Save button with hover effect
            save_btn = tk.Button(
                action_frame,
                text="🔖 Save This Book",
                font=("Arial", 11, "bold"),
                bg=mood_color,
                fg="white",
                padx=12,
                pady=6,
                relief=tk.RAISED,
                bd=1,
                cursor="hand2",
                command=lambda b=book, m=mood: self.save_book(b, m)
            )
            save_btn.pack(side=tk.LEFT, pady=5)
            
            # Add hover effect to save button
            def on_save_enter(e, btn=save_btn):
                btn.config(bg=mood_text)
                
            def on_save_leave(e, btn=save_btn):
                btn.config(bg=mood_color)
                
            save_btn.bind("<Enter>", on_save_enter)
            save_btn.bind("<Leave>", on_save_leave)
        
        # Reset scroll position to top
        self.canvas.yview_moveto(0)

def main():
    root = tk.Tk()
    app = BookRecommendationSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()