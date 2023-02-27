myDict = {'Arctic Fox': 0,
 'Arctic Hare': 1,
 'Arctic Skua': 2,
 'Arctic Tern': 3,
 'Arctic Wolf': 4,
 'Arctic Woolly Bear Moth': 5,
 'Bald Eagle': 6,
 'Bearded Seal': 7,
 'Beluga Whale': 8,
 "Brunnich's Guillemots": 9,
 'Canada Goose': 10,
 'Caribou': 11,
 'Dall Sheep': 12,
 'Ermine': 13,
 'Greenland Shark': 14,
 'Harp Seal': 15,
 'Hooded Seal': 16,
 'Lemming': 17,
 'Moose': 18,
 'Musk Ox': 19,
 'Narwhal': 20,
 'Orca': 21,
 'Polar Bear': 22,
 'Ptarmigan': 23,
 'Puffin': 24,
 'Ribbon Seal': 25,
 'Ringed Seal': 26,
 'Sea Otter': 27,
 'Snow Goose': 28,
 'Snowshoe Hare': 29,
 'Snowy Owl': 30,
 'Spotted Seal': 31,
 'Walrus': 32,
 'Wolverine': 33}
print("The input dictionary is:")
print(myDict)
reversedDict = dict()
for key in myDict:
    val = myDict[key]
    reversedDict[val] = key
print("The reversed dictionary is:")
print(reversedDict)