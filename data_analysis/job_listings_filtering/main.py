import pandas as pd
from scripts.filter import *

if __name__ == "__main__":
  df = pd.read_csv("./data/postings.csv", index_col="company_name")

  result = filter_jobs(
        df,
        titles=["Software Engineer"],
        skills=["C#"],
        locations=["Los Angeles, CA", "New York, NY"],
        salary_range=[70000, 90000]
    )
  if result.empty:
    print("No jobs found with the current filters.")
  else: 
    print(result)
  
  print(df.columns)