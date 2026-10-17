enigma2-display-skins
=====================

This git contains skins for the STB display (VFD/LCD)

### DAB and RDS radio display

All display skins include `RdsInfoDisplaySummary` for the current OpenATV
radio-display integration. It shows the station name and scrolling RDS/DLS
text, falling back to the service's RTP information when no radio text is
available. Ordinary DVB radio without RDS keeps its normal summary.

Color LCD skins also support the DAB settings for radio text, slideshow
with station-logo fallback, or station logo only. These modes are independent
of the TV slideshow setting. Monochrome display skins use text only.

The summary uses the existing `station` and `message` sources and the optional
`picture` widget. Enigma2 controls image visibility and aspect-ratio-preserving
decoding; skins must not force the picture visible with a converter. Clock and
recording indicators are retained where space permits. The summary is hidden
when menus, movie playback or standby take over the receiver display.
