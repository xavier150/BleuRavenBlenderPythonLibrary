# BleuRaven Blender Python Library
This is my personal Python Library for Blender use.  (The wiki is not finished.)  
BBPL -> BleuRaven Blender Python Library

You free to use it, you can also credit me or support my works.


# Blender Layout
## Layout Extent Sections
For use this:  
![image](https://github.com/xavier150/BleuRavenBlenderPythonLibrary/assets/7216958/5be147d6-2081-4874-98a4-0aeceb65dc1e)

1. Import and register bbpl
```
from . import bbpl
bbpl.register()
```

2. Create a child class of BBPL_UI_ExpendSection from bbpl.blender_layout.layout_expend_section and register the child class
```
from .bbpl.blender_layout.layout_expend_section.types import (
        BBPL_UI_ExpendSection,
        )

class MyAddon_UI_ExpendSection(BBPL_UI_ExpendSection):
    pass

bpy.utils.register_class(BFU_UI_ExpendSection)
```

2. Create a pointer of your child class
```
bpy.types.Scene.bfu_object_properties_expanded = bpy.props.PointerProperty(type=MyAddon_UI_ExpendSection, name="Object Properties")
```

3. Use draw(layout: bpy.types.UILayout) for draw the section button and is_expend() to check if the section is open.
```
scene.bfu_nomenclature_properties_expanded.draw(layout)
if scene.bfu_nomenclature_properties_expanded.is_expend():
    # The data to show when is expend
```

# Other
In progress...
