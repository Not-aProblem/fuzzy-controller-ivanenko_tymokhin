import model
import model2
import inference_mamdani
import fuzzy_operators
import streamlit as st
import pandas as pd

########################################
# Завантажуємо таблицю з раніше зробленими експерементами
########################################

table = pd.read_csv("data.csv")


########################################
#            Ввід даних
#######################################
crisp = []  # [22, 185, 20, 50_000]

begin = {"Age": 14, "Weight": 10, "Nutrition": 9}

try:
    for i in ["Age", "Weight", "Nutrition"]:
        crisp.append(float(st.text_input(i, begin[i])))

    type_pet = st.selectbox(
        "What type of pat?", ("Small_Breeds", "Medium_Breeds", "Large_Breeds")
    )

    metrick = st.selectbox("metrick type?", ("cog", "fom", "lom", "mom"))

    #########################################
    #    Обчислення
    #########################################

    inference_mamdani.preprocessing(
        model2.input_lvs[type_pet], model2.output_lv[type_pet]
    )

    num, val, result_fuzzy_set = inference_mamdani.process(
        model2.input_lvs[type_pet],
        model2.output_lv[type_pet],
        model2.rule_base,
        crisp,
        metrick,
    )
    ###############################################
    #   Вивід отриманих результатів
    ###############################################
    print(num, val)

    st.header("Вхідні літерали")
    for lv in model2.input_lvs[type_pet]:
        fuzzy_operators.draw_lv_strimlit(lv)

    st.header("Вихідний Літерал")

    fuzzy_operators.draw_lv_strimlit(model2.output_lv[type_pet], result_fuzzy_set)

    st.text(f"{str(num)}, {str(val)}")

    new_row = {
        "Age": crisp[0],
        "Height": crisp[1],
        "Nutrition": crisp[2],
        "metrick": metrick,
        "Value": num,
        "term": val,
    }

    new_df = pd.DataFrame(new_row, index=[0])
    print(new_df)
    print("==================")
    print(table)
    print("55555555555555555555555555")
    table = pd.concat([table, new_df], ignore_index=True)
    table = table.drop_duplicates()

    st.table(table)

    table.to_csv("data.csv", index=False)
except:
    st.header("Некорктне значення")


# 5.200000000000001, medium
