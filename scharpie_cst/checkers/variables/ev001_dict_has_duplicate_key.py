import libcst
from libcst.metadata.position_provider import PositionProvider

from scharpie_cst.checkers.base import BaseCSTChecker

__all__ = [
    'DictHasDuplicateKeyChecker'
]

class DictHasDuplicateKeyChecker(BaseCSTChecker):
    def __init__(self) -> None:
        super().__init__(issue_code = 'EV001')
        self.message = "Dict has duplicate key {val}"

    def visit_Dict(self, node: libcst.Dict):
        seen = set()

        for element in node.elements:
            if not isinstance(element.key, (libcst.BaseNumber, libcst.BaseString)):
                continue
            
            value = element.key.value
            
            if value in seen:
                pos = self.get_metadata(PositionProvider, element.key).start
                self.report_violation(node, metadata=pos, message_formatting={
                    'val': value
                })
            else:
                seen.add(value)