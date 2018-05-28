from plotly.basedatatypes import BaseTraceHierarchyType


class Font(BaseTraceHierarchyType):

    # color
    # -----
    @property
    def color(self):
        """
        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color:
                aliceblue, antiquewhite, aqua, aquamarine, azure,
                beige, bisque, black, blanchedalmond, blue,
                blueviolet, brown, burlywood, cadetblue,
                chartreuse, chocolate, coral, cornflowerblue,
                cornsilk, crimson, cyan, darkblue, darkcyan,
                darkgoldenrod, darkgray, darkgrey, darkgreen,
                darkkhaki, darkmagenta, darkolivegreen, darkorange,
                darkorchid, darkred, darksalmon, darkseagreen,
                darkslateblue, darkslategray, darkslategrey,
                darkturquoise, darkviolet, deeppink, deepskyblue,
                dimgray, dimgrey, dodgerblue, firebrick,
                floralwhite, forestgreen, fuchsia, gainsboro,
                ghostwhite, gold, goldenrod, gray, grey, green,
                greenyellow, honeydew, hotpink, indianred, indigo,
                ivory, khaki, lavender, lavenderblush, lawngreen,
                lemonchiffon, lightblue, lightcoral, lightcyan,
                lightgoldenrodyellow, lightgray, lightgrey,
                lightgreen, lightpink, lightsalmon, lightseagreen,
                lightskyblue, lightslategray, lightslategrey,
                lightsteelblue, lightyellow, lime, limegreen,
                linen, magenta, maroon, mediumaquamarine,
                mediumblue, mediumorchid, mediumpurple,
                mediumseagreen, mediumslateblue, mediumspringgreen,
                mediumturquoise, mediumvioletred, midnightblue,
                mintcream, mistyrose, moccasin, navajowhite, navy,
                oldlace, olive, olivedrab, orange, orangered,
                orchid, palegoldenrod, palegreen, paleturquoise,
                palevioletred, papayawhip, peachpuff, peru, pink,
                plum, powderblue, purple, red, rosybrown,
                royalblue, saddlebrown, salmon, sandybrown,
                seagreen, seashell, sienna, silver, skyblue,
                slateblue, slategray, slategrey, snow, springgreen,
                steelblue, tan, teal, thistle, tomato, turquoise,
                violet, wheat, white, whitesmoke, yellow,
                yellowgreen
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # colorsrc
    # --------
    @property
    def colorsrc(self):
        """
        Sets the source reference on plot.ly for  color .
    
        The 'colorsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['colorsrc']

    @colorsrc.setter
    def colorsrc(self, val):
        self['colorsrc'] = val

    # family
    # ------
    @property
    def family(self):
        """
        HTML font family - the typeface that will be applied by the web
        browser. The web browser will only be able to apply a font if
        it is available on the system which it operates. Provide
        multiple font families, separated by commas, to indicate the
        preference in which to apply fonts if they aren't available on
        the system. The plotly service (at https://plot.ly or on-
        premise) generates images on a server, where only a select
        number of fonts are installed and supported. These include
        *Arial*, *Balto*, *Courier New*, *Droid Sans*,, *Droid Serif*,
        *Droid Sans Mono*, *Gravitas One*, *Old Standard TT*, *Open
        Sans*, *Overpass*, *PT Sans Narrow*, *Raleway*, *Times New
        Roman*.
    
        The 'family' property is a string and must be specified as:
          - A non-empty string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        return self['family']

    @family.setter
    def family(self, val):
        self['family'] = val

    # familysrc
    # ---------
    @property
    def familysrc(self):
        """
        Sets the source reference on plot.ly for  family .
    
        The 'familysrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['familysrc']

    @familysrc.setter
    def familysrc(self, val):
        self['familysrc'] = val

    # size
    # ----
    @property
    def size(self):
        """
        The 'size' property is a number and may be specified as:
          - An int or float in the interval [1, inf]
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        int|float|numpy.ndarray
        """
        return self['size']

    @size.setter
    def size(self, val):
        self['size'] = val

    # sizesrc
    # -------
    @property
    def sizesrc(self):
        """
        Sets the source reference on plot.ly for  size .
    
        The 'sizesrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['sizesrc']

    @sizesrc.setter
    def sizesrc(self, val):
        self['sizesrc'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'pointcloud.hoverlabel'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        color

        colorsrc
            Sets the source reference on plot.ly for  color .
        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The
            plotly service (at https://plot.ly or on-premise)
            generates images on a server, where only a select
            number of fonts are installed and supported. These
            include *Arial*, *Balto*, *Courier New*, *Droid Sans*,,
            *Droid Serif*, *Droid Sans Mono*, *Gravitas One*, *Old
            Standard TT*, *Open Sans*, *Overpass*, *PT Sans
            Narrow*, *Raleway*, *Times New Roman*.
        familysrc
            Sets the source reference on plot.ly for  family .
        size

        sizesrc
            Sets the source reference on plot.ly for  size .
        """

    def __init__(
        self,
        color=None,
        colorsrc=None,
        family=None,
        familysrc=None,
        size=None,
        sizesrc=None,
        **kwargs
    ):
        """
        Construct a new Font object
        
        Sets the font used in hover labels.

        Parameters
        ----------
        color

        colorsrc
            Sets the source reference on plot.ly for  color .
        family
            HTML font family - the typeface that will be applied by
            the web browser. The web browser will only be able to
            apply a font if it is available on the system which it
            operates. Provide multiple font families, separated by
            commas, to indicate the preference in which to apply
            fonts if they aren't available on the system. The
            plotly service (at https://plot.ly or on-premise)
            generates images on a server, where only a select
            number of fonts are installed and supported. These
            include *Arial*, *Balto*, *Courier New*, *Droid Sans*,,
            *Droid Serif*, *Droid Sans Mono*, *Gravitas One*, *Old
            Standard TT*, *Open Sans*, *Overpass*, *PT Sans
            Narrow*, *Raleway*, *Times New Roman*.
        familysrc
            Sets the source reference on plot.ly for  family .
        size

        sizesrc
            Sets the source reference on plot.ly for  size .

        Returns
        -------
        Font
        """
        super(Font, self).__init__('font')

        # Import validators
        # -----------------
        from plotly.validators.pointcloud.hoverlabel import (font as v_font)

        # Initialize validators
        # ---------------------
        self._validators['color'] = v_font.ColorValidator()
        self._validators['colorsrc'] = v_font.ColorsrcValidator()
        self._validators['family'] = v_font.FamilyValidator()
        self._validators['familysrc'] = v_font.FamilysrcValidator()
        self._validators['size'] = v_font.SizeValidator()
        self._validators['sizesrc'] = v_font.SizesrcValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.color = color
        self.colorsrc = colorsrc
        self.family = family
        self.familysrc = familysrc
        self.size = size
        self.sizesrc = sizesrc

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
