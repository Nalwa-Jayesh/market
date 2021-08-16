from kivymd.app import MDApp
from farmersmapview import FarmersMapView
import sqlite3
from searchpopupmenu import SearchPopupMenu
from gpshelper import GpsHelper
class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None
    def on_start(self):
        GpsHelper().run()
        self.connection = sqlite3.connect("markets.db")
        self.cursor = self.connection.cursor()
        self.search_menu = SearchPopupMenu()
MainApp().run()