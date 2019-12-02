import pickle

EnDict = open("spell.words.txt").readlines()
EnDict = [word.strip() for word in EnDict]

with open("ENDict.pickle", "wb") as handle:
    pickle.dump(EnDict, handle, protocol=pickle.HIGHEST_PROTOCOL)
