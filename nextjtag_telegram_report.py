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
        data = subprocess.check_output(["nextjtag", "-a", "-t", "-v"]).decode("utf-8")
        data = data.split("\r\n")[1:-1]
        tempList = []

        for entry in data:
            tempList.append(entry.split("] ")[1].replace(": ", "\n").replace(", ", "\n") + "\n\n")
        output = "".join(tempList)

    return output
