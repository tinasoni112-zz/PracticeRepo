def get_version_using_pkg_attribute():
    import pandas as module #change it to required module name
    print(module.__version__)

def get_version_using_importlib():
    # REquired python version to be > = 0.38
    from importlib.metadata import version
    version('pandas')
