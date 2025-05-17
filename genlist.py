import os
import sys

directory = sys.argv[1]
stopAt = int(sys.argv[2])  #minutes

def print_html_head():
    print("<html><head><script>")
    print("function stopAt(elemId) {\n" +
    "    var stopAt = " + str(stopAt) +".0; // minutes\n" +
    "    var grace = 2.0; // seconds\n" +
    "    var elem = document.getElementById(elemId);\n" +
    "    elem.currentTime = 0.0;\n" +
    "    setTimeout(function() {\n" +
    "        elem.pause();\n" +
    "        //elem.currentTime = 0; // rewinds to beginning\n" +
    "    }, ((stopAt * 60) + grace) * 1000);\n" +
    "}\n")
    print("function toggleBackground(elem) {\n" +
    "    //alert(elem)                \n" +
    "    if (elem.bgColor == '#DDD') {\n" +
    "        elem.bgColor = '#FFF';   \n" +
    "    } else {                     \n" +
    "        elem.bgColor = '#DDD';   \n" +
    "    }                            \n" +
    "}                                \n")
    print("</script>")
    print("<style>")
    print("body {font-family: sans-serif;}")
    print("td { max-width: 400px; min-width: 20px; padding: 10px; }")
    print("td:nth-child(3) { font-size: 12;}")
    print("</style></head>")
    print("<body><h1>" + directory + "  stop at " + str(stopAt) + " minutes</h1><table border>")

def print_one_music(id, name, filename):
    print("<tr onclick='toggleBackground(this);'>")
    print("<td>" + str(id) + "</td>")
    print("<td>" + name + "</td>")
    print("<td><audio id='" + str(id) + "' controls src='" + filename + "' " +
          "type='audio/mpeg' onplay='stopAt(this.id)'></audio><br>")
    print(filename)
    print("<br></td>")
    print("</tr>")

def print_html_tail():
    print("</table></body></html>")


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

# output

print_html_head()

for i, p in enumerate(players):
    file = find_player_file(p, files)
    print_one_music(i + 1, p, directory + '/' + file)

print_html_tail()
