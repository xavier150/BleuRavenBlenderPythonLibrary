# BleuRaven Blender Python Library
This is my personal Python Library for Blender use.  (The wiki is not finished.)  
BBPL -> BleuRaven Blender Python Library

You free to use it, you can also credit me or support my works.

Discord:
If you need help or you want see my sides project you can join the discord!
-> https://discord.gg/XuYeGCFtxa


# Blender Layout
## Layout Extent Sections
For use this:  
![image](https://github.com/xavier150/BleuRavenBlenderPythonLibrary/assets/7216958/5be147d6-2081-4874-98a4-0aeceb65dc1e)

1. Import and register bbpl.
```
from . import bbpl
bbpl.register()
```

2. Create a child class of BBPL_UI_ExpendSection from bbpl.blender_layout.layout_expend_section and register the child class.
```
from .bbpl.blender_layout.layout_expend_section.types import (
        BBPL_UI_ExpendSection,
        )

class MyAddon_UI_ExpendSection(BBPL_UI_ExpendSection):
    pass

bpy.utils.register_class(BFU_UI_ExpendSection)
```

2. Create a pointer of your child class and add an name.
```
bpy.types.Scene.bfu_object_properties_expanded = bpy.props.PointerProperty(type=MyAddon_UI_ExpendSection, name="Object Properties")
```

3. Use draw(layout: bpy.types.UILayout) for draw the section button and is_expend() to check if the section is open.
```
scene.bfu_nomenclature_properties_expanded.draw(layout)
if scene.bfu_nomenclature_properties_expanded.is_expend():
    # The data to show when is expend
```
Here the result in my addon [Blender For Unreal Engine](https://github.com/xavier150/Blender-For-UnrealEngine-Addons):  
![Layout Extent Sections](https://github.com/xavier150/BleuRavenBlenderPythonLibrary/assets/7216958/7fceb7a9-2c33-47dc-b9d0-6e53229aebf6)

## Layout Template List

1. Import and register bbpl.
```
from . import bbpl
bbpl.register()
```

2. Create a child class of BBPL_UI_TemplateItem, BBPL_UI_TemplateItemDraw and BBPL_UI_TemplateList from bbpl.blender_layout.layout_template_list.  
        - BBPL_UI_TemplateList manage the list and actions.  
        - BBPL_UI_TemplateItem manage the item and content.  
        - BBPL_UI_TemplateItemDraw manage how the item should draw.
In your TemplateList class you need set your Item Class and Draw Item Class.
```
from .bbpl.blender_layout.layout_template_list.types import (
        BBPL_UI_TemplateItem,
        BBPL_UI_TemplateItemDraw,
        BBPL_UI_TemplateList,
        )



class MyAddon_UI_TemplateItem(BBPL_UI_TemplateItem): # Item class (bpy.types.PropertyGroup)
    pass

class MyAddon_UI_TemplateItemDraw(BBPL_UI_TemplateItemDraw): # Draw Item class (bpy.types.UIList)
    pass

class MyAddon_UI_TemplateList(BBPL_UI_TemplateList): # Template List class
    template_collection: bpy.props.CollectionProperty(type=MyAddon_UI_TemplateItem)
    template_collection_uilist_class: bpy.props.StringProperty(default = "MyAddon_UI_TemplateItemDraw")
```

3. register the childs class and create a pointer of your TemplateList class.
```
bpy.utils.register_class(MyAddon_UI_TemplateItem)
bpy.utils.register_class(MyAddon_UI_TemplateItemDraw)
bpy.utils.register_class(MyAddon_UI_TemplateList) # Need be register after Item and Draw Item.

bpy.types.Scene.my_properties_list = bpy.props.PointerProperty(type=MyAddon_UI_TemplateList)
```

You can now use draw(layout: bpy.types.UILayout) on your list for draw in the UI  
```
my_properties_list.draw(layout)
```

Here the result:  
![Layout Template List](https://github.com/xavier150/BleuRavenBlenderPythonLibrary/assets/7216958/fd498044-eb73-4da7-a413-1aa096f4ba77)

4. Edit your Item Class like an bpy.types.PropertyGroup for add the content and property you need.
```
# Example
class MyAddon_UI_TemplateItem(BBPL_UI_TemplateItem): # Your Item class
    use: bpy.props.BoolProperty(
        name="Use",
        default=True
        )

    name: bpy.props.StringProperty(
        name="Bone groups name",
        description="Your bone group",
        default="MyGroup",
        )
```

6. Edit your Draw Item Class following bpy.types.UIList API. [Basic UIList Example](https://docs.blender.org/api/current/bpy.types.UIList.html)
```
# Example
class MyAddon_UI_TemplateItemDraw(BBPL_UI_TemplateItemDraw): # Your Draw Item class
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):

        prop_line = layout

        indexText = layout.row()
        indexText.alignment = 'LEFT'
        indexText.scale_x = 1
        indexText.label(text=str(index))

        prop_use = prop_line.row()
        prop_use.alignment = 'LEFT'
        prop_use.prop(item, "use", text="")

        #icon = bbpl.ui_utils.getIconByGroupTheme(item.theme)
        icon = "NONE"

        prop_data = prop_line.row()
        prop_data.alignment = 'EXPAND'
        prop_data.prop(item, "name", text="")
        prop_data.enabled = item.use
```

7. API
   - draw(layout: bpy.types.UILayout) for draw the template.
   - get_template_collection() for get the list collection. Now you can also use len()
   - get_active_index() Get the active index
   - get_active_item() Get the active item
   - clear() 

  BBPL_UI_TemplateList can be used with the native list fonctions like len(), iter()...

   


# Rig Backward Compatibility
1. Import and register bbpl.
```
from . import bbpl
bbpl.register()
```

2. Create a new class RigActionUpdater.
```
my_rig_updater = bbpl.backward_compatibility.RigActionUpdater()
```
bbpl.backward_compatibility.RigActionUpdater.update_action_curve_data_path()  
Update the data paths of FCurves in a given action by replacing old data paths with a new one.

bbpl.backward_compatibility.RigActionUpdater.remove_action_curve_by_data_path()  
Remove FCurves from a given action based on specified data paths.  

bbpl.backward_compatibility.RigActionUpdater.edit_action_curve()  
Edit FCurves in a given action based on specified data paths using a custom callback function.  

bbpl.backward_compatibility.RigActionUpdater.print_update_log()  
Print a log of the number of FCurves updated and removed.

3 You can now use this function for update tour actions. Here an example
```
def Invert_old_rig_neck_callback(action, fcurve, data_path):
    if fcurve.array_index == 0: #X
        for keyframe_point in fcurve.keyframe_points:
            keyframe_point.co.y *= -1
            keyframe_point.handle_left.y *= -1
            keyframe_point.handle_right.y *= -1
            #keyframe_point.co.x = 10
    

def update_rig_backward_compatibility():

    print("Start update_rig_backward_compatibility")

    scene = bpy.context.scene


    my_rig_updater = bbpl.backward_compatibility.RigActionUpdater()
    for action in bpy.data.actions:

        ## Follow controllers rename
        my_rig_updater.update_action_curve_data_path(action, ['"]["Follow_c_Head"]'], '"]["Follow_Head"]', True)
        my_rig_updater.update_action_curve_data_path(action, ['"]["Follow_c_Skull_02"]'], '"]["Follow_Skull_02"]', True)
        my_rig_updater.update_action_curve_data_path(action, ['"]["Follow_c_Tongue_01"]'], '"]["Follow_Tongue_01"]', True)

        ## Game data controllers rename
        my_rig_updater.update_action_curve_data_path(action, ['pose.bones["c_BodyForward"]', 'pose.bones["BodyForward"]'], 'pose.bones["c_BaseBodyAim"]', True)
        my_rig_updater.update_action_curve_data_path(action, ['pose.bones["FootPrint_L"]'], 'pose.bones["c_FootPrint_L"]', True)

        ## Old deprecated controllers
        my_rig_updater.remove_action_curve_by_data_path(action, ['pose.bones["c_Hat"]', 'pose.bones["Hat"]'])
        my_rig_updater.remove_action_curve_by_data_path(action, ['pose.bones["c_Glasses"]', 'pose.bones["Glasses"]'])

        ## Hidden Rig Points that should not be animate
        my_rig_updater.remove_action_curve_by_data_path(action, ['pose.bones["rp_c_Eye', 'pose.bones["rp_Eye'])
        my_rig_updater.remove_action_curve_by_data_path(action, ['pose.bones["rp_Interp_'])

        my_rig_updater.edit_action_curve(action, ['pose.bones["c_Neck"].rotation_euler'], Invert_old_rig_neck_callback)
    
    print("End update_rig_backward_compatibility")
    my_rig_updater.print_update_log()

update_rig_backward_compatibility()
```
![image](https://github.com/xavier150/BleuRavenBlenderPythonLibrary/assets/7216958/98213b7e-2f1d-4a07-b461-65d02af45737)


# Addon Backward Compatibility
1. Import and register bbpl.
```
from . import bbpl
bbpl.register()
```
2.In progress...





# Other
In progress...
