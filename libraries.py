import pkg_resources

# List of installed packages and their version numbers
installed_packages = pkg_resources.working_set

# List of packages used in the notebook
used_packages = sorted(
    [i.key for i in pkg_resources.working_set if i.project_name.startswith('model.ipynb')])

# Loop through the used packages and print their version number
for package in used_packages:
    version = installed_packages.by_key[package].version
    print(f"{package}=={version}")
