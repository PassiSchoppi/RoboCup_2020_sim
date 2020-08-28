# RoboCup_2020_sim

## Installing

Clone das Repo mit:

```
git clone https://github.com/PassiSchoppi/RoboCup_2020_sim.git
```

Erstmal braucht du Python 3.7.
Wenn du ```python``` in der Konsole laufen lässt, siehst du die Version.


```
Python 
``` ***3.7.9***
``` (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) 8MSC v.1900 64 bit (AMD64)9 on win32
Type "help", "copyright", "credits" or "license" for more information. 
```

Alternativ kann auch ```python3``` der Command sein.

Wenn du Python installierst, musst du den Pfad in die Environment Variables hinzufügen.

Dann brauchst du noch WeBots um die Arena zu simulieren.

Installiere die Version [Webots R2020a revision 1](https://github.com/cyberbotics/webots/releases/tag/R2020a-rev1).

Dann lade den neusten Release (.zip Datei) von dem [RoboCup Repo](https://github.com/Shadow149/RescueMaze/releases) herunter.

Dadrin gibt es eine Datei ```Game/worlds/*.wbt``` die kann man mit Webots öffnen.

Dann müsstest du auf der Linken Seite ein Teil sehen wo man den Code laden kann.

Wenn nicht:

1. Click the „Show the Scene Tree side bar“ button in the top left of the Simulation view window.
2. Find the „MAINSUPERVISOR“ node.
3. Right click the Mainsupervisor node and click „Show Robot Window“
4. Close the „Show the Scene Tree side bar“ using the same button as before.

Dann mache bei den Einstellungen ```tools—> Preferences —> python command``` den Python Command bei dem dann Version 3.7 läuft.

Wenn’s da Probleme gibt empfehle ich Windows neu zu installieren und alle persönliche Dateien zu löschen!

Nice! Du hast es geschafft!

## Extra Stuff

[GitHub Wiki](https://github.com/Shadow149/RescueMaze/wiki)
(Alle 3 Tutorials durchlesen!)

[Discord Server](https://discord.gg/DJWqnQ)

[YouTube Tuts](https://www.youtube.com/channel/UCsK3Oe0yhcyCAzbYyvfEbyw)

## Programming

Wie Importe ich eigene Python Dateien um Code zu organisieren?

[Tutorial](https://realpython.com/lessons/module-search-path/)

Code:

```
import sys
sys.path.append(‚C:\\Users\\kalli\\Documents\\RoboCup_2020_sim\\code‘)
from movements import *
```

Du kannst mehrmals z.B. ```from controller import Robot``` importieren. Python hat da keine Probleme.

—

Lass mal unsre ganze Codebase in Functional Programming machen ; )
