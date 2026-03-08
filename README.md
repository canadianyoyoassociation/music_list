# CANYA Music List

Generates an HTML page with audio players for a list of music files.

## Setup

```bash
# [optional] create and activate a venv
python -m venv venv
source venv/bin/activate

# install dependencies
pip install -r required.txt

# test code by following usage instructions
```

## Usage

```bash
# [optional] create and activate a venv
# [required] install dependencies

# command usage:
python genlist.py <music_directory> <stop_minutes>

# e.g.: save html code to file
python genlist.py <music_directory> <stop_minutes> > index.html
```

- `music_directory`: path to folder containing audio files and a `playerlist.txt`
- `stop_minutes`: auto-stop playback after this many minutes

### `playerlist.txt`

A plain text file in the music directory with one player name per line.
Names are matched against audio filenames.
