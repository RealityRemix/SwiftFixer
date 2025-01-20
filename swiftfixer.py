import os
import urllib.request

def get_desktop_folder():
    """Retrieve the path to the user's desktop."""
    return os.path.join(os.path.expanduser("~"), "Desktop")

def download_file(url, destination):
    """Download a file from a given URL to a specified destination."""
    try:
        print(f"Downloading {os.path.basename(destination)}...")
        urllib.request.urlretrieve(url, destination)
        print(f"{os.path.basename(destination)} downloaded successfully.")
        return True
    except Exception as e:
        print(f"Failed to download {os.path.basename(destination)}: {e}")
        return False

def download_and_setup_dll_fixer():
    """Download Injector.exe and DLL3.dll to the desktop."""
    desktop_folder = get_desktop_folder()
    fixer_folder = os.path.join(desktop_folder, "Fixer")

    os.makedirs(fixer_folder, exist_ok=True)

    injector_url = "https://github.com/RealityRemix/SwiftFixer/raw/main/injector.exe"
    dll_url = "https://github.com/RealityRemix/SwiftFixer/raw/main/Dll3.dll"

    injector_path = os.path.join(fixer_folder, "Injector.exe")
    dll_path = os.path.join(fixer_folder, "DLL3.dll")

    injector_success = download_file(injector_url, injector_path)
    dll_success = download_file(dll_url, dll_path)

    if injector_success and dll_success:
        print("\nAll files have been downloaded successfully.")
        print(f"Files are located in: {fixer_folder}")
        print("Drag and drop 'Injector.exe' and 'DLL3.dll'in the swift bin folder.")
    else:
        print("\nFailed to download one or more files. Please check the URLs or your connection.")

def blox_strap_fix():
    url = "https://github.com/RealityRemix/SwiftFixer/raw/main/BlackScreenFix%20-%20Bloxstrap.bat"
    download_and_run(url, "BloxstrapFix.bat")

def fish_strap_fix():
    url = "https://github.com/RealityRemix/SwiftFixer/raw/main/BlackScreenFix%20-%20Fishstrap.bat"
    download_and_run(url, "FishstrapFix.bat")

def normal_fix():
    url = "https://github.com/RealityRemix/SwiftFixer/raw/main/BlackScreenFix%20-%20Normal.bat"
    download_and_run(url, "NormalFix.bat")

def black_screen_fixer_menu():
    while True:
        print("\nBlack Screen Fixer")
        print("1. Blox Strap Fix")
        print("2. Fish Strap Fix")
        print("3. Normal Fix")
        print("4. Go Back")
        choice = input("Select an option (1-4): ")
        if choice == "1":
            blox_strap_fix()
        elif choice == "2":
            fish_strap_fix()
        elif choice == "3":
            normal_fix()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Black Screen Fixer")
        print("2. DLL Fixer")
        print("3. Exit")
        choice = input("Select an option (1-3): ").strip()
        if choice == "1":
            black_screen_fixer_menu()
        elif choice == "2":
            download_and_setup_dll_fixer()
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
