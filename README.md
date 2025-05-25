# Oblivion Remastered CVars

This repository contains Unreal Engine 5 console variable dumps for different graphics settings and template ini-files to generate custom graphics settings.

## TL;DR

- [All CVars table](all-0-normalized.csv) with values at LOW settings
- All CVars affected by graphics settings in the `Engine.ini` format:
  - [Full list](GatheredQualitySettings.ini)
  - [Deduplicated list](DeduplicatedQualitySettings.ini)

## Dumps

There are some different dumps:

- `all-groups/cvars-all-{quality_level}.csv` files contain dumps for overall quality level (HWRT disabled)
- `all-groups/cvars-scalability-{quality_level}.csv` files contain only variables set by scalability. They were produced by a simple text filtering (`cat cvars-all-{quality_level}.csv | grep ",Scalability"`)
- `by-group/all-0.csv` is dumped for all low settings
- `by-group/{group}-{quality_level}.csv` files contain dumps when only one setting is changed from low
- `all-0-normalized.csv` - crated from `by-group/all-0.csv` but with normalized values to properly display in Github UI (value commas replaced with semicolons)

## Engine.ini Templates

The `gather.py` script collects variables set by different quality levels and outputs them in the `ini` format. Every entry has the format: `Variable.Name=LOW; (LOW/MEDIUM/HIGH/ULTRA)`.

Script output is saved as `GatheredQualitySettings.ini`. But because of the game scalability group configuration it contains duplicated entries in different categories.

The `DeduplicatedQualitySettings.ini` is a cleaned output version (without duplicated variables and scalability group settings).
It gives a good overview of actual quality settings and can be used as a template for custom graphics settings.

Files are produced with these commands:
```
./gather.py > GatheredQualitySettings.ini
./gather.py tidy > DeduplicatedQualitySettings.ini
```

### Duplicated CVars

These variables are defined in multiple categories. Set them in your custom `Engine.ini` to have expected values.

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

## Virtuos CVars

Full list of Virtuos custom CVars and values for all-low settings.

```csv
vts.AdditiveFOVBias,6,Constructor
Vts.anim.OBAT.FarFrameOffset,60,Scalability
Vts.anim.OBAT.Level,1,Scalability
Vts.anim.OBAT.NearFrameOffset,10,Scalability
Vts.anim.OBAT.RadiusThreshold,0.1,Constructor
Vts.anim.OBAT.Tolerance,1.1,Constructor
vts.Animation.CameraControl.Enable,true,Constructor
vts.Camera.VanityTimeToActivate,120,Constructor
vts.ClothQuality,0,Scalability
vts.ForceTextureStreamingInFadeToGame,true,Constructor
vts.grass.ControlPoints.InGroundDistanceToDiscard,-70,Constructor
vts.LastFramePreExposure,1,Constructor
vts.LightRig.ApplyBetterShadowResolutionInDialogue,true,Constructor
vts.LightRig.EnableMaxRoughnessToTrace,true,Constructor
vts.LightRig.EnableShadowResolutionLodBiasLocal,false,Constructor
vts.LightRig.ForceLightIntensityBasedOnExposure,-1,Constructor
vts.LightRig.MaxRoughnessToTrace,0.15,Constructor
vts.LightRig.OverrideFallOffIntensityFactor,0,Constructor
vts.LightRig.OverrideTimeBeforeDelete,0,Constructor
vts.LightRig.OverrideTimeToReachIntensity,0,Constructor
vts.LightRig.PreExposureMax,0.06,Constructor
vts.LightRig.PreExposureMin,0.045,Constructor
vts.LightRig.ShadowResolutionLodBiasLocal,1,Constructor
vts.Lumen.Reflections.RaycastTranslucent,1,Scalability
vts.Lumen.ScreenProbeGather.RaycastTranslucent,1,Scalability
vts.Lumen.ScreenTraceIntensityScale,1,Constructor
vts.LumenDebugPostprocessValues,false,Constructor
vts.LumenFinalGatherQuality.Max,100,Constructor
vts.LumenFinalGatherQuality.Scale,1,Constructor
vts.LumenSceneLightingQuality.Max,7,Constructor
vts.LumenSceneLightingQuality.Scale,1,Constructor
vts.MergedSkeletalMesh.Cache.Enable,true,Constructor
vts.MergedSkeletalMesh.Cache.LookupCleanupFactor,1.5,Constructor
vts.MergedSkeletalMesh.Cache.MaxHistoryPerComponent,3,Constructor
vts.MergedSkeletalMesh.Cache.MaxParallelTasks,2,Constructor
vts.MergedSkeletalMesh.Cache.MaxRememberUnusedComponent,5,Constructor
vts.MergedSkeletalMesh.StripLODs,0,Constructor
vts.Nanite.MaxWPOScale,0.1,DeviceProfile
vts.NaniteCulling.MaxWPOScale,0.1,DeviceProfile
Vts.Optim.SkletalMeshOcclusionOptim.DefaultDeltatime,0.016,Constructor
Vts.Optim.SkletalMeshOcclusionOptim.Enabled,true,Constructor
Vts.Optim.SkletalMeshOcclusionOptim.VisibleTickRate,0,Constructor
VTS.PawnvPawnInterationDebugClearInterval,1,Constructor
vts.PSOShowRoom.ActorsLocationZ,10,Constructor
vts.PSOShowRoom.ActorsRotationYaw,90,Constructor
vts.SceneColorExtractionBeforeTranslucency,1,Constructor
vts.ShaderLoadingScreen.BatchNum,10,Constructor
vts.ShaderLoadingScreen.BatchSize,200,Constructor
vts.ShaderLoadingScreen.PrecompileTaskProgressWeight,0.8,DeviceProfile
vts.ShaderLoadingScreen.ProgressBarDelay,1,Constructor
VTS.ShowPawnPhysicsInteractionDebug,false,Constructor
vts.SkyLight.CubemapResolution,512,Scalability
vts.SSS.ForegroundDistance,70,Constructor
vts.SSS.ForegroundTransition,10,Constructor
vts.SSS.ForegroundWorldUnitGlobalScale,1,Code
vts.SSS.WorldUnitGlobalScale,1,Constructor
vts.steamDeck.FloatingKeyboardDefaultTextLocationX,100,Constructor
vts.steamDeck.FloatingKeyboardDefaultTextLocationY,100,Constructor
vts.steamDeck.FloatingKeyboardScreenAvoidRatio,3,Constructor
```
