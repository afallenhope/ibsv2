import wx

from fallen.bot import FallenBot

APP_EXIT = 1


class MainFrameUI(wx.Frame):

    def __init__(self, parent, title):
        super(MainFrameUI, self).__init__(parent, title=title, size=(300, 200))

        self.Centre()
        self.init_ui()
        self.Show(True)

    def init_ui(self) -> None:
        """ Create a menu """
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        menu_item = wx.MenuItem(file_menu, APP_EXIT, "&Quit\tCTRL+Q")
        menu_item.SetBitmap(wx.Bitmap("resources/images/exit16x16.png"))
        file_menu.Append(menu_item)

        self.Bind(wx.EVT_MENU, self.quit_application, id=APP_EXIT)

        menu_bar.Append(file_menu, "&File")
        self.SetMenuBar(menu_bar)

        """ Build the panel, with a 50px padding"""
        panel = wx.Panel(self)
        panel.SetBackgroundColour("#4f5049")
        panel.Bind(wx.EVT_RIGHT_DOWN, self.right_mouse_down)

        grid_bag_sizer = wx.GridBagSizer(5, 5)

        text_header = wx.StaticText(panel, label="FallenBot")
        grid_bag_sizer.Add(text_header, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=15)

    def quit_application(self, e) -> None:
        fb = FallenBot.FallenBot()
        fb.start_twitchclient("afallenhope")
        print(e)
        self.Close()

    def right_mouse_down(self, e) -> None:
        self.PopupMenu(PopupMenuUI(self), e.GetPosition())


class PopupMenuUI(wx.Menu):
    def __init__(self, parent):
        super(PopupMenuUI, self).__init__()
        self.parent = parent

        minimize_menu_item = wx.MenuItem(self, wx.NewId(), 'Minimize')
        minimize_menu_item.SetBitmap(wx.Bitmap("resources/images/minimize16x16.png"))
        self.Append(minimize_menu_item)
        self.Bind(wx.EVT_MENU, self.minimize_window, minimize_menu_item)

        close_menu_item = wx.MenuItem(self, wx.NewId(), '&Close')
        close_menu_item.SetBitmap(wx.Bitmap("resources/images/exit16x16.png"))
        self.Append(close_menu_item)
        self.Bind(wx.EVT_MENU, self.close_window, close_menu_item)

    def minimize_window(self, e):
        self.parent.Iconize()

    def close_window(self, e):
        self.parent.Close()


if __name__ == '__main__':
    app = wx.App()
    MainFrameUI(None, "FallenBot")
    app.MainLoop()
