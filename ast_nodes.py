from dataclasses import dataclass
from typing import List, Optional

class ASTNode:
    pass

@dataclass
class NumberNode(ASTNode):
    value: float

@dataclass
class IdNode(ASTNode):
    name: str

@dataclass
class BinOpNode(ASTNode):
    left: ASTNode
    op: str
    right: ASTNode

@dataclass
class VarDeclNode(ASTNode):
    name: str
    var_type: str
    value: ASTNode
@dataclass
class ProgramNode(ASTNode):
    statements: List[ASTNode]
@dataclass
class AssignNode(ASTNode):
    name: str
    value: ASTNode
@dataclass
class PrintNode(ASTNode):
    value: ASTNode
@dataclass
class BlockNode(ASTNode):
    statements: List[ASTNode]
@dataclass
class IfNode(ASTNode):
    condition: ASTNode
    then_block: BlockNode
    else_block: Optional[BlockNode]
@dataclass
class WhileNode(ASTNode):
    condition: ASTNode
    body: BlockNode