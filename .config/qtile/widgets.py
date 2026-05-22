from libqtile import widget

widgets = [
    widget.CurrentLayout(),
    widget.GroupBox(
        highlight_method="line",
        this_current_screen_border="#89b4fa",
    ),
    widget.Prompt(),
    widget.WindowName(),
    widget.CPU(),
    widget.Memory(),
    widget.Clock(format="%a %d %b %H:%M"),
]