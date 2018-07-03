"""Contains a collection of basic calculations for geology.

These include:

* Snell's Law

"""

from __future__ import division

import numpy as np


def snell_angle(incoming_angle, velocity_top, velocity_bottom):
    r"""Calculate refration in the lower layer of Snell's law.

    Parameters
    ----------
    incoming_angle : array_like
        Angle from vertical of incoming ray to boundary in degrees
    velocity_top : array_like
        Velocity of the top layer
    velocity_bottom : array_like
        Velocity of the bottom layer

    Returns
    -------
    outgoing_angle: array_like
        Angle from vertical of the outgoing ray from the boundary in degrees

    """
    if velocity_top == 0:
        raise ValueError('Top layer velocity can not be zero.')
    sin_of_outgoing_ray = np.sin(np.radians(incoming_angle)) * (velocity_bottom / velocity_top)
    return np.degrees(np.arcsin(sin_of_outgoing_ray))
