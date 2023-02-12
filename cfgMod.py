import ioMod as io


def readCfg(id, cfgpath):
    file = io.fopen(cfgpath, "r")
    lst = []
    tag = False
    for line in file:
        if tag:
            if ("$END") in line:
                break
            if '|' in line:
                line = tuple(line.split("|"))
            lst.append(line[:-1])
        if id in line:
            tag = True
    return lst


if __name__ == "__main__":
    fpath = "bookDB.cfg"

    prompts = readCfg("$PROMPTS:",fpath)
    print(prompts)

    path = readCfg("$FPATH:",fpath)
    print(path)

    format_tpl = readCfg("$FORMAT:",fpath)
    print(format_tpl)

    symbols = readCfg("$SYMBOLS:",fpath)
    print(symbols)

    headers = readCfg("$HEADERS:",fpath)
    print(headers)