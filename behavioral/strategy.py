# TODO add a description
# TODO add an anti-strategy pattern

from abc import abstractmethod, ABC


class CompressorStrategy(ABC):
    "Abstract Class for all the compressor strategies"

    @abstractmethod
    def compress(self, file_name):
        """the method for filtering which is implemented in the concrete sub-classes"""
        pass


class FilterStrategy(ABC):
    """Abstract class for all the filter strategies"""

    @abstractmethod
    def filter(self, file_name):
        """the method for compressing which is implemented in the concrete sub-classes"""
        pass


class BlackAndWhiteFilterStrategy(FilterStrategy):
    """Concrete black and white filtering strategy"""

    def filter(self, file_name):
        """overriding the filter for black and white filtering"""
        print('Doing Black and White Filtering')


class PNGCompressorStrategy(CompressorStrategy):
    """Concrete PNG Compressing strategy"""

    def compress(self, file_name):
        """override the compressing algorithm for the PNG compressing"""
        print("Compressing with the PNG format")


class ImageStorage:
    """The class that needs some good strategies for determining types of player"""

    def __init__(self, compressor_algorithm, filter_algorithm):
        self.__compressor_algorithm = compressor_algorithm
        self.__filter_algorithm = filter_algorithm

    def store(self, image_path):
        """Based on the type of the strategies this method will compress and filter
            the images and then store them"""

        self.__filter_algorithm.filter(image_path)
        self.__compressor_algorithm.compress(image_path)

        print(f'Storing Image Ha Ha Ha {image_path}')

    @property
    def compressor_algorithm(self):
        """Getter for the self.__compressor_algorithm"""
        return self.__compressor_algorithm

    @compressor_algorithm.setter
    def compressor_algorithm(self, compressor_algorithm):
        """Setter for the self.__compressor_algorithm"""
        self.__compressor_algorithm = compressor_algorithm

    @property
    def filter_algorithm(self):
        """Getter for the self.__filter_algorithm"""
        return self.__filter_algorithm

    @filter_algorithm.setter
    def filter_algorithm(self, filter_algorithm):
        """Setter for the self.__filter_algorithm"""
        self.__filter_algorithm = filter_algorithm


if __name__ == '__main__':
    storage = ImageStorage(
        PNGCompressorStrategy(),
        BlackAndWhiteFilterStrategy()
    )

    storage.store('/tmp')
