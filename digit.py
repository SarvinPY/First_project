import pip


def install(package_name):

    if hasattr(pip, 'main'):

        pip.main(['install', package_name])

    else:

        pip._internal.main(['install', package_name])


install('requests')