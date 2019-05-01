# Standard Import
import subprocess

# Report General
def report(arg):
    """Gets the temperature and voltage readings from NextJtag."""

    # Call "nextjtag -t -v"
    # Read the input back
    if arg == "devices":
        return subprocess.check_output(["nextjtag"]).decode("utf-8")
    elif arg == "general":
        return subprocess.check_output(["nextjtag", "-a", "-t", "-v"]).decode("utf-8")

    return output
