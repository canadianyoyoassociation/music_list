# CANYA Music List

Generates an HTML page with audio players for a list of music files.

## Usage

```bash
# install Python 3

# command usage:
python genlist.py [-h | --help] <music_directory> <stop_minutes>

# e.g.: save html code to file
python genlist.py <music_directory> <stop_minutes> > index.html
```

- `music_directory`: path to folder containing audio files and a `playerlist.txt`
- `stop_minutes`: auto-stop playback after this many minutes

### `playerlist.txt`

A plain text file in the music directory with one player name per line.
Names are matched against audio filenames.
