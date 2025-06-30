import os
import random
import ctypes

def change_wallpaper(folder_path):
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    if not images:
        print("No images found in the folder.")
        return
    
    chosen_image = random.choice(images)
    full_path = os.path.join(folder_path, chosen_image)
    
    # Change wallpaper (Windows only)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, full_path, 3)
    print(f"Wallpaper changed to: {chosen_image}")

# 👇 Change this path to the folder where you store your wallpapers
wallpaper_folder = r"C:\Users\YourName\Pictures\Wallpapers"
change_wallpaper(wallpaper_folder)
