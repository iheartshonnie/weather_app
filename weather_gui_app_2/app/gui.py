import tkinter as tk
from tkinter import ttk, messagebox
from app import weather_api, file_manager

def launch_app():
    root = tk.Tk()
    root.title("Weather GUI App")


    tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e")
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1)

    tk.Label(root, text="Age:").grid(row=1, column=0, sticky="e")
    age_entry = tk.Entry(root)
    age_entry.grid(row=1, column=1)

    tk.Label(root, text="Favorite Weather:").grid(row=2, column=0, sticky="e")
    weather_options = ["Sunny", "Rainy", "Snowy", "Cloudy"]
    weather_var = tk.StringVar()
    weather_dropdown = ttk.Combobox(root, textvariable=weather_var, values=weather_options)
    weather_dropdown.grid(row=2, column=1)
    weather_dropdown.current(0)

    def submit_info():
        name = name_entry.get()
        age = age_entry.get()
        fav_weather = weather_var.get()
        message = f"Hello {name}, you are {age} years old and you like {fav_weather}."
        messagebox.showinfo("Summary", message)

    submit_btn = tk.Button(root, text="Submit", command=submit_info)
    submit_btn.grid(row=3, columnspan=2, pady=5)


    tk.Label(root, text="City Name:").grid(row=4, column=0, sticky="e")
    city_entry = tk.Entry(root)
    city_entry.grid(row=4, column=1)

    result_label = tk.Label(root, text="", font=('Arial', 10, 'bold'))
    result_label.grid(row=6, columnspan=2, pady=10)

    def get_weather():
        city = city_entry.get()
        result = weather_api.get_weather_for_city(city)
        temp = result['temperature']
        desc = result['description']

        if temp is not None:
            file_manager.log_weather_data(city, temp, desc)
            result_label.config(text=f"{city}: {temp}°F, {desc}")
        else:
            result_label.config(text="City not found.")

    get_weather_btn = tk.Button(root, text="Get Weather", command=get_weather)
    get_weather_btn.grid(row=5, columnspan=2, pady=5)

    root.mainloop()