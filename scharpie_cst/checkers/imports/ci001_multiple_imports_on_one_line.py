
import libcst

from scharpie_cst.checkers.base import BaseCSTChecker

__all__ = [
    'MultipleImportsOnOneLineChecker'
]

class MultipleImportsOnOneLineChecker(BaseCSTChecker):
    def __init__(self) -> None:
        super(MultipleImportsOnOneLineChecker, self).__init__(issue_code='CI001')
        self.message = "Multiple package imports on one line"

    def visit_Import(self, node: "libcst.Import"):
        if len(node.names) > 1:
            self.report_violation(node)