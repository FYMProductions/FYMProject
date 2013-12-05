import bpy

class ButtonsSub(bpy.types.Menu):
    bl_label = 'my materials'
    bl_idname = 'view3d.mymenu_submenu'

    def draw(self, context):
        layout = self.layout

        layout.label("This is a submenu")
        layout.operator("render.render")


class ButtonsMain(bpy.types.Menu):
    bl_label = 'my materials'
    bl_idname = 'view3d.mymenu'

    def draw(self, context):
        layout = self.layout

        layout.label("This is a main menu")
        layout.menu(ButtonsSub.bl_idname)
        layout.operator("render.render")

def register():
    bpy.utils.register_module(__name__)

    # call menu now!
    bpy.ops.wm.call_menu(name=ButtonsMain.bl_idname)


def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()