import multiprocessing
import epic7_bot.cli as cli
import os

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn", force=True)
    multiprocessing.freeze_support()
    # os.environ['SYSTEMROOT'] = "C:\\Users\\kurtzs\\work\\epic7_bot"
    cli.main()
