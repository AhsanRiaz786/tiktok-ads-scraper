import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
import logging
from scraper import scrape_tiktok_ads

class TikTokAdsScraperApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TikTok Ads Scraper")
        self.geometry("400x300")
        self.resizable(False, False)
        self.create_widgets()
    
    def create_widgets(self):
        self.title_label = tk.Label(self, text="TikTok Ads Scraper", font=("Arial", 18))
        self.title_label.pack(pady=20)
        
        self.info_label = tk.Label(self, text="If this is your first time using this tool, please login.\nOtherwise, you can start scraping directly.")
        self.info_label.pack(pady=10)
        
        self.login_button = tk.Button(self, text="Login", command=self.show_login_window, width=20)
        self.login_button.pack(pady=5)
        
        self.scrape_button = tk.Button(self, text="Scrape Ads", command=self.show_scrape_window, width=20)
        self.scrape_button.pack(pady=5)
        
    def show_login_window(self):
        self.withdraw()  # Hide the main window
        self.login_window = tk.Toplevel(self)
        self.login_window.title("Login")
        self.login_window.geometry("300x200")
        
        tk.Label(self.login_window, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(self.login_window)
        self.email_entry.pack(pady=5)
        
        tk.Label(self.login_window, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(self.login_window, show="*")
        self.password_entry.pack(pady=5)
        
        tk.Button(self.login_window, text="Login", command=self.perform_login).pack(pady=10)
        
    def perform_login(self):
        from login import login
        email = self.email_entry.get()
        password = self.password_entry.get()
        login(email, password)
        self.login_window.destroy()
        self.deiconify()  # Show the main window again
        messagebox.showinfo("Login", "Login successful!")
        
    def show_scrape_window(self):
        self.withdraw()  # Hide the main window
        self.scrape_window = tk.Toplevel(self)
        self.scrape_window.title("Scrape Ads")
        self.scrape_window.geometry("400x300")
        
        tk.Label(self.scrape_window, text="Select brands file (Excel):").pack(pady=5)
        self.file_entry = tk.Entry(self.scrape_window, width=50)
        self.file_entry.pack(pady=5)
        tk.Button(self.scrape_window, text="Browse", command=self.browse_file).pack(pady=5)
        
        self.progress_label = tk.Label(self.scrape_window, text="")
        self.progress_label.pack(pady=10)
        
        tk.Button(self.scrape_window, text="Start Scraping", command=self.start_scraping).pack(pady=10)
        
    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)
    
    def update_progress(self, message):
        self.progress_label.config(text=message)
        self.update_idletasks()  # Ensure that the GUI updates the progress message immediately
        
    def start_scraping(self):
        brands_file = self.file_entry.get()
        if not brands_file or not os.path.isfile(brands_file):
            messagebox.showwarning("Warning", "Please select a valid Excel file.")
            return
        
        self.update_progress("Starting scraping process...")
        
        # Run the scraping process in a separate thread
        scraping_thread = threading.Thread(target=self.run_scraping, args=(brands_file,))
        scraping_thread.start()
    
    def run_scraping(self, brands_file):
        try:
            scrape_tiktok_ads(brands_file, self.update_progress)
            self.update_progress("Scraping completed successfully!")
            messagebox.showinfo("Success", "Scraping completed successfully!")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            self.update_progress("An error occurred during scraping. Check the log for details.")
            messagebox.showerror("Error", "An error occurred during scraping. Check the log for details.")
        finally:
            self.scrape_window.destroy()
            self.deiconify()  # Show the main window again
