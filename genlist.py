import os
import sys

from jinja2 import Environment, FileSystemLoader, select_autoescape

directory = sys.argv[1]
stopAt = int(sys.argv[2])  # minutes


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


files = os.listdir(directory)

with open(directory + '/playerlist.txt') as f:
    players = [line.strip() for line in f]

# build template data
player_files = []
for i, p in enumerate(players):
    filename = find_player_file(p, files)
    player_files.append({
        'id': i + 1,
        'name': p,
        'filename': f'{directory}/{filename}',
    })

# render with jinja2
template_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(template_dir), autoescape=select_autoescape())
template = env.get_template('template.jinja')
print(template.render(directory=directory, stop_at=stopAt, player_files=player_files))
