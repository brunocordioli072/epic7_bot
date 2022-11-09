# epic7_bot
> epic7_bot

Epic7 Bot is a [Epic 7](https://epic7.smilegatemegaport.com/) toolkit/bot used via cli to perform automated actions inside the game. All actions are **cheat detection proof** by doing only randomized click inputs inside the emulator screen.

The bot currently automates:
- Secret shop refreshing;
- Hunt battling;
- Arena NPC battling;
- All daily actions, like daily summon and pet summon, sanctuary daily rewards, guild donations, etc.

Check the [Docs](https://brunocordioli072.github.io/epic7_bot/) for more info! 

## Requirements:
- [Chocolatey](https://chocolatey.org/)
- [Android Debug Bridge (adb)](https://community.chocolatey.org/packages/adb)
- [Python 3.4+](https://www.python.org/downloads/release/python-392/)

## Instalation

```bash
pip install epic7-bot
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