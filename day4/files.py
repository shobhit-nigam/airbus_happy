"""library for working with files
"""

class fileops:
    """for working with files"""
    path = "/Users/shobhit/Desktop/airbus_python/day4/"
    
    def __init__(self, n):
        self.name = self.path + n
        import os
        
        if not os.path.exists(self.name):
            print("check the file name")
    
    
    def read_col(self, num):
        """reads a particular column from the opened text file
        mention the column number, zero will be assumed by default"""
        
        with open(self.name, "r") as fa:
            stra = fa.read()
            
        lista = stra.splitlines()
        list_col = []

        for line in lista:
            temp = line.split()
            if len(temp) > num:
                list_col.append(temp[num])
        return list_col
    
    def read_col_num(self, num):
        """reads a particular column from the opened text file
        mention the column number, zero will be assumed by default"""
        
        with open(self.name, "r") as fa:
            stra = fa.read()
            
        lista = stra.splitlines()
        list_col = []

        for line in lista:
            temp = line.split()
            if len(temp) > num:
                if temp[num].isdigit():
                    list_col.append(int(temp[num])) 
        return list_col
    
    def concert_to_csv(self):
        self.new_name = self.name.replace(".txt", ".csv")
        with open(self.name, "r") as fa:
            stra = fa.read()
        with open(self.new_name, "w") as fa:
            strb = stra.replace(" ", ",")
            fa.write(strb)
            
    @classmethod
    def change_file(cls, new_path):
        cls.path = new_path
