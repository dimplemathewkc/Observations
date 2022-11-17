from .models import ValueTypes, ValueUnits


def get_value_type(value_type):
    """
    Get value type from the ValueTypes table
    """
    return ValueTypes.objects.get(value_type=value_type)


def get_value_unit(value_unit):
    """
    Get value unit from the ValueUnits table
    """
    return ValueUnits.objects.get(value_unit=value_unit)


def create_value_type(value_type):
    """
    Create value type in the ValueTypes table
    """
    return ValueTypes.objects.create(value_type=value_type)


def create_value_unit(value_unit):
    """
    Create value unit in the ValueUnits table
    """
    return ValueUnits.objects.create(value_unit=value_unit)
