bl_info = {
    "name": "Blender Shortcut Video Guide",
    "author": "MemoTech",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "Sidebar > Help Tab",
    "description": "Displays tutorial videos for Blender shortcuts",
    "category": "3D View",
}

import bpy
import webbrowser
from pathlib import Path
import platform


# Detect the downloads folder depending on the OS
def get_downloads_folder():
    home = Path.home()
    system = platform.system()

    if system == "Windows":
        return home / "Downloads"
    elif system == "Darwin":  
        return home / "Downloads"
    else:
        return home / "Downloads"
       
DOWNLOADS_DIR = get_downloads_folder()
MP4_DIR = DOWNLOADS_DIR / "MP4"

print("MP4 dir:", MP4_DIR)


VIDEOS = [
    {"title": "Alt + G or R = Reset location or rotation", "file": "Ultra_fix_ALTG_ALTR.mp4"},
    {"title": "Proportional Editing", "file": "PropEditRENDU.mp4"},
    {"title": "G = Move", "file": "g = move.mp4"},
    {"title": "G + X = Move along X axis", "file": "G+ X = move X axis.mp4"},
    {"title": "G + Y = Move along Y axis", "file": "G+Y = move Y axis.mp4"},
    {"title": "G + Z = Move along Z axis", "file": "G+Z = Move Z axis.mp4"},
    {"title": "A = Select All", "file": "a = select all.mp4"},
    {"title": "H = Hide", "file": "h-hide.mp4"},
    {"title": "N = Info Menu", "file": "N= info menu.mp4"},
    {"title": "Numpad 0 = Camera View", "file": "numpad 0 = camera view.mp4"},
    {"title": "Numpad 1 = Front View", "file": "numpad 1 = front view.mp4"},
    {"title": "Numpad 3 = Side View", "file": "Numpad 3 = side view.mp4"},
    {"title": "Numpad 5 = Orthographic View", "file": "Numpad 5 = orthographic view.mp4"},
    {"title": "Numpad 7 = Top View", "file": "Numpad 7 = top view.mp4"},
    {"title": "Shift + A = Add Menu", "file": "shift+A = Addmenu.mp4"},
    {"title": "X = Delete", "file": "X = delete.mp4"},
    {"title": "Z = Material Preview", "file": "Z = material preview menu.mp4"},
]


# Operator to open video
class WM_OT_open_video(bpy.types.Operator):
    bl_idname = "wm.open_video"
    bl_label = "Open Video"

    video_path: bpy.props.StringProperty()

    def execute(self, context):
        webbrowser.open(self.video_path)
        return {'FINISHED'}

# UI Panel
class VIEW3D_PT_video_panel(bpy.types.Panel):
    bl_label = "Video Help"
    bl_idname = "VIEW3D_PT_video_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Help"

    def draw(self, context):
        layout = self.layout

        for video in VIDEOS:
            layout.label(text=video["title"])
            video_path = MP4_DIR / video["file"]

            if video_path.exists():
                op = layout.operator("wm.open_video", text="Watch Video")
                op.video_path = str(video_path)
            else:
                layout.label(text="Video not found", icon='ERROR')


# Registration
classes = (
    WM_OT_open_video,
    VIEW3D_PT_video_panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
