
from pathlib import Path

import PyInstaller.__main__

HERE = Path(__file__).parent.absolute()
path_to_main = str(HERE / "main.py")


def main() -> None:
    PyInstaller.__main__.run([
        path_to_main,
        '--onefile',
        '--windowed',
    ])


if __name__ == "__main__":
    main()
