import thunderrange as tr

a = tr.Range(min=1, max=4)
'''
a now equals the range object which has range property. This property
now equals [1, 2, 3, 4]
'''

b = tr.Range.empty(elements=3)
'''
b now equals the range object which has range property. This property
now equals [any_random_number, any_random_number, any_random_number]
'''

a.range  # [1, 2, 3, 4]
b.range  # [any_random_number, any_random_number, any_random_number]

tr.Range(1, 4).range = ...  # Error
del tr.Range(1, 4).range  # Error
