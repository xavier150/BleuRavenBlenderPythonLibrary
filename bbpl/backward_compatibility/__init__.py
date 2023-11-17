# ====================== BEGIN GPL LICENSE BLOCK ============================
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.	 If not, see <http://www.gnu.org/licenses/>.
#  All rights reserved.
#
# ======================= END GPL LICENSE BLOCK =============================

# ----------------------------------------------
#  BBPL -> BleuRaven Blender Python Library
#  BleuRaven.fr
#  XavierLoux.com
# ----------------------------------------------

import bpy
import importlib

classes = (
)



def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


def update_data_variable(data, old_var_names, new_var_name, callback=None):
    for old_var_name in old_var_names:
        if old_var_name in data:
            try:
                if callback:
                    new_value = callback(data, old_var_name, new_var_name)
                    setattr(data, new_var_name, new_value)
                else:
                    setattr(data, new_var_name, data[old_var_name])

                del data[old_var_name]
                print(f'"{old_var_name}" updated to "{new_var_name}" in {data.name}')
            except Exception as e:
                print(f'Error updating "{old_var_name}" to "{new_var_name}" in {data.name}: {str(e)}')


class RigActionUpdater:
    """
    """
    def __init__(self):
        self.update_fcurve = 0
        self.remove_fcurve = 0

    def update_action_whole_variable_names(self, action, old_var_names, new_var_name, callback=None):
        for fcurve in action.fcurves:
            for old_var_name in old_var_names:
                current_target = fcurve.data_path
                if fcurve.data_path == old_var_name:
                    fcurve.data_path = new_var_name
                    print(f'"{current_target}" updated to "{new_var_name}" in {action.name} action.')
                    self.update_fcurve += 1

    def update_action_variable_names(self, action, old_var_names, new_var_name, remove_if_already_exists=False, callback=None):
        action_fcurves = []
        data_paths = []
        for fcurve in action.fcurves:
            action_fcurves.append(fcurve)
            data_paths.append(fcurve.data_path)
            

        for action_fcurve in action_fcurves:
            for old_var_name in old_var_names:
                current_target = action_fcurve.data_path
                if old_var_name in current_target:
                    new_target = current_target.replace(old_var_name, new_var_name)
                    if new_target not in data_paths:
                        action_fcurve.data_path = new_target
                        print(f'"{current_target}" updated to "{new_target}" in {action.name} action.')
                        self.update_fcurve += 1
                    else:
                        if remove_if_already_exists:
                            action.fcurves.remove(action_fcurve)
                            print(f'"{current_target}" removed in {action.name} action.')
                            self.remove_fcurve += 1
                            break #FCurve removed so no neew to test the other old_var_names
                        else:
                            print(f'"{current_target}" can not be updated to "{new_target}" in {action.name} action. (Alredy exist!)')

    def remove_action_curve_by_name(self, action, old_var_names, callback=None):
        for fcurve in action.fcurves:
            for old_var_name in old_var_names:
                current_target = fcurve.data_path
                if old_var_name in current_target:
                    action.fcurves.remove(fcurve)
                    print(f'"{current_target}" removed in {action.name} action.')
                    self.remove_fcurve += 1
                    break #FCurve removed so no neew to test the other old_var_names

    def print_update_log(self):
        print(f'{self.update_fcurve} fcurve data_path have been updated.')
        print(f'{self.remove_fcurve} fcurve data_path have been removed.')
