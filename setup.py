from cx_Freeze import setup, Executable

executables = [Executable("Pandora.py")]

setup(
    name="Pandora",
    version="1.0",
    description="Dial Up",
    executables=executables
)
