import json, sys, rpp

try:
    with open(sys.argv[1], "rb") as f:
        data = f.read().decode("utf-8")
        r = rpp.loads(data)

        trackList = {}
        
        for item in r.iterfind(".//TRACK"):
            trackName = item.find(".//NAME")[1]
            if (trackName.startswith("!")):
                if not trackName in trackList:
                	trackList[trackName] = []
                for pos in item.iterfind(".//POSITION"):
                    itemType = item.find(".//SOURCE").attrib
                    itemPos = float(pos[1])
                    if (itemType not in ["MIDI"]):
                        trackList[trackName].append(itemPos)
        
        if (len(sys.argv) > 2):
            with open(sys.argv[2], "w") as out:
                json.dump(trackList, out)
            print("File saved to " + sys.argv[2])
        else:
            print(json.dumps(trackList))
except Exception as e:
    print(e)