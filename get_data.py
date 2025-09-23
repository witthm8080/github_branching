# %%

def download_data(force=False):
    """Download and extract course data from Zenodo."""
    import urllib.request
    import zipfile
    import os
    
    zip_path = 'data.zip'
    data_dir = 'data'
    
    if not os.path.exists(zip_path) or force:
        print("Downloading course data...")
        urllib.request.urlretrieve(
            'https://zenodo.org/records/16954427/files/data.zip?download=1',
            zip_path
        )
        print("Download complete")
    if not os.path.exists(data_dir) or force:
        print("Extracting data files...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(data_dir)
        print("Data extracted")
    
    return data_dir

download_data()











# %%
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('./data_1/nhanes_data_17_18.csv', low_memory=False)

## Handle missings:
na_vars = np.sum(df.isna(),axis=0)
keep = na_vars[na_vars<1200].sort_values(ascending=False).index
df = df.loc[:,keep]
df = df.dropna()
print(keep)

# %%

expl =['AnnualHouseholdIncome', 'TotalPolyunsaturatedFattyAcidsGm_DR1TOT',
       'EnergyKcal_DR1TOT', 'TotalSugarsGm_DR1TOT', 'CarbohydrateGm_DR1TOT',
       'ProteinGm_DR1TOT', 'CholesterolMg_DR1TOT', 'AlcoholGm_DR1TOT',
       'TotalSaturatedFattyAcidsGm_DR1TOT', 'TotalFatGm_DR1TOT',
       'DietaryFiberGm_DR1TOT', 'TotalMonounsaturatedFattyAcidsGm_DR1TOT',
       'RatioOfFamilyIncomeToPoverty', 'AnnualFamilyIncome', 'OnSpecialDiet',
       'BloodManganeseUgl', 'BloodCadmiumUgl', 'BloodMercuryTotalUgl',
       'BloodSeleniumUgl', 'HaveSeriousDifficultyConcentrating',
       'HaveSeriousDifficultyWalking', 'WaistCircumferenceCm',
       'HaveDifficultyDressingOrBathing', 'BodyMassIndexKgm2',
       'StandingHeightCm', 'WeightKg', 'OfFrozenMealspizzaInPast30Days',
       'OfReadytoeatFoodsInPast30Days', 'OfMealsNotHomePrepared',
       'CoveredByHealthInsurance', 'EverBeenToldYouHaveAsthma',
       'DoctorToldYouHaveDiabetes', 'HaveSeriousDifficultyHearing',
       'Past30DayMilkProductConsumption', 'TakingInsulinNow',
       'HaveSeriousDifficultySeeing', 'SEQN', 'OfAdults60YearsOrOlderInHh',
       'Gender', 'OfChildren617YearsOldInHh', 'OfChildren5YearsOrYoungerInHh',
       'TotalNumberOfPeopleInTheFamily', 'RacehispanicOriginWNhAsian',
       'TotalNumberOfPeopleInTheHousehold', 'RacehispanicOrigin',
       'AgeInYearsAtScreening']

x_var = df['AnnualHouseholdIncome']
y_var = df['CarbohydrateGm_DR1TOT']
sns.scatterplot(x=x_var,y=y_var,alpha=.05)

# %%
x_var = np.log(df['AnnualHouseholdIncome'])
y_var = df['EnergyKcal_DR1TOT']
sns.scatterplot(x=x_var,y=y_var,alpha=.05)

# %%
x_var = df['OfFrozenMealspizzaInPast30Days']
y_var = df['WeightKg']
sns.scatterplot(x=x_var,y=y_var,alpha=.05)


# %%

x_var = df['CarbohydrateGm_DR1TOT']
y_var = df['TotalFatGm_DR1TOT']
sns.scatterplot(x=x_var,y=y_var,alpha=.05)

# %%

x_var = df['WeightKg']
y_var = df['TotalFatGm_DR1TOT']
sns.scatterplot(x=x_var,y=y_var,alpha=.01)

# %%





# %%
x_var = df['AgeInYearsAtScreening']
y_var = df['AnnualHouseholdIncome']
sns.scatterplot(x=x_var,y=y_var,alpha=.05)

# %%

df['avg_income'] = df['AnnualHouseholdIncome']/float(df['TotalNumberOfPeopleInTheFamily'])










# %%






x_var = df['AgeInYearsAtScreening']
y_var = df['WeightKg']
sns.scatterplot(x=x_var,y=y_var,hue=df['Gender'],alpha=.05)
