from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but they might need fine-tuning.
build_exe_options = {
    "excludes": [],
    "zip_include_packages": ["bcrypt", "prompt_toolkit", "wcwidth", "alive-progress", "cx-Freeze"],
}

setup(
    name="VAIIYA Terminal",
    version="11.1.11",
    description="VAIIYA Terminal is a fictional terminal-like tool for VAIIYA, in the world of THE FINALS.",
    options={"build_exe": build_exe_options},
    executables=[Executable("VAIIYA_terminal.py", base="console")],
)