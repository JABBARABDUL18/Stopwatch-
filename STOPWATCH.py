import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime
import threading

class StopwatchClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch & Clock")
        self.root.geometry("600x500")
        self.root.configure(bg='#1a1a2e')
        
        # Stopwatch variables
        self.stopwatch_running = False
        self.stopwatch_time = 0.0
        self.start_time = 0.0
        
        # Create main container
        self.main_frame = tk.Frame(root, bg='#1a1a2e')
        self.main_frame.pack(fill='both', expand=True)
        
        # Create notebook for tabs
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background='#16213e', borderwidth=0)
        style.configure('TNotebook.Tab', background='#0f3460', foreground='white', 
                       padding=[20, 10], font=('Arial', 12, 'bold'))
        style.map('TNotebook.Tab', background=[('selected', '#e94560')])
        
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create frames for different pages
        self.create_clock_page()
        self.create_stopwatch_page()
        
        # Start the clock update
        self.update_clock()
    
    def create_clock_page(self):
        # Clock page with gradient-like background
        clock_frame = tk.Frame(self.notebook, bg='#0f3460')
        self.notebook.add(clock_frame, text='🕐 Clock')
        
        # Create gradient effect with multiple frames
        gradient_frame = tk.Frame(clock_frame, bg='#0f3460')
        gradient_frame.pack(fill='both', expand=True)
        
        # Title
        title_label = tk.Label(gradient_frame, text="Digital Clock", 
                              font=('Arial', 24, 'bold'), 
                              fg='#00d4ff', bg='#0f3460')
        title_label.pack(pady=30)
        
        # Time display with colorful background
        time_bg_frame = tk.Frame(gradient_frame, bg='#e94560', bd=5, relief='raised')
        time_bg_frame.pack(pady=20)
        
        self.time_label = tk.Label(time_bg_frame, text="", 
                                  font=('Digital-7', 48, 'bold'), 
                                  fg='white', bg='#e94560', padx=30, pady=20)
        self.time_label.pack()
        
        # Date display
        date_bg_frame = tk.Frame(gradient_frame, bg='#f39c12', bd=3, relief='raised')
        date_bg_frame.pack(pady=10)
        
        self.date_label = tk.Label(date_bg_frame, text="", 
                                  font=('Arial', 18, 'bold'), 
                                  fg='white', bg='#f39c12', padx=20, pady=10)
        self.date_label.pack()
        
        # Day display
        day_bg_frame = tk.Frame(gradient_frame, bg='#27ae60', bd=3, relief='raised')
        day_bg_frame.pack(pady=10)
        
        self.day_label = tk.Label(day_bg_frame, text="", 
                                 font=('Arial', 16, 'bold'), 
                                 fg='white', bg='#27ae60', padx=20, pady=8)
        self.day_label.pack()
    
    def create_stopwatch_page(self):
        # Stopwatch page with vibrant background
        stopwatch_frame = tk.Frame(self.notebook, bg='#16213e')
        self.notebook.add(stopwatch_frame, text='⏱️ Stopwatch')
        
        # Title
        title_label = tk.Label(stopwatch_frame, text="Stopwatch", 
                              font=('Arial', 24, 'bold'), 
                              fg='#ff6b6b', bg='#16213e')
        title_label.pack(pady=30)
        
        # Stopwatch display with colorful background
        stopwatch_bg_frame = tk.Frame(stopwatch_frame, bg='#4ecdc4', bd=8, relief='raised')
        stopwatch_bg_frame.pack(pady=20)
        
        self.stopwatch_label = tk.Label(stopwatch_bg_frame, text="00:00.00", 
                                       font=('Digital-7', 42, 'bold'), 
                                       fg='white', bg='#4ecdc4', padx=40, pady=30)
        self.stopwatch_label.pack()
        
        # Button frame with gradient background
        button_frame = tk.Frame(stopwatch_frame, bg='#16213e')
        button_frame.pack(pady=30)
        
        # Colorful buttons
        self.start_button = tk.Button(button_frame, text="START", 
                                     font=('Arial', 14, 'bold'),
                                     bg='#2ecc71', fg='white', 
                                     activebackground='#27ae60',
                                     width=10, height=2, bd=0, relief='raised',
                                     command=self.start_stopwatch)
        self.start_button.pack(side='left', padx=10)
        
        self.stop_button = tk.Button(button_frame, text="STOP", 
                                    font=('Arial', 14, 'bold'),
                                    bg='#e74c3c', fg='white', 
                                    activebackground='#c0392b',
                                    width=10, height=2, bd=0, relief='raised',
                                    command=self.stop_stopwatch)
        self.stop_button.pack(side='left', padx=10)
        
        self.reset_button = tk.Button(button_frame, text="RESET", 
                                     font=('Arial', 14, 'bold'),
                                     bg='#f39c12', fg='white', 
                                     activebackground='#e67e22',
                                     width=10, height=2, bd=0, relief='raised',
                                     command=self.reset_stopwatch)
        self.reset_button.pack(side='left', padx=10)
        
        # Start updating stopwatch
        self.update_stopwatch()
    
    def update_clock(self):
        # Update clock display
        current_time = datetime.now()
        time_string = current_time.strftime("%H:%M:%S")
        date_string = current_time.strftime("%B %d, %Y")
        day_string = current_time.strftime("%A")
        
        self.time_label.config(text=time_string)
        self.date_label.config(text=date_string)
        self.day_label.config(text=day_string)
        
        # Schedule next update
        self.root.after(1000, self.update_clock)
    
    def start_stopwatch(self):
        if not self.stopwatch_running:
            self.stopwatch_running = True
            self.start_time = time.time() - self.stopwatch_time
    
    def stop_stopwatch(self):
        if self.stopwatch_running:
            self.stopwatch_running = False
    
    def reset_stopwatch(self):
        self.stopwatch_running = False
        self.stopwatch_time = 0.0
        self.stopwatch_label.config(text="00:00.00")
    
    def update_stopwatch(self):
        if self.stopwatch_running:
            self.stopwatch_time = time.time() - self.start_time
        
        # Format time as MM:SS.CC
        minutes = int(self.stopwatch_time // 60)
        seconds = int(self.stopwatch_time % 60)
        centiseconds = int((self.stopwatch_time % 1) * 100)
        
        time_string = f"{minutes:02d}:{seconds:02d}.{centiseconds:02d}"
        self.stopwatch_label.config(text=time_string)
        
        # Update button colors based on state
        if self.stopwatch_running:
            self.start_button.config(bg='#95a5a6', activebackground='#7f8c8d')
            self.stop_button.config(bg='#e74c3c', activebackground='#c0392b')
        else:
            self.start_button.config(bg='#2ecc71', activebackground='#27ae60')
            self.stop_button.config(bg='#95a5a6', activebackground='#7f8c8d')
        
        # Schedule next update
        self.root.after(10, self.update_stopwatch)

def main():
    root = tk.Tk()
    app = StopwatchClockApp(root)
    
    # Center the window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (600 // 2)
    y = (root.winfo_screenheight() // 2) - (500 // 2)
    root.geometry(f"600x500+{x}+{y}")
    
    # Make window resizable
    root.minsize(500, 400)
    
    root.mainloop()

if __name__ == "__main__":
    main()