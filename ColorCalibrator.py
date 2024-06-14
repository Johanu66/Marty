class ColorCalibrator:
    colors1 = {}
    colors2 = {}

    @staticmethod
    def hex_to_rgb(hex_color):
        """
        Converts a hexadecimal color string to an RGB tuple.
        
        :param hex_color: Hexadecimal color string.
        :return: Tuple of (R, G, B).
        """
        if hex_color is None:
            raise ValueError("Invalid color: None")
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb_to_hex(rgb_color):
        """
        Converts an RGB tuple to a hexadecimal color string.
        
        :param rgb_color: Tuple of (R, G, B).
        :return: Hexadecimal color string.
        """
        return '#{:02x}{:02x}{:02x}'.format(*rgb_color)

    @staticmethod
    def clamp(value, min_value=0, max_value=255):
        """
        Clamps a value between a minimum and maximum value.
        
        :param value: Value to clamp.
        :param min_value: Minimum value.
        :param max_value: Maximum value.
        :return: Clamped value.
        """
        return max(min_value, min(value, max_value))

    @staticmethod
    def create_color_interval(hex_color, delta):
        """
        Creates a color interval around a given hex color with a specified tolerance.
        
        :param hex_color: Hexadecimal color string.
        :param delta: Tolerance for the interval.
        :return: Tuple of (min_color, max_color) in hex.
        """
        r, g, b = ColorCalibrator.hex_to_rgb(hex_color)
        
        r_min = ColorCalibrator.clamp(r - delta)
        r_max = ColorCalibrator.clamp(r + delta)
        g_min = ColorCalibrator.clamp(g - delta)
        g_max = ColorCalibrator.clamp(g + delta)
        b_min = ColorCalibrator.clamp(b - delta)
        b_max = ColorCalibrator.clamp(b + delta)
        
        min_color = ColorCalibrator.rgb_to_hex((r_min, g_min, b_min))
        max_color = ColorCalibrator.rgb_to_hex((r_max, g_max, b_max))
        
        return (min_color, max_color)

    @staticmethod
    def create_intervals(colors):
        """
        Creates intervals for all calibrated colors.
        
        :param colors: Dictionary of color names and their hex values.
        :return: Dictionary of color intervals.
        """
        intervals = {}
        for color_name, hex_color in colors.items():
            intervals[color_name] = ColorCalibrator.create_color_interval(hex_color, 20)
        return intervals

    @staticmethod
    def hex_in_interval(hex_color, interval):
        """
        Checks if a hex color is within a given interval.
        
        :param hex_color: Hexadecimal color string.
        :param interval: Tuple of (min_color, max_color) in hex.
        :return: Boolean indicating if the color is within the interval.
        """
        rgb = ColorCalibrator.hex_to_rgb(hex_color)
        min_rgb = ColorCalibrator.hex_to_rgb(interval[0])
        max_rgb = ColorCalibrator.hex_to_rgb(interval[1])
        return all(min_rgb[i] <= rgb[i] <= max_rgb[i] for i in range(3))

    @staticmethod
    def color_in_intervals(hex_color, intervals):
        """
        Determines the calibrated color that matches a given hex color.
        
        :param hex_color: Hexadecimal color string.
        :param intervals: Dictionary of color intervals.
        :return: Name of the matched color or 'Unknown' if no match is found.
        """
        for color_name, interval in intervals.items():
            if ColorCalibrator.hex_in_interval(hex_color, interval):
                return color_name
        return 'Unknown'

    @staticmethod
    def calibrate_color(robot_number, color_name, hex_value):
        """
        Calibrates a color for a given robot.
        
        :param robot_number: Number of the robot (1 or 2).
        :param color_name: Name of the color.
        :param hex_value: Hexadecimal color string.
        """
        if robot_number == 1:
            ColorCalibrator.colors1[color_name] = hex_value
        elif robot_number == 2:
            ColorCalibrator.colors2[color_name] = hex_value
        else:
            raise ValueError("Invalid robot number. Must be 1 or 2.")

    @staticmethod
    def detect_color(robot_number, hex_color):
        """
        Detects a calibrated color for a given robot.
        
        :param robot_number: Number of the robot (1 or 2).
        :param hex_color: Hexadecimal color string.
        :return: Name of the detected color.
        """
        if robot_number == 1:
            intervals = ColorCalibrator.create_intervals(ColorCalibrator.colors1)
        elif robot_number == 2:
            intervals = ColorCalibrator.create_intervals(ColorCalibrator.colors2)
        else:
            raise ValueError("Invalid robot number. Must be 1 or 2.")
        
        return ColorCalibrator.color_in_intervals(hex_color, intervals)


# # Example usage:
# calibrator = ColorCalibrator()

# # Calibrating colors for Robot 1
# ColorCalibrator.calibrate_color(1, 'Red', '#FF0000')
# ColorCalibrator.calibrate_color(1, 'Green', '#00FF00')
# ColorCalibrator.calibrate_color(1, 'Blue', '#0000FF')

# # Calibrating colors for Robot 2
# ColorCalibrator.calibrate_color(2, 'Yellow', '#FFFF00')
# ColorCalibrator.calibrate_color(2, 'Cyan', '#00FFFF')
# ColorCalibrator.calibrate_color(2, 'Magenta', '#FF00FF')

# # Detecting colors for Robot 1
# print(ColorCalibrator.detect_color(1, '#FF0000'))  # Should output 'Red'
# print(ColorCalibrator.detect_color(1, '#00FF00'))  # Should output 'Green'

# # Detecting colors for Robot 2
# print(ColorCalibrator.detect_color(2, '#FFFF00'))  # Should output 'Yellow'
# print(ColorCalibrator.detect_color(2, '#00FFFF'))  # Should output 'Cyan'
