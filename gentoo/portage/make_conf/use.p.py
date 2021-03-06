collections = [ "USE_UNWANTED", "USE_OPTIMIZE", "USE_LANGUAGES",
"USE_HARDWARE", "USE_ADDONS", "USE_FEATURES",
"USE_NETWORK", "USE_COMPRESSION", "USE_ARCH", ]

inpdevs = [ "evdev" ]

if "desktop" in options.tags:
    collections += ["USE_X", "USE_DESKENV",
                    "USE_MEDIA", "USE_DESKDEVS", ]
if "laptop" in options.tags:
    collections.append("USE_LAPTOP")
    inpdevs.append("synaptics")

use = [ "${%s}" % flag for flag in collections ]

text("""# $warning
USE="$use"
INPUT_DEVICES="$inpdevs"
VIDEO_CARDS="radeon vesa dummy none"
NUT_DRIVERS="usbhid-ups"
SANE_BACKENDS=""
CAMERAS="ptp2"
""").render(use=" ".join(use), inpdevs=" ".join(inpdevs))
