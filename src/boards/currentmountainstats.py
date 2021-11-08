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
                (1, 3),
                mountain_name,
                font=self.font,
                fill=(200, 0, 0),
                backgroundColor=(220,220,220),
                backgroundOffset=[6, 1, 6, 1]
            )

            mountain_data = api.mountain.mountaindata.get_todays_mountain_forecast(self.pref_mountain_id, self.app_id, self.app_key)
            self.matrix.render()
            self.sleepEvent.wait(10)
            # self.sleepEvent.wait(0.5)
            # self.matrix.draw_text(
            #     (37, 7),
            #     str(self.data.year),
            #     font=self.font,
            #     fill=(0, 0, 0),
            #     backgroundColor=(200,200,200)
            # )
            # self.matrix.render()
            # self.sleepEvent.wait(0.5)
            # self.matrix.draw_text(
            #     (12, 14),
            #     "STANLEY CUP",
            #     font=self.font,
            #     fill=(255,255,255),
            # )
            # self.matrix.render()
            # self.sleepEvent.wait(0.5)
            # self.matrix.draw_text(
            #     (16, 21),
            #     "CHAMPIONS",
            #     font=self.font,
            #     fill=(team_color_accent['r'], team_color_accent['g'], team_color_accent['b']),
            #     backgroundColor=(team_color_main['r'], team_color_main['g'], team_color_main['b']),
            #     backgroundOffset=[4, 1, 4, 1]
            # )
            # self.matrix.render()
            # self.sleepEvent.wait(10)
        else:
            debug.info("No Stanley Cup Champions, going to next board")
