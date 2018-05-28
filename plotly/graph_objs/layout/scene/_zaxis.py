from plotly.basedatatypes import BaseLayoutHierarchyType


class ZAxis(BaseLayoutHierarchyType):

    # autorange
    # ---------
    @property
    def autorange(self):
        """
        Determines whether or not the range of this axis is computed in
        relation to the input data. See `rangemode` for more info. If
        `range` is provided, then `autorange` is set to *false*.
    
        The 'autorange' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'reversed']

        Returns
        -------
        Any
        """
        return self['autorange']

    @autorange.setter
    def autorange(self, val):
        self['autorange'] = val

    # backgroundcolor
    # ---------------
    @property
    def backgroundcolor(self):
        """
        Sets the background color of this axis' wall.
    
        The 'backgroundcolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        return self['backgroundcolor']

    @backgroundcolor.setter
    def backgroundcolor(self, val):
        self['backgroundcolor'] = val

    # calendar
    # --------
    @property
    def calendar(self):
        """
        Sets the calendar system to use for `range` and `tick0` if this
        is a date axis. This does not set the calendar for interpreting
        data on this axis, that's specified in the trace or via the
        global `layout.calendar`
    
        The 'calendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['gregorian', 'chinese', 'coptic', 'discworld',
                'ethiopian', 'hebrew', 'islamic', 'julian', 'mayan',
                'nanakshahi', 'nepali', 'persian', 'jalali', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        return self['calendar']

    @calendar.setter
    def calendar(self, val):
        self['calendar'] = val

    # categoryarray
    # -------------
    @property
    def categoryarray(self):
        """
        Sets the order in which categories on this axis appear. Only
        has an effect if `categoryorder` is set to *array*. Used with
        `categoryorder`.
    
        The 'categoryarray' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['categoryarray']

    @categoryarray.setter
    def categoryarray(self, val):
        self['categoryarray'] = val

    # categoryarraysrc
    # ----------------
    @property
    def categoryarraysrc(self):
        """
        Sets the source reference on plot.ly for  categoryarray .
    
        The 'categoryarraysrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['categoryarraysrc']

    @categoryarraysrc.setter
    def categoryarraysrc(self, val):
        self['categoryarraysrc'] = val

    # categoryorder
    # -------------
    @property
    def categoryorder(self):
        """
        Specifies the ordering logic for the case of categorical
        variables. By default, plotly uses *trace*, which specifies the
        order that is present in the data supplied. Set `categoryorder`
        to *category ascending* or *category descending* if order
        should be determined by the alphanumerical order of the
        category names. Set `categoryorder` to *array* to derive the
        ordering from the attribute `categoryarray`. If a category is
        not found in the `categoryarray` array, the sorting behavior
        for that attribute will be identical to the *trace* mode. The
        unspecified categories will follow the categories in
        `categoryarray`.
    
        The 'categoryorder' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['trace', 'category ascending', 'category descending',
                'array']

        Returns
        -------
        Any
        """
        return self['categoryorder']

    @categoryorder.setter
    def categoryorder(self, val):
        self['categoryorder'] = val

    # color
    # -----
    @property
    def color(self):
        """
        Sets default for all colors associated with this axis all at
        once: line, font, tick, and grid colors. Grid color is
        lightened by blending this with the plot background Individual
        pieces can override this.
    
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

        Returns
        -------
        str
        """
        return self['color']

    @color.setter
    def color(self, val):
        self['color'] = val

    # dtick
    # -----
    @property
    def dtick(self):
        """
        Sets the step in-between ticks on this axis. Use with `tick0`.
        Must be a positive number, or special strings available to
        *log* and *date* axes. If the axis `type` is *log*, then ticks
        are set every 10^(n*dtick) where n is the tick number. For
        example, to set a tick mark at 1, 10, 100, 1000, ... set dtick
        to 1. To set tick marks at 1, 100, 10000, ... set dtick to 2.
        To set tick marks at 1, 5, 25, 125, 625, 3125, ... set dtick to
        log_10(5), or 0.69897000433. *log* has several special values;
        *L<f>*, where `f` is a positive number, gives ticks linearly
        spaced in value (but not position). For example `tick0` = 0.1,
        `dtick` = *L0.5* will put ticks at 0.1, 0.6, 1.1, 1.6 etc. To
        show powers of 10 plus small digits between, use *D1* (all
        digits) or *D2* (only 2 and 5). `tick0` is ignored for *D1* and
        *D2*. If the axis `type` is *date*, then you must convert the
        time to milliseconds. For example, to set the interval between
        ticks to one day, set `dtick` to 86400000.0. *date* also has
        special values *M<n>* gives ticks spaced by a number of months.
        `n` must be a positive integer. To set ticks on the 15th of
        every third month, set `tick0` to *2000-01-15* and `dtick` to
        *M3*. To set ticks every 4 years, set `dtick` to *M48*
    
        The 'dtick' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['dtick']

    @dtick.setter
    def dtick(self, val):
        self['dtick'] = val

    # exponentformat
    # --------------
    @property
    def exponentformat(self):
        """
        Determines a formatting rule for the tick exponents. For
        example, consider the number 1,000,000,000. If *none*, it
        appears as 1,000,000,000. If *e*, 1e+9. If *E*, 1E+9. If
        *power*, 1x10^9 (with 9 in a super script). If *SI*, 1G. If
        *B*, 1B.
    
        The 'exponentformat' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['none', 'e', 'E', 'power', 'SI', 'B']

        Returns
        -------
        Any
        """
        return self['exponentformat']

    @exponentformat.setter
    def exponentformat(self, val):
        self['exponentformat'] = val

    # gridcolor
    # ---------
    @property
    def gridcolor(self):
        """
        Sets the color of the grid lines.
    
        The 'gridcolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        return self['gridcolor']

    @gridcolor.setter
    def gridcolor(self, val):
        self['gridcolor'] = val

    # gridwidth
    # ---------
    @property
    def gridwidth(self):
        """
        Sets the width (in px) of the grid lines.
    
        The 'gridwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['gridwidth']

    @gridwidth.setter
    def gridwidth(self, val):
        self['gridwidth'] = val

    # hoverformat
    # -----------
    @property
    def hoverformat(self):
        """
        Sets the hover text formatting rule using d3 formatting mini-
        languages which are very similar to those in Python. For
        numbers, see: https://github.com/d3/d3-format/blob/master/READM
        E.md#locale_format And for dates see:
        https://github.com/d3/d3-time-
        format/blob/master/README.md#locale_format We add one item to
        d3's date formatter: *%{n}f* for fractional seconds with n
        digits. For example, *2016-10-13 09:15:23.456* with tickformat
        *%H~%M~%S.%2f* would display *09~15~23.46*
    
        The 'hoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['hoverformat']

    @hoverformat.setter
    def hoverformat(self, val):
        self['hoverformat'] = val

    # linecolor
    # ---------
    @property
    def linecolor(self):
        """
        Sets the axis line color.
    
        The 'linecolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        return self['linecolor']

    @linecolor.setter
    def linecolor(self, val):
        self['linecolor'] = val

    # linewidth
    # ---------
    @property
    def linewidth(self):
        """
        Sets the width (in px) of the axis line.
    
        The 'linewidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['linewidth']

    @linewidth.setter
    def linewidth(self, val):
        self['linewidth'] = val

    # mirror
    # ------
    @property
    def mirror(self):
        """
        Determines if the axis lines or/and ticks are mirrored to the
        opposite side of the plotting area. If *true*, the axis lines
        are mirrored. If *ticks*, the axis lines and ticks are
        mirrored. If *false*, mirroring is disable. If *all*, axis
        lines are mirrored on all shared-axes subplots. If *allticks*,
        axis lines and ticks are mirrored on all shared-axes subplots.
    
        The 'mirror' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, 'ticks', False, 'all', 'allticks']

        Returns
        -------
        Any
        """
        return self['mirror']

    @mirror.setter
    def mirror(self, val):
        self['mirror'] = val

    # nticks
    # ------
    @property
    def nticks(self):
        """
        Specifies the maximum number of ticks for the particular axis.
        The actual number of ticks will be chosen automatically to be
        less than or equal to `nticks`. Has an effect only if
        `tickmode` is set to *auto*.
    
        The 'nticks' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)
            in the interval [0, 9223372036854775807]

        Returns
        -------
        int
        """
        return self['nticks']

    @nticks.setter
    def nticks(self, val):
        self['nticks'] = val

    # range
    # -----
    @property
    def range(self):
        """
        Sets the range of this axis. If the axis `type` is *log*, then
        you must take the log of your desired range (e.g. to set the
        range from 1 to 100, set the range from 0 to 2). If the axis
        `type` is *date*, it should be date strings, like date data,
        though Date objects and unix milliseconds will be accepted and
        converted to strings. If the axis `type` is *category*, it
        should be numbers, using the scale where each category is
        assigned a serial number from zero in the order it appears.
    
        The 'range' property is an info array that may be specified as a
        list or tuple of 2 elements where:
    
    (0) The 'range[0]' property accepts values of any type
    (1) The 'range[1]' property accepts values of any type

        Returns
        -------
        list
        """
        return self['range']

    @range.setter
    def range(self, val):
        self['range'] = val

    # rangemode
    # ---------
    @property
    def rangemode(self):
        """
        If *normal*, the range is computed in relation to the extrema
        of the input data. If *tozero*`, the range extends to 0,
        regardless of the input data If *nonnegative*, the range is
        non-negative, regardless of the input data.
    
        The 'rangemode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['normal', 'tozero', 'nonnegative']

        Returns
        -------
        Any
        """
        return self['rangemode']

    @rangemode.setter
    def rangemode(self, val):
        self['rangemode'] = val

    # separatethousands
    # -----------------
    @property
    def separatethousands(self):
        """
        If "true", even 4-digit integers are separated
    
        The 'separatethousands' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['separatethousands']

    @separatethousands.setter
    def separatethousands(self, val):
        self['separatethousands'] = val

    # showaxeslabels
    # --------------
    @property
    def showaxeslabels(self):
        """
        Sets whether or not this axis is labeled
    
        The 'showaxeslabels' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showaxeslabels']

    @showaxeslabels.setter
    def showaxeslabels(self, val):
        self['showaxeslabels'] = val

    # showbackground
    # --------------
    @property
    def showbackground(self):
        """
        Sets whether or not this axis' wall has a background color.
    
        The 'showbackground' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showbackground']

    @showbackground.setter
    def showbackground(self, val):
        self['showbackground'] = val

    # showexponent
    # ------------
    @property
    def showexponent(self):
        """
        If *all*, all exponents are shown besides their significands.
        If *first*, only the exponent of the first tick is shown. If
        *last*, only the exponent of the last tick is shown. If *none*,
        no exponents appear.
    
        The 'showexponent' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self['showexponent']

    @showexponent.setter
    def showexponent(self, val):
        self['showexponent'] = val

    # showgrid
    # --------
    @property
    def showgrid(self):
        """
        Determines whether or not grid lines are drawn. If *true*, the
        grid lines are drawn at every tick mark.
    
        The 'showgrid' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showgrid']

    @showgrid.setter
    def showgrid(self, val):
        self['showgrid'] = val

    # showline
    # --------
    @property
    def showline(self):
        """
        Determines whether or not a line bounding this axis is drawn.
    
        The 'showline' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showline']

    @showline.setter
    def showline(self, val):
        self['showline'] = val

    # showspikes
    # ----------
    @property
    def showspikes(self):
        """
        Sets whether or not spikes starting from data points to this
        axis' wall are shown on hover.
    
        The 'showspikes' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showspikes']

    @showspikes.setter
    def showspikes(self, val):
        self['showspikes'] = val

    # showticklabels
    # --------------
    @property
    def showticklabels(self):
        """
        Determines whether or not the tick labels are drawn.
    
        The 'showticklabels' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['showticklabels']

    @showticklabels.setter
    def showticklabels(self, val):
        self['showticklabels'] = val

    # showtickprefix
    # --------------
    @property
    def showtickprefix(self):
        """
        If *all*, all tick labels are displayed with a prefix. If
        *first*, only the first tick is displayed with a prefix. If
        *last*, only the last tick is displayed with a suffix. If
        *none*, tick prefixes are hidden.
    
        The 'showtickprefix' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self['showtickprefix']

    @showtickprefix.setter
    def showtickprefix(self, val):
        self['showtickprefix'] = val

    # showticksuffix
    # --------------
    @property
    def showticksuffix(self):
        """
        Same as `showtickprefix` but for tick suffixes.
    
        The 'showticksuffix' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'first', 'last', 'none']

        Returns
        -------
        Any
        """
        return self['showticksuffix']

    @showticksuffix.setter
    def showticksuffix(self, val):
        self['showticksuffix'] = val

    # spikecolor
    # ----------
    @property
    def spikecolor(self):
        """
        Sets the color of the spikes.
    
        The 'spikecolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        return self['spikecolor']

    @spikecolor.setter
    def spikecolor(self, val):
        self['spikecolor'] = val

    # spikesides
    # ----------
    @property
    def spikesides(self):
        """
        Sets whether or not spikes extending from the projection data
        points to this axis' wall boundaries are shown on hover.
    
        The 'spikesides' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['spikesides']

    @spikesides.setter
    def spikesides(self, val):
        self['spikesides'] = val

    # spikethickness
    # --------------
    @property
    def spikethickness(self):
        """
        Sets the thickness (in px) of the spikes.
    
        The 'spikethickness' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['spikethickness']

    @spikethickness.setter
    def spikethickness(self, val):
        self['spikethickness'] = val

    # tick0
    # -----
    @property
    def tick0(self):
        """
        Sets the placement of the first tick on this axis. Use with
        `dtick`. If the axis `type` is *log*, then you must take the
        log of your starting tick (e.g. to set the starting tick to
        100, set the `tick0` to 2) except when `dtick`=*L<f>* (see
        `dtick` for more info). If the axis `type` is *date*, it should
        be a date string, like date data. If the axis `type` is
        *category*, it should be a number, using the scale where each
        category is assigned a serial number from zero in the order it
        appears.
    
        The 'tick0' property accepts values of any type

        Returns
        -------
        Any
        """
        return self['tick0']

    @tick0.setter
    def tick0(self, val):
        self['tick0'] = val

    # tickangle
    # ---------
    @property
    def tickangle(self):
        """
        Sets the angle of the tick labels with respect to the
        horizontal. For example, a `tickangle` of -90 draws the tick
        labels vertically.
    
        The 'tickangle' property is a angle (in degrees) that may be
        specified as a number between -180 and 180. Numeric values outside this
        range are converted to the equivalent value
        (e.g. 270 is converted to -90).

        Returns
        -------
        int|float
        """
        return self['tickangle']

    @tickangle.setter
    def tickangle(self, val):
        self['tickangle'] = val

    # tickcolor
    # ---------
    @property
    def tickcolor(self):
        """
        Sets the tick color.
    
        The 'tickcolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        return self['tickcolor']

    @tickcolor.setter
    def tickcolor(self, val):
        self['tickcolor'] = val

    # tickfont
    # --------
    @property
    def tickfont(self):
        """
        Sets the tick font.
    
        The 'tickfont' property is an instance of Tickfont
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.zaxis.Tickfont
          - A dict of string/value properties that will be passed
            to the Tickfont constructor
    
            Supported dict properties:
                
                color
    
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The plotly service (at https://plot.ly
                    or on-premise) generates images on a server,
                    where only a select number of fonts are
                    installed and supported. These include *Arial*,
                    *Balto*, *Courier New*, *Droid Sans*,, *Droid
                    Serif*, *Droid Sans Mono*, *Gravitas One*, *Old
                    Standard TT*, *Open Sans*, *Overpass*, *PT Sans
                    Narrow*, *Raleway*, *Times New Roman*.
                size

        Returns
        -------
        plotly.graph_objs.layout.scene.zaxis.Tickfont
        """
        return self['tickfont']

    @tickfont.setter
    def tickfont(self, val):
        self['tickfont'] = val

    # tickformat
    # ----------
    @property
    def tickformat(self):
        """
        Sets the tick label formatting rule using d3 formatting mini-
        languages which are very similar to those in Python. For
        numbers, see: https://github.com/d3/d3-format/blob/master/READM
        E.md#locale_format And for dates see:
        https://github.com/d3/d3-time-
        format/blob/master/README.md#locale_format We add one item to
        d3's date formatter: *%{n}f* for fractional seconds with n
        digits. For example, *2016-10-13 09:15:23.456* with tickformat
        *%H~%M~%S.%2f* would display *09~15~23.46*
    
        The 'tickformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['tickformat']

    @tickformat.setter
    def tickformat(self, val):
        self['tickformat'] = val

    # tickformatstops
    # ---------------
    @property
    def tickformatstops(self):
        """
        The 'tickformatstops' property is a tuple of instances of
        Tickformatstop that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.scene.zaxis.Tickformatstop
          - A list or tuple of dicts of string/value properties that
            will be passed to the Tickformatstop constructor
    
            Supported dict properties:
                
                dtickrange
                    range [*min*, *max*], where *min*, *max* -
                    dtick values which describe some zoom level, it
                    is possible to omit *min* or *max* value by
                    passing *null*
                value
                    string - dtickformat for described zoom level,
                    the same as *tickformat*

        Returns
        -------
        tuple[plotly.graph_objs.layout.scene.zaxis.Tickformatstop]
        """
        return self['tickformatstops']

    @tickformatstops.setter
    def tickformatstops(self, val):
        self['tickformatstops'] = val

    # ticklen
    # -------
    @property
    def ticklen(self):
        """
        Sets the tick length (in px).
    
        The 'ticklen' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['ticklen']

    @ticklen.setter
    def ticklen(self, val):
        self['ticklen'] = val

    # tickmode
    # --------
    @property
    def tickmode(self):
        """
        Sets the tick mode for this axis. If *auto*, the number of
        ticks is set via `nticks`. If *linear*, the placement of the
        ticks is determined by a starting position `tick0` and a tick
        step `dtick` (*linear* is the default value if `tick0` and
        `dtick` are provided). If *array*, the placement of the ticks
        is set via `tickvals` and the tick text is `ticktext`. (*array*
        is the default value if `tickvals` is provided).
    
        The 'tickmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'linear', 'array']

        Returns
        -------
        Any
        """
        return self['tickmode']

    @tickmode.setter
    def tickmode(self, val):
        self['tickmode'] = val

    # tickprefix
    # ----------
    @property
    def tickprefix(self):
        """
        Sets a tick label prefix.
    
        The 'tickprefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['tickprefix']

    @tickprefix.setter
    def tickprefix(self, val):
        self['tickprefix'] = val

    # ticks
    # -----
    @property
    def ticks(self):
        """
        Determines whether ticks are drawn or not. If **, this axis'
        ticks are not drawn. If *outside* (*inside*), this axis' are
        drawn outside (inside) the axis lines.
    
        The 'ticks' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['outside', 'inside', '']

        Returns
        -------
        Any
        """
        return self['ticks']

    @ticks.setter
    def ticks(self, val):
        self['ticks'] = val

    # ticksuffix
    # ----------
    @property
    def ticksuffix(self):
        """
        Sets a tick label suffix.
    
        The 'ticksuffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['ticksuffix']

    @ticksuffix.setter
    def ticksuffix(self, val):
        self['ticksuffix'] = val

    # ticktext
    # --------
    @property
    def ticktext(self):
        """
        Sets the text displayed at the ticks position via `tickvals`.
        Only has an effect if `tickmode` is set to *array*. Used with
        `tickvals`.
    
        The 'ticktext' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['ticktext']

    @ticktext.setter
    def ticktext(self, val):
        self['ticktext'] = val

    # ticktextsrc
    # -----------
    @property
    def ticktextsrc(self):
        """
        Sets the source reference on plot.ly for  ticktext .
    
        The 'ticktextsrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['ticktextsrc']

    @ticktextsrc.setter
    def ticktextsrc(self, val):
        self['ticktextsrc'] = val

    # tickvals
    # --------
    @property
    def tickvals(self):
        """
        Sets the values at which ticks on this axis appear. Only has an
        effect if `tickmode` is set to *array*. Used with `ticktext`.
    
        The 'tickvals' property is an array that may be specified as a tuple,
        list, one-dimensional numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['tickvals']

    @tickvals.setter
    def tickvals(self, val):
        self['tickvals'] = val

    # tickvalssrc
    # -----------
    @property
    def tickvalssrc(self):
        """
        Sets the source reference on plot.ly for  tickvals .
    
        The 'tickvalssrc' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['tickvalssrc']

    @tickvalssrc.setter
    def tickvalssrc(self, val):
        self['tickvalssrc'] = val

    # tickwidth
    # ---------
    @property
    def tickwidth(self):
        """
        Sets the tick width (in px).
    
        The 'tickwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        return self['tickwidth']

    @tickwidth.setter
    def tickwidth(self, val):
        self['tickwidth'] = val

    # title
    # -----
    @property
    def title(self):
        """
        Sets the title of this axis.
    
        The 'title' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['title']

    @title.setter
    def title(self, val):
        self['title'] = val

    # titlefont
    # ---------
    @property
    def titlefont(self):
        """
        Sets this axis' title font.
    
        The 'titlefont' property is an instance of Titlefont
        that may be specified as:
          - An instance of plotly.graph_objs.layout.scene.zaxis.Titlefont
          - A dict of string/value properties that will be passed
            to the Titlefont constructor
    
            Supported dict properties:
                
                color
    
                family
                    HTML font family - the typeface that will be
                    applied by the web browser. The web browser
                    will only be able to apply a font if it is
                    available on the system which it operates.
                    Provide multiple font families, separated by
                    commas, to indicate the preference in which to
                    apply fonts if they aren't available on the
                    system. The plotly service (at https://plot.ly
                    or on-premise) generates images on a server,
                    where only a select number of fonts are
                    installed and supported. These include *Arial*,
                    *Balto*, *Courier New*, *Droid Sans*,, *Droid
                    Serif*, *Droid Sans Mono*, *Gravitas One*, *Old
                    Standard TT*, *Open Sans*, *Overpass*, *PT Sans
                    Narrow*, *Raleway*, *Times New Roman*.
                size

        Returns
        -------
        plotly.graph_objs.layout.scene.zaxis.Titlefont
        """
        return self['titlefont']

    @titlefont.setter
    def titlefont(self, val):
        self['titlefont'] = val

    # type
    # ----
    @property
    def type(self):
        """
        Sets the axis type. By default, plotly attempts to determined
        the axis type by looking into the data of the traces that
        referenced the axis in question.
    
        The 'type' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['-', 'linear', 'log', 'date', 'category']

        Returns
        -------
        Any
        """
        return self['type']

    @type.setter
    def type(self, val):
        self['type'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        A single toggle to hide the axis while preserving interaction
        like dragging. Default is true when a cheater plot is present
        on the axis, otherwise false
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # zeroline
    # --------
    @property
    def zeroline(self):
        """
        Determines whether or not a line is drawn at along the 0 value
        of this axis. If *true*, the zero line is drawn on top of the
        grid lines.
    
        The 'zeroline' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['zeroline']

    @zeroline.setter
    def zeroline(self, val):
        self['zeroline'] = val

    # zerolinecolor
    # -------------
    @property
    def zerolinecolor(self):
        """
        Sets the line color of the zero line.
    
        The 'zerolinecolor' property is a color and may be specified as:
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

        Returns
        -------
        str
        """
        return self['zerolinecolor']

    @zerolinecolor.setter
    def zerolinecolor(self, val):
        self['zerolinecolor'] = val

    # zerolinewidth
    # -------------
    @property
    def zerolinewidth(self):
        """
        Sets the width (in px) of the zero line.
    
        The 'zerolinewidth' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        return self['zerolinewidth']

    @zerolinewidth.setter
    def zerolinewidth(self, val):
        self['zerolinewidth'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'layout.scene'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        autorange
            Determines whether or not the range of this axis is
            computed in relation to the input data. See `rangemode`
            for more info. If `range` is provided, then `autorange`
            is set to *false*.
        backgroundcolor
            Sets the background color of this axis' wall.
        calendar
            Sets the calendar system to use for `range` and `tick0`
            if this is a date axis. This does not set the calendar
            for interpreting data on this axis, that's specified in
            the trace or via the global `layout.calendar`
        categoryarray
            Sets the order in which categories on this axis appear.
            Only has an effect if `categoryorder` is set to
            *array*. Used with `categoryorder`.
        categoryarraysrc
            Sets the source reference on plot.ly for  categoryarray
            .
        categoryorder
            Specifies the ordering logic for the case of
            categorical variables. By default, plotly uses *trace*,
            which specifies the order that is present in the data
            supplied. Set `categoryorder` to *category ascending*
            or *category descending* if order should be determined
            by the alphanumerical order of the category names. Set
            `categoryorder` to *array* to derive the ordering from
            the attribute `categoryarray`. If a category is not
            found in the `categoryarray` array, the sorting
            behavior for that attribute will be identical to the
            *trace* mode. The unspecified categories will follow
            the categories in `categoryarray`.
        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        dtick
            Sets the step in-between ticks on this axis. Use with
            `tick0`. Must be a positive number, or special strings
            available to *log* and *date* axes. If the axis `type`
            is *log*, then ticks are set every 10^(n*dtick) where n
            is the tick number. For example, to set a tick mark at
            1, 10, 100, 1000, ... set dtick to 1. To set tick marks
            at 1, 100, 10000, ... set dtick to 2. To set tick marks
            at 1, 5, 25, 125, 625, 3125, ... set dtick to
            log_10(5), or 0.69897000433. *log* has several special
            values; *L<f>*, where `f` is a positive number, gives
            ticks linearly spaced in value (but not position). For
            example `tick0` = 0.1, `dtick` = *L0.5* will put ticks
            at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10 plus
            small digits between, use *D1* (all digits) or *D2*
            (only 2 and 5). `tick0` is ignored for *D1* and *D2*.
            If the axis `type` is *date*, then you must convert the
            time to milliseconds. For example, to set the interval
            between ticks to one day, set `dtick` to 86400000.0.
            *date* also has special values *M<n>* gives ticks
            spaced by a number of months. `n` must be a positive
            integer. To set ticks on the 15th of every third month,
            set `tick0` to *2000-01-15* and `dtick` to *M3*. To set
            ticks every 4 years, set `dtick` to *M48*
        exponentformat
            Determines a formatting rule for the tick exponents.
            For example, consider the number 1,000,000,000. If
            *none*, it appears as 1,000,000,000. If *e*, 1e+9. If
            *E*, 1E+9. If *power*, 1x10^9 (with 9 in a super
            script). If *SI*, 1G. If *B*, 1B.
        gridcolor
            Sets the color of the grid lines.
        gridwidth
            Sets the width (in px) of the grid lines.
        hoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see: https://github.com/d3/d3-form
            at/blob/master/README.md#locale_format And for dates
            see: https://github.com/d3/d3-time-
            format/blob/master/README.md#locale_format We add one
            item to d3's date formatter: *%{n}f* for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat *%H~%M~%S.%2f* would
            display *09~15~23.46*
        linecolor
            Sets the axis line color.
        linewidth
            Sets the width (in px) of the axis line.
        mirror
            Determines if the axis lines or/and ticks are mirrored
            to the opposite side of the plotting area. If *true*,
            the axis lines are mirrored. If *ticks*, the axis lines
            and ticks are mirrored. If *false*, mirroring is
            disable. If *all*, axis lines are mirrored on all
            shared-axes subplots. If *allticks*, axis lines and
            ticks are mirrored on all shared-axes subplots.
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            *auto*.
        range
            Sets the range of this axis. If the axis `type` is
            *log*, then you must take the log of your desired range
            (e.g. to set the range from 1 to 100, set the range
            from 0 to 2). If the axis `type` is *date*, it should
            be date strings, like date data, though Date objects
            and unix milliseconds will be accepted and converted to
            strings. If the axis `type` is *category*, it should be
            numbers, using the scale where each category is
            assigned a serial number from zero in the order it
            appears.
        rangemode
            If *normal*, the range is computed in relation to the
            extrema of the input data. If *tozero*`, the range
            extends to 0, regardless of the input data If
            *nonnegative*, the range is non-negative, regardless of
            the input data.
        separatethousands
            If "true", even 4-digit integers are separated
        showaxeslabels
            Sets whether or not this axis is labeled
        showbackground
            Sets whether or not this axis' wall has a background
            color.
        showexponent
            If *all*, all exponents are shown besides their
            significands. If *first*, only the exponent of the
            first tick is shown. If *last*, only the exponent of
            the last tick is shown. If *none*, no exponents appear.
        showgrid
            Determines whether or not grid lines are drawn. If
            *true*, the grid lines are drawn at every tick mark.
        showline
            Determines whether or not a line bounding this axis is
            drawn.
        showspikes
            Sets whether or not spikes starting from data points to
            this axis' wall are shown on hover.
        showticklabels
            Determines whether or not the tick labels are drawn.
        showtickprefix
            If *all*, all tick labels are displayed with a prefix.
            If *first*, only the first tick is displayed with a
            prefix. If *last*, only the last tick is displayed with
            a suffix. If *none*, tick prefixes are hidden.
        showticksuffix
            Same as `showtickprefix` but for tick suffixes.
        spikecolor
            Sets the color of the spikes.
        spikesides
            Sets whether or not spikes extending from the
            projection data points to this axis' wall boundaries
            are shown on hover.
        spikethickness
            Sets the thickness (in px) of the spikes.
        tick0
            Sets the placement of the first tick on this axis. Use
            with `dtick`. If the axis `type` is *log*, then you
            must take the log of your starting tick (e.g. to set
            the starting tick to 100, set the `tick0` to 2) except
            when `dtick`=*L<f>* (see `dtick` for more info). If the
            axis `type` is *date*, it should be a date string, like
            date data. If the axis `type` is *category*, it should
            be a number, using the scale where each category is
            assigned a serial number from zero in the order it
            appears.
        tickangle
            Sets the angle of the tick labels with respect to the
            horizontal. For example, a `tickangle` of -90 draws the
            tick labels vertically.
        tickcolor
            Sets the tick color.
        tickfont
            Sets the tick font.
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see: https://github.com/d3/d3-form
            at/blob/master/README.md#locale_format And for dates
            see: https://github.com/d3/d3-time-
            format/blob/master/README.md#locale_format We add one
            item to d3's date formatter: *%{n}f* for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat *%H~%M~%S.%2f* would
            display *09~15~23.46*
        tickformatstops
            plotly.graph_objs.layout.scene.zaxis.Tickformatstop
            instance or dict with compatible properties
        ticklen
            Sets the tick length (in px).
        tickmode
            Sets the tick mode for this axis. If *auto*, the number
            of ticks is set via `nticks`. If *linear*, the
            placement of the ticks is determined by a starting
            position `tick0` and a tick step `dtick` (*linear* is
            the default value if `tick0` and `dtick` are provided).
            If *array*, the placement of the ticks is set via
            `tickvals` and the tick text is `ticktext`. (*array* is
            the default value if `tickvals` is provided).
        tickprefix
            Sets a tick label prefix.
        ticks
            Determines whether ticks are drawn or not. If **, this
            axis' ticks are not drawn. If *outside* (*inside*),
            this axis' are drawn outside (inside) the axis lines.
        ticksuffix
            Sets a tick label suffix.
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            *array*. Used with `tickvals`.
        ticktextsrc
            Sets the source reference on plot.ly for  ticktext .
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to *array*.
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on plot.ly for  tickvals .
        tickwidth
            Sets the tick width (in px).
        title
            Sets the title of this axis.
        titlefont
            Sets this axis' title font.
        type
            Sets the axis type. By default, plotly attempts to
            determined the axis type by looking into the data of
            the traces that referenced the axis in question.
        visible
            A single toggle to hide the axis while preserving
            interaction like dragging. Default is true when a
            cheater plot is present on the axis, otherwise false
        zeroline
            Determines whether or not a line is drawn at along the
            0 value of this axis. If *true*, the zero line is drawn
            on top of the grid lines.
        zerolinecolor
            Sets the line color of the zero line.
        zerolinewidth
            Sets the width (in px) of the zero line.
        """

    def __init__(
        self,
        autorange=None,
        backgroundcolor=None,
        calendar=None,
        categoryarray=None,
        categoryarraysrc=None,
        categoryorder=None,
        color=None,
        dtick=None,
        exponentformat=None,
        gridcolor=None,
        gridwidth=None,
        hoverformat=None,
        linecolor=None,
        linewidth=None,
        mirror=None,
        nticks=None,
        range=None,
        rangemode=None,
        separatethousands=None,
        showaxeslabels=None,
        showbackground=None,
        showexponent=None,
        showgrid=None,
        showline=None,
        showspikes=None,
        showticklabels=None,
        showtickprefix=None,
        showticksuffix=None,
        spikecolor=None,
        spikesides=None,
        spikethickness=None,
        tick0=None,
        tickangle=None,
        tickcolor=None,
        tickfont=None,
        tickformat=None,
        tickformatstops=None,
        ticklen=None,
        tickmode=None,
        tickprefix=None,
        ticks=None,
        ticksuffix=None,
        ticktext=None,
        ticktextsrc=None,
        tickvals=None,
        tickvalssrc=None,
        tickwidth=None,
        title=None,
        titlefont=None,
        type=None,
        visible=None,
        zeroline=None,
        zerolinecolor=None,
        zerolinewidth=None,
        **kwargs
    ):
        """
        Construct a new ZAxis object
        
        Parameters
        ----------
        autorange
            Determines whether or not the range of this axis is
            computed in relation to the input data. See `rangemode`
            for more info. If `range` is provided, then `autorange`
            is set to *false*.
        backgroundcolor
            Sets the background color of this axis' wall.
        calendar
            Sets the calendar system to use for `range` and `tick0`
            if this is a date axis. This does not set the calendar
            for interpreting data on this axis, that's specified in
            the trace or via the global `layout.calendar`
        categoryarray
            Sets the order in which categories on this axis appear.
            Only has an effect if `categoryorder` is set to
            *array*. Used with `categoryorder`.
        categoryarraysrc
            Sets the source reference on plot.ly for  categoryarray
            .
        categoryorder
            Specifies the ordering logic for the case of
            categorical variables. By default, plotly uses *trace*,
            which specifies the order that is present in the data
            supplied. Set `categoryorder` to *category ascending*
            or *category descending* if order should be determined
            by the alphanumerical order of the category names. Set
            `categoryorder` to *array* to derive the ordering from
            the attribute `categoryarray`. If a category is not
            found in the `categoryarray` array, the sorting
            behavior for that attribute will be identical to the
            *trace* mode. The unspecified categories will follow
            the categories in `categoryarray`.
        color
            Sets default for all colors associated with this axis
            all at once: line, font, tick, and grid colors. Grid
            color is lightened by blending this with the plot
            background Individual pieces can override this.
        dtick
            Sets the step in-between ticks on this axis. Use with
            `tick0`. Must be a positive number, or special strings
            available to *log* and *date* axes. If the axis `type`
            is *log*, then ticks are set every 10^(n*dtick) where n
            is the tick number. For example, to set a tick mark at
            1, 10, 100, 1000, ... set dtick to 1. To set tick marks
            at 1, 100, 10000, ... set dtick to 2. To set tick marks
            at 1, 5, 25, 125, 625, 3125, ... set dtick to
            log_10(5), or 0.69897000433. *log* has several special
            values; *L<f>*, where `f` is a positive number, gives
            ticks linearly spaced in value (but not position). For
            example `tick0` = 0.1, `dtick` = *L0.5* will put ticks
            at 0.1, 0.6, 1.1, 1.6 etc. To show powers of 10 plus
            small digits between, use *D1* (all digits) or *D2*
            (only 2 and 5). `tick0` is ignored for *D1* and *D2*.
            If the axis `type` is *date*, then you must convert the
            time to milliseconds. For example, to set the interval
            between ticks to one day, set `dtick` to 86400000.0.
            *date* also has special values *M<n>* gives ticks
            spaced by a number of months. `n` must be a positive
            integer. To set ticks on the 15th of every third month,
            set `tick0` to *2000-01-15* and `dtick` to *M3*. To set
            ticks every 4 years, set `dtick` to *M48*
        exponentformat
            Determines a formatting rule for the tick exponents.
            For example, consider the number 1,000,000,000. If
            *none*, it appears as 1,000,000,000. If *e*, 1e+9. If
            *E*, 1E+9. If *power*, 1x10^9 (with 9 in a super
            script). If *SI*, 1G. If *B*, 1B.
        gridcolor
            Sets the color of the grid lines.
        gridwidth
            Sets the width (in px) of the grid lines.
        hoverformat
            Sets the hover text formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see: https://github.com/d3/d3-form
            at/blob/master/README.md#locale_format And for dates
            see: https://github.com/d3/d3-time-
            format/blob/master/README.md#locale_format We add one
            item to d3's date formatter: *%{n}f* for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat *%H~%M~%S.%2f* would
            display *09~15~23.46*
        linecolor
            Sets the axis line color.
        linewidth
            Sets the width (in px) of the axis line.
        mirror
            Determines if the axis lines or/and ticks are mirrored
            to the opposite side of the plotting area. If *true*,
            the axis lines are mirrored. If *ticks*, the axis lines
            and ticks are mirrored. If *false*, mirroring is
            disable. If *all*, axis lines are mirrored on all
            shared-axes subplots. If *allticks*, axis lines and
            ticks are mirrored on all shared-axes subplots.
        nticks
            Specifies the maximum number of ticks for the
            particular axis. The actual number of ticks will be
            chosen automatically to be less than or equal to
            `nticks`. Has an effect only if `tickmode` is set to
            *auto*.
        range
            Sets the range of this axis. If the axis `type` is
            *log*, then you must take the log of your desired range
            (e.g. to set the range from 1 to 100, set the range
            from 0 to 2). If the axis `type` is *date*, it should
            be date strings, like date data, though Date objects
            and unix milliseconds will be accepted and converted to
            strings. If the axis `type` is *category*, it should be
            numbers, using the scale where each category is
            assigned a serial number from zero in the order it
            appears.
        rangemode
            If *normal*, the range is computed in relation to the
            extrema of the input data. If *tozero*`, the range
            extends to 0, regardless of the input data If
            *nonnegative*, the range is non-negative, regardless of
            the input data.
        separatethousands
            If "true", even 4-digit integers are separated
        showaxeslabels
            Sets whether or not this axis is labeled
        showbackground
            Sets whether or not this axis' wall has a background
            color.
        showexponent
            If *all*, all exponents are shown besides their
            significands. If *first*, only the exponent of the
            first tick is shown. If *last*, only the exponent of
            the last tick is shown. If *none*, no exponents appear.
        showgrid
            Determines whether or not grid lines are drawn. If
            *true*, the grid lines are drawn at every tick mark.
        showline
            Determines whether or not a line bounding this axis is
            drawn.
        showspikes
            Sets whether or not spikes starting from data points to
            this axis' wall are shown on hover.
        showticklabels
            Determines whether or not the tick labels are drawn.
        showtickprefix
            If *all*, all tick labels are displayed with a prefix.
            If *first*, only the first tick is displayed with a
            prefix. If *last*, only the last tick is displayed with
            a suffix. If *none*, tick prefixes are hidden.
        showticksuffix
            Same as `showtickprefix` but for tick suffixes.
        spikecolor
            Sets the color of the spikes.
        spikesides
            Sets whether or not spikes extending from the
            projection data points to this axis' wall boundaries
            are shown on hover.
        spikethickness
            Sets the thickness (in px) of the spikes.
        tick0
            Sets the placement of the first tick on this axis. Use
            with `dtick`. If the axis `type` is *log*, then you
            must take the log of your starting tick (e.g. to set
            the starting tick to 100, set the `tick0` to 2) except
            when `dtick`=*L<f>* (see `dtick` for more info). If the
            axis `type` is *date*, it should be a date string, like
            date data. If the axis `type` is *category*, it should
            be a number, using the scale where each category is
            assigned a serial number from zero in the order it
            appears.
        tickangle
            Sets the angle of the tick labels with respect to the
            horizontal. For example, a `tickangle` of -90 draws the
            tick labels vertically.
        tickcolor
            Sets the tick color.
        tickfont
            Sets the tick font.
        tickformat
            Sets the tick label formatting rule using d3 formatting
            mini-languages which are very similar to those in
            Python. For numbers, see: https://github.com/d3/d3-form
            at/blob/master/README.md#locale_format And for dates
            see: https://github.com/d3/d3-time-
            format/blob/master/README.md#locale_format We add one
            item to d3's date formatter: *%{n}f* for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat *%H~%M~%S.%2f* would
            display *09~15~23.46*
        tickformatstops
            plotly.graph_objs.layout.scene.zaxis.Tickformatstop
            instance or dict with compatible properties
        ticklen
            Sets the tick length (in px).
        tickmode
            Sets the tick mode for this axis. If *auto*, the number
            of ticks is set via `nticks`. If *linear*, the
            placement of the ticks is determined by a starting
            position `tick0` and a tick step `dtick` (*linear* is
            the default value if `tick0` and `dtick` are provided).
            If *array*, the placement of the ticks is set via
            `tickvals` and the tick text is `ticktext`. (*array* is
            the default value if `tickvals` is provided).
        tickprefix
            Sets a tick label prefix.
        ticks
            Determines whether ticks are drawn or not. If **, this
            axis' ticks are not drawn. If *outside* (*inside*),
            this axis' are drawn outside (inside) the axis lines.
        ticksuffix
            Sets a tick label suffix.
        ticktext
            Sets the text displayed at the ticks position via
            `tickvals`. Only has an effect if `tickmode` is set to
            *array*. Used with `tickvals`.
        ticktextsrc
            Sets the source reference on plot.ly for  ticktext .
        tickvals
            Sets the values at which ticks on this axis appear.
            Only has an effect if `tickmode` is set to *array*.
            Used with `ticktext`.
        tickvalssrc
            Sets the source reference on plot.ly for  tickvals .
        tickwidth
            Sets the tick width (in px).
        title
            Sets the title of this axis.
        titlefont
            Sets this axis' title font.
        type
            Sets the axis type. By default, plotly attempts to
            determined the axis type by looking into the data of
            the traces that referenced the axis in question.
        visible
            A single toggle to hide the axis while preserving
            interaction like dragging. Default is true when a
            cheater plot is present on the axis, otherwise false
        zeroline
            Determines whether or not a line is drawn at along the
            0 value of this axis. If *true*, the zero line is drawn
            on top of the grid lines.
        zerolinecolor
            Sets the line color of the zero line.
        zerolinewidth
            Sets the width (in px) of the zero line.

        Returns
        -------
        ZAxis
        """
        super(ZAxis, self).__init__('zaxis')

        # Import validators
        # -----------------
        from plotly.validators.layout.scene import (zaxis as v_zaxis)

        # Initialize validators
        # ---------------------
        self._validators['autorange'] = v_zaxis.AutorangeValidator()
        self._validators['backgroundcolor'
                        ] = v_zaxis.BackgroundcolorValidator()
        self._validators['calendar'] = v_zaxis.CalendarValidator()
        self._validators['categoryarray'] = v_zaxis.CategoryarrayValidator()
        self._validators['categoryarraysrc'
                        ] = v_zaxis.CategoryarraysrcValidator()
        self._validators['categoryorder'] = v_zaxis.CategoryorderValidator()
        self._validators['color'] = v_zaxis.ColorValidator()
        self._validators['dtick'] = v_zaxis.DtickValidator()
        self._validators['exponentformat'] = v_zaxis.ExponentformatValidator()
        self._validators['gridcolor'] = v_zaxis.GridcolorValidator()
        self._validators['gridwidth'] = v_zaxis.GridwidthValidator()
        self._validators['hoverformat'] = v_zaxis.HoverformatValidator()
        self._validators['linecolor'] = v_zaxis.LinecolorValidator()
        self._validators['linewidth'] = v_zaxis.LinewidthValidator()
        self._validators['mirror'] = v_zaxis.MirrorValidator()
        self._validators['nticks'] = v_zaxis.NticksValidator()
        self._validators['range'] = v_zaxis.RangeValidator()
        self._validators['rangemode'] = v_zaxis.RangemodeValidator()
        self._validators['separatethousands'
                        ] = v_zaxis.SeparatethousandsValidator()
        self._validators['showaxeslabels'] = v_zaxis.ShowaxeslabelsValidator()
        self._validators['showbackground'] = v_zaxis.ShowbackgroundValidator()
        self._validators['showexponent'] = v_zaxis.ShowexponentValidator()
        self._validators['showgrid'] = v_zaxis.ShowgridValidator()
        self._validators['showline'] = v_zaxis.ShowlineValidator()
        self._validators['showspikes'] = v_zaxis.ShowspikesValidator()
        self._validators['showticklabels'] = v_zaxis.ShowticklabelsValidator()
        self._validators['showtickprefix'] = v_zaxis.ShowtickprefixValidator()
        self._validators['showticksuffix'] = v_zaxis.ShowticksuffixValidator()
        self._validators['spikecolor'] = v_zaxis.SpikecolorValidator()
        self._validators['spikesides'] = v_zaxis.SpikesidesValidator()
        self._validators['spikethickness'] = v_zaxis.SpikethicknessValidator()
        self._validators['tick0'] = v_zaxis.Tick0Validator()
        self._validators['tickangle'] = v_zaxis.TickangleValidator()
        self._validators['tickcolor'] = v_zaxis.TickcolorValidator()
        self._validators['tickfont'] = v_zaxis.TickfontValidator()
        self._validators['tickformat'] = v_zaxis.TickformatValidator()
        self._validators['tickformatstops'
                        ] = v_zaxis.TickformatstopsValidator()
        self._validators['ticklen'] = v_zaxis.TicklenValidator()
        self._validators['tickmode'] = v_zaxis.TickmodeValidator()
        self._validators['tickprefix'] = v_zaxis.TickprefixValidator()
        self._validators['ticks'] = v_zaxis.TicksValidator()
        self._validators['ticksuffix'] = v_zaxis.TicksuffixValidator()
        self._validators['ticktext'] = v_zaxis.TicktextValidator()
        self._validators['ticktextsrc'] = v_zaxis.TicktextsrcValidator()
        self._validators['tickvals'] = v_zaxis.TickvalsValidator()
        self._validators['tickvalssrc'] = v_zaxis.TickvalssrcValidator()
        self._validators['tickwidth'] = v_zaxis.TickwidthValidator()
        self._validators['title'] = v_zaxis.TitleValidator()
        self._validators['titlefont'] = v_zaxis.TitlefontValidator()
        self._validators['type'] = v_zaxis.TypeValidator()
        self._validators['visible'] = v_zaxis.VisibleValidator()
        self._validators['zeroline'] = v_zaxis.ZerolineValidator()
        self._validators['zerolinecolor'] = v_zaxis.ZerolinecolorValidator()
        self._validators['zerolinewidth'] = v_zaxis.ZerolinewidthValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.autorange = autorange
        self.backgroundcolor = backgroundcolor
        self.calendar = calendar
        self.categoryarray = categoryarray
        self.categoryarraysrc = categoryarraysrc
        self.categoryorder = categoryorder
        self.color = color
        self.dtick = dtick
        self.exponentformat = exponentformat
        self.gridcolor = gridcolor
        self.gridwidth = gridwidth
        self.hoverformat = hoverformat
        self.linecolor = linecolor
        self.linewidth = linewidth
        self.mirror = mirror
        self.nticks = nticks
        self.range = range
        self.rangemode = rangemode
        self.separatethousands = separatethousands
        self.showaxeslabels = showaxeslabels
        self.showbackground = showbackground
        self.showexponent = showexponent
        self.showgrid = showgrid
        self.showline = showline
        self.showspikes = showspikes
        self.showticklabels = showticklabels
        self.showtickprefix = showtickprefix
        self.showticksuffix = showticksuffix
        self.spikecolor = spikecolor
        self.spikesides = spikesides
        self.spikethickness = spikethickness
        self.tick0 = tick0
        self.tickangle = tickangle
        self.tickcolor = tickcolor
        self.tickfont = tickfont
        self.tickformat = tickformat
        self.tickformatstops = tickformatstops
        self.ticklen = ticklen
        self.tickmode = tickmode
        self.tickprefix = tickprefix
        self.ticks = ticks
        self.ticksuffix = ticksuffix
        self.ticktext = ticktext
        self.ticktextsrc = ticktextsrc
        self.tickvals = tickvals
        self.tickvalssrc = tickvalssrc
        self.tickwidth = tickwidth
        self.title = title
        self.titlefont = titlefont
        self.type = type
        self.visible = visible
        self.zeroline = zeroline
        self.zerolinecolor = zerolinecolor
        self.zerolinewidth = zerolinewidth

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)
