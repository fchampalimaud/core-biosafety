from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from biosafety.models import Level

class LevelAdminApp(ModelAdminWidget):
    

    UID   = 'biosafety-level-app'
    MODEL = Level
    
    TITLE = 'Levels'

    #list of filters fields
    #LIST_FILTER    = ['room','id','code','label']

    #list of fields to display in the table
    #LIST_DISPLAY   = ['room','id','code','label']
    
    #fields to be used in the search
    #SEARCH_FIELDS  = ['room','id','code','label']
    
    #sub models to show in the interface
    #INLINES        = []
    
    #formset of the edit form
    #FIELDSETS      = ['room','id','code','label']
    
    #read only fields
    #READ_ONLY      = ['room','id','code','label']
    
    #EDITFORM_CLASS = LevelModelFormWidget    #edit form class
    #CONTROL_LIST   = ControlQueryList #Control to be used in to list the values
    
    #AUTHORIZED_GROUPS   = ['superuser'] #groups with authorization to visualize the app
    
    ########################################################
    #### ORQUESTRA CONFIGURATION ###########################
    ########################################################
    LAYOUT_POSITION      = conf.ORQUESTRA_HOME
    ORQUESTRA_MENU       = 'middle-left>BiosafetyDashboard'
    ORQUESTRA_MENU_ORDER = 0
    ORQUESTRA_MENU_ICON  = 'dollar'
    ########################################################
    
    
    