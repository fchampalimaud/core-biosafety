from confapp import conf
from pyforms_web.widgets.django import ModelAdminWidget

from biosafety.models import Risk

class RiskAdminApp(ModelAdminWidget):
    

    UID   = 'biosafety-Risk-app'.lower()
    MODEL = Risk
    
    TITLE = 'Risks'

    #list of filters fields
    #LIST_FILTER    = ['id','code','label','url','description']

    #list of fields to display in the table
    #LIST_DISPLAY   = ['id','code','label','url','description']
    
    #fields to be used in the search
    #SEARCH_FIELDS  = ['id','code','label','url','description']
    
    #sub models to show in the interface
    #INLINES        = []
    
    #formset of the edit form
    #FIELDSETS      = ['id','code','label','url','description']
    
    #read only fields
    #READ_ONLY      = ['id','code','label','url','description']
    
    #EDITFORM_CLASS = RiskModelFormWidget    #edit form class
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
    
    
    