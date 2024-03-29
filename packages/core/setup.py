from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


setup(
    name="epic7_bot",
    version="1.0.3",
    description="Epic7 Bot used via cli",
    author="brunocordioli072",
    packages=["epic7_bot"].extend(find_packages("epic7_bot")),
    package_data={"": ["images/**/*.png"]},
    include_package_data=True,
    install_requires=[
        "numpy ==1.23.2",
        "opencv_python ==4.6.0.66",
        "pure_python_adb ==0.3.0.dev0",
        "docopt ==0.6.2",
        "python-dotenv ==0.21.0",
        "psutil ==5.9.3",
        "pywebview ==4.3.2",
    ],
)
