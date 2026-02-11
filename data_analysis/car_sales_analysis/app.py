from scripts.analysis import *

def main():
  print("\nOpening file...")
  file_path = "../data/car_sales_small.csv"
  data = read_file(file_path=file_path)
  
  if data is not None:
    print("\nFirst 5 rows:")
    print(data.head(5))

    print("\nLast 5 rows:")
    print(data.tail(5))
  else:
    print("Failed to load data. Check log file for details.")

if __name__ == "__main__":
  main()