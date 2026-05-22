from libqtile import bar, widget
from libqtile.config import Screen
from libqtile import widget, hook
import os
import subprocess

colors = {
    "bg": "#1e1e2e",
    "fg": "#cdd6f4",
    "blue": "#89b4fa",
    "target": "#D93514",
    "vpn": "#008000"
}


def get_vpn():
    ip = subprocess.check_output("ip addr show ens33 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1", shell=True).decode().strip()

    return ip 

def get_target():
    try:
        with open(os.path.expanduser("~/.config/qtile/target.txt")) as target:
            result = target.read().strip()
            return result
    except FileNotFoundError:
        return "No target"

screens = [
    Screen(
        top=bar.Bar(
            [
                # ARCH LOGO
                widget.TextBox(
                    text="󰣇",
                    fontsize=22,
                    foreground=colors["blue"],
                    padding=12,
                    name = "arch_logo",
                ),

                # WINDOW TITLE
                widget.WindowName(
                    fmt ="󰖯  {}",
                    max_chars=50,
                    foreground=colors["fg"],
                    padding=10,
                ),

                # SPACER LEFT
                widget.Spacer(),

                # WORKSPACES
                widget.GroupBox(
                    active=colors["blue"],
                    inactive="#6c7086",
                    highlight_method="text",
                    this_current_screen_border=colors["blue"],
                    disable_drag=True,
                    rounded=False,
                    fontsize=18,
                    padding=8,
                    margin_y=4,
                    margin_x=2,
                    borderwidth=0,

                    # ICONOS
                    fmt="{}",
                ),

                # SPACER RIGHT
                widget.Spacer(),

                # SYSTEM TRAY
                widget.Systray(
                    icon_size=16,
                    padding=8,
                ),
                
                widget.GenPollText(
                    fmt = "󰒍 {}",
                    func = get_vpn,
                    foreground = colors["vpn"],
                    update_interval = 5
                ),

                widget.GenPollText(
                    fmt = "󰓾 {}",
                    func = get_target,
                    foreground = colors["target"],
                    update_interval = 5
                ),
                # CLOCK
                widget.Clock(
                    format="󰥔  %H:%M:%S",
                    foreground=colors["fg"],
                    padding=12,
                ),
            ],
            28,
            background=colors["bg"],
            margin=0,
        ),
    ),
]