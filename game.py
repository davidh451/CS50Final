import pygame
from pygame.locals import *

# ---------------- Story Data ----------------
story = {
    "start": {
        "text": "You are a villager in a part of the desert, but one day curiosity gets the best of you and\n"
                "you go explore the desert more. You find yourself in a dark desert. The path splits into \nfour directions. . . Go to:",
        "choices": {"The Desert Oasis Near The Village": "desert_oasis",
                    "Investigate a half-buried ruin\n": "ruin",
                    "Investigate a camel caravan.": "caravan",
                    "Discover what lies in the heart of a sandstorm.": "sandstorm"},
        "image": "images/DesertBeginning.webp",
        "font": "fonts/PressStart2P-vaV7.ttf",
        "sound": "sounds/DesertAmbience.mp3",
    },
    "desert_oasis": {
        "text": "At the oasis, palm trees provide shade and water sparkles. But you're not alone..",
        "choices": {"Approach the water": "water",
                    "Search around the oasis": "search_oasis"},
        "image": "images/DesertOasis.png",
        "font": "fonts/PressStart2P-vaV7.ttf",
        "sound": "sounds/OasisAmbience.mp3",
        "npcs": ["oasis_creature"],
    },
    "ruin": {
        "text": "You step into the crumbling walls of an ancient structure buried in the sands. \n"
                " Strange carvings cover the stones.",
        "choices": {"Explore the main chamber": "explore_chamber",
                    "Climb to the highest wall": "climb_highestwall"},
        "image": "images/DesertRuin.png",
        "font": "fonts/PressStart2P-vaV7.ttf",
        "sound": "sounds/RuinAmbience.mp3",
    },
    "caravan": {
        "text": "You hurry to catch up with the camel caravan. They notice you struggling in the heat.",
        "choices": {"Ask them for water": "ask_water",
                    "Try to sneak into their supplies without asking": "sneak_supplies"},
        "image": "images/DesertCaravan.png",
        "font": "fonts/PressStart2P-vaV7.ttf",
        "sound": "sounds/CaravanAmbience.mp3",
        "npcs": ["caravan_man", "caravan_camel"],
    },
    "sandstorm": {
        "text": "The sandstorm rages around you, blinding and disorienting. You must find shelter quickly.",
        "choices": {"Seek shelter in a nearby cave": "caveEntrance",
                    "Try to ride out the storm": "ride_out_storm"},
        "image": "images/DesertSandstorm.png",
        "font": "fonts/PressStart2P-vaV7.ttf",
        "sound": "sounds/SandStormAmbience.mp3",
    },
    "caveEntrance": {
        "text": "You find a cave and wait out the storm.",
        "choices": {"Press the number 1 to go inside": "CaveInterior"},
        "image": "images/DesertCaveEntrance.png",
        "sound": "sounds/CaveAmbience.mp3",
        "font": "fonts/PressStart2P-vaV7.ttf",
        "ending": False,
    },

    # Endings
    "water": {
        "text": "You drink from the oasis, but a hidden creature attacks you.\n"
                "You barely escape with your life.",
        "choices": {"Return to start": "start"},
        "image": "images/DesertOasis.png",
        "sound": "sounds/OasisAmbience.mp3",
        "font": "fonts/PressStart2P-vaV7.ttf",
        "npcs": ["oasis_creature"],
        "ending": True,
    },
    "search_oasis": {
        "text": "You find a hidden cache of supplies left by previous travelers. You take what you can carry.",
        "choices": {"Return to start": "start"},
        "image": "images/DesertOasis.png",
        "sound": "sounds/OasisAmbience.mp3",
        "font": "fonts/PressStart2P-vaV7.ttf",
        "ending": True,
    },
    "explore_chamber": {
        "text": "You discover a hidden chamber filled with ancient artifacts. \n"
                "You take a few for your journey. But you discover these are not worth lots of money. \n"
                "You decide to leave them behind.",
        "choices": {"Return to start": "start"},
        "image": "images/DesertExploreChamber.webp",
        "sound": "sounds/RuinAmbience.mp3",
        "font": "fonts/PressStart2P-vaV7.ttf",
        "ending": True,
    },
    "climb_highestwall": {
        "text": "From the top of the wall, you spot nothing on the other side. You climb down safely\n"
                " and head back to the start.",
        "choices": {"Return to start": "start"},
        "image": "images/DesertWall.png",
        "sound": "sounds/OasisAmbience.mp3",
        "font": "fonts/PressStart2P-vaV7.ttf",
        "ending": True,
    },
    "ask_water": {
        "text": "The caravan gives you water, but they are suspicious of you. They decide to keep an eye on you. Then they ask you to join them, and you agree.",
        "choices": {"Return to start": "start"},
        "image": "images/DesertCaravan.png",
        "npcs": ["caravan_man", "caravan_camel"],
        "sound": "sounds/CaravanAmbience.mp3",
        "font": "fonts/PressStart2P-vaV7.ttf",
        "ending": True,
    },
    "sneak_supplies": {
        "text": "You try to sneak into their supplies, but they catch you. They take your belongings and leave you in the desert.",
        "choices": {"Return to start": "start"},
        "image": "images/DesertCaravan.png",
        "npcs": ["caravan_man", "caravan_camel"],
        "sound": "sounds/CaravanAmbience.mp3",
        "font": "fonts/PressStart2P-vaV7.ttf",
        "ending": True,
    },

    "CaveInterior": {
        "text": "Inside the cave, you find ancient drawings and artifacts worth lots of money on the walls. You feel a sense of wonder and respect for the people who once lived here.",
        "choices": {"Return to start": "start"},
        "image": "images/DesertCaveInterior.png",
        "sound": "sounds/CaveAmbience.mp3",
        "font": "fonts/PressStart2P-vaV7.ttf",
        "ending": True,
    },
    "ride_out_storm": {
        "text": "You try to ride out the storm, but it overwhelms you. You lose your way and succumb to the desert.",
        "choices": {"Return to start": "start"},
        "image": "images/DesertSandstorm.png",
        "sound": "sounds/SandStormAmbience.mp3",
        "font": "fonts/PressStart2P-vaV7.ttf",
        "ending": True,
    }
}

