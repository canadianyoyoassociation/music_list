import os
import string
import sys

directory = sys.argv[1]
stop_at = int(sys.argv[2])  # minutes


# find a file based on the player's full name
def find_player_file(player, files):
    pwords = player.split(" ")

    # match the first word on player's name
    result = [f for f in files if (pwords[0].lower() in f.lower())]

    if (len(result) == 0):
        return '<strong>NOT FOUND</strong>'

    elif (len(result) == 1):
        return result[0]

    else:
        # further match the second word on player's name
        result = [f for f in result if (pwords[1].lower() in f.lower())]

        if (len(result) > 1):
            return '<strong>ERROR</strong>'
        else:
            return result[0]


def build_player_row(player_id, player_name, player_filename):
    return f"""
          <tr onclick="toggleBackground(this)">
            <td>{player_id}</td>
            <td>{player_name}</td>
            <td>
              <button onclick="rewindAudio('{player_id}')">
                Rewind
              </button>
            </td>
            <td>
              <audio
                id="{player_id}"
                controls
                src="{player_filename}"
                type="audio/mpeg"
                onplay="stopAt(this)"
              ></audio>
              <br />
              <small>{player_filename}</small>
            </td>
          </tr>
    """


files = os.listdir(directory)

with open(os.path.join(directory, 'playerlist.txt')) as f:
    players = [line.strip() for line in f]

# build template data
players_table = ""
for i, p in enumerate(players):
    filename = find_player_file(p, files)
    players_table += build_player_row(
        player_id=i + 1,
        player_name=p,
        player_filename=f'{directory}/{filename}',
    )

# output
with open('template.html') as f:
    template = f.read()

print(string.Template(template).safe_substitute(
    stop_at=stop_at,
    stop_at_unit='minute' if stop_at == 1 else 'minutes',
    directory=directory,
    players_table=players_table,
))
