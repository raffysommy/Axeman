"""Author:       Olivier van der Toorn <oliviervdtoorn@gmail.com>
Description:     Makes dict keys available as attributes.
"""
class AttrDict(dict):
    """Allows a dictionary to be used as a namespace.
    source: http://stackoverflow.com/questions/4984647/
    """
    def __init__(self, *args, **kwargs):
        """Calls the dict init and sets the internal dict to self.
        """
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self
        self.convert_children()

    def __repr__(self):
        """Print the dictionary in a sysctl like way.
        """
        lines = []
        for item in self.__dict__:
            value = self.__dict__[item]
            if not isinstance(value, AttrDict):
                if value != '':
                    lines.append("{0} = {1}".format(
                        item, self.__dict__[item]))

            else:
                sublines = self.__dict__[item].__repr__().split('\n')
                for line in sublines:
                    lines.append("{0}.{1}".format(item, line))
        return "\n".join(sorted(lines))

    def convert_children(self):
        """Converts any values which are dictionaries to AttrDict too.
        """
        for key, value in self.__dict__.items():
            if isinstance(value, dict):
                self.__dict__[key] = AttrDict(value)
