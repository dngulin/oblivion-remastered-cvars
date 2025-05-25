#!/usr/bin/env python3

import sys

tidy = len(sys.argv) > 1 and sys.argv[1] == "tidy"

tidy_key_groups = {
    "r.AOQuality": "postprocessing",
    "r.Lumen.Reflections.ScreenTraces": "reflection",
    "r.SSR.Quality": "reflection",
}

def index(file_path):
    lines = open(file_path, "r").readlines()
    result = {}
    for i in range(len(lines)):
        columns = lines[i].split(",")
        key = columns[0]
        value = columns[1]
        result[key] = value
    return result

def get_diff_keys(a, b, group):
    result = []
    for k, v in a.items():
        if k == "r.SetRes":
            continue

        if tidy and k in tidy_key_groups and tidy_key_groups[k] != group:
            continue
        if tidy and k.startswith("r.DOF.") and group != "postprocessing":
            continue
        if tidy and k.startswith("sg.") or k.startswith("Altar.GraphicsOptions."):
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

printed_keys = set()

for group, levels in groups:
    sg = [settings_low]
    diff_key_set = set()

    for level in range(1, levels):
        settings = index(f"by-group/{group}-{level}.csv")
        sg.append(settings)
        diff_keys = get_diff_keys(settings_low, settings, group)
        diff_key_set.update(diff_keys)

    if len(diff_key_set) > 0:
        print(f"; Quality setting: {group}")

    for key in sorted(diff_key_set):
        dup_flag = "[duplicated] " if tidy and key in printed_keys else ""
        printed_keys.add(key)

        if len(sg) == 4:
            values = [sg[0][key], sg[1][key], sg[2][key], sg[3][key]]
            print(f"{key}={values[0]}; {dup_flag}({values[0]}/{values[1]}/{values[2]}/{values[3]})")
        else:
            values = [sg[0][key], sg[1][key]]
            print(f"{key}={values[0]}; {dup_flag}({values[0]}/{values[1]})")

    if len(diff_key_set) > 0:
        print()
