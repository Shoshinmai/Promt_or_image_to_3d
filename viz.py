
import trimesh
import pyrender

# Load the textured mesh (trimesh auto-loads the .mtl and image if referenced correctly)
mesh = trimesh.load('PATH_0F_.obj_FILE', force='mesh')

# Ensure the mesh is in a Scene object (trimesh might load a Scene if multiple geometries)
if isinstance(mesh, trimesh.Scene):
    combined = trimesh.util.concatenate(mesh.dump())
else:
    combined = mesh

# Convert to pyrender mesh, preserving the texture
pyrender_mesh = pyrender.Mesh.from_trimesh(combined, smooth=True)

# Create and show the scene
scene = pyrender.Scene()
scene.add(pyrender_mesh)

# Open interactive viewer
pyrender.Viewer(scene, use_raymond_lighting=True)
