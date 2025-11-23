def copy_file(command: str) -> None:
    list_com = command.split()
    if len(list_com) < 3:
        return
    if list_com[0] != "cp":
        return
    if list_com[1] == list_com[2]:
        return
    try:
        with (open(list_com[1],
                   "r",
                  newline="",
                  encoding="utf-8") as f_r,
              open(list_com[2],
                   "w",
                   newline="",
                   encoding="utf-8") as f_w):
            for line in f_r:
                f_w.write(line)
    except FileNotFoundError:
        return
