import pandas as pd
import matplotlib.pyplot as plt
import textwrap


npc_relations = {
    "Angler": {
        "Loves": [],
        "Likes": ["Princess", "Tax Collector", "Demolitionist", "Party Girl"],
        "Dislikes": [],
        "Hates": ["Tavernkeep"],
        "Biome_Likes": ["Ocean"],
        "Biome_Dislikes": ["Desert"],
        "howTo": "Found and rescued sleeping in an Ocean biome.",
        "whatTheyDo": "Provides fishing quests, rewards, and related items."
    },
    "Arms Dealer": {
        "Loves": ["Nurse"],
        "Likes": ["Princess", "Steampunker"],
        "Dislikes": ["Golfer"],
        "Hates": ["Demolitionist"],
        "Biome_Likes": ["Desert"],
        "Biome_Dislikes": ["Snow"],
        "howTo": "Move into an available house once the player has bullets or a gun in their inventory.",
        "whatTheyDo": "Sells guns, bullets, and other ammunition."
    },
    "Clothier": {
        "Loves": ["Truffle"],
        "Likes": ["Princess", "Tax Collector"],
        "Dislikes": ["Nurse"],
        "Hates": ["Mechanic"],
        "Biome_Likes": ["Underground"],
        "Biome_Dislikes": ["Hallow"],
        "howTo": "Defeat Skeletron and ensure an available house.",
        "whatTheyDo": "Sells vanity clothing items and accessories."
    },
    "Cyborg": {
        "Loves": [],
        "Likes": ["Princess", "Steampunker", "Pirate", "Stylist"],
        "Dislikes": ["Zoologist"],
        "Hates": ["Wizard"],
        "Biome_Likes": ["Snow"],
        "Biome_Dislikes": ["Jungle"],
        "howTo": "Defeat Plantera and ensure an available house.",
        "whatTheyDo": "Sells futuristic and explosive items."
    },
    "Demolitionist": {
        "Loves": ["Tavernkeep"],
        "Likes": ["Princess", "Merchant"],
        "Dislikes": ["Arms Dealer", "Goblin Tinkerer"],
        "Hates": [],
        "Biome_Likes": ["Underground"],
        "Biome_Dislikes": ["Ocean"],
        "howTo": "Move into an available house when the player has explosives in their inventory.",
        "whatTheyDo": "Sells explosives and related items."
    },
    "Dryad": {
        "Loves": [],
        "Likes": ["Princess", "Truffle", "Witch Doctor"],
        "Dislikes": ["Angler"],
        "Hates": ["Golfer"],
        "Biome_Likes": ["Jungle"],
        "Biome_Dislikes": ["Desert"],
        "howTo": "Defeat any boss and ensure an available house.",
        "whatTheyDo": "Sells nature-related items and provides status on Corruption/Crimson and Hallow."
    },
    "Dye Trader": {
        "Loves": [],
        "Likes": ["Princess", "Arms Dealer", "Painter"],
        "Dislikes": ["Steampunker"],
        "Hates": ["Pirate"],
        "Biome_Likes": ["Desert"],
        "Biome_Dislikes": ["Forest"],
        "howTo": "Move into an available house when the player has any dye or dye ingredients in their inventory.",
        "whatTheyDo": "Sells dyes and dye-related items."
    },
    "Goblin Tinkerer": {
        "Loves": ["Mechanic"],
        "Likes": ["Princess", "Dye Trader"],
        "Dislikes": ["Clothier"],
        "Hates": ["Stylist"],
        "Biome_Likes": ["Underground"],
        "Biome_Dislikes": ["Jungle"],
        "howTo": "Found bound in the Cavern layer after defeating a Goblin Army.",
        "whatTheyDo": "Provides reforging services and sells tinkering tools."
    },
    "Golfer": {
        "Loves": ["Angler"],
        "Likes": ["Princess", "Painter", "Zoologist"],
        "Dislikes": ["Pirate"],
        "Hates": ["Merchant"],
        "Biome_Likes": ["Forest"],
        "Biome_Dislikes": ["Underground"],
        "howTo": "Found and rescued in the Underground Desert.",
        "whatTheyDo": "Sells golfing equipment and related items."
    },
    "Guide": {
        "Loves": [],
        "Likes": ["Princess", "Clothier", "Zoologist"],
        "Dislikes": ["Steampunker"],
        "Hates": ["Painter"],
        "Biome_Likes": ["Forest"],
        "Biome_Dislikes": ["Underground"],
        "howTo": "Automatically appears when the world is created and there is an available house.",
        "whatTheyDo": "Provides advice on crafting and progression, and necessary for summoning the Wall of Flesh."
    },
    "Mechanic": {
        "Loves": ["Goblin Tinkerer"],
        "Likes": ["Princess", "Cyborg"],
        "Dislikes": ["Arms Dealer"],
        "Hates": ["Clothier"],
        "Biome_Likes": ["Snow"],
        "Biome_Dislikes": ["Underground"],
        "howTo": "Found bound in the Dungeon after defeating Skeletron.",
        "whatTheyDo": "Sells wires, tools, and mechanical items."
    },
    "Merchant": {
        "Loves": [],
        "Likes": ["Princess", "Golfer", "Nurse"],
        "Dislikes": ["Tax Collector"],
        "Hates": ["Angler"],
        "Biome_Likes": ["Forest"],
        "Biome_Dislikes": ["Desert"],
        "howTo": "Move into an available house when the player has 50 silver coins or more in their inventory.",
        "whatTheyDo": "Sells basic supplies, potions, and other miscellaneous items."
    },
    "Nurse": {
        "Loves": ["Arms Dealer"],
        "Likes": ["Princess", "Wizard"],
        "Dislikes": ["Dryad", "Party Girl"],
        "Hates": ["Zoologist"],
        "Biome_Likes": ["Hallow"],
        "Biome_Dislikes": ["Snow"],
        "howTo": "Move into an available house when the player has increased their maximum health.",
        "whatTheyDo": "Heals the player for a price."
    },
    "Painter": {
        "Loves": ["Dryad"],
        "Likes": ["Princess", "Party Girl"],
        "Dislikes": ["Truffle", "Cyborg"],
        "Hates": [],
        "Biome_Likes": ["Jungle"],
        "Biome_Dislikes": ["Forest"],
        "howTo": "Move into an available house after at least 8 other NPCs are in the world.",
        "whatTheyDo": "Sells paint, painting tools, and paintings."
    },
    "Party Girl": {
        "Loves": ["Wizard", "Zoologist"],
        "Likes": ["Princess", "Stylist"],
        "Dislikes": ["Merchant"],
        "Hates": ["Tax Collector"],
        "Biome_Likes": ["Hallow"],
        "Biome_Dislikes": ["Underground"],
        "howTo": "Has a 1 in 40 chance to move into an available house each day once 14 other NPCs are in the world.",
        "whatTheyDo": "Sells party-related items and summons parties."
    },
    "Princess": {
        "Loves": [],
        "Likes": [],
        "Dislikes": [],
        "Hates": [],
        "Biome_Likes": [],
        "Biome_Dislikes": [],
        "howTo": "Move into an available house once all other NPCs are present in the world.",
        "whatTheyDo": "Sells various vanity items and has high happiness with all other NPCs."
    },
    "Pirate": {
        "Loves": ["Angler"],
        "Likes": ["Princess", "Tavernkeep"],
        "Dislikes": ["Stylist"],
        "Hates": ["Guide"],
        "Biome_Likes": ["Ocean"],
        "Biome_Dislikes": ["Underground"],
        "howTo": "Move into an available house after defeating a Pirate Invasion.",
        "whatTheyDo": "Sells pirate-themed items and weapons."
    },
    "Santa Claus": {
        "Loves": [],
        "Likes": ["Princess"],
        "Dislikes": [],
        "Hates": ["Tax Collector"],
        "Biome_Likes": ["Snow"],
        "Biome_Dislikes": ["Desert"],
        "howTo": "Move into an available house during the Christmas season (December 15-31) after defeating the Frost Legion.",
        "whatTheyDo": "Sells Christmas-themed items and decorations."
    },
    "Steampunker": {
        "Loves": ["Cyborg"],
        "Likes": ["Princess", "Painter"],
        "Dislikes": ["Dryad", "Wizard", "Party Girl"],
        "Hates": [],
        "Biome_Likes": ["Desert"],
        "Biome_Dislikes": ["Jungle"],
        "howTo": "Move into an available house after defeating any mechanical boss.",
        "whatTheyDo": "Sells steampunk-themed items and the Clentaminator."
    },
    "Stylist": {
        "Loves": ["Dye Trader"],
        "Likes": ["Princess", "Pirate"],
        "Dislikes": ["Tavernkeep"],
        "Hates": ["Goblin Tinkerer"],
        "Biome_Likes": ["Ocean"],
        "Biome_Dislikes": ["Snow"],
        "howTo": "Found bound in Spider Nests in the Cavern layer.",
        "whatTheyDo": "Provides haircuts and sells hair-dye items."
    },
    "Tavernkeep": {
        "Loves": ["Demolitionist"],
        "Likes": ["Princess", "Goblin Tinkerer"],
        "Dislikes": ["Guide"],
        "Hates": ["Dye Trader"],
        "Biome_Likes": ["Hallow"],
        "Biome_Dislikes": ["Snow"],
        "howTo": "Found and rescued after defeating the Eater of Worlds or Brain of Cthulhu.",
        "whatTheyDo": "Sells items related to the Old One's Army event and provides Etherian Mana."
    },
    "Tax Collector": {
        "Loves": ["Merchant"],
        "Likes": ["Princess", "Party Girl"],
        "Dislikes": ["Demolitionist", "Mechanic"],
        "Hates": ["Santa Claus"],
        "Biome_Likes": ["Snow"],
        "Biome_Dislikes": ["Hallow"],
        "howTo": "Transform a Tortured Soul in the Underworld using Purification Powder.",
        "whatTheyDo": "Collects taxes from other NPCs and gives coins to the player."
    },
    "Truffle": {
        "Loves": ["Guide"],
        "Likes": ["Princess", "Dryad"],
        "Dislikes": ["Clothier"],
        "Hates": ["Witch Doctor"],
        "Biome_Likes": ["Mushroom"],
        "Biome_Dislikes": [],
        "howTo": "Move into an available house in a surface Glowing Mushroom biome.",
        "whatTheyDo": "Sells mushroom-themed items and weapons."
    },
    "Witch Doctor": {
        "Loves": [],
        "Likes": ["Princess", "Dryad", "Guide"],
        "Dislikes": ["Nurse"],
        "Hates": ["Truffle"],
        "Biome_Likes": ["Jungle"],
        "Biome_Dislikes": ["Hallow"],
        "howTo": "Move into an available house after defeating the Queen Bee.",
        "whatTheyDo": "Sells jungle-themed and summoning items."
    },
    "Wizard": {
        "Loves": ["Golfer"],
        "Likes": ["Princess", "Merchant"],
        "Dislikes": ["Witch Doctor"],
        "Hates": ["Cyborg"],
        "Biome_Likes": ["Hallow"],
        "Biome_Dislikes": ["Ocean"],
        "howTo": "Found bound in the Cavern layer after defeating the Wall of Flesh.",
        "whatTheyDo": "Sells magic-themed items and spells."
    },
    "Zoologist": {
        "Loves": ["Witch Doctor"],
        "Likes": ["Princess", "Golfer"],
        "Dislikes": ["Angler"],
        "Hates": ["Arms Dealer"],
        "Biome_Likes": ["Forest"],
        "Biome_Dislikes": ["Desert"],
        "howTo": "Move into an available house once at least 10% of the Bestiary is completed.",
        "whatTheyDo": "Sells pets, mounts, and animal-related items."
    },
}

