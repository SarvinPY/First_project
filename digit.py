import pip


def install(package_name):

    if hasattr(pip, 'main'):

        pip.main(['install', package_name])

    elif:

        pip._internal.main(['install', package_name])
    else:
        print('0")


install('requests')
