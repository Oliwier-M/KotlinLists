import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def heart_diseases_analytic():
    data = pd.read_csv("heart_disease_dataset.csv", index_col='Unnamed = 0')
    df = pd.DataFrame(data)
    return df

def heart_diseases():
    df = heart_diseases_analytic()

    m = np.sum(df[df['Sex'] == 'male', 'Disease'])
    f = 0
    males = np.sum(df['Sex'] == 'male')
    females = np.sum(df['Sex'] == 'female')

heart_diseases()




    # data = pd.read_csv("heart_disease_dataset.csv", index_col='Unnamed: 0')
    # df = pd.DataFrame(data)
    # # print(df)
    # return df


# def heart_diseases():
#     df = heart_diseases_analytic()
#
#     m = 0
#     f = 0
#     males = 0
#     females = 0
#
#     males += np.sum((df['Sex'] == 'male'))
#     females += np.sum((df['Sex'] == 'female'))
#
#     for i in range(len(df)):
#         if df.loc[i, 'Disease']:
#             if df.loc[i, 'Sex'] == 'male':
#                 m += 1
#             elif df.loc[i, 'Sex'] == 'female':
#                 f += 1
#
#     m_per = m / males * 100
#     f_per = f / females * 100
#
#     m_per = np.round(m_per, 2)
#     f_per = np.round(f_per, 2)
#
#     dif = np.abs(m_per - f_per)
#
#     # print(m_per, "%")
#     # print(f_per, "%")
#     # print(dif, "%")
#
#     return dif


def cholesterol_compare():
    data_frame = heart_diseases_analytic()

    dm = []
    df = []
    hm = []
    hf = []

    for i in range(len(data_frame)):
        if not data_frame.loc[i, 'Disease']:
            if data_frame.loc[i, 'Sex'] == 'male':
                dm.append(data_frame.loc[i, "Serum cholesterol in mg/dl"])
            elif data_frame.loc[i, 'Sex'] == 'female':
                df.append(data_frame.loc[i, "Serum cholesterol in mg/dl"])
        else:
            if data_frame.loc[i, 'Sex'] == 'male':
                hm.append(data_frame.loc[i, "Serum cholesterol in mg/dl"])
            elif data_frame.loc[i, 'Sex'] == 'female':
                hf.append(data_frame.loc[i, "Serum cholesterol in mg/dl"])

    # print("diseased males: ", dm)
    # print("diseased females: ", df)
    # print("healthy males: ", hm)
    # print("healthy females: ", hf)

    male_diseased_avg = np.round(np.mean(dm), 2)
    female_diseased_avg = np.round(np.mean(df), 2)
    male_healthy_avg = np.round(np.mean(hm), 2)
    female_healthy_avg = np.round(np.mean(hf), 2)

    return male_diseased_avg, female_diseased_avg, male_healthy_avg, female_healthy_avg


def draw_histo(df):
    ages = []

    # first gather diseased
    for i in range(len(df)):
        if df.loc[i, 'Disease']:
            # then gather age
            ages.append(df.loc[i, 'Age'])

    plt.hist(ages, bins=50, edgecolor='black')
    plt.title("People with heart diseases")
    plt.xlabel("age")
    plt.ylabel("frequency")
    plt.show()

    print(np.min(ages))


def box_plot(df):
    # Create separate lists for diseased and healthy individuals
    diseased = df.loc[df['Disease'], 'Maximum heart rate achieved'].tolist()
    healthy = df.loc[~df['Disease'], 'Maximum heart rate achieved'].tolist()

    # Create a box plot

    plt.boxplot([diseased, healthy], labels=['Diseased', 'Healthy'])
    plt.title('Box Plot of Maximum Heart Rate by Disease Condition')
    plt.xlabel('Condition')
    plt.ylabel('Maximum Heart Rate Achieved')
    plt.grid(True)
    plt.show()


def bar_chart(df):
    diseased_angina = np.sum(df.loc[df['Disease'], 'Exercise induced angina'])
    healthy_angina = np.sum(df.loc[~df['Disease'], 'Exercise induced angina'])
    diseased = np.sum(df.loc[~df['Exercise induced angina'], 'Disease'])
    healthy = np.sum(~df['Exercise induced angina'] & ~df['Disease'])

    cat = ["diseased with angina", "healthy with angina", "diseased without angina", "healthy without angina"]
    numb = [diseased_angina, healthy_angina, diseased, healthy]

    bar_width = 0.4  # Adjust the width as needed
    bar_positions = np.arange(len(cat))

    # Create a bar chart with customized width and tick positions
    plt.bar(bar_positions, numb, width=bar_width, edgecolor='black')
    plt.subplots_adjust(bottom=0.35)
    # Customize x-axis ticks and labels
    plt.xticks(bar_positions, cat, rotation=40)
    plt.grid(True)
    plt.yticks(range(0, max(numb) + 1, 40))
    plt.xlabel("Categories")
    plt.ylabel("Numbers")
    plt.title(" The frequency of heart disease occurrence depending on whether \n"
              "the patient has angina during the exercise test")
    plt.show()

    # diseased = []
    # healthy = []
    #
    # for i in range(len(df)):
    #     if df.loc[i, 'Disease']:
    #         diseased.append(df.loc[i, 'Maximum heart rate achieved'])
    #     else:
    #         healthy.append(df.loc[i, 'Maximum heart rate achieved'])
    #
    # plt.boxplot(diseased)
    # plt.show()


# heart_diseases()
# print(cholesterol_compare())
# draw_histo(heart_diseases_analytic())
box_plot(heart_diseases_analytic())
bar_chart(heart_diseases_analytic())

# s = pd.Series([1,2,4,"word","leg", np.nan])
#
#     cat = (["student", "teacher","nurse","headmaster","janitor","vice headmaster"])
#
#     dates = pd.date_range("20040304", periods=5)
#
#     df = pd.DataFrame(np.random.randn(5,3), index=list("12345"), columns=list("ABC"))
#
#     df2 = pd.DataFrame({
#         "A": s,
#         "B": pd.Series(1, index=list(range(6)), dtype="int"),
#         "C": pd.Categorical(cat)
#     })
#
#
#     print(df2)
#     print(df2.dtypes)
#
#     print(df)
#
#     print(dates)
#
#     print(s)
