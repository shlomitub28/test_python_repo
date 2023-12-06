# Databricks Python Task
def main():
    # Your Python code here

    # Install libraries from requirements.txt in the Git repository
    import subprocess
    import sys
    subprocess.call([sys.executable, '-r requirements.txt', 'pip', 'install'])
    
    #%pip install -r requirements.txt

    # Continue with your code
    import pandas as pd
    import numpy as np

    df = pd.DataFrame({"column1": [1, 2, 3], "column2": [4, 5, 6]})
    print(df.head())

if __name__ == "__main__":
    main()