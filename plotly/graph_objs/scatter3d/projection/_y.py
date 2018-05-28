from plotly.basedatatypes import BaseTraceHierarchyType


class Y(BaseTraceHierarchyType):

    # opacity
    # -------
    @property
    def opacity(self):
        """
        Sets the projection color.
    
        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['opacity']

    @opacity.setter
    def opacity(self, val):
        self['opacity'] = val

    # scale
    # -----
    @property
    def scale(self):
        """
        Sets the scale factor determining the size of the projection
        marker points.
    
        The 'scale' property is a number and may be specified as:
          - An int or float in the interval [0, 10]

        Returns
        -------
        int|float
        """
        return self['scale']

    @scale.setter
    def scale(self, val):
        self['scale'] = val

    # show
    # ----
    @property
    def show(self):
        """
        Sets whether or not projections are shown along the y axis.
    
        The 'show' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['show']

    @show.setter
    def show(self, val):
        self['show'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'scatter3d.projection'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        opacity
            Sets the projection color.
        scale
            Sets the scale factor determining the size of the
            projection marker points.
        show
            Sets whether or not projections are shown along the y
            axis.
        """

    def __init__(self, opacity=None, scale=None, show=None, **kwargs):
        """
        Construct a new Y object
        
        Parameters
        ----------
        opacity
            Sets the projection color.
        scale
            Sets the scale factor determining the size of the
            projection marker points.
        show
            Sets whether or not projections are shown along the y
            axis.

        Returns
        -------
        Y
        """
        super(Y, self).__init__('y')

        # Import validators
        # -----------------
        from plotly.validators.scatter3d.projection import (y as v_y)

        # Initialize validators
        # ---------------------
        self._validators['opacity'] = v_y.OpacityValidator()
        self._validators['scale'] = v_y.ScaleValidator()
        self._validators['show'] = v_y.ShowValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.opacity = opacity
        self.scale = scale
        self.show = show

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
