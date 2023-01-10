class WebPush:

    def __init__(self, platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_gapping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        print(self.push_type + " Push gönderildi!")

    def get_push_info(self):
        return self.platform, self.optin, self.global_frequency_gapping, self.start_date, self.end_date, \
               self.language, self.push_type


class TriggerPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 trigger_page: str):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.trigger_page = trigger_page


class BulkPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 send_date: int):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.send_date = send_date


class SegmentPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 segment_name: str):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.segment_name = segment_name


class PriceAlertPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 price_info: int, discount_rate: float):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.price_info = price_info
        self.discount_rate = discount_rate

    def discountPrice(self, price_info, discount_rate):
        return price_info * discount_rate


class InstockPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 stock_info: bool):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        self.stock_info = stock_info

    def stockUpdate(self):
        self.stock_info = not self.stock_info
        return self.stock_info


trigger_push = TriggerPush("android", True, 6, 2021, 2022, "TR", "Trigger", "main page")
trigger_push.send_push()
print(trigger_push.get_push_info())
print(f"Trigger page: {trigger_push.trigger_page}")

print("--------------------------------")

bulk_push = BulkPush("ios", True, 6, 2020, 2021, "EN", "Bulk", 2023)
bulk_push.send_push()
print(bulk_push.get_push_info())
print(f"Send date: {bulk_push.send_date}")

print("--------------------------------")

segment_push = SegmentPush("linux", False, 6, 2020, 2023, "DE", "Segment", "12 yaşından küçük erkek çocukları")
segment_push.send_push()
print(segment_push.get_push_info())
print(f"Segment name: {segment_push.segment_name}")

print("--------------------------------")

price_alert_push = PriceAlertPush("android", True, 6, 2018, 2022, "FR", "Price Alert", 350, 0.3)
print(f"Price info before discount: {price_alert_push.price_info}")
print(f"The amount of discount: {price_alert_push.discount_rate}")
discount_amount = price_alert_push.discountPrice(price_alert_push.price_info, price_alert_push.discount_rate)
price_alert_push.price_info -= discount_amount
price_alert_push.send_push()
print(price_alert_push.get_push_info())
print(f"Price info: {price_alert_push.price_info}")

print("--------------------------------")

instock_push = InstockPush("android", True, 6, 2020, 2023, "TR", "Instock", True)
print(f"Stock info before stock update: {instock_push.stock_info}")
instock_push.send_push()
print(instock_push.get_push_info())
instock_push.stockUpdate()
print(f"Stock info after stock update: {instock_push.stock_info}")







