

import pickle
import requests

dataObject = {"key":"val","kay2":"val2"}

with open("data.pickle","wb") as fileHandle:
    pickle.dump(dataObject,fileHandle)