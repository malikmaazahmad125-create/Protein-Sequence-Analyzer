import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("." * 30)
print("PROTEIN SEQUENCE ANALYZER")
print("." * 30)

protein_sequence = """
MKWVTFISLLFLFSSAYSRGVFRRDTHKSEIAHRFKDLGE
"""

sequence = protein_sequence.replace("\n", "").replace(" ", "").upper()
print(sequence)

amino_acids = "ACDEFGHIKLMNPQRSTVWY"

print("\n", "." * 10, "CHECK VALIDATION USING FUNCTIONS", "." * 10)


def valid(seq):
    """Check whether sequence contains valid amino acids."""
    invalid = set(seq) - set(amino_acids)

    if invalid:
        return False, invalid

    return True, None


print("Check Amino Acid valid or not:")
is_valid, invalid = valid(sequence)
print(is_valid)

if invalid:
    print("Invalid Amino Acids:", invalid)


def count_amino_acid(seq):
    """Count amino acids using dictionary."""
    return {aa: seq.count(aa) for aa in amino_acids}


print("\nCounting of Amino Acids are given below:")

aa_counts = count_amino_acid(sequence)
print(aa_counts)


def calculate_statistics(seq, counts):
    """Calculate Protein Sequence Statistics."""

    length = len(seq)
    unique_amino_acids = len(set(seq))

    most_common = max(counts, key=counts.get)

    non_zero_counts = {
        aa: count
        for aa, count in counts.items()
        if count > 0
    }

    least_common = min(
        non_zero_counts,
        key=non_zero_counts.get
    )

    return {
        "Length is ": length,
        "Unique Amino Acids ": unique_amino_acids,
        "Most common Amino Acids ": most_common,
        "Count Most Common ": counts[most_common],
        "Least Common Amino Acids ": least_common,
        "Count Least Common Amino Acids ": counts[least_common]
    }


print("\nProtein Sequence Statistics:")

counts = calculate_statistics(sequence, aa_counts)
print(counts)


print("." * 20)
print("NUMPY ARRAYS AND STATISTICS")
print("." * 20)

numpy_array = np.array(list(aa_counts.values()))

print("Convert Amino Acid values into NumPy Array:")
print(numpy_array)

non_zero_values = numpy_array[numpy_array > 0]

print("Non-zero Amino Acid Counts:")
print(non_zero_values)


print("\n", "." * 10, "STATISTICAL CALCULATIONS", "." * 10)

mean = np.mean(non_zero_values)

median = np.median(non_zero_values)

std = np.std(non_zero_values)

min_value = np.min(non_zero_values)

max_value = np.max(non_zero_values)


print("Following are the statistical methods:")

print("Mean:", round(mean, 2))

print("Median:", median)

print("Standard Deviation:", round(std, 2))

print("Maximum Value:", max_value)

print("Minimum Value:", min_value)


print("\n", "." * 10, "PANDAS DATAFRAME", "." * 10)

amino_acids_data = pd.DataFrame({
    "Amino Acid": list(aa_counts.keys()),
    "Count": list(aa_counts.values())
})

print("\nAmino Acid DataFrame is:\n")

print(amino_acids_data)


print("\nPercentage Calculation:")

amino_acids_data["Percentage"] = (
    amino_acids_data["Count"] / len(sequence)
) * 100

amino_acids_data["Percentage"] = (
    amino_acids_data["Percentage"].round(2)
)

print(amino_acids_data)


# Sirf amino acids jinki count 0 se zyada hai

filtered_data = amino_acids_data[
    amino_acids_data["Count"] > 0
]

print("\nFILTERED DATA:")

print(filtered_data)


# ==========================================
# VISUALIZATION 1
# ==========================================

print("\n", "." * 10, "BAR GRAPH", "." * 10)

plt.figure(figsize=(12, 6))

plt.bar(
    filtered_data["Amino Acid"],
    filtered_data["Count"]
)

plt.title("Amino Acid Count in Protein Sequence")

plt.xlabel("Amino Acids")

plt.ylabel("Count")

plt.grid(axis="y", alpha=0.3)

plt.show()


# ==========================================
# VISUALIZATION 2
# ==========================================

print("\n", "." * 10, "PIE CHART", "." * 10)

plt.figure(figsize=(10, 8))

plt.pie(
    filtered_data["Count"],
    labels=filtered_data["Amino Acid"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Amino Acid Distribution")

plt.show()


# ==========================================
# VISUALIZATION 3 - SEABORN
# ==========================================

print("\n", "." * 10, "SEABORN VISUALIZATION", "." * 10)

plt.figure(figsize=(12, 6))

sns.barplot(
    data=filtered_data,
    x="Amino Acid",
    y="Percentage"
)

plt.title("Amino Acid Percentage Distribution")

plt.xlabel("Amino Acids")

plt.ylabel("Percentage (%)")

plt.show()


# ==========================================
# FINAL REPORT
# ==========================================

print("\n", "." * 10, "FINAL REPORT", "." * 10)

print("\n", "." * 30)

print("FINAL PROTEIN SEQUENCE REPORT")

print("." * 30)

print("Protein Sequence:", sequence)

print("Total Length:", counts["Length is "])

print("Unique Amino Acids:", counts["Unique Amino Acids "])


print(
    "Most Common Amino Acid:",
    counts["Most common Amino Acids "]
)

print(
    "Most Common Count:",
    counts["Count Most Common "]
)


print(
    "Least Common Amino Acid:",
    counts["Least Common Amino Acids "]
)

print(
    "Least Common Count:",
    counts["Count Least Common Amino Acids "]
)


print("Mean Count:", round(mean, 2))

print("Median Count:", median)

print("Standard Deviation:", round(std, 2))


print("." * 40)

print("ANALYSIS COMPLETE")

print("." * 40)
