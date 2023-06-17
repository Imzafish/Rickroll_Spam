import webbrowser

def open_chrome():
    url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    profile_path = 'C:/Users/YourUsername/AppData/Local/Google/Chrome/User Data/Profile 2'  # Replace with the path to your desired profile

    browser = f'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe --profile-directory="{profile_path}" %s'

    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser))
    webbrowser.get('chrome').open(url)

open_chrome()
