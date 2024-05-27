import os
import itertools
import subprocess
from pywinauto.application import Application

# Define the map layouts
maps = {
    "smallEmpty": """
%%%%%%%%%%%%%%%%%%%%
%P                G%
%                 G%
%                 G%
%                 G%
%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%
% % % % %%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%
""",
    "smallWalls": """
%%%%%%%%%%%%%%%%%%%%
%P      %%%      G %
%  %%        %%  G %
%       %%     G  %%
%                G %
%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%
% % % % %%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%
""",
    "bigEmpty": """
%%%%%%%%%%%%%%%%%%%%
%P                 %
%                  %
%                  %
%                  %
%                  %
%                  %
%                  %
%                  %
%                  %
%G                G%
%G                G%
%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%
% % % % %%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%
""",
    "bigWalls": """
%%%%%%%%%%%%%%%%%%%%
%P      %%%       %%
%  %%        %%    %
%       %%        %%
%  %%        %%    %
%       %%        %%
%  %%        %%    %
%       %%        %%
%G %%        %%   G%
%G     %%         G%
%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%
% % % % %%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%
"""
}

# Define the default values for constant parameters
default_params = {
    "checkUniform": "False",
    "errorMsg": "Exact inference full test: %d inference errors.",
    "L2Tolerance": "0.0001",
    "ghost": "SeededRandomGhostAgent",
}


# Parameter values to combine
seeds = [188, 42, 10]
numGhosts = [1, 2, 3, 4]
layouts = ["smallEmpty", "smallWalls", "bigEmpty", "bigWalls"]
observes = ["True", "False"]
elapses = ["True", "False"]
inferences = ["ExactInference", "ParticleFilter"]


def clean_layout(layout):
    """
    Removes empty lines at the top and bottom of the layout.

    Args:
        layout (str): The original layout string.

    Returns:
        str: The cleaned layout string.
    """
    lines = layout.strip().split('\n')
    cleaned_layout = '\n'.join(line for line in lines if line.strip())
    return cleaned_layout


def generate_test_file(directory, filename, params):
    """
    Generates a test definition file with the given parameters.

    Args:
        directory (str): The directory where the file will be saved.
        filename (str): The name of the file.
        params (dict): A dictionary of parameters to include in the file.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, filename)

    with open(file_path, 'w') as f:
        f.write('class: "DoubleInferenceAgentTestCustom"\n\n')
        for key, value in params.items():
            if key == 'layout':
                cleaned_layout = clean_layout(value)
                f.write(f'{key}: """\n{cleaned_layout}\n"""\n\n')
            else:
                f.write(f'{key}: "{value}"\n\n')
        # Write the default parameters
        for key, value in default_params.items():
            f.write(f'{key}: "{value}"\n\n')


def main():
    # Define the directory where the files will be saved
    directory = 'test_cases\\custom'
    max_moves = "200"
    filename_counter = 1

    # Generate combinations of all parameters
    combinations = itertools.product(
        seeds, numGhosts, layouts, observes, elapses, inferences)

    # Generate the test files
    for combo in combinations:
        seed, numGhost, layout_key, observe, elapse, inference = combo
        params = {
            "seed": str(seed),
            "layout": maps[layout_key],
            "observe": observe,
            "elapse": elapse,
            "maxMoves": max_moves,
            "numGhosts": str(numGhost),
            "inference": inference,
            "mapName": layout_key,
            "testName": f"customTest{filename_counter}"
        }
        filename = f"customTest{filename_counter}.test"
        generate_test_file(directory, filename, params)
        filename_counter += 1

    # Generate the
    generate_solutions()

    # input to continue or not
    input("Press Enter to continue...")

    # Run the autograder
    csv_path = "custom_results"
    run_autograder(filename_counter-1, csv_path, directory)


def generate_solutions():
    """
    Executes the command to generate solutions and handles the interactive input.
    """
    command = "C:\\Python27\\python.exe .\\autograderCustom.py --generate-solutions"
    process = subprocess.Popen(command, shell=True)

    # Wait for the process to start and the prompt to appear
    process.wait()


def run_autograder(filename_counter, csv_path, directory):
    for i in range(1, filename_counter + 1):
        test_file = f"{directory}\\customTest{i}"
        command = f"C:\\Python27\\python.exe .\\autograderCustom.py -t {test_file} -c {csv_path}.csv --no-graphics"
        subprocess.run(command, shell=True)


if __name__ == "__main__":
    main()
