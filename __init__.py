# ##### BEGIN GPL LICENSE BLOCK #####
#
#  <Demo Addon 4 Addon>
#    Copyright (C) <2022>  <Joel Benkwitz>
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy

bl_info = {
    "name": "Demo Addon 4",
    "author": "Joel Benkwitz (BD)",
    "version": (1, 0, 1),
    "blender": (2, 83, 0),
    "warning": "",
    "tracker_url": "https://github.com/Joel-dev-IMP/jufo-oeff-5/issues/new",
    "endpoint_url": "https://raw.githubusercontent.com/Joel-dev-IMP/jufo-oeff-5/main/endpoint.json",
    "category": "General"
}

def register():
    print("Demo Addon 4!")
def unregister():
    pass
