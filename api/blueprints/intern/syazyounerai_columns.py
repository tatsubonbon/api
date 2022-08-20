from turtle import st


class SyazyouneraiData:
    GUILTY_NAME = "罪名"
    TEGUCHI = "手口"
    POLICE_STATION_AREA = "管轄警察署（発生地）"
    POLICE_STATION_RESI_AREA = "管轄交番・駐在所（発生地）"
    MUNICIPALITIES_CODE = "市区町村コード（発生地）"
    PREFECTURE = "都道府県（発生地）"
    MUNICIPALITIES = "市区町村（発生地）"
    MACHI = "町丁目（発生地）"
    OCCURENCE_DATE = "発生年月日（始期）"
    OCCURENCE_TIME = "発生時（始期）"
    OCCURENCE_PLACE = "発生場所"
    OCCURENCE_PLACE_DETAIL = "発生場所の詳細"
    LOCKING = "施錠関係"
    CASH_DAMAGE = "現金被害の有無"

    columns = [
        GUILTY_NAME,
        TEGUCHI,
        POLICE_STATION_AREA,
        POLICE_STATION_RESI_AREA,
        MUNICIPALITIES_CODE,
        PREFECTURE,
        MUNICIPALITIES,
        MACHI,
        OCCURENCE_DATE,
        OCCURENCE_TIME,
        OCCURENCE_PLACE,
        OCCURENCE_PLACE_DETAIL,
        LOCKING,
        CASH_DAMAGE,
    ]

    dtypes = {
        GUILTY_NAME: str,
        TEGUCHI: str,
        POLICE_STATION_AREA: str,
        POLICE_STATION_RESI_AREA: str,
        MUNICIPALITIES_CODE: str,
        PREFECTURE: str,
        MUNICIPALITIES: str,
        MACHI: str,
        OCCURENCE_DATE: str,
        OCCURENCE_TIME: str,
        OCCURENCE_PLACE: str,
        OCCURENCE_PLACE_DETAIL: str,
        LOCKING: str,
        CASH_DAMAGE: str,
    }


class SyazyouneraiDataAdd:
    POLICE_STATION_AREA_COUNT = "管轄警察署（発生地）ごとの数"
