import webbrowser

for i in range(1, 21):
    webbrowser.open_new_tab(f"https://flatmates.com.au/rooms/sydney/newest?page={i}")
