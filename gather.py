#!/usr/bin/env python3

def index(file_path):
    lines = open(file_path, "r").readlines()
    result = {}
    for i in range(len(lines)):
        columns = lines[i].split(",")
        key = columns[0]
        value = columns[1]
        result[key] = value
    return result

def get_diff_keys(a, b):
    result = []
    for k, v in a.items():
        if k == "r.SetRes":
            continue
        if b[k] != v:
            result.append(k)
    result.sort()
    return result


settings_low = index("by-group/all-0.csv");
groups = [
    ("blur", 2),
    ("ssr", 2),
    ("view-distance", 4),
    ("effects", 4),
    ("foliage", 4),
    ("shadow", 4),
    ("gi", 4),
    ("texture", 4),
    ("reflection", 4),
    ("postprocessing", 4),
    ("hair", 4),
    ("cloth", 4),
    ("swrt", 2),
]

print("[/Script/Engine.RendererSettings]")

for group, levels in groups:
    print(f"; Quality setting: {group}")

    sg = [settings_low]
    diff_key_set = set()

    for level in range(1, levels):
        settings = index(f"by-group/{group}-{level}.csv")
        sg.append(settings)
        diff_keys = get_diff_keys(settings_low, settings)
        diff_key_set.update(diff_keys)

    for key in sorted(diff_key_set):
        if len(sg) == 4:
            values = [sg[0][key], sg[1][key], sg[2][key], sg[3][key]]
            print(f"{key}={values[0]}; ({values[0]}/{values[1]}/{values[2]}/{values[3]})")
        else:
            values = [sg[0][key], sg[1][key]]
            print(f"{key}={values[0]}; ({values[0]}/{values[1]})")

    print()
