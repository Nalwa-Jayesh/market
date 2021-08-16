from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from marketmarker import MarketMarker

class FarmersMapView(MapView):
    getting_markets_timer = None
    market_names = []
    def start_getting_markets_in_fov(self):
        try:
            self.getting_markets_timer.cancel()
        except:
            pass
        self.getting_markets_timer = Clock.schedule_once(self.get_markets_in_fov,1)
    def get_markets_in_fov(self,*args):
        app = App.get_running_app()
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        sql_statement = "SELECT * FROM markets WHERE x > %s AND x < %s AND y > %s AND y < %s "%(min_lon,max_lon,min_lat,max_lat)
        print(self.get_bbox())
        app.cursor.execute(sql_statement)
        markets = app.cursor.fetchall()
        for market in markets:
            name = market[1]
            if name in self.market_names:
                continue
            else:
                self.add_market(market)
    
    def add_market(self,market):
        lat,lon = market[21], market[20]
        marker = MarketMarker(lat=lat, lon=lon)
        marker.market_data = market
        self.add_widget(marker)
        name = market[1]
        self.market_names.append(name)
