from PIL import Image
from utils import get_file
import api.mountain.mountaindata
import debug

class CurrentMountainStats:
    def __init__(self, data, matrix, sleepEvent):
        self.pref_mountain_id = data.pref_mountain_id
        self.data = data
        self.matrix = matrix
        self.font = data.config.layout.font
        self.font_medium = data.config.layout.font_medium
        self.app_id = data.config.mountain_app_id
        self.app_key = data.config.mountain_app_key
        self.sleepEvent = sleepEvent
        self.sleepEvent.clear()

    def render(self):
        # Render the current weather and snow statistics for the preferred mountains
        if True:
            self.matrix.clear()
            #Fetch and display the name of the mountain
            mountain_name = api.mountain.mountaindata.get_mountain_name(self.pref_mountain_id, self.app_id, self.app_key)
            self.matrix.draw_text(
                (1, 1),
                mountain_name,
                font=self.font_medium,
                fill=(200, 200, 200),
                backgroundColor=(0,0,0),
                backgroundOffset=[6, 1, 6, 1]
            )

            mountain_data = api.mountain.mountaindata.get_todays_mountain_forecast(self.pref_mountain_id, self.app_id, self.app_key)
            debug.info(mountain_data)
            self.matrix.draw_text(
                (1, 16),
                str("Fresh"),
                font=self.font,
                fill=(135, 206, 235),
                backgroundColor=(0,0,0)
            )
            self.matrix.draw_text(
                (1, 23),
                str("Snow"),
                font=self.font,
                fill=(135, 206, 235),
                backgroundColor=(0,0,0)
            )

            self.matrix.draw_text(
                (22, 17),
                str(mountain_data["fresh_snow"]),
                font=self.font_medium,
                fill=(200, 200, 200),
                backgroundColor=(0,0,0)
            )

            self.matrix.draw_text(
                ((29, 36)[int(mountain_data["fresh_snow"]) >= 10], 22),
                "in",
                font=self.font,
                fill=(135, 206, 235),
                backgroundColor=(0,0,0)
            )

            
            self.matrix.render()
            self.sleepEvent.wait(20)
        else:
            debug.info("No Stanley Cup Champions, going to next board")
