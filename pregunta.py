"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";" , index_col=0)

    # Delete the na values
    df = df.dropna()

    # Lowercase for the "sex" and "tipo_de_emprendimiento" columns
    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()

    # Lowercase for the "idea_negocio" column and remplace the "_" and "-" for " "
    df["idea_negocio"] = df["idea_negocio"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.replace("_", " ")
    df["idea_negocio"] = df["idea_negocio"].str.replace("-", " ")
    df["idea_negocio"] = df["idea_negocio"].str.strip()

    # Same for "barrio"
    df["barrio"] = df["barrio"].str.lower()
    df["barrio"] = df["barrio"].str.replace("_", " ")
    df["barrio"] = df["barrio"].str.replace("-", " ")

    # Convert the "estrato" and "comuna_ciudadano" column to int
    df["estrato"] = df["estrato"].astype(int)
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)

    # Convert the "fecha_de_beneficio" column to datetime
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda fecha: '/'.join(fecha.split('/')[::-1]) if len(fecha.split('/')[0]) == 4 else fecha)

    # Lowercase for the "monto_del_credito" column and remplace the " ", "$" for " " and "," for "" and convert to float
    df['monto_del_credito'] = df.monto_del_credito.str.replace(' ', '')
    df['monto_del_credito'] = df.monto_del_credito.str.replace('$', '')
    df['monto_del_credito'] = df.monto_del_credito.str.replace(',', '')
    df.monto_del_credito = df.monto_del_credito.astype(float)

    # Lowercase for the "línea_credito" column and remplace the "_" and "-" for " "
    df['línea_credito'] = df.línea_credito.str.lower()
    df['línea_credito'] = df.línea_credito.str.replace('_', ' ')
    df['línea_credito'] = df.línea_credito.str.replace('-', ' ')

    df.drop_duplicates(inplace=True)

    #
    # Inserte su código aquí
    #
    # print(df)

    return df


clean_data()