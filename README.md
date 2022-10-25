# epic7_bot
> epic7_bot

epic7_bot is a [Epic 7](https://epic7.smilegatemegaport.com/) toolkit/bot used via cli to perform automated actions inside the game like:

- Automatic buy of covenant and mystic charms on secret shop until out of gold or skystone.
- Automatic battle all NPCs available on Arena.
- Automatic battle chosen hunt until out of energy.
- Automatic perform all daily actions, like daily summon and pet summon, sanctuary daily rewards, guild donations, etc.

The bot uses Android Debug Bridge to perform actions inside the game, because of that all actions are propmt directly into the emulator in use, enabling the user to use his PC while the bot perform it's actions on background. 

## Requirements:
- [Android Debug Bridge (adb)](https://developer.android.com/studio/command-line/adb)
    - Can be installed via [Chocolatey](https://chocolatey.org/) ($choco install adb)
- [Python 3.4+](https://www.python.org/downloads/release/python-392/)

## Instalation

```bash
pip install git+https://github.com/brunocordioli072/epic7_bot
```

## Usage

- Enable Android Debug Bridge(ADB) on your emulator of choice. **(more stable on Bluestacks)**
    - Bluestacks: Settings > Advanced > Enable Android Debug Bridge
    - Nox: Settings > Device > Enable Network Bridge Mode

```
epic7 --help
Usage:
    epic7 <command> [options]

All commands should be run when the game screen is in the lobby!

The most commonly used commands are:
    shop            Start secret shop auto buy
    arena           Start arena npc auto battle
    hunt            Start hunt auto battle
    daily           Start daily actions

Options:
    -h --help       Show this help message and exit
    -v --version    Show version and exit
    -c --current    Run command on current screen
```

## Credits

- https://github.com/EpicScipted/E7-Auto-Shop-Refresh-Custom
- https://github.com/EmaOlay/E7-Auto-Shop-Refresh
- https://github.com/JohnnyKaime/Epic7_Shop_Refresh