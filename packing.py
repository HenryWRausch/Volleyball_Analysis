# Defining the packer and unpacker for the attack line and defense points

def pack_attack_line(x_origin: float, y_origin: float, x_end: float, y_end: float) -> str:
    """
    Packs two sets of coordinates into a string for entry into the database.

    Parameters:
    x_origin (float): The x coordinate of the line origin.
    y_origin (float): The y coordinate of the line origin.
    x_end (float): The x coordinate of the line endpoint.
    y_end (float): The y coordinate of the line endpoint.

    Returns:
    str: The packed string to be entered into the database.
    """
    
    return f"{x_origin}|{y_origin}|{x_end}|{y_end}"


def unpack_attack_line(data: str) -> tuple:
    """
    Unpacks a string of coordinates into two coordinate pairs (tuples).

    Parameters:
    data (str): A packed string in the format 'x_origin|y_origin|x_end|y_end'.

    Returns:
    tuple: Two tuples, each containing x and y coordinates as floats.
    """

    split_data = data.split('|')
    

    if len(split_data) != 4:
        raise ValueError("Input data must contain exactly four parts separated by '|'.")


    x_origin, y_origin = float(split_data[0]), float(split_data[1])
    x_end, y_end = float(split_data[2]), float(split_data[3])


    return (x_origin, y_origin), (x_end, y_end)


def pack_defense_point(x_coordinate: float, y_coordinate: float) -> str:
    """
    Packs a coordinate into a string

    Parameters:
    x_coordinate (float): The x Coordinate of the point to be packed
    y_coordinate (float): The y Coordinate of the point to be packed

    Returns:
    str: A packed string in the format 'x_coordinate|y_coordinate'
    """

    return f'{x_coordinate}|{y_coordinate}'

def unpack_defense_point(data: str) -> tuple:
    split_data = data.split('|')

    if len(split_data) != 2:
        raise ValueError("Input data must contain exactly two points separated by '|'")

    return float(split_data[0]), float(split_data[1])

