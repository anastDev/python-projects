import pandas as pd
import matplotlib.pyplot as plt
from scripts.filter import *

if __name__ == "__main__":

  # Opening the csv file
  df = pd.read_csv("./data/postings.csv")
  df = df.fillna("N/A")

  titles = ["Software Engineer"]
  skills = ["React", "TypeScript", "Node.js", "Java", "Python", ".NET", "JavaScript"]
  locations = []

  result = filter_jobs(
        df,
        titles=titles,
    )

if result.empty:
    print("No jobs found with the current filters.")
else: 
    print(f"{len(result)} matching jobs were found.\n")

print("Filters applied: \n")

if titles: 
      print(f" - Titles: {', '.join(titles)}")

if skills: 
      print(f" - Skills: {', '.join(skills)}")

if locations:
      print(f" - Locations: {', '.join(locations)}")
print()

filtered = result[
  (result["title"]== "Software Engineer") 
  & (result["location"] != "United States")
] 

location_counts = filtered["location"].value_counts().head(10)

location_counts.plot(kind="bar",figsize=(12, 6), color="green")
plt.title("Number of job posting for Software Engineer", fontweight="bold")
plt.xlabel("Location", fontweight="bold")
plt.ylabel("Number of postings", fontweight="bold")
plt.xticks(rotation=45, ha="right")
plt.savefig("postings_filtered.png")
plt.show()

skills_count = {}
for skill in skills:
  pattern = rf"\b{skill}\b"
  skills_count[skill] = df["description"].str.contains(pattern, case=False, na=False).sum()

skill_count_series = pd.Series(skills_count).sort_values(ascending=False)

skill_count_series.plot(kind='pie', figsize=(8, 8), autopct="%1.1f%%")
plt.title("Top skills in job postings", family="Arial", fontweight="bold")
plt.ylabel("")
plt.savefig("skills_pie.png")
plt.show()
      
location_counts = df["location"].value_counts().head(20)
location_counts.plot(kind='bar', figsize=(10, 6))
plt.title("Number of job postings per location", family="Arial", fontweight="bold")
plt.xlabel("Location", family="Arial",fontsize="12", fontweight="bold")
plt.ylabel("Count",family="Arial", fontweight="bold")
plt.savefig("locations_bar.png")
plt.show()