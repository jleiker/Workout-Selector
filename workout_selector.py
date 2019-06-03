import datetime
import random

# Strength workouts
strength = ["Cyberpunk",
            "Watchman",
            "Endgame+",
            "Tripitaka",
            "Hotel",
            "Lift & Tone",
            "Jacked",
            "The Gainer",
            "The Boogeyman",
            "The Vindicator",
            "Power Circuit",
            "Power Circuit+",
            "Power Row",
            "Stealth Master",
            "Code Zero",
            "Postal",
            "Night's Watch",
            "Solid Snake",
            "Master Chief"]

# Abs workouts
abs = ["Rapid Fire",
       "Ab Hub",
       "Back Up",
       "Codex",
       "Lean & Mean",
       "Burn Mode",
       "Core Sculpt",
       "Killer Core",
       "Core Control",
       "Ironclad Abs",
       "Fab Abs",
       "Abs on Fire",
       "Overhaul"]

# Upper body workouts
upperbody = ["Super Smash",
             "Upper Body Tendon Strength+",
             "The Kitten",
             "Chest & Back",
             "Brute Arms & Back",
             "Upper Body Forge",
             "Hardgainer",
             "Marauder",
             "Muscle Factory Upperbody",
             "Arm Day",
             "Arm Shred",
             "Power Punch",
             "Butcher",
             "Hardback",
             "Barbarian",
             "The Brawler",
             "Upperbody Builder",
             "Tank Top",
             "Savage",
             "Knockout",
             "Arms of Steel",
             "Homemade Back",
             "Upper Body Sculpt",
             "Hammer",
             "Back & Biceps",
             "Power 10",
             "Lannister"]

# Lower body workouts
lowerbody = ["The Prowler",
             "I am my Own Hero",
             "Siren",
             "Lowerbody Tendon Strength",
             "Leg Shred",
             "Brute Leg Day",
             "Legs of Steel",
             "Killer Legs",
             "Muscle Factory Lowerbody",
             "Iron Bar",
             "Sonic",
             "Leg Day"]

weekday = datetime.datetime.today().weekday()

# If Monday or Saturday, choose strength workout
if(weekday == 0 or weekday == 5):
    workout = random.choice(strength)
# If Tuesday, Friday or Sunday, choose abs workout
elif(weekday == 1 or weekday == 4 or weekday == 6):
    workout = random.choice(abs)
# If Wednesday, choose upper body workout
elif(weekday == 2):
    workout = random.choice(upperbody)
# If Thursday, choose lower body workout
else:
    workout = random.choice(lowerbody)

# Convert weekday to text
if(weekday == 0):
    weekday = "Monday"
elif(weekday == 1):
    weekday = "Tuesday"
elif(weekday == 2):
    weekday = "Wednesday"
elif(weekday == 3):
    weekday = "Thursday"
elif(weekday == 4):
    weekday = "Friday"
elif(weekday == 5):
    weekday = "Saturday"
else:
    weekday = "Sunday"

print(str(weekday) + ": " + workout)