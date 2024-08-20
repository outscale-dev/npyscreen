#!/usr/bin/env python
RETURN = []
import osc_npyscreen
class TestApp(osc_npyscreen.NPSApp):
    def main(self):
        F = osc_npyscreen.Form(name = "Testing Tree class",)
        #wgtree = F.add(osc_npyscreen.MLTree)
        wgtree = F.add(osc_npyscreen.MLTreeMultiSelect)
        
        treedata = osc_npyscreen.NPSTreeData(content='Root', selectable=True,ignoreRoot=False)
        c1 = treedata.newChild(content='Child 1', selectable=True, selected=True)
        c2 = treedata.newChild(content='Child 2', selectable=True)
        g1 = c1.newChild(content='Grand-child 1', selectable=True)
        g2 = c1.newChild(content='Grand-child 2', selectable=True)
        g3 = c1.newChild(content='Grand-child 3')
        gg1 = g1.newChild(content='Great Grand-child 1', selectable=True)
        gg2 = g1.newChild(content='Great Grand-child 2', selectable=True)
        gg3 = g1.newChild(content='Great Grand-child 3')
        wgtree.values = treedata
        
        F.edit()
        
        global RETURN
        #RETURN = wgtree.values
        RETURN = wgtree.get_selected_objects()




if __name__ == "__main__":
    App = TestApp()
    App.run()   
    for v in RETURN:
        print v
