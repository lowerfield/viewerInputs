import nuke

__all__ = ['viewerInputs']

viewerList = [] 

def viewerInputsToogle():

    for node in nuke.allNodes('Viewer'):

        if node['hide_input'].value() == False:
            node['hide_input'].setValue(True)

        elif node['hide_input'].value() == True:
            node['hide_input'].setValue(False)

    for node in nuke.allNodes('Viewer'):
        viewerList.append(node)

def viewerInputs():

    currentViewers = nuke.allNodes('Viewer')

    if viewerList == []:
        viewerInputsToogle()
           
    elif viewerList != [] and viewerList == currentViewers:
        viewerInputsToogle()
            
    elif viewerList != [] and viewerList != currentViewers:

        for node in list(set(nuke.allNodes('Viewer')).difference(viewerList)):
            node['hide_input'].setValue(True)

        viewerInputsToogle()
    