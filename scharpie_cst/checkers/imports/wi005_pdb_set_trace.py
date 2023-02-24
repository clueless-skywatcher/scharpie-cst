import libcst
from libcst.metadata.position_provider import PositionProvider

from scharpie_cst.checkers.base import BaseCSTChecker
from scharpie_cst.scharpie_cst import Violation

__all__ = [
    'PdbSetTraceChecker'
]

class PdbSetTraceChecker(BaseCSTChecker):
    def __init__(self) -> None:
        super().__init__(issue_code='WI005')
        self.message = "pdb.set_trace() call detected. Code may halt here in debugging mode"

    
    def visit_Call(self, node: "libcst.Call"):
        if node.func.value.value == 'pdb' and node.func.attr.value == 'set_trace':
            self.report_violation(node)