import json
import os
from datetime import date

FILE = "moods.json"

# Load saved moods
if os.path.exists(FILE):
    with open(FILE, "r") as file:
        moods = json.load(file)
else:
    moods = []

while True:
    print("\n💗 DAILY MOOD TRACKER 💗")
    print("1. Add Today's Mood")
    print("2. View Mood History")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        mood = input("How are you feeling today? 😊 😐 😢 😴 : ")
        note = input("Write a short note: ")

        moods.append({
            "date": str(date.today()),
            "mood": mood,
            "note": note
        })

        with open(FILE, "w") as file:
            json.dump(moods, file, indent=4)

        print("🌸 Mood saved successfully!")

    elif choice == "2":
        if len(moods) == 0:
            print("No moods saved yet.")
        else:
            print("\n📖 Mood History")
            print("-" * 30)
            for entry in moods:
                print(f"📅 {entry['date']}")
                print(f"😊 Mood: {entry['mood']}")
                print(f"📝 Note: {entry['note']}")
                print("-" * 30)

    elif choice == "3":
        print("Take care! 💖 Bye!")
        break

    else:
        print("❌ Invalid option.")
