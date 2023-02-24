import libcst

from scharpie_cst.checkers.base import BaseCSTChecker

__all__ = [
    'MultipleStatementsOnOneLineChecker'
]

class MultipleStatementsOnOneLineChecker(BaseCSTChecker):
    def __init__(self) -> None:
        super(MultipleStatementsOnOneLineChecker, self).__init__(issue_code = 'CC002')
        self.message = "Multiple statements on one line"

    def visit_SimpleStatementLine(self, node: "libcst.SimpleStatementLine"):
        if len(node.body) > 1:
            self.report_violation(node)