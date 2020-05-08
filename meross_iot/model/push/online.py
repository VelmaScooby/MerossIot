from meross_iot.model.enums import OnlineStatus, Namespace
from meross_iot.model.push.generic import GenericPushNotification


class OnlinePushNotification(GenericPushNotification):
    def __init__(self, online_status: OnlineStatus, originating_device_uuid: str, raw_data: dict):
        super().__init__(namespace=Namespace.ONLINE, originating_device_uuid=originating_device_uuid, raw_data=raw_data)
        self.online_status = online_status

    @classmethod
    def from_dict(cls, data: dict, originating_device_uuid: str):
        online_data = data.get("online")
        status = OnlineStatus(online_data.get("status"))
        return OnlinePushNotification(online_status=status, originating_device_uuid=originating_device_uuid, raw_data=data)