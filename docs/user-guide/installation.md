# Installation

A detailed guide.

---

## Requirements

- [Python 3.4+]
- [Chocolatey]
- [Android Debug Bridge]


## Install Python

Visit [Python install page](https://www.python.org/downloads/release/python-392/).

Install the windows installer one.

![Windows Installer](../img/windows-installer.png)


## Installing Chocolatey
[Chocolatey] is a package manager for windows. It is easier to install all the requirements by using it.

Visit [Chocolatey install page].

## Installing Android Debug Bridge
[Android Debug Bridge] is command-line tool that enable communication with a device. The bot uses it to
sent click inputs to the screen.

Install via [Chocolatey].

```console
$ choco install adb
```

## Install Epic7 Bot
To install Epic7 Bot, run the following command from the command line:

```bash
pip install epic7-bot
```



[Chocolatey]: https://chocolatey.org/
[Chocolatey install page]: https://chocolatey.org/install
[Android Debug Bridge]: https://community.chocolatey.org/packages/adb
[Python 3.4+]: https://www.python.org/downloads/release/python-392/
