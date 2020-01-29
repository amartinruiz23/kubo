import PIL, random, sys
from PIL import Image, ImageDraw

# TYPE:
# 1. flat
# 2. horizontal
# 3. vertical

BLOCK_SIZE = 50

class Block:
    def __init__(self, v, colour1, colour2, type, draw):
        self.colour1 = colour1
        self.colour2 = colour2
        self.v = (v[0]*BLOCK_SIZE, v[1]*BLOCK_SIZE, v[2]*BLOCK_SIZE, v[3]*BLOCK_SIZE)
        self.draw = draw
        self.type = type

    def print(self):
        if (self.type == 1):
            self.draw.rectangle(self.v, self.colour1)
        if (self.type == 2):
            self.draw.rectangle((self.v[0], self.v[1], self.v[2], ((self.v[1]+self.v[3])/2)), self.colour1)
            self.draw.rectangle((self.v[0], (self.v[1]+self.v[3])/2, self.v[2], self.v[3]), self.colour2)
        if (self.type == 3):
            self.draw.rectangle((self.v[0], self.v[1], (self.v[0] + self.v[2])/2, self.v[3]), self.colour1)
            self.draw.rectangle(((self.v[0] + self.v[2])/2, self.v[1], self.v[2], self.v[3]), self.colour2)

def main(size, n_type1, n_type2, n_type3):

    if(size*size < n_type1 + n_type2 + n_type3):
        print("Incorrect parameters")
    else:
        dimension = BLOCK_SIZE*size
        image = Image.new('RGB', (dimension,dimension))
        draw = ImageDraw.Draw(image)

        type_matrix = [ [ 0 for i in range(size) ] for j in range(size) ]

        i = n_type1
        while(i > 0):
            r1 = random.randint(0, size-1)
            r2 = random.randint(0, size-1)
            if(type_matrix[r1][r2] == 0):
                type_matrix[r1][r2] = 1
                i = i-1

        i = n_type2
        while(i > 0):
            r1 = random.randint(0, size-1)
            r2 = random.randint(0, size-1)
            if(type_matrix[r1][r2] == 0):
                type_matrix[r1][r2] = 2
                i = i-1

        i = n_type3
        while(i > 0):
            r1 = random.randint(0, size-1)
            r2 = random.randint(0, size-1)
            if(type_matrix[r1][r2] == 0):
                type_matrix[r1][r2] = 3
                i = i-1

        """
        colour1_1 = (0,0,0)
        colour1_2 = (0,0,0)
        colour2_1 = (0,0,0)
        colour2_2 = (0,0,0)
        colour3_1 = (0,0,0)
        colour3_2 = (0,0,0)
        """

        colours = [ [ 0 for i in range(2) ] for j in range(3) ]
        colours[0][0] = (random.randint(50,215), random.randint(50,215), random.randint(50,215))
        colours[0][1] = (0,0,0)
        colours[1][0] = (random.randint(50,215), random.randint(50,215), random.randint(50,215))
        colours[1][1] = (random.randint(50,215), random.randint(50,215), random.randint(50,215))
        colours[2][0] = (random.randint(50,215), random.randint(50,215), random.randint(50,215))
        colours[2][1] = (random.randint(50,215), random.randint(50,215), random.randint(50,215))

        print(colours)

        b1 = Block((0,0,1,1), (50,50,80), (200,50,80), 2, draw)
        b2 = Block((1,0,2,1), (100,80,800), (200,80,80), 3, draw)
        b3 = Block((0,1,1,2), (50,50,80), (200,50,80), 2, draw)
        b4 = Block((1,1,2,2), (100,80,800), (200,80,80), 3, draw)

        for i in range(size):
            for j in range(size):
                if (type_matrix[i][j] == 0):
                    actual_type = random.randint(1,3)
                else:
                    actual_type = type_matrix[i][j]
                b = Block((i, j, i+1, j+1), colours[actual_type-1][0], colours[actual_type-1][1], actual_type, draw)
                b.print()

        image.save("prueba.png")

if __name__ == "__main__":
  main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
