print("this module does so & so")

if __name__ == "__main__":
    def funca():
        print("funca when used within this module")
        
    def funcb():
        print("funcb when used within this module")    

elif __name__ == "one":
    def funca():
        print("funca when someone else uses")    
        
        
        
funca()
    

  