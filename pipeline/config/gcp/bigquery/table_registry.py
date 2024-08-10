class STG:
    class api_data:
        @staticmethod
        def schema():
            return "ARRIVAL_DATE:DATETIME, data:STRING"

        @staticmethod
        def get_table_name():
            return "STG.api_data"
