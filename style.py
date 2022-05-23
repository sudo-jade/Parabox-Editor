import imgui

def set(style: imgui.core.GuiStyle):
    io = imgui.get_io()
    imgui.style_colors_dark(style)
    style.colors[imgui.COLOR_BORDER] = (0,0,0,0)
    style.colors[imgui.COLOR_WINDOW_BACKGROUND] = (0,0,0,1)
    style.colors[imgui.COLOR_TITLE_BACKGROUND] = (0.353,0,0.212,1)
    style.colors[imgui.COLOR_TITLE_BACKGROUND_COLLAPSED] = (0.353,0,0.212,1)
    style.colors[imgui.COLOR_TITLE_BACKGROUND_ACTIVE] = (0.7,0,0.42,1)
    style.colors[imgui.COLOR_BUTTON_HOVERED] = (0.7,0,0.42,1)
    style.colors[imgui.COLOR_BUTTON_ACTIVE] = (1,1,1,1)
    style.colors[imgui.COLOR_BUTTON] = (0.353,0,0.212,1)
    style.colors[imgui.COLOR_FRAME_BACKGROUND] = (0.1,0.1,0.1,1)
    style.colors[imgui.COLOR_FRAME_BACKGROUND_ACTIVE] = (0.05,0.05,0.05,1)
    style.colors[imgui.COLOR_FRAME_BACKGROUND_HOVERED] = (0.15,0.15,0.15,1)
    style.colors[imgui.COLOR_POPUP_BACKGROUND] = (0,0,0,1)
    style.colors[imgui.COLOR_CHECK_MARK] = (1,1,1,1)
    style.colors[imgui.COLOR_HEADER] = (0.353,0,0.212,1)
    style.colors[imgui.COLOR_HEADER_ACTIVE] = (0.7,0,0.42,1)
    style.colors[imgui.COLOR_HEADER_HOVERED] = (0.7,0,0.42,1)
    style.colors[imgui.COLOR_RESIZE_GRIP] = (1,1,1,0.4)
    style.colors[imgui.COLOR_RESIZE_GRIP_HOVERED] = (1,1,1,1)
    style.colors[imgui.COLOR_RESIZE_GRIP_ACTIVE] = (1,1,1,1)
    style.colors[imgui.COLOR_TEXT_SELECTED_BACKGROUND] = (1,1,1,0.3)
    style.colors[imgui.COLOR_MENUBAR_BACKGROUND] = (0,0,0,1)
    style.window_rounding = 0