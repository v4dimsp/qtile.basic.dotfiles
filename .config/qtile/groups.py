from libqtile.config import Group, Key
from libqtile.lazy import lazy

mod = "mod1"

groups = [Group(i) for i in "123456789"]

keys = []

for group in groups:
    keys.extend([
        Key(
            [mod],
            group.name,
            lazy.group[group.name].toscreen(),
        ),

        Key(
            [mod, "shift"],
            group.name,
            lazy.window.togroup(group.name, switch_group=True),
        ),
    ])