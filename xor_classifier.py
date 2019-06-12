from nn import NeuralNetwork
import random
from graphics import *
nn = NeuralNetwork(2,4,1)
training_data = [([1, 0], [1]), ([0, 1], [1]), ([0, 0], [0]), ([1, 1], [0])]
random.seed(None, 2)

def mapping(x, x0, x1, y0, y1):        
        return ((x-x0)/(x0-x1) * (y1-y0) + y1)

width = 400
height = 400
global win2
win2 = GraphWin('Actual results', width, height) # give title and dimensions 
resolution = 10
cols = width / resolution
rows = height / resolution
rects = []
for i in range(0, int(cols)):
        for j in range(0, int(rows)):
            rect = Rectangle(Point(j * resolution, i * resolution), Point(j * resolution + resolution, i * resolution + resolution))
            rand = random.randint(0, 255)
            aColor = color_rgb(rand, rand, rand)
            rect.setFill(aColor)
            rect.setWidth(0)
            rect.draw(win2)
            rects.append(rect)

while(True):
    random.seed(None, 2)
    for i in range(0, 1000): 
        j = random.randint(0, 3)
        #print(training_data[j][0])
        nn.train(training_data[j][0], training_data[j][1])
    for rect in rects:
        x1 = rect.getP1().getY() / resolution / cols
        x2 = rect.getP1().getX() / resolution / rows
        inputs = [x1, x2]
        #print(inputs)
        color = int(255 * nn.guess(inputs).toArray()[0])
        aColor = color_rgb(color, color, color)
        rect.setFill(aColor)