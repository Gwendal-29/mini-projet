import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from scipy.stats import chi2_contingency

file_path = 'oral_cancer_prediction_dataset.csv'
data = pd.read_csv(file_path)


data_encoded = data.copy()
label_encoder = LabelEncoder()

categorical_columns = ['Country', 'Gender', 'Tobacco Use', 'Alcohol Consumption', 
                       'HPV Infection', 'Betel Quid Use', 'Chronic Sun Exposure', 
                       'Poor Oral Hygiene', 'Difficulty Swallowing', 
                       'White or Red Patches in Mouth', 'Treatment Type', 'Early Diagnosis', 
                       'Oral Cancer (Diagnosis)']

for col in categorical_columns:
    data_encoded[col] = label_encoder.fit_transform(data_encoded[col])

boolean_columns = ['Family History of Cancer', 'Compromised Immune System', 'Oral Lesions', 
                   'Unexplained Bleeding']

for col in boolean_columns:
    data_encoded[col] = label_encoder.fit_transform(data_encoded[col])

data_encoded['Diet (Fruits & Vegetables Intake)'] = label_encoder.fit_transform(data_encoded['Diet (Fruits & Vegetables Intake)'])

corr_matrix = data_encoded.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matrice de Corrélation des Variables')
plt.show()

correlation_with_cancer = corr_matrix['Oral Cancer (Diagnosis)'].sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=correlation_with_cancer.index, y=correlation_with_cancer.values, palette='coolwarm')
plt.title('Corrélation entre les variables et la présence du Cancer Oral')
plt.xlabel('Variables')
plt.ylabel('Corrélation avec la présence du Cancer Oral')
plt.xticks(rotation=90)
plt.show()

top_10_correlation = correlation_with_cancer.head(10)
print("Les 10 variables les plus corrélées avec le cancer oral et leur taux de corrélation :")
print(top_10_correlation)

contingency_tobacco = pd.crosstab(data['Tobacco Use'], data['Oral Cancer (Diagnosis)'])
contingency_alcohol = pd.crosstab(data['Alcohol Consumption'], data['Oral Cancer (Diagnosis)'])

chi2_tobacco, p_tobacco, dof_tobacco, expected_tobacco = chi2_contingency(contingency_tobacco)
chi2_alcohol, p_alcohol, dof_alcohol, expected_alcohol = chi2_contingency(contingency_alcohol)

print("\nTest Chi-Carré pour le tabagisme et le cancer oral :")
print(f"p-value pour le tabagisme : {p_tobacco}")

print("\nTest Chi-Carré pour la consommation d'alcool et le cancer oral :")
print(f"p-value pour l'alcool : {p_alcohol}")

if p_tobacco < 0.05:
    print("\nIl y a une association significative entre le tabagisme et le cancer oral.")
else:
    print("\nIl n'y a pas d'association significative entre le tabagisme et le cancer oral.")

if p_alcohol < 0.05:
    print("\nIl y a une association significative entre la consommation d'alcool et le cancer oral.")
else:
    print("\nIl n'y a pas d'association significative entre la consommation d'alcool et le cancer oral.")
