import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="main",
    options={
        "build_exe": {"packages": ["pygame","random","math"],
                      "include_files": ["ufo.png", "player1.png", "enemy1.png", "bullet1.png", "background.png"]}},
    description="This is a space game Enjoy my first game",
    executables=executables
)