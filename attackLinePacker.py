# Defining the packer and unpacker for the attack line.

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
