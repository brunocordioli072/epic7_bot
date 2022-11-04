# epic7_bot
> epic7_bot

epic7_bot is a [Epic 7](https://epic7.smilegatemegaport.com/) toolkit/bot used via cli to perform automated actions inside the game like:

- Secret shop refreshing;
- Hunt battling;
- Arena NPC battling;
- All daily actions, like daily summon and pet summon, sanctuary daily rewards, guild donations, etc.

The bot uses [Android Debug Bridge](https://developer.android.com/studio/command-line/adb) to perform actions inside the game and [openCV](https://opencv.org/) to enable image recognition. All actions are performed in the background directly inside the emulator of your choice. So the user can still use the computer while the bot is running. All actions are several sorted clicks sent by the [Android Debug Bridge](https://developer.android.com/studio/command-line/adb) as a input to the screen, which are randomized so that the bot can't click in the same place twice, avoiding any cheat detection Super Creative might have.

Check the [Docs](https://brunocordioli072.github.io/epic7_bot/) for more info! 

## Requirements:
- [Chocolatey](https://chocolatey.org/)
- [Android Debug Bridge (adb)](https://community.chocolatey.org/packages/adb)
- [Python 3.4+](https://www.python.org/downloads/release/python-392/)
- [Git](https://community.chocolatey.org/packages/git)

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
```

## Credits

- https://github.com/EpicScipted/E7-Auto-Shop-Refresh-Custom
- https://github.com/EmaOlay/E7-Auto-Shop-Refresh
- https://github.com/JohnnyKaime/Epic7_Shop_Refresh