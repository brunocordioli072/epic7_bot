import multiprocessing
import epic7_bot.cli as cli

multiprocessing.set_start_method("spawn", force=True)

if __name__ == "__main__":
    cli.main()
