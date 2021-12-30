import numpy
import random
import sys

'''
ThunderRange
============
Module which helps you with creating a ranges.
Developed by tixonochek:
- Github: tixcode = https://github.com/tixcode
- Website of ThunderEngine: https://sites.google.com/view/thundercode/главная-страница

+ Documentation of Library can be finded on ThunderEngine website (ONLY RUSSIAN LANGUAGE)
'''


class Range:
    '''
    Range Class
    ==========
    Using this class you can create ranges simply:

    "Range(1, 4).range" equals [1, 2, 3, 4]
    '''

    def __init__(self, min: int, max: int) -> None:
        '''
        Initializator of Range class
        '''
        self._minimal: int = min
        self._maximal: int = max
        self._range: numpy.array = numpy.arange(min, max+1)

    def step_through(self, step_function, reversed: bool = False) -> None:
        '''
        Step Through Method
        =====================
        Example of using:

        def test(step: int):
            print(step ** 2)

        Range(1, 3).step_through(test)

        Outputs 1, 4, 9
        --------------
        '''
        if not reversed:
            for step in self.range:
                step_function(step)
        else:
            reversed_range = self.range
            reversed_range.reverse()
            for step in reversed_range:
                step_function(step)

    def empty(elements: int):
        '''
        Empty Function
        ===============
        This function returns a range object with a specified
        elements count (bases on "elements" parameter). Value of
        every element = random number.
        Example:

        print(Range.empty(2).range)

        Outputs [random_number, random_number] where random_number
        it's a random number.
        '''
        specialList: list = []
        for i in range(0, elements+1):
            specialList.append(random.randint(-sys.maxsize, sys.maxsize))
        specialRange: Range = Range(0, elements)
        specialRange._range = numpy.array(specialList)
        return specialRange

    @property
    def range(self):
        '''
        Range Property
        ----
        It's a range of this Range class object (as list)
        '''
        return list(self._range)

    @range.setter
    def range(self, value):
        raise ValueError("Range is a constant!")

    @range.deleter
    def range(self):
        raise Exception("You can't delete a range property!")
