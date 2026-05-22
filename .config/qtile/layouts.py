from libqtile import layout

layouts = [
    layout.MonadTall(
        margin=6,
        border_width=2,
        border_focus="#89b4fa",
        border_normal="#313244",
    ),

    layout.Max(),

    layout.Floating(),
]