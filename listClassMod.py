import ioMod as io
import editMod as ed


PINK = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[0;31m'
WHITE_ON_RED = '\033[0;37;41m'
WHITE_ON_RED2 = '\033[101;97m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
MAGENTA = '\033[1;35m'

class List:

    # Constructor
    def __init__(self, fpath):
        self.fpath = fpath
        self.list = []
        self.load_list()
        self.changed = False

    # Destructor
    def __del__(self):
        if self.changed:
            answer = input("Save your changes? y/n: ")
            if answer == "y":
                self.save_list()

    def modify_sublist(self, mod_no, prompts, allowed_symbols_tpl):
        # Creating a new Sublist
        mod_sublist = []
        mod_sublist.append(mod_no)
        for index in range(1,len(prompts)):
            item = ed.edit_item(prompts[index], allowed_symbols_tpl[index])
            if item == 'q':
                break
            mod_sublist.append(item)

        if item != 'q':
            # suche den Index
            for index, sublist in enumerate(self.list):
                if sublist[0] == mod_no:
                    self.list[index] = mod_sublist
                    self.changed = True
                    break
        return mod_no

    def edit_list(self, prompts, allowed_symbols_tpl):
        while True:
            sublist = []
            for index, prompt in enumerate(prompts):
                if index == 0: # Id-Vergabe
                    # bookid = Las list element for (id-number + 1)
                    if len(self.list) == 0:
                        item = "001"
                    else:
                        bookid = int(self.list[-1][0]) + 1
                        item = f"{bookid:>03}"
                    sublist.append(item)
                    continue
                item = ed.edit_item(prompt, allowed_symbols_tpl[index])
                if item == 'q':
                    break
                sublist.append(item)
            if item == 'q':
                break
            self.list.append(sublist)
            self.changed = True

    def print_list(self, format_tpl, headers):
        formatStr = ""
        for index, header in enumerate(headers):
            if format_tpl[index] == 0:
                continue
            formatStr += f"{header:{format_tpl[index]}}"
        print(formatStr)
        # draw line after header line
        sum = 0
        for i in format_tpl:
            if i == 0:
                continue
            sum += i
        print(sum * '-')

        for sublist in self.list:
            formatStr = f""
            for index, item in enumerate(sublist):
                if format_tpl[index] == 0:
                    continue
                if index == 2:
                    formatStr += f"{GREEN}"
                item = item[:format_tpl[index]-1]
                formatStr += f"{item:{format_tpl[index]}}"
                formatStr += f"{ENDC}"
            print(formatStr)

    def load_list(self):
        file = io.fopen(self.fpath,"r")
        if file:
            for line in file:
                line = line[:-1]
                sublist = line.split(sep=",")
                self.list.append(sublist)
            file.close()

    def save_list(self):
        file = io.fopen(self.fpath, "w")
        for sublist in self.list:
            formatStr = f""
            for item in sublist:
                formatStr += f"{item},"
            formatStr = formatStr[:-1] + '\n'
            file.write(formatStr)
        file.close()
        self.changed = False

    def del_sublist(self,del_no):
        deleted_sublist = False
        if int(self.list[-1][0]) >= int(del_no):
            # looks for id in file
            for index, sublist in enumerate(self.list):
                if sublist[0] == del_no:
                    # self.list.pop deletes the item
                    deleted_sublist = self.list.pop(index)
                    break
        return deleted_sublist