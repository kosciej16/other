from collections import namedtuple


class VolumeAndPath(namedtuple("VolumeAndPath", ["volume", "path"])):
    def get_as_arg(self):
        return f"{self.volume or ''}:{self.path or ''}"

    @staticmethod
    def create(volume_and_path, only_path_if_no_colon=True):
        if ":" in volume_and_path:
            vol, path = volume_and_path.split(":", 1)
        elif only_path_if_no_colon:
            vol = None
            path = volume_and_path
        else:
            vol = volume_and_path
            path = ""
        return VolumeAndPath(vol, path)

    split = create


class VolumePathPIT(namedtuple("VolumePathPIT", ["volume", "path", "pit"])):
    def get_as_arg(self):
        return f"{self.volume or ''}:{self.path or ''}"

    @staticmethod
    def create(string: str, only_path_if_no_colon=True):
        pit = None
        if string.count(":") == 2:
            string, pit = string.rsplit(":", 1)
        x = VolumeAndPath.split(string, only_path_if_no_colon)
        return VolumePathPIT(*x, pit)

    split = create


s = "abc:def"
print(VolumePathPIT.split(s))
