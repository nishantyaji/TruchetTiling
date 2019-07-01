from PIL import Image
from PrimitiveRotator import PrimitiveRotator
import itertools
import datetime


class ImageTilerTruncet:

    def __init__(self, img, grid_dimensions):
        self.img = img
        self.width, self.height = self.img.size
        self.grid_dimensions = grid_dimensions

        if grid_dimensions[0] != grid_dimensions[1]:
            raise Exception(
                'The grid dimensions should be equal (like in a square')

        self.width_unit, width_remain = divmod(self.width,
                                               self.grid_dimensions[0])
        self.height_unit, height_remain = divmod(self.height,
                                                 self.grid_dimensions[1])

        if width_remain > 0 or height_remain > 0:
            raise Exception(
                'The width and height should be proper multiples of the grid')

        self.new_img_filename = "Truchet" + \
            str(datetime.datetime.now()) + ".png"

        self.new_image = Image.new("RGB", self.img.size, (0, 0, 0))

    @staticmethod
    def decentrify(center, coord):
        return coord[0]-center[0], coord[1]-center[1]

    @staticmethod
    def centrify(center, coord):
        return coord[0]+center[0], coord[1]+center[1]

    @staticmethod
    def quad_vectors():
        base_elems = [1, -1]
        return itertools.product(base_elems, repeat=2)

    def rotate(self, cell_num, direction, numtimes):
        numtimes = numtimes % 4
        pr = PrimitiveRotator(direction)
        # cell alignment is
        # 1, 2, ... width_unit
        # width_unit+1.... 2*width_unit
        first_cell_center = self.grid_dimensions[0] / \
            2, self.grid_dimensions[1]/2
        present_cell_coord = divmod(cell_num, self.width_unit)
        this_center = first_cell_center[0] + \
            (present_cell_coord[0]-1)*self.grid_dimensions[0],
        first_cell_center[1] + (present_cell_coord[1]-1) * \
            self.grid_dimensions[1]

        max_coord = this_center[0] + \
            self.grid_dimensions[0]//2, this_center[1] + \
            self.grid_dimensions[1]//2

        """
        min_coord = this_center[0] - \
            self.grid_dimensions[0]//2, this_center[1] - \
            self.grid_dimensions[1]//2
        """
        for x in
        for y
        for vect in self.quad_vectors():

        pass


if __name__ == '__main__':
    img = Image.open('C:\\Workspace\\Python\\TruchetTiling\\Tile1.png', 'r')
    itt = ImageTilerTruncet(img, (8, 8))
    for x in itt.quad_vectors():
        print(x)
