from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="epic7_bot",
    version="1.0.0",
    description="Epic7 Bot used via cli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="brunocordioli072",
    packages=["epic7_bot"].extend(find_packages("epic7_bot")),
    package_data={'': ['images/*.png']},
    include_package_data=True,
    install_requires=["numpy ==1.23.2",
                      "opencv_python ==4.6.0.66",
                      "pure_python_adb ==0.3.0.dev0",
                      "docopt"],
    entry_points={
        "console_scripts": [
            "epic7=epic7_bot.cli:main",
        ],
    },
)
