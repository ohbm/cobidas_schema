"""Prepare labels for LabelBuddy based on the items of a Reproshema activity."""

import json
from pathlib import Path

from rich import print

protocol = "eyetracking"

colors = [
    "#a6cee3",
    "#1f78b4",
    "#b2df8a",
    "#33a02c",
    "#fb9a99",
    "#e31a1c",
    "#fdbf6f",
    "#ff7f00",
    "#cab2d6",
    "#6a3d9a",
    "#ffff99",
    "#b15928",
]

root = Path(__file__).parent.parent

label_folder = root / "labels" / protocol
label_folder.mkdir(exist_ok=True, parents=True)

schema_folder = root / "schemas"
protocol_file = schema_folder / protocol / "protocols" / f"{protocol}_schema.jsonld"

protocol_label_file = label_folder / f"{protocol}_labels.jsonl"
protocol_label_file.unlink(missing_ok=True)

with open(protocol_file) as f:
    protocol_json = json.load(f)

activities_order = protocol_json["ui"]["order"]

for i, activity in enumerate(activities_order):

    activity_file = protocol_file.parent / activity

    activity_name = activity_file.stem.replace("_schema", "")
    print(f" Processing activity {activity_name}")

    activity_color = colors[i]

    activity_label_file = label_folder / (f"{i}_{activity_name}_labels.jsonl")
    activity_label_file.unlink(missing_ok=True)

    with open(activity_file) as f:
        activity_json = json.load(f)

    items_order = activity_json["ui"]["order"]

    for item in items_order:

        with open(activity_file.parent / item) as f:
            item_json = json.load(f)

        question = item_json["question"]["en"]
        # remove anything after <div>
        if "<div" in question:
            question = question.split("<div")[0]
        print(question)

        with open(activity_label_file, "a") as output_f:
            output_f.write(f'{{"name": "{question}", "color": "{activity_color}"}}\n')
        with open(protocol_label_file, "a") as output_f:
            output_f.write(f'{{"name": "{question}", "color": "{activity_color}"}}\n')
