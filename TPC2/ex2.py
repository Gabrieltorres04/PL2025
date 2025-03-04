
def read_csv_rows(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        header = f.readline().rstrip("\n")
        row = ""
        for line in f:
            row += line
            # Verificar numero par de "
            if row.count('"') % 2 == 0:
                yield row.rstrip("\n")
                row = ""
        if row:
            yield row.rstrip("\n")


def parse_csv_line(line):
    fields = []
    field = ""
    in_quotes = False
    i = 0
    while i < len(line):
        ch = line[i]
        if in_quotes:
            if ch == '"':
                if i + 1 < len(line) and line[i + 1] == '"':
                    field += '"'
                    i += 1
                else:
                    in_quotes = False
            else:
                field += ch
        else:
            if ch == '"':
                in_quotes = True
            elif ch == ';':
                fields.append(field)
                field = ""
            else:
                field += ch
        i += 1
    fields.append(field)
    return fields


def parse_obras(filepath):
    compositores = []
    obras_por_periodo = {}
    for row in read_csv_rows(filepath):
        row = row.rstrip("\n")
        if not row:
            continue
        fields = parse_csv_line(row)
        if len(fields) < 7:
            print("skipped row: ", row)
            continue  
        if fields[3] not in obras_por_periodo:
            obras_por_periodo[fields[3]] = []
        if fields[0] not in obras_por_periodo[fields[3]]:
            obras_por_periodo[fields[3]].append(fields[0])      
        if fields[4] not in compositores:
            compositores.append(fields[4])
    return compositores, obras_por_periodo


if __name__ == "__main__":
    filepath = "PL2025-A104169/TP2/obras.csv"
    compositores, obras = parse_obras(filepath)
    compositores.sort()
    print("Compositores:", compositores)
    print("Obras por periodo:",obras)
    