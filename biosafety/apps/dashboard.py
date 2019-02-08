from pyforms_web.basewidget import BaseWidget
from confapp import conf

class BiosafetyDashboard(BaseWidget):

    UID = 'biosafety-dashboard'
    TITLE = 'Biosafety'

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'middle-left'
    ORQUESTRA_MENU_ORDER = 40
    ORQUESTRA_MENU_ICON = 'heartbeat red'
    ########################################################

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)