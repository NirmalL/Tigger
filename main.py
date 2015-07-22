from gi.repository import Gtk, Gio

class TiggerMain (Gtk.Window):

    def __init__(self):

        # window
        Gtk.Window.__init__(self, title="Stack Demo")
        self.set_border_width(10)
        self.set_default_size(600, 400)

        # headerbar
        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "Tigger"
        self.set_titlebar(hb)
        # headerbar-tools
        button = Gtk.Button()
        icon = Gio.ThemedIcon(name="mail-send-receive-symbolic")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button.add(image)
        hb.pack_end(button)
        # headerbar-tools-box
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")
        # headerbar-tools-box-button
        button = Gtk.Button()
        button.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        box.add(button)
        # headerbar-tools-box-button
        button = Gtk.Button()
        button.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        box.add(button)
        # headerbar
        hb.pack_start(box)

        # contentbox
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # contentbox-stack
        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(500)

        # contentbox-stack-tab
        stackOne = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        checkbutton = Gtk.CheckButton("Click me!")
        stackOne.add(checkbutton)
        stack.add_titled(stackOne, "check", "Check Button")

        # contentbox-stack-tab
        stackTwo = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        label = Gtk.Label()
        label.set_markup("<big>A fancy label</big>")
        stackTwo.add(label)
        stack.add_titled(stackTwo, "label", "A label")

        # contentbox-stack
        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        stack_switcher.set_halign(Gtk.Align.CENTER)
        stack_switcher.set_valign(Gtk.Align.CENTER)

        # contentbox
        vbox.pack_start(stack_switcher, False, False, 0)
        vbox.pack_start(stack, True, True, 0)


# load window
win = TiggerMain()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
