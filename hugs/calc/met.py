"""Contains a collection of basic calculations.

These include:

* wind components

"""

from __future__ import division

import warnings
import numpy as np


def get_wind_speed(u, v):
    r"""Compute the wind speed from u and v-components.

    Parameters
    ----------
    u : array_like
        Wind component in the X (East-West) direction
    v : array_like
        Wind component in the Y (North-South) direction

    Returns
    -------
    wind speed: array_like
        The speed of the wind

    See Also
    --------
    get_wind_components

    """
    speed = np.sqrt(u * u + v * v)
    return speed


def get_wind_dir(u, v):
    r"""Compute the wind direction from u and v-components.

    Parameters
    ----------
    u : array_like
        Wind component in the X (East-West) direction
    v : array_like
        Wind component in the Y (North-South) direction

    Returns
    -------
    wind direction: `pint.Quantity`
        The direction of the wind, specified as the direction from
        which it is blowing, with 0 being North.

    See Also
    --------
    get_wind_components

    """
    wdir = 90. - np.degrees(np.arctan2(-v, -u))
    wdir[wdir < 0] += 360.
    return wdir


def get_wind_components(speed, wdir):
    r"""Calculate the U, V wind vector components from the speed and direction.

    Parameters
    ----------
    speed : array_like
        The wind speed (magnitude)
    wdir : array_like
        The wind direction, specified as the direction from which the wind is
        blowing, with 0 being North.

    Returns
    -------
    u, v : tuple of array_like
        The wind components in the X (East-West) and Y (North-South)
        directions, respectively.

    See Also
    --------
    get_wind_speed
    get_wind_dir

    """
    if wdir > 360:
        warnings.warn('Wind direction greater than 360 degrees.')
    wdir = np.radians(wdir)
    u = -speed * np.sin(wdir)
    v = -speed * np.cos(wdir)
    return u, v
