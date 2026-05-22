from libqtile import hook
from os.path import expanduser
from subprocess import Popen


from keys import keys
from groups import groups, keys as group_keys

from groups import groups
from layouts import layouts
from screens import screens
from mouse import mouse
from floating import floating_layout

mod = "mod1"
terminal = "ghostty"
keys.extend(group_keys)

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=14,
    padding=4,
)

extension_defaults = widget_defaults.copy()


@hook.subscribe.startup_once
def startup():
    Popen(expanduser("~/.config/qtile/startup.sh"))


dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = False
bring_front_click = "floating_only"
floats_kept_above = True
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "LG3D"