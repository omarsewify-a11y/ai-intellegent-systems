import matplotlib.pyplot as plt

print("Category counts:")
print(df["category"].value_counts())

print("\nPending requests:")
print((df["status"] == "Pending").sum())

df["msg_length"] = df["message"].str.len()

print("\nAverage message length:")
print(df.groupby("category")["msg_length"].mean())

df["category"].value_counts().plot(kind="bar")
plt.title("Requests by Category")
plt.show()
