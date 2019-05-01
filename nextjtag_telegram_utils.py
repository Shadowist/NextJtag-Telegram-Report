CONFIG_FILE = "nextjtag_telegram.cfg"

def receive_cfg():
    '''Reads and saves the config file into a dictionary'''
    output_dict = {}

    with open(CONFIG_FILE) as f:
        for line in f.readlines():
            if '#' not in line and line.strip():
                parsed_line = line.replace(' ', '').rstrip('\n').split('=')
                if parsed_line[1].title() == "True":
                    parsed_line[1] = True
                elif parsed_line[1].title() == "False":
                    parsed_line[1] = False
                output_dict[parsed_line[0]] = parsed_line[1]
    return output_dict

def show_commands():
    '''Returns a string with the list of commands'''

    text = "The following commands are supported:\n"
    text += "1. /start\n"
    text += "2. /devices\n"
    text += "3. /report\n"
    text += "4. /help\n"

    return text
    
