# Oblivion Remastered CVars

This repository contains Unreal Engine 5 console variable dumps for different graphics settings and template ini-files to generate custom graphics settings.

## Dumps

There are some different dumps:

- `all-groups/cvars-all-{quality_level}.csv` files contain dumps for overall quality level (HWRT disabled)
- `all-groups/cvars-scalaility-{quality_level}.csv` files contain only variables set by scalability. They were produced by a simple text filtering (`cat cvars-all-{quality_level}.csv | grep ",Scalability"`)
- `by-group/all-0.csv` is dumped for all low settings
- `by-group/{group}-{quality_level}.csv` files contain dumps when only one setting is changed from low

## INI Templates

The `gather.py` script collects variables set by different quality levels and outputs them in the `ini` format. Every entry has the format: `Variable.Name=LOW; LOW/MEDIUM/HIGH/ULTRA`.

Script output is saved as `GatheredQualitySettings.ini`. But because of the game scalaility group configuration it contains duplicated entries in different categories.

The `FilteredQualitySettings.ini` is manually cleaned up version of that file. It gives a good overview of actual quality settings and can be used as a template for custom graphics settings.
