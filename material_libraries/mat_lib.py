'''
class that obtains material properties from materials.csv
'''

import pandas as pd

def read_materials():
    return  pd.read_csv('materials.csv',index_col = 'material')

def get_properties(mats,props):
    '''
    mat: str or list of str containing names of materials to get properties of
    props: str or list of str of properties to get for materials
    
    returns: mat_dict - dictionairy of materials and properties
    '''
    #df materials
    df = read_materials()
    
    #case inputs to list if they are just string
    if type(mats) == str: mats = [mats]
    if type(props) == str: props = [props]
    
    #build dictionairy
    out_dict = {}
    for m in mats:
        prop_dict = {}
        for p in props:
            val = df.loc[m][p]
            prop_dict[p] = val
        out_dict[m] = prop_dict
    
    return out_dict

#
def list_materials():
    df = read_materials()
    return df.index.to_list()

def list_properties():
    df = read_materials()
    return df.columns


#test script
if __name__ == "__main__":
    mat_list = list_materials()
    get_properties(mat_list,'Conductance '):
    