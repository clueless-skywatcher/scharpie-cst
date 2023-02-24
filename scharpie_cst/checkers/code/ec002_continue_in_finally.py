import libcst

from scharpie_cst.checkers.base import BaseCSTChecker

__all__ = [
    'ContinueInFinallyChecker'
]

class ContinueInFinallyChecker(BaseCSTChecker):
    '''
    Error: `continue` statement should not be within a `finally` block
    '''
    def __init__(self) -> None:
        super(ContinueInFinallyChecker, self).__init__(issue_code = 'EC002')
        self.message = "`continue` statement should not be within a `finally` block"

    def _has_continue(self, node):
        for child in node.body:
            if isinstance(child, libcst.Continue):
                return True
        return False

    def visit_Finally(self, node: "libcst.Finally"):
        for child in node.body.body:
            if self._has_continue(child):
                self.report_violation(child)
            