# Flatten the dictionary for creating a DataFrame
data = []

for npc, relations in npc_relations.items():
    row = {
        "NPC": npc,
        "Loves": '\n'.join(textwrap.wrap(', '.join(relations.get("Loves", [])), 20)),
        "Likes": '\n'.join(textwrap.wrap(', '.join(relations.get("Likes", [])), 20)),
        "Dislikes": '\n'.join(textwrap.wrap(', '.join(relations.get("Dislikes", [])), 20)),
        "Hates": '\n'.join(textwrap.wrap(', '.join(relations.get("Hates", [])), 20)),
        "Biome Likes": '\n'.join(textwrap.wrap(', '.join(relations.get("Biome_Likes", [])), 20)),
        "Biome Dislikes": '\n'.join(textwrap.wrap(', '.join(relations.get("Biome_Dislikes", [])), 20)),
        "How To Obtain": '\n'.join(textwrap.wrap(relations.get("howTo", ""), 20)),
        "What They Do": '\n'.join(textwrap.wrap(relations.get("whatTheyDo", ""), 20))
    }
    data.append(row)

# Create DataFrame
df = pd.DataFrame(data)

# Plot the table
fig, ax = plt.subplots(figsize=(15, 10))  # Adjust the size as needed
ax.axis('tight')
ax.axis('off')

# Add table with colors
colors = [['#f0f0f0' if i % 2 == 0 else '#ffffff' for _ in range(len(df.columns))] for i in range(len(df))]
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center', cellColours=colors)

# Make the table more compact
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.2, 1.2)

# Adjust column widths and set cell properties
for key, cell in table.get_celld().items():
    cell.set_edgecolor('black')
    if key[0] == 0:  # Header
        cell.set_fontsize(10)
        cell.set_text_props(weight='bold')
        cell.set_facecolor('#d3d3d3')
    cell.set_height(0.1)
    cell.set_width(0.15)

# Save the table as an image
plt.savefig("npc_relations_table.png", bbox_inches='tight', dpi=300)
plt.show()