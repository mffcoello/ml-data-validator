# ml-data-validator

Checks a dataset for three things before you train on it: missing values, class imbalance, outliers.

## why

Bad data breaks models before bad architecture does. This catches the stuff you'd normally eyeball a dataframe for, but as an actual testable tool instead of guesswork.

## dataset

UCI's "Predict Students' Dropout and Academic Success." 4424 rows, 3-class target (Dropout / Enrolled / Graduate).

Real data has zero missing values, so I added a copy (`students_dropout_dirty.csv`) with ~3% synthetic missing values in 3 columns, seeded so it's reproducible. Clean file's still in `data/` too.

## checks

- **missing values** : flags columns above a missing % threshold
- **class imbalance** : flags classes below a minority ratio threshold
- **outliers** : IQR-based, 1.5x interquartile range

## output

=== Missing Values ===
Previous qualification (grade): 2.7% missing
Mother's occupation: 3.1% missing
Admission grade: 3.0% missing

=== Class Imbalance ===
Imbalanced: True
Minority class: Enrolled (17.9%)

=== Outliers ===
Age at enrollment: 441 outliers (bounds: 10.0 to 34.0)

## worth noting

441 outliers on age sounds like a lot. It's not 441 errors, it's a right-skewed distribution, most students are 18-25, but plenty of real students enroll older. IQR just flags statistical rarity, not correctness. You still have to look at what's flagged.
