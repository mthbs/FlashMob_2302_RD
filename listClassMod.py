
import os
import ioMod as io
import editMod as ed
import pickle


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
        pass

    def get_changed_status(self):
        return self.changed

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

    def print_list(self, format_tpl, show_tpl, headers):
        formatStr = ""
        for x in range(len(show_tpl)):
            if format_tpl[x] == 0:
                continue
            formatStr += f"{headers[show_tpl[x]]:{format_tpl[show_tpl[x]]}}"
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
            for x in range(len(show_tpl)):
                if format_tpl[x] == 0:
                    continue
                item = sublist[show_tpl[x]][:format_tpl[show_tpl[x]]-1]
                formatStr += f"{item:{format_tpl[show_tpl[x]]}}"
            print(formatStr)

    def import_list(self):
        self.list = []
        filename, file_extension = os.path.splitext(self.fpath)
        filename += ".csv"
        print(f"{filename} successful imported")
        file = io.fopen(filename, "r")
        if file:
            for line in file:
                line = line[:-1]
                sublist = line.split(",")
                self.list.append(sublist)
            file.close()

    def load_list(self):
        try:
            file = io.fopen(self.fpath, "rb")
            self.list = pickle.load(file)
            file.close()
        except:
            self.list = []

    def export2csv_list(self):
        filename, file_extension = os.path.splitext(self.fpath)
        filename += ".csv"
        print("filename:", filename)
        file = io.fopen(filename, "w")
        for sublist in self.list:
            formatStr = f""
            for item in sublist:
                formatStr += f"{item},"
            formatStr = formatStr[:-1] + '\n'
            file.write(formatStr)
        file.close()
        self.changed = False

    def save_list(self):
        file = io.fopen(self.fpath, "wb")
        pickle.dump(self.list, file)
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