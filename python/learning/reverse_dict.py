original_dict={'A':0,'C':2,'B':1}
new_dict={}
for k,v in original_dict.items():
    dict_element={k:v}
    dict_element.update(new_dict)
    new_dict=dict_element
print(new_dict)
