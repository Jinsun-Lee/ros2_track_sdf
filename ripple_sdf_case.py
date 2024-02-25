import os
from itertools import product

# Define possible values for attributes
types = ["track.png", "ripple.png"]

# Template for the SDF file
sdf_template = """<?xml version='1.0'?>
<sdf version="1.6">
  <model name="track_with_ripple">
    <static>true</static>
    <link name='link'>

      <collision name="collision">
        <geometry>
          <heightmap>
            <uri>model://track_with_ripple/materials/textures/{uri}</uri>
            <size>17 13 0.07</size>
            <pos>0 0 0</pos>
          </heightmap>
        </geometry>
        <surface>
          <contact>
            <collide_bitmask>0xffff</collide_bitmask> <!-- 모든 물체와 충돌 -->       
          </contact>
        </surface>
      </collision>

      <visual name="visual">
        <geometry>
          <heightmap>
            <use_terrain_paging>false</use_terrain_paging>
            <texture>
              <diffuse>model://track_with_ripple/materials/textures/{diffuse}</diffuse> <!-- 기본 -->
              <normal>model://track_with_ripple/materials/textures/{normal}</normal> <!-- 굴곡 -->
              <size>17</size> <!-- 지형 크기와 동일한 텍스처 크기 -->
            </texture>
            <uri>model://track_with_ripple/materials/textures/{uri}</uri> <!-- 텍스처 -->
            <size>17 13 0.07</size> <!-- 지형 크기, 최소 크기 2x2 -->
            <pos>0 0 0</pos>
          </heightmap>
        </geometry>
      </visual>
      
    </link>
  </model>
</sdf>
"""

# Output directory for SDF files
output_dir = "sdf_combinations"
os.makedirs(output_dir, exist_ok=True)

# Generate all combinations of attributes
combinations = product(types, repeat=3)

# Mapping for file name prefixes
file_name_map = {
    "track.png": "t",
    "ripple.png": "r"
}

# Create and save an SDF file for each combination
for (diffuse, normal, uri) in combinations:
    sdf_content = sdf_template.format(diffuse=diffuse, normal=normal, uri=uri)
    file_prefix = f"{file_name_map[diffuse]}{file_name_map[normal]}{file_name_map[uri]}"
    file_name = f"{file_prefix}.sdf"
    file_path = os.path.join(output_dir, file_name)
    
    with open(file_path, "w") as sdf_file:
        sdf_file.write(sdf_content)

print(f"Generated {len(types)**3} SDF files in '{output_dir}' directory.")

