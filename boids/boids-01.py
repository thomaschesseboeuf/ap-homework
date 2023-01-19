import arcade
import math
import numpy as np

BACKGROUND = arcade.color.ALMOND
IMAGE = "arrow-resized.png"
OBSTACLE = 'obstacle-resized.png'
HEIGHT = 800
WIDTH = 800

def grid():
    Grid = []
    X = np.linspace(0,WIDTH,12)
    Y = np.linspace(0,HEIGHT,12)
    for x in X[1:-1]:
        for y in Y[1:-1]:
            Grid.append((x,y))
    return Grid

def distance(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5


class Window(arcade.Window):

    def __init__(self):
        super().__init__(HEIGHT, WIDTH, "My first boid")
        arcade.set_background_color(BACKGROUND)
        self.set_location(800, 200)
        self.boids = None
        self.obstacles = None
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            for boid in self.boids:
                boid.turning = 1
        if key == arcade.key.RIGHT:
            for boid in self.boids:
                boid.turning = -1
            
    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            for boid in self.boids:
                boid.turning = min(boid.turning,0)
        
        if key == arcade.key.RIGHT:
            for boid in self.boids:
                boid.turning = max(boid.turning,0)


    def setup(self):
        boid = Boid()
        self.boids = arcade.SpriteList()
        self.boids.append(boid)
        self.obstacles = arcade.SpriteList()
        for (x,y)in grid():
            self.obstacles.append(Obstacle(x,y))

    def on_draw(self):
        arcade.start_render()
        self.obstacles.draw()
        self.boids.draw()


    def on_update(self, delta_time):
        self.boids.on_update()

class Boid(arcade.Sprite):
    def __init__(self):
        super().__init__(IMAGE)
        self.turning = 0
        self.alpha = 255
        self.obstacles = arcade.SpriteList()
        for (x,y) in grid():
            self.obstacles.append(Obstacle(x,y))
        self.distances = []
        for obstacle in self.obstacles:
            self.distances.append(distance((self.center_x, self.center_y), (obstacle.center_x, obstacle.center_y)))
        self.rotation_speed = 100
        self.angle = -135
        self.speed = 100
        self.center_x, self.center_y = 100, 100

    
    def on_update(self, delta_time):
        self.angle += np.random.normal(0, 1) + self.turning * self.rotation_speed * delta_time
        self.center_x += self.speed * math.cos(self.angle*math.pi/180) * delta_time
        self.center_y += self.speed * math.sin(self.angle*math.pi/180)  * delta_time
        self.distances = []
        for obstacle in self.obstacles:
            self.distances.append(distance((self.center_x, self.center_y), (obstacle.center_x, obstacle.center_y)))
        
        #SEPARATION
        delta = [0,0]
        for i,d in enumerate(self.distances):
            if d<20:
                delta[0] += (self.center_x-self.obstacles[i].center_x)*2*(1-d/20)
                delta[1] += (self.center_y-self.obstacles[i].center_y)*2*(1-d/20)
        self.center_x += delta[0]
        self.center_y += delta[1]
        if delta != [0,0]:
            self.angle = math.atan2(delta[1], delta[0])
        
        self.center_x = self.center_x % 800
        self.center_y = self.center_y % 800

class Obstacle(arcade.Sprite):
    def __init__(self, x=WIDTH/2, y=HEIGHT/2):
        super().__init__(OBSTACLE)
        self.center_x, self.center_y = x, y

window = Window()
window.setup()
arcade.run()


