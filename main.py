"""
* Name : Maxim Neumann
* Date created: 20230207
* main.py
* Purpose: Program for editing
*          books
*
* Revision:  20230207
* History:
*
*  Date       Author        Ref     Revision
*  20230207   mneumann      1       Erste Version
"""
# import listClassMod
# from listClassMod import *
import listClassMod as lc
import cfgMod as cfg
import os

def load_config(cfgpath):
    fpath = cfg.readCfg("$FPATH:", cfgpath)[0]
    headers = cfg.readCfg("$HEADERS:", cfgpath)
    prompts = cfg.readCfg("$PROMPTS:", cfgpath)
    for i in range(len(prompts)):
        prompts[i] += " "
    allowed_symbols_tpl = cfg.readCfg("$SYMBOLS:", cfgpath)
    format_lst = cfg.readCfg("$FORMAT:", cfgpath)
    for i in range(len(format_lst)):
        format_lst[i] = int(format_lst[i])
    format_tpl = tuple(format_lst)

    return fpath, headers, prompts, allowed_symbols_tpl, format_tpl

def openDB(default_tpl):
    prompt = "Enter filename: "
    cfgpath = input(prompt)
    if os.path.exists(cfgpath):
        fpath, headers, prompts, allowed_symbols_tpl, format_tpl = load_config(cfgpath)
        return fpath, headers, prompts, allowed_symbols_tpl, format_tpl
    else:
        return default_tpl

def delete_entry():
    prompt = "Enter number to delete: "
    while True:
        del_no = input(prompt)
        if del_no == "q":
            break
        if del_no.isdigit():
            deleted_sublist = lco.del_sublist(f"{del_no:>03}")
            if not deleted_sublist:
                print(f"Could not delete {del_no}")
            else:
                print(f"{deleted_sublist[0]}, {deleted_sublist[1]} deleted")
            break
        else:
            prompt = "Enter a valid number please: "

def modify_entry():
    prompt = "Enter number to modify: "
    while True:
        mod_no = input(prompt)
        if mod_no == "q":
            break
        if mod_no.isdigit():
            modified = lco.modify_sublist(f"{mod_no:>03}", prompts, allowed_symbols_tpl)
            break
        else:
            prompt = "Enter a valid number please: "

# ------------------------------- start program ----------------------------------------

cfgpath="./bookDB.cfg"
fpath, headers, prompts, allowed_symbols_tpl, format_tpl = load_config(cfgpath)
default_tpl = fpath, headers, prompts, allowed_symbols_tpl, format_tpl

lco = lc.List(fpath)

menu = "show books 'l'\n" \
       "edit books 'e'\n" \
       "change book'm'\n" \
       "save books 's'\n" \
       "del. book  'd'\n" \
       "open DB    'o'\n" \
       "exit       'x'\n"

while True:
    print(menu)
    prompt = "select: "
    choice = input(prompt)

    if choice == 'l':
        lco.print_list(format_tpl, headers)
    if choice == 'e':
        lco.edit_list(prompts, allowed_symbols_tpl)
    if choice == 'm':
        modify_entry()
    if choice == 's':
        lco.save_list()
    if choice == 'd':
        delete_entry()
    if choice == 'o':
        fpath, headers, prompts, allowed_symbols_tpl, format_tpl = openDB(default_tpl)
        default_tpl = fpath, headers, prompts, allowed_symbols_tpl, format_tpl
        print(fpath)
        if fpath:
            lco = lc.List(fpath)
    if choice == 'x':
        break

if __name__ == '__main__': # Wird nur ausgeführt, wenn diese Datei als Main aufgerufen wird, Wird nur zum Testen verwendet
    # Ánstatt Test-Klassen
    # Beim importieren spielt der Code im Block keine Rolle
    pass
