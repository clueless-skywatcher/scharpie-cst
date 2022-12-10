import libcst
from libcst.metadata.position_provider import PositionProvider

from scharpie_cst.checkers.base import BaseCSTChecker

class SetHasDuplicateItemChecker(BaseCSTChecker):
    def __init__(self) -> None:
        super().__init__(issue_code = 'WV001')
        self.message = "Set has duplicate item {val}"

    def visit_Set(self, node: "libcst.Set"):
        seen = set()

        for element in node.elements:
            if not isinstance(element.value, (libcst.BaseNumber, libcst.BaseString)):
                continue
            
            value = element.value.value
            
            if value in seen:
                pos = self.get_metadata(PositionProvider, element.value).start
                self.report_violation(node, metadata=pos, message_formatting={
                    'val': value
                })
            else:
                seen.add(value)