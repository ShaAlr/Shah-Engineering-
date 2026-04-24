"""
SAMPLE DATASET GENERATOR
========================

Script ini untuk membuat sample dataset kecil untuk testing aplikasi.
Gunakan hanya untuk testing - untuk aplikasi sebenarnya, gunakan dataset lengkap dari Kaggle.

WARNING: Sample dataset tidak akan memberikan rekomendasi yang akurat!
         Hanya untuk memastikan aplikasi berjalan dengan benar.
"""

import pandas as pd
import numpy as np
import random

print("=" * 60)
print("SAMPLE DATASET GENERATOR")
print("Steam Game Recommender - Kelompok 12")
print("=" * 60)
print()

# Sample data
games = [
    "Counter-Strike: Global Offensive",
    "Dota 2",
    "PLAYERUNKNOWN'S BATTLEGROUNDS",
    "Grand Theft Auto V",
    "The Witcher 3: Wild Hunt",
    "Cyberpunk 2077",
    "Red Dead Redemption 2",
    "Elden Ring",
    "Dark Souls III",
    "Sekiro: Shadows Die Twice",
    "Stardew Valley",
    "Terraria",
    "Minecraft",
    "Among Us",
    "Fall Guys",
    "Valorant",
    "League of Legends",
    "Portal 2",
    "Half-Life 2",
    "Team Fortress 2",
    "Left 4 Dead 2",
    "Resident Evil 4",
    "Silent Hill 2",
    "Dead Space",
    "Amnesia: The Dark Descent",
    "Outlast",
    "FIFA 23",
    "NBA 2K23",
    "Rocket League",
    "Forza Horizon 5",
    "The Sims 4",
    "Cities: Skylines",
    "Civilization VI",
    "Age of Empires IV",
    "StarCraft II",
    "Warcraft III",
    "Final Fantasy XIV",
    "World of Warcraft",
    "Overwatch 2",
    "Apex Legends",
    "Fortnite",
    "Call of Duty: Modern Warfare II",
    "Battlefield 2042",
    "Rainbow Six Siege",
    "Destiny 2",
    "Warframe",
    "Path of Exile",
    "Diablo IV",
    "Lost Ark",
    "Genshin Impact"
]

genres_list = [
    "Action",
    "Action,Adventure",
    "Action,Multiplayer,Shooter",
    "Adventure,RPG",
    "RPG,Open World",
    "RPG,Action",
    "Strategy,Simulation",
    "Simulation",
    "Horror,Survival",
    "Horror,Action",
    "Sports",
    "Racing",
    "Puzzle",
    "Platformer",
    "Indie,Adventure"
]

prices = [0, 4.99, 9.99, 14.99, 19.99, 29.99, 39.99, 49.99, 59.99]

ram_requirements = [
    "Minimum: 4 GB RAM",
    "Minimum: 8 GB RAM",
    "Minimum: 12 GB RAM",
    "Minimum: 16 GB RAM",
    "Minimum: 2 GB RAM",
    "Minimum: 6 GB RAM"
]

# Generate sample data
data = {
    'AppID': [random.randint(10000, 999999) for _ in range(len(games))],
    'Name': games,
    'Release date': ['2023-01-01' for _ in range(len(games))],
    'Estimated owners': [f'{random.randint(1, 50)} million' for _ in range(len(games))],
    'Peak CCU': [random.randint(1000, 500000) for _ in range(len(games))],
    'Required age': [random.choice([0, 13, 16, 18]) for _ in range(len(games))],
    'Price': [f'${random.choice(prices)}' for _ in range(len(games))],
    'DLC count': [random.randint(0, 20) for _ in range(len(games))],
    'About the game': [f'An exciting game about {game}' for game in games],
    'Supported languages': ['English' for _ in range(len(games))],
    'Windows': [True for _ in range(len(games))],
    'Mac': [random.choice([True, False]) for _ in range(len(games))],
    'Linux': [random.choice([True, False]) for _ in range(len(games))],
    'Positive': [random.randint(1000, 500000) for _ in range(len(games))],
    'Negative': [random.randint(100, 50000) for _ in range(len(games))],
    'Score rank': [random.randint(1, 100) for _ in range(len(games))],
    'Developers': [f'Developer {i}' for i in range(len(games))],
    'Publishers': [f'Publisher {i}' for i in range(len(games))],
    'Categories': ['Single-player,Multi-player' for _ in range(len(games))],
    'Genres': [random.choice(genres_list) for _ in range(len(games))],
    'Tags': [random.choice(genres_list) for _ in range(len(games))],
    'Achievements': [random.randint(0, 100) for _ in range(len(games))],
    'Recommendations': [random.randint(0, 100000) for _ in range(len(games))],
    'Notes': [''] * len(games),
    'Average playtime forever': [random.randint(0, 1000) for _ in range(len(games))],
    'Average playtime two weeks': [random.randint(0, 100) for _ in range(len(games))],
    'Median playtime forever': [random.randint(0, 500) for _ in range(len(games))],
    'Median playtime two weeks': [random.randint(0, 50) for _ in range(len(games))],
    'Peak CCU yesterday': [random.randint(100, 100000) for _ in range(len(games))],
    'Minimum requirements': [random.choice(ram_requirements) for _ in range(len(games))],
    'Recommended requirements': [''] * len(games)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
output_file = 'games_sample.csv'
df.to_csv(output_file, index=False)

print(f"✅ Sample dataset created: {output_file}")
print(f"📊 Total games: {len(df)}")
print()
print("⚠️  WARNING:")
print("   This is a SAMPLE dataset for TESTING only!")
print("   For actual use, download the full dataset from Kaggle.")
print()
print("📥 Full Dataset:")
print("   https://www.kaggle.com/datasets/fronkongames/steam-games-dataset")
print()
print("🔧 To use this sample:")
print("   1. Rename 'games_sample.csv' to 'games.csv'")
print("   2. Run the application")
print()
print("✨ To use the full dataset:")
print("   1. Download from Kaggle")
print("   2. Extract 'games.csv'")
print("   3. Place in this folder")
print("   4. Delete 'games_sample.csv'")
print()
print("=" * 60)
