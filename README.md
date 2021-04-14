# AddMarkersFromJSON

Helper scripts for importing REAPER track position data into After Effects for streamlined YTPMV/音MAD creation. Code is a mess currently so don't reference this project for other things. I don't know what else to name this \o/

## Usage

**Note:** This script expects you have Python 3 installed and in your `PATH` as `python`, as well as the packages listed in `requirements.txt`.

1. Grab the source of this repo.
2. Put the `.jsx` and `.py` file into your After Effects' ScriptUI Panels folder (`Support Files/Scripts/ScriptUI Panels/`).
3. Launch After Effects and access the script panel from the `Window` menu.

When importing a REAPER project file, the script will read tracks prefixed with `!`, and return a JSON object of the timecodes for the start of each item *and* MIDI note for each respective track. After selecting a track and hitting the `Go!` button, comp markers will be added to the current comp for each item of the selected track.

The markers added to the comp can be used in conjunction with expressions to determine when a video should be flipped, restart, animated, etc.

A brief example of using this script with the expressions from [my expressions library](https://github.com/stysmmaker/mmkr):
```js
// Apply to time remap
const { YTPMV } = footage('mmkr.jsx').sourceData.get_functions();
YTPMV.time_reset(thisComp.marker);
```
```js
// Apply to an instance of the Transform effect
const { YTPMV } = footage('mmkr.jsx').sourceData.get_functions();
YTPMV.flip(thisComp.marker);
```

## Roadmap

Currently this is essentially just a dump of the script files I use currently, eventually I'd like to clean them up and add a few more features.