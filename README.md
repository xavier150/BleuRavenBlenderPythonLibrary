# BleuRaven Blender Python Library
This is my personal Python Library for Blender use.  (The wiki is not finished.)  
BBPL -> BleuRaven Blender Python Library

You free to use it, you can also credit me or support my works.


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
```
from .bbpl.blender_layout.layout_expend_section.types import (
        BBPL_UI_TemplateItem,
        BBPL_UI_TemplateItemDraw,
        BBPL_UI_TemplateList,
        )



class MyAddon_UI_TemplateItem(BBPL_UI_TemplateItem): # Your Item class
    pass

class MyAddon_UI_TemplateItemDraw(BBPL_UI_TemplateItemDraw): # Your Draw Item class
    pass

class MyAddon_UI_TemplateList(BBPL_UI_TemplateList): # Your Template List class
    pass
```

3. register the childs class and create a pointer of your TemplateList class.
```
bpy.utils.register_class(MyAddon_UI_TemplateItem)
bpy.utils.register_class(MyAddon_UI_TemplateItemDraw)
bpy.utils.register_class(MyAddon_UI_TemplateList) # Need be register after Item and Draw Item.

bpy.types.Scene.bfu_object_properties_expanded = bpy.props.PointerProperty(type=MyAddon_UI_TemplateList)
```

4. Edit your TemplateList class for set your Item Class and Draw Item Class
```
class MyAddon_UI_TemplateList(BBPL_UI_TemplateList):
    template_collection: bpy.props.CollectionProperty(type=MyAddon_UI_TemplateItem)
    template_collection_uilist_class: bpy.props.StringProperty(default = "MyAddon_UI_TemplateItemDraw")
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
   - Use draw(layout: bpy.types.UILayout) for draw the template.
   - Use get_template_collection() for get the list collection
   - Use get_active_index() for get the active index
   - Use get_active_item() for get the active item


# Other
In progress...
