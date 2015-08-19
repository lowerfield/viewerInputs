import nuke


__all__ = ['viewerInputs']

def viewerInputs():

	for node in nuke.allNodes('Viewer'):

	    if node['hide_input'].value() == False:
	        node['hide_input'].setValue(True)

	    elif node['hide_input'].value() == True:
	        node['hide_input'].setValue(False)