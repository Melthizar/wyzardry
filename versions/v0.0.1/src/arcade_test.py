import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade Test"

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.DARK_BLUE)
        
        # Sprite lists
        self.all_sprites = arcade.SpriteList()
        
        # Create a player sprite
        self.player = arcade.SpriteSolidColor(50, 50, arcade.color.YELLOW)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.all_sprites.append(self.player)

    def on_draw(self):
        """Render the screen"""
        self.clear()
        self.all_sprites.draw()
    
    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed"""
        if key == arcade.key.ESCAPE:
            arcade.close_window()

def main():
    window = GameWindow()
    arcade.run()

if __name__ == "__main__":
    main()