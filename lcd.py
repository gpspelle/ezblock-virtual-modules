class LCD1602:
    def __init__(self):
        print(" [.] Created LCD1602")

    def write_line(self, line, data, align='LEFT'):
        print(" [.] Write line", line, data, align)
