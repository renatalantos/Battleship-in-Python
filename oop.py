# ship Class
class Ship:

    def __init__(self, size, orientation, location):
        self.size = size

        if orientation == 'horizontal' or orientation == 'vertical':
            self.orientation = orientation
        
        else:
            raise ValueError('Orientation must be either "horizontal" or "vertical"')

        if orientation == 'horizontal':
            if location['row'] in range(1, int(board_size)):
                self.coordinates = []

                for index in range(size):
                    if location['col'] + index in range(int(1, board_size)):
                        self.coordinates.append({'row': location['row'], 'col': location['col'] + index})
                    else: 
                        raise IndexError('Column is not in range')
            else: 
                raise IndexError('Row is not in range')
        
        elif orientation == 'vertical':
            if location['col'] in range(1, int(board_size)):
                self.coordinates = []

                for index in range(size):
                    if location['row'] + index in range(int(1, board_size)):
                        self.coordinates.append({'row': location['row'] + index, 'col': location['col']})
                    else: 
                        raise IndexError('Row is not in range')
            else: 
                raise IndexError('Column is not in range')              