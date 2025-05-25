# Oblivion Remastered CVars

This repository contains Unreal Engine 5 console variable dumps for different graphics settings and template ini-files to generate custom graphics settings.

## Dumps

There are some different dumps:

- `all-groups/cvars-all-{quality_level}.csv` files contain dumps for overall quality level (HWRT disabled)
- `all-groups/cvars-scalaility-{quality_level}.csv` files contain only variables set by scalability. They were produced by a simple text filtering (`cat cvars-all-{quality_level}.csv | grep ",Scalability"`)
- `by-group/all-0.csv` is dumped for all low settings
- `by-group/{group}-{quality_level}.csv` files contain dumps when only one setting is changed from low

## INI Templates

The `gather.py` script collects variables set by different quality levels and outputs them in the `ini` format. Every entry has the format: `Variable.Name=LOW; (LOW/MEDIUM/HIGH/ULTRA)`.

Script output is saved as `GatheredQualitySettings.ini`. But because of the game scalaility group configuration it contains duplicated entries in different categories.

The `DeduplicatedQualitySettings.ini` is a cleaned output version (without duplicated variables and scalability group settings).
It gives a good overview of actual quality settings and can be used as a template for custom graphics settings.

Files are produced with these commands:
```
./gather.py > GatheredQualitySettings.ini
./gather.py tidy > DeduplicatedQualitySettings.ini
```

### Duplicated CVars

Theese variables are defined in multiple categories. It is better to set them in your custom `Engine.ini` to have expected values.

```ini
r.AOQuality=1; gi, texture, reflection, postprocessing, hair, cloth, swrt: (1/2/2/2)
r.Lumen.Reflections.ScreenTraces=1; reflection: (1/1/0/0); postprocessing, hair, cloth, (1/0/0/0); swrt: (1/0)
r.SSR.Quality=0; ssr: (0/1); reflection: (0/0/2/3)
r.DOF.Gather.AccumulatorQuality=0; postprocessing: (0/0/0/1); hair, cloth: (0/1/1/1); swrt: (0/1)
r.DOF.Gather.PostfilterMethod=2; postprocessing, hair, cloth: (2/1/1/1); swrt: (2/1)
r.DOF.Gather.RingCount=3; postprocessing: (3/3/4/4); hair, cloth: (3/4/4/4); swrt: (3/4)
r.DOF.Kernel.MaxBackgroundRadius=0.006; postprocessing: (0.006/0.006/0.012/0.025); hair, cloth: (0.006/0.025/0.025/0.025); swrt: (0.006/0.025)
r.DOF.Kernel.MaxForegroundRadius=0.006; postprocessing: (0.006/0.006/0.012/0.025); hair, cloth: (0.006/0.025/0.025/0.025); swrt: (0.006/0.025)
r.DOF.Recombine.Quality=0; postprocessing: (0/0/0/1); hair, cloth: (0/1/1/1); swrt: (0/1)
r.DOF.Scatter.BackgroundCompositing=0; postprocessing: (0/0/1/2); hair, cloth: (0/2/2/2); swrt: (0/2)
r.DOF.Scatter.ForegroundCompositing=0; postprocessing: (0/0/1/1); hair, cloth: (0/1/1/1); swrt: (0/1)
r.DOF.TemporalAAQuality=0; postprocessing: (0/0/0/1); hair, cloth: (0/1/1/1); swrt: (0/1)
```
