from pyforms_web.basewidget import BaseWidget
from confapp import conf

class BiosafetyDashboard(BaseWidget):

    UID = 'biosafety-dashboard'
    TITLE = 'Biosafety'

    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU = 'left'
    ORQUESTRA_MENU_ORDER = 999
    ORQUESTRA_MENU_ICON = 'heartbeat red'
    ########################################################
    
    
    AUTHORIZED_GROUPS = ['superuser']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)