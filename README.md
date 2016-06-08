# Description
convinent script to adapt python's sys.path

# Install
    pip install adaptpath

# Usage
    * Say we have dir-tree below:
        a / b / c.py
        x / y / z.py
    
    * Now suppose we are in "z.py" and we want to do this:
        from a.b import c
    
    * We can put the lines below ahead of "z.py"
        from adaptpath import adaptpath
        adaptpath.adapt_from_path(2, __file__)
        
# Test
    pytest test   
    