# ---------------- Initialize Pygame ----------------
pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Desert Adventure Game CS50 Final Project")
clock = pygame.time.Clock()
running = True

# Optional: if mixer fails on some machines, wrap init in try/except. If it fails, just skip sound.
try:
    pygame.mixer.init()
except Exception:
    pass

game_state = "start_screen"
current_scene = "start"
current_npc = None

# ---------------- Font Handling ----------------
pygame.font.init()

# Load our fonts
def load_font(path, size):
    try:
        return pygame.font.Font(path, size)
    except FileNotFoundError:
        return pygame.font.SysFont("arial", size)


title_font = load_font("fonts/PressStart2P-vaV7.ttf", 48)
ui_font = load_font("fonts/PressStart2P-vaV7.ttf", 20)
text_font = load_font("fonts/PressStart2P-vaV7.ttf", 24)

# ---------------- Player + Sprites ----------------
# Use try/except for each image so missing files won't crash the game
def load_image(path, fallback_size=(200, 200)):
    try:
        img = pygame.image.load(path).convert_alpha()
        return img
    except FileNotFoundError:
        s = pygame.Surface(fallback_size, pygame.SRCALPHA)
        s.fill((0, 0, 0, 0))
        return s


# Load and scale all our sprites
adventurer_sprite = load_image("images/DesertAdventurer.gif", (200, 200))
adventurer_sprite = pygame.transform.scale(adventurer_sprite, (200, 200))

caravan_man_sprite = load_image("images/CaravanMan.gif", (200, 200))
caravan_man_sprite = pygame.transform.scale(caravan_man_sprite, (200, 200))

