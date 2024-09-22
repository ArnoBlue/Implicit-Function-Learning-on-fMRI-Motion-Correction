from typing import Union
from os import PathLike
import torch

PathType = Union[str, PathLike]
DeviceType = Union[torch.device, str, None]
