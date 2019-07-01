from PIL import Image


class Generate2TriangleInSquarGrid:

    def generate(self):
        size = (640, 640)
        black = (0, 0, 0)
        white = (255, 255, 255)
        img = Image.new("RGB", size, black)
        grid = (8, 8)

        for x in range(0, size[0]//grid[0]):
            for y in range(0, size[1]//grid[1]):
                for x_offset in range(0, grid[0]):
                    x_coord = (x+1) * grid[0]-x_offset
                    for y_offset in range(0, x_offset):
                        y_coord = y*grid[1]+y_offset
                        img.putpixel((x_coord-1, y_coord), white)
                        # x_coord-1 because there would be a line in the leftmost in the left border

        img.save("Tile1.png", "PNG")
        img.show()


if __name__ == "__main__":
    gt = Generate2TriangleInSquarGrid()
    gt.generate()
