import importlib
import os
import types

from enum import Enum

primitiveTypes = (int, str, bool, type(None), float, dict, list, tuple)
definedTypes = ()  # definedTypes are defined below


def init_types(folder, type_list):
    for f in os.listdir(
        os.path.join(
            os.path.abspath(
            os.path.dirname(__file__)),
            folder.replace(
                '.',
            '/'))):
        name = str(f.split('.')[0])
        if not name.startswith('_'):
            mod = init_type(folder, name)
            mem_name = getattr(mod, dir(mod)[0])
            type_list += type(mem_name),
    return type_list


def init_type(folder, name):
    imported_module = importlib.import_module('.' + name, 'dvlssdk.' + folder)
    imported_type = getattr(imported_module, name)
    return imported_type


def init_model(folder, name):
    return init_type(folder + '.models', name)()


def init_enum(folder, name):
    return init_type(folder + '.enums', name)


definedTypes = init_types('generated.enums', definedTypes)


# This function fills an object using imported models from auto-generated
# code and the options dictionary. The object is filled where keys are
# found in the corresponding model. The options dictionary must contain
# the same keys as in the model in order to fill the model with data.
def fill_data(obj, options, keepFields = False):
    lowercase_options = dict((k.lower(), v) for k, v in options.items())
    keys_to_delete = []
    for name, subObj in vars(obj).items():
        if isinstance(subObj, primitiveTypes):
            if not lowercase_options.get(name.lower()) is None:
                 setattr(obj, name, lowercase_options.get(name.lower()))
                 if obj.__dict__[name] is None and not keepFields:
                    keys_to_delete.append(name)
        elif isinstance(subObj, definedTypes):
            type_name = str(subObj).split('.')[0]
            type_module = init_enum('generated', type_name)
            if name.lower() in lowercase_options:
                if isinstance(lowercase_options.get(name.lower()), str):
                    setattr(
                        obj, name, type_module.value_from_name(
                            lowercase_options.get(name.lower())))
                else:
                    if not lowercase_options.get(name.lower()) is None:
                        setattr(obj, name, lowercase_options.get(name.lower()))
                if obj.__dict__[name] is None and not keepFields:
                    keys_to_delete.append(name)
        elif not isinstance(subObj, types.FunctionType) \
                and not isinstance(subObj, Enum) \
                and not name.startswith('_'):
            setattr(obj, name, fill_data(subObj, lowercase_options))
    for k in keys_to_delete:
        del obj.__dict__[k]
    return obj
