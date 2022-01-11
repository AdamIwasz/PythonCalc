from PyCalcCtrl import ERROR_MSG


class PyCalcModel:
    
    @staticmethod
    def evaluateExpression(expression):
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
          result = ERROR_MSG
        return result