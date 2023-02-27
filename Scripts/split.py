import splitfolders

input_folder = 'Data/'

splitfolders.ratio(input_folder, output="Data_Refined",
                  seed=1337, ratio=(.7, .2, .1),
                  group_prefix=None)