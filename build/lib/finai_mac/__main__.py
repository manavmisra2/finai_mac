import site;
import os
os.system("pip install jupyterlab_templates")
os.system("jupyter labextension install jupyterlab_templates")
os.system("jupyter serverextension enable --py jupyterlab_templates")
def main():
    print("Running Jupyter platform!") 
    out=site.getsitepackages()
    str_out = out   
    out1=' '.join(str_out)  
    filename =  os.path.join(out1, "finai_mac", "jupyter_notebook_config.py")
    filename2 = filename.replace(os.sep, '/')    
    os.system("jupyter lab --config=" + filename2)
   

if __name__ == "__main__":
    main()


def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 