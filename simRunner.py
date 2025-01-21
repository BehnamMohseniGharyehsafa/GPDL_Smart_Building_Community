####################################################################################
# Import Required Libraries
####################################################################################
import os
import sys
import subprocess
import pandas as pd
import numpy as np
import time
from datetime import timedelta, datetime
from collections import defaultdict
import plotly.graph_objects as go
import openstudio
from pyenergyplus.api import EnergyPlusAPI

# Optional Libraries
import esoreader  # For processing EnergyPlus output files
import threading  # For parallel operations
#___________________________________________________________________________________#

####################################################################################
# BIM Representation and Visualization
####################################################################################

def convert_idf_to_osm_using_ruby(idf_path, osm_output_path):
    """
    Converts an EnergyPlus IDF file to an OpenStudio OSM file using a Ruby script.

    Parameters:
        idf_path (str): Path to the IDF file.
        osm_output_path (str): Path to save the converted OSM file.
    """
    ruby_executable = r"C:\Ruby27-x64\bin\ruby.exe"  # Ruby SDK path
    ruby_script_path = r"Path\to\ruby\script"  # Replace with actual Ruby script path

    # Check if the Ruby script exists
    if not os.path.exists(ruby_script_path):
        raise FileNotFoundError(f"Ruby script not found: {ruby_script_path}")

    # Setup Ruby environment
    env = os.environ.copy()
    env['GEM_HOME'] = r"C:\ladybug\openstudio-3.7.0\Ruby"
    env['GEM_PATH'] = r"C:\ladybug\openstudio-3.7.0\Ruby"
    env['RUBYLIB'] = r"C:\ladybug\openstudio-3.7.0\Ruby"
    env['PATH'] += f";C:\\Ruby27-x64\\bin"

    # Execute the Ruby script
    result = subprocess.run([ruby_executable, ruby_script_path, idf_path, osm_output_path],
                            capture_output=True, text=True, env=env)

    print(f"Output:\n{result.stdout}")
    print(f"Error:\n{result.stderr}")

    if result.returncode != 0:
        raise RuntimeError(f"Conversion failed with exit code {result.returncode}")
    else:
        print(f"Conversion successful! OSM saved at {osm_output_path}")


def visualize_bim_model(osm_path):
    """
    Visualizes a BIM model from an OpenStudio OSM file using Plotly.

    Parameters:
        osm_path (str): Path to the OSM file.
    """
    translator = openstudio.osversion.VersionTranslator()
    model = translator.loadModel(openstudio.path(osm_path))

    if not model.is_initialized():
        raise RuntimeError("Failed to load the OpenStudio model.")

    model = model.get()
    vertices_list, i_list, j_list, k_list, colors = [], [], [], [], []

    # Process Spaces and Surfaces in the Model
    for space in model.getSpaces():
        for surface in space.surfaces():
            vertices = [[v.x(), v.y(), v.z()] for v in surface.vertices()]
            if len(vertices) >= 3:
                start_idx = len(vertices_list)
                vertices_list.extend(vertices)
                for n in range(1, len(vertices) - 1):
                    i_list.append(start_idx)
                    j_list.append(start_idx + n)
                    k_list.append(start_idx + n + 1)
                colors.extend(get_surface_color(surface.surfaceType()))

    # Generate 3D Plot
    x, y, z = zip(*vertices_list)
    fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, i=i_list, j=j_list, k=k_list,
                                    facecolor=colors, opacity=0.8, flatshading=True)])
    fig.update_layout(scene=dict(aspectmode='data'), margin=dict(l=0, r=0, b=0, t=0))
    fig.show()


def get_surface_color(surface_type):
    """
    Returns color mappings for different surface types.

    Parameters:
        surface_type (str): The type of the surface.

    Returns:
        list: RGB color values.
    """
    if surface_type == "Wall":
        return [[1.0, 0.8, 0.6]]
    elif surface_type == "RoofCeiling":
        return [[1.0, 0.4, 0.2]]
    elif surface_type == "Floor":
        return [[0.6, 0.6, 0.6]]
    else:
        return [[0.7, 0.7, 0.7]]
#___________________________________________________________________________________#

####################################################################################
# EnergyPlus Simulation Setup
####################################################################################

def setup_energyplus_environment(install_path):
    """
    Configures the environment for running EnergyPlus.

    Parameters:
        install_path (str): Path to the EnergyPlus installation directory.
    """
    os.environ['ENERGYPLUS_INSTALL_PATH'] = install_path
    os.environ['PATH'] += os.pathsep + os.path.join(install_path, 'PostProcess')
    sys.path.insert(0, os.path.join(install_path, 'Python', 'Runtime'))


def run_energyplus_simulation(idf_path, epw_path, output_dir):
    """
    Runs an EnergyPlus simulation using the Python API.

    Parameters:
        idf_path (str): Path to the IDF file.
        epw_path (str): Path to the EPW weather file.
        output_dir (str): Directory to save simulation results.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    api = EnergyPlusAPI()
    state = api.state_manager.new_state()
    api.runtime.run_energyplus(state, ['-r', '-d', output_dir, '-w', epw_path, idf_path])
    print("Simulation completed successfully.")
#___________________________________________________________________________________#

####################################################################################
# Main Execution
####################################################################################
if __name__ == "__main__":
    # Define file paths
    energyplus_install_path = r"C:\EnergyPlusV24-2-0"
    idf_path = r"Path\to\your\IDF\file.idf"
    epw_path = r"Path\to\your\EPW\file.epw"
    output_dir = r"Path\to\simulation\results"

    # Setup and Run
    setup_energyplus_environment(energyplus_install_path)
    run_energyplus_simulation(idf_path, epw_path, output_dir)

    # Optional Visualization
    osm_path = r"Path\to\your\OSM\file.osm"
    visualize_bim_model(osm_path)