caravan_camel_sprite = load_image("images/CaravanCamel.gif", (300, 300))
caravan_camel_sprite = pygame.transform.scale(caravan_camel_sprite, (300, 300))

oasis_creature_sprite = load_image("images/OasisCreature.gif", (200, 200))
oasis_creature_sprite = pygame.transform.scale(oasis_creature_sprite, (200, 200))

# Dictionary of NPC sprites
npc_sprites = {
    "caravan_man": caravan_man_sprite,
    "caravan_camel": caravan_camel_sprite,
    "oasis_creature": oasis_creature_sprite,
}

# small list of npc dicts you can expand for dialogue, movement, etc.
npcs = [
    {
        "name": "caravan_man",
        "sprite": caravan_man_sprite,
        "position": pygame.Vector2(600, WINDOW_HEIGHT - 250),
        "active": False,
        "dialogue": ["Hello there, traveler! Need some water?", "Join us on our journey through the desert. But we will be watching you."],
        "dialogue_index": 0
    }
]

current_npc = None
show_dialogue = False

player_pos = pygame.Vector2(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
player_speed = 200
dt = 0

# ---------------- Scene Music ----------------
def play_scene_music(scene_name):
    pygame.mixer.music.stop()
    music_file = story.get(scene_name, {}).get("sound")
    if music_file:
        try:
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play(-1)
        except Exception:
            # ignore if file not found or mixer error
            pass

# Load story images (scale them safely)
for scene in story.values():
    if "image" in scene and scene["image"]:
        try:
            img = pygame.image.load(scene["image"]).convert_alpha()
            scene["image"] = pygame.transform.scale(img, (WINDOW_WIDTH, WINDOW_HEIGHT))
        except Exception:
            scene["image"] = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            scene["image"].fill((50, 50, 50))  # placeholder gray
    else:
        scene["image"] = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        scene["image"].fill((50, 50, 50))

# ---------------- Helper Functions ----------------
def draw_text(surface, text, font, color, rect, bg_overlay=False):
    if bg_overlay:
        overlay = pygame.Surface((rect.width, rect.height))
        overlay.set_alpha(150)
        overlay.fill((0, 0, 0))
        surface.blit(overlay, rect.topleft)
    
    # preserve newlines: split by '\n' first, then wrap each line by words
    paragraphs = text.split('\n')
    y = rect.top
    for para in paragraphs:
        words = para.split(' ')
        line = ""
        for word in words:
            test_line = (line + word + " ").strip()
            if font.size(test_line)[0] <= rect.width:
                line = (line + word + " ").strip() + " "
            else:
                # draw current line
                rendered = font.render(line.strip(), True, color)
                surface.blit(rendered, (rect.left, y))
                y += rendered.get_height()
                line = word + " "
        # draw remaining line of paragraph
        if line.strip() != "":
            rendered = font.render(line.strip(), True, color)
            surface.blit(rendered, (rect.left, y))
            y += rendered.get_height()
        # add a little space after paragraph
        y += 4

def reset_player():
    global player_pos
    player_pos = pygame.Vector2(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

# ---------------- Main Game Loop ----------------
# ---------------- Main Game Loop ----------------
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == K_e:  # interact key
                for npc in npcs:
                    # simple distance check to player
                    if player_pos.distance_to(npc["position"]) < 150:
                        show_dialogue = True
                        current_npc = npc

            # Step 2: Advance dialogue with SPACE
            if event.key == K_SPACE and show_dialogue and current_npc:
                current_npc["dialogue_index"] += 1
                if current_npc["dialogue_index"] >= len(current_npc["dialogue"]):
                    # dialogue finished
                    show_dialogue = False
                    current_npc["dialogue_index"] = 0
                    current_npc = None

            # Start screen key changed to ENTER
            if game_state == "start_screen" and event.key == K_RETURN:
                game_state = "story"
                current_scene = "start"
                reset_player()
                play_scene_music(current_scene)
            elif game_state == "story" and "choices" in story.get(current_scene, {}):
                choices = list(story[current_scene]["choices"].keys())
                key_map = [K_1, K_2, K_3, K_4]
                for i, key in enumerate(key_map[:len(choices)]):
                    if event.key == key:
                        current_scene = story[current_scene]["choices"][choices[i]]
                        reset_player()
                        play_scene_music(current_scene)
                        if story.get(current_scene, {}).get("ending"):
                            game_state = "ending"
            elif game_state == "ending" and event.key == K_r:
                try:
                    pygame.mixer.music.stop()
                except Exception:
                    pass
                game_state = "start_screen"
                current_scene = "start"
                reset_player()

            elif event.key == K_e and show_dialogue and current_npc:
                npc = current_npc
                if npc and npc["dialogue_index"] < len(npc["dialogue"]) - 1:
                    npc["dialogue_index"] += 1
                else:
                    show_dialogue = False
                    current_npc = None
                    npc["dialogue_index"] = 0   
                #play_scene_music(current_scene)

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_pos.x -= player_speed * dt
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_pos.x += player_speed * dt
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_pos.y -= player_speed * dt
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_pos.y += player_speed * dt


    sprite_w, sprite_h = adventurer_sprite.get_size()
    player_pos.x = max(0, min(player_pos.x, WINDOW_WIDTH - sprite_w))
    player_pos.y = max(0, min(player_pos.y, WINDOW_HEIGHT - sprite_h))

    # Draw background
    screen.blit(story[current_scene]["image"], (0, 0))
    overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    overlay.set_alpha(120)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))






    # Draw NPCs if scene has them (from story definition)
    if "npcs" in story.get(current_scene, {}):
        for i, npc in enumerate(story[current_scene]["npcs"]):
            sprite = npc_sprites.get(npc)
            if sprite:
                screen.blit(sprite, (200 + i * 150, WINDOW_HEIGHT - 200))

    # You can also draw npcs from the `npcs` list if you want
    for npc in npcs:
        if npc.get("active"):
            screen.blit(npc["sprite"], npc["position"])

    # Player Sprite
    screen.blit(adventurer_sprite, (int(player_pos.x), int(player_pos.y)))

    # UI Text
    if game_state == "start_screen":
        draw_text(screen,
                  "Hello Player!\nPress ENTER to start this adventure game!\n" \
                  "Controls:\n- Press Arrow keys or WASD to move\n"
                  "You will have 4 choices to choose from press the number to choose\n- " \
                  "R to restart",
                  ui_font, (255, 255, 255),
                  pygame.Rect(100, 200, 800, 400), bg_overlay=True)
    elif game_state == "story":
        draw_text(screen, story[current_scene]["text"], text_font, (255, 255, 255),
                  pygame.Rect(50, 50, WINDOW_WIDTH - 200, 400), bg_overlay=True)
        if "choices" in story[current_scene]:
            choice_text = " / ".join([f"[{i+1}] {c}" for i, c in enumerate(story[current_scene]["choices"].keys())])
            draw_text(screen, choice_text, ui_font, (200, 255, 200),
                      pygame.Rect(50, 500, WINDOW_WIDTH - 100, 200), bg_overlay=True)
    elif game_state == "ending":
        draw_text(screen, story[current_scene]["text"] + "\n\nPress R to restart the game!",
                  text_font, (255, 255, 255),
                  pygame.Rect(50, 50, WINDOW_WIDTH - 100, 700), bg_overlay=True)
        
    if show_dialogue and current_npc:
        dialogue_text = current_npc["dialogue"][current_npc["dialogue_index"]]
        draw_text(screen, dialogue_text, ui_font, (255, 255, 0),
                  pygame.Rect(50, WINDOW_HEIGHT - 150, WINDOW_WIDTH - 100, 100), bg_overlay=True)

    dt = clock.tick(60) / 1000
    pygame.display.flip()

pygame.quit()