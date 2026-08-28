import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================
# SALES DATA ANALYZER & DATA VISUALIZATION
# ==========================================

print("\n===== SALES DATA ANALYZER =====")

# your csv file path

file_path = r"C:\Users\Armin Khareghat\OneDrive\Desktop\AI ML data science\Python\python-projects\Pandas Analyzer & Data Visualization\sales_data.csv"

# load csv file 
try:
     df = pd.read_csv(file_path)
     print("\n File Loaded Successfully!")
     print("Sales_data:", os.path.basename(file_path))
     print("Total Rows:", df.shape[0])
     print("Total Columns:", df.shape[1])

     print("\n ----- SALES DATASET -----")
     print(df.head())

except FileNotFoundError:
    print("\n File Not Found!")
    print("Please check the complete CSV file path.")

except PermissionError:
    print("\n Permission Denied!")
    print("\n please make sure you selected the CSV file, not the folder.")

    

except Exception as e:
    print("\n Error while loading file:",e)


# ------------------------------------------
# 2. BASIC DATA INFORMATION
# ------------------------------------------

print("\n----- DATASET INFORMATION -----")

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()


# ------------------------------------------
# 3. STATISTICAL ANALYSIS
# ------------------------------------------

print("\n----- STATISTICAL ANALYSIS -----")
print(df.describe())


# ------------------------------------------
# 4. CHECK MISSING VALUES
# ------------------------------------------

print("\n----- MISSING VALUES -----")
print(df.isnull().sum())


# ------------------------------------------
# 5. TOTAL SALES
# ------------------------------------------

total_sales = df["Sales"].sum()

print("\n----- TOTAL SALES -----")
print("Total Sales: $", total_sales)


# ------------------------------------------
# 6. AVERAGE SALES
# ------------------------------------------

average_sales = df["Sales"].mean()

print("\n----- AVERAGE SALES -----")
print("Average Sales: $", average_sales)


# ------------------------------------------
# 7. HIGHEST SALE
# ------------------------------------------

highest_sale = df.loc[df["Sales"].idxmax()]

print("\n----- HIGHEST SALE -----")
print(highest_sale)


# ------------------------------------------
# 8. REGION-WISE SALES
# ------------------------------------------

print("\n----- REGION-WISE SALES -----")

try:
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    print("\n File Loaded Successfully!")

    print("\n column Names:")
    print(df.columns.tolist())

except Exception as e:
    print("Error while loading file:", e)
    

# ------------------------------------------
# 9. REGION-WISE SALES
# ------------------------------------------

region_sales = df.groupby("Region")["Sales"].sum()

print("\n----- REGION-WISE SALES -----")
print(region_sales)


# ==========================================
# DATA VISUALIZATION
# ==========================================


# ------------------------------------------
# 10. BAR CHART - REGION SALES
# ------------------------------------------

plt.figure(figsize=(10, 5))
plt.bar(region_sales.index, region_sales.values)

plt.title("Region-Wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()


# ------------------------------------------
# 11. PIE CHART - REGION SALES
# ------------------------------------------

plt.figure(figsize=(7, 7))

plt.pie(
    region_sales.values,
    labels=region_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Region-Wise Sales Distribution")

plt.show()


# ------------------------------------------
# 12. LINE CHART - SALES BY ORDER
# ------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(
    df.index,
    df["Sales"],
    marker="o"
)

print(df.columns)

plt.title("Sales Trend by Order")
plt.xlabel("Order Number")
plt.ylabel("Sales ($)")

plt.tight_layout()
plt.show()

print("\n===== SALES ANALYSIS COMPLETED SUCCESSFULLY =====")