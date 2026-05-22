from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod1"
terminal = "ghostty"

keys = [
    # Movimiento
    Key([mod], "left", lazy.layout.left()),
    Key([mod], "right", lazy.layout.right()),
    Key([mod], "up", lazy.layout.down()),
    Key([mod], "down", lazy.layout.up()),

    # Mover ventanas
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Resize
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),

    # Apps
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "f", lazy.spawn("rofi -show drun")),

    # Layouts
    Key([mod], "Tab", lazy.next_layout()),
    #Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "c", lazy.window.kill()),

    # Qtile
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),

    # Floating
    Key([mod], "t", lazy.window.toggle_floating()),

    # Screenshot
    Key([], "Print", lazy.spawn("grimshot save area ~/Pictures/screenshot.png")),

    # Audio
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+")),

    Key([], "XF86AudioLowerVolume",
        lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-")),

    Key([], "XF86AudioMute",
        lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle")),
]