access_log = open("./generators-uk/access-log")

each_line = (line.rsplit(None, 1)[1] for line in access_log)

last_col = (int(col) for col in each_line if col != '-')

if __name__ == '__main__':
    print sum(last_col) / 1024 /1024