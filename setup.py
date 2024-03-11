from cx_Freeze import setup, Executable

setup(
    name="FoldIT",
    version="1.0",
    description="GUI application to create folder structure",
    executables=[Executable("doit.py", base="Win32GUI")],
)