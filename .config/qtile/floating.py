from libqtile import layout
from libqtile.config import Match

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,

        Match(wm_class="pavucontrol"),
        Match(wm_class="blueman-manager"),
        Match(title="pinentry"),
    ]
)