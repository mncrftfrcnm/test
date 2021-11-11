"""Example game client"""

import pygame
from pygame import mixer 
import pygame.locals
from pygase import Client
import time
from pygame import mixer 
import pygame.mixer_music
from pyjoycon import JoyCon, get_R_id

joycon_id = get_R_id()
joycon = JoyCon(*joycon_id)

joycon.get_status()

### SETUP ###

# Subclass pygase classes to scope event handlers and game-specific variables.
class ChaseClient(Client):
    def __init__(self):
        super().__init__()
        self.player_id = None
        # The backend will send a "PLAYER_CREATED" event in response to a "JOIN" event.
        self.register_event_handler("PLAYER_CREATED", self.on_player_created)

    # "PLAYER_CREATED" event handler
    def on_player_created(self, player_id):
        # Remember the id the backend assigned the player.
        self.player_id = player_id


# Create a client.
client = ChaseClient()

### MAIN PROCESS ###
#192.168.10.204
if __name__ == "__main__":
    pygame.mixer.init()

    # Connect the client, let the player input a name and join the server.
    client.connect_in_thread(hostname="192.168.10.185", port=8080)
    client.dispatch_event("JOIN", input("Player name: "))
    # Wait until "PLAYER_CREATED" has been handled.
    while client.player_id is None:
        pass
    # Set up pygame.
    keys_pressed = set()  # all keys that are currently pressed down
    clock = pygame.time.Clock()
    # Initialize a pygame screen.
    pygame.init()
    screen_width = 740
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))
    # Start the actual main loop.
    game_loop_is_running = True
    while game_loop_is_running:
                
                
                
        
        # Run at 50 FPS
        if trer == 1:
            dt = clock.tick(35)
        else:    
            dt = clock.tick(50)
        # Clear the screen.
        screen.fill((0, 100, 0))
        # Handle pygame input events.
        for event in pygame.event.get():

            if event.type == pygame.locals.QUIT:
                game_loop_is_running = False
            if event.type == pygame.locals.KEYDOWN:
                keys_pressed.add(event.key)
            
            if event.type == pygame.locals.KEYUP:
                keys_pressed.remove(event.key)
        # Handle player movement.
        dx, dy = 0, 0
        if pygame.locals.K_DOWN in keys_pressed:
            dy += 0.5 * dt
        elif pygame.locals.K_UP in keys_pressed:
            dy -= 0.5 * dt
        elif pygame.locals.K_RIGHT in keys_pressed:
            dx += 0.5 * dt
        elif pygame.locals.K_LEFT in keys_pressed:
            dx -= 0.5 * dt
#ssh 192.168.10.185 -l pi

        elif pygame.locals.K_a in keys_pressed:
            if trer == 4:
                dx -= 1 * dt
        elif pygame.locals.K_d in keys_pressed:
            if trer == 4:
                dx += 1 * dt
        elif pygame.locals.K_w in keys_pressed:
            if trer == 4:
                dy -= 1 * dt
        elif pygame.locals.K_s in keys_pressed:
            if trer == 4:
                dy += 1 * dt
        # elif pygame.locals.K_o in keys_pressed:
            
        #     xe,ye = pygame.mouse.get_pos()
        #     dx, dy = xe, ye
        #     #print(xe,ye)
        #     time.sleep(0.1)
            
        elif pygame.locals.K_e in keys_pressed:
            dy = 0
            
            if trer == 3:
                time.sleep(1)
        elif pygame.locals.K_q in keys_pressed:
            dx = 0

            time.sleep(1)
        # Safely access the synchronized shared game state.
        with client.access_game_state() as game_state:


            # Notify server about player movement.
            old_position = game_state.players[client.player_id]["position"]
            client.dispatch_event(
                event_type="MOVE",
                player_id=client.player_id,
                new_position=((old_position[0] + dx) % screen_width, (old_position[1] + dy) % screen_height),
            )
            # Draw all players as little circles.
            for player_id, player in game_state.players.items():
                if player_id == client.player_id:
                    # Green: Yourself
                    dt += 0.1
                    color = (50, 50, 255)
                    
                elif player_id == game_state.chaser_id:
                    # Red: The chaser
                    dt += 2
                    color = (255, 50, 50)
                else:
                    # Blue: Others
                    color = (50, 255, 50)
                x, y = [int(coordinate) for coordinate in player["position"]]
                pygame.draw.circle(screen, color, (x, y), 10)
                if trer == 2:
                    pygame.draw.circle(screen,(0, 0, 0), (x, y+1*dt), 10)
                    pygame.draw.circle(screen,(0, 0, 0), (x, y-1*dt), 10)
                    pygame.draw.circle(screen,(0, 0, 0), (x-1*dt, y), 10)
                    pygame.draw.circle(screen,(0, 0, 0), (x+1*dt, y), 10)
        # Do the thing.
        pygame.display.flip()
    # Clean up.
    pygame.quit()

    # Disconnect afterwards and shut down the server if the client is the host.
    client.disconnect(shutdown_server=True)