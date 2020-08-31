from .timestamped_model import TimeStampModel
from .uuid_model import UUIDPkModel


class BaseModel(UUIDPkModel, TimeStampModel):
    class Meta:
        abstract = True
