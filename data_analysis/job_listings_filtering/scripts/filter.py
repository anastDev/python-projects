from typing import List, Tuple, Optional
import pandas as pd

def filter_jobs(
    df: pd.DataFrame,
    titles: Optional[List[str]] = None,
    skills: Optional[List[str]] = None,
    locations: Optional[List[str]] = None,
    salary_range: Optional[Tuple[int, int]] = None
) -> pd.DataFrame | pd.Series:
  """
  Filters a DataFrame of job postings based on user-specified criteria.

  Params:
    df (pandas.DataFrame): The dataset containing job postings.
    title (str, optional): Filter jobs by exact job title.
    skills (str, optional): Filter jobs containing specific skills.
    locations (list of str, optional): Filter jobs located in these cities.
    salary_range (tuple of two numbers, optional): Filter jobs with Salary between (min, max).
  
  Returns:
    pandas.DataFrame: Filtered DataFrame containing only jobs matching all specified criteria.
  """
  try: 
    filtered = df.copy()

    if titles:
      mask = pd.Series(False, index=filtered.index)
      for t in titles:
        mask |= filtered["title"].str.contains(t, case=False, na=False)
      filtered = filtered.loc[mask]
      
    if skills:
      mask = pd.Series(False, index=filtered.index)
      for s in skills:
        mask |= filtered["skills_desc"].str.contains(s, case=False, na=False)
      filtered = filtered.loc[mask]

    if locations:
      filtered = filtered.loc[filtered["location"].isin(locations)]

    if salary_range:
      lower, upper = salary_range
      filtered = filtered.loc[filtered["med_salary"].between(lower, upper)]

    return filtered
  except TypeError as e:
    print(f"Error: {e}")