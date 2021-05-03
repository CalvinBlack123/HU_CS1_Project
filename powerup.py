import pygame

BLACK = (0,0,0)

class Powerup(pygame.sprite.Sprite):
    
    def __init__ (self, color, width, height):
        super().__init__()
        # Pass in the color of the ball, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        #pygame.draw.rect(self.image, color, [0, 0, width, height])
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        
        #self.velocity = [5,5]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